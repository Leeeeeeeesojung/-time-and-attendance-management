/*****************************************************************************
* file : eCAM130_TRICUTX2.cpp
* author : Mingu Kang
* date : 2019.02.08
* environment : Qt 5.5.1, Ubuntu 16.04 LTS 64bit
* brief : eCAM130_TRICUTX2 class, eCAM namespace
* version : 2019.01.17-0.1
*****************************************************************************/

#include <stdlib.h>
#include <assert.h>
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <string.h> // strerrno
#include <sys/stat.h>
#include <sys/types.h>
#include <sys/time.h>
#include <sys/mman.h>
#include <sys/ioctl.h>
#include <sys/poll.h>
#include <stdexcept>

#include "eCAM130_TRICUTX2.h"

#define CLEAR(x)        memset(&(x), 0, sizeof(x))
#define PIXEL_FORMAT    V4L2_PIX_FMT_UYVY;

namespace eCAM{

/**
 * @fn      eCAM130_TRICUTX2(int cam_num, size_t width, size_t height, __u32 buffer_count)
 * @brief   Constructor
 *          Initialization of camera
 * @param   cam_num : number of buffer
 * @param   width : width of buffer
 * @param   height : height of buffer
 * @param   buffer_count : buffer size of camera
 * @return  void
 */
eCAM130_TRICUTX2::eCAM130_TRICUTX2(int cam_num, size_t width, size_t height, __u32 buffer_count)
    : cam_num(cam_num), xres(width), yres(height), buffer_count(buffer_count)
{
    Initialize(cam_num);
}

/**
 * @fn      ~eCAM130_TRICUTX2()
 * @brief   Destructor
 *          Uninitialization of camera
 * @param   void
 * @return  void
 */
eCAM130_TRICUTX2::~eCAM130_TRICUTX2()
{
    //Deivce close and memory off
    Close();
}

/**
 * @fn      Open(int cam_num, size_t width, size_t height, __u32 buffer_count)
 * @brief   Connect camera device
 * @param   cam_num : number of camera
 * @param   width : buffer of width
 * @param   height : buffer of height
 * @param   buffer_count : size of buffer
 * @return  void
 */
void eCAM130_TRICUTX2::Open(int cam_num, size_t width, size_t height, __u32 buffer_count)
{
    this->cam_num = cam_num;
    this->buffer_count = buffer_count;
    xres = width;
    yres = height;

    Initialize(cam_num);
}

void eCAM130_TRICUTX2::Close()
{
    //Deivce close and memory off
    StopCapturing();
    UninitDevice();
    CloseDevice();
}

/**
 * @fn      Initialize(int cam_num)
 * @brief   Initialization of camera
 * @param   cam_num : number of camera
 * @return  void
 */
void eCAM130_TRICUTX2::Initialize(int cam_num)
{
    // Device name of Linux file system
    for(int i=0;i<cam_num;i++)
        device[i]="/dev/video"+std::to_string(i);

    //Device open and memory allotment
    OpenDevice();
    InitDevice();
}

/**
 * @fn      Uninitialize()
 * @brief   Uninitialization of camera
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::Uninitialize()
{
    //Deivce close and memory off
    StopCapturing();
    UninitDevice();
    CloseDevice();
}

/**
 * @fn      GetFrame()
 * @brief   Get frame of camera device
 * @param   void
 * @return  Data of capture frame
 */
const buffer eCAM130_TRICUTX2::GetFrame()
{
    struct pollfd fds[cam_num];
    int r = 0;

    /* Setting fds */
    for(int i=0; i<cam_num; i++){
        fds[i].fd = fd[i];
        fds[i].events = POLLIN;
    }

    while(true){

        //Wait until data in buffer changes
        r = poll(fds, cam_num, -1);

        switch (r) {
        case -1:
            if(EINTR == errno)
                continue;
            throw std::runtime_error("Poll function error");
            break;

        case 0:
            throw std::runtime_error("Device select(poll) timeout");
            break;

        default:
            //Return frame data
            if(ReadFrame() == true)
                return frame;
            else if(ReadFrame() == false)
                continue;

            break;
        }

    }
}

/**
 * @fn      Xioctl(int fh, unsigned long int request, void *arg)
 * @brief   Access the camera device of Linux system file
 *          using ioctl function.
 * @param   fh : file pointer
 * @param   request : ioctl code of camera device
 * @param   arg : v4l2_control struct
 * @return  error code of ioctl function
 */
int eCAM130_TRICUTX2::Xioctl(int fh, unsigned long int request, void *arg)
{
    int r;

    do {
          r = ioctl(fh, request, arg);
    } while (-1 == r && EINTR == errno);

    return r;
}

/**
 * @fn      Initmmap()
 * @brief   Initialization of buffer memory
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::Initmmap()
{
    struct v4l2_requestbuffers req;

    CLEAR(req);

    req.count = buffer_count;
    req.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    req.memory = V4L2_MEMORY_MMAP;

    for(int j=0; j<cam_num; j++){

        if (-1 == Xioctl(fd[j], VIDIOC_REQBUFS, &req)) {
            if (EINVAL == errno) {
                throw std::runtime_error(device[j] + " does not support memory mapping");
            } else {
                throw std::runtime_error("VIDIOC_REQBUFS");
            }
        }

        if (req.count < 2) {
            throw std::runtime_error(std::string("Insufficient buffer memory on ") + device[j]);
        }

    }

    buffers = (buffer*) calloc(req.count, sizeof(*buffers));

    if (!buffers) {
        throw std::runtime_error("Out of memory");
    }


    struct v4l2_buffer buf;

    CLEAR(buf);

    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory = V4L2_MEMORY_MMAP;

    for(int j=0; j<cam_num; j++){

        for (n_buffers = 0; n_buffers < req.count; ++n_buffers) {

            buf.index = n_buffers;

            if (-1 == Xioctl(fd[j], VIDIOC_QUERYBUF, &buf))
                throw std::runtime_error("VIDIOC_QUERYBUF");

            buffers[n_buffers].size = buf.length;
            buffers[n_buffers].data[j] =
                    mmap(NULL /* start anywhere */,
                         buf.length,
                         PROT_READ | PROT_WRITE /* required */,
                         MAP_SHARED /* recommended */,
                         fd[j], buf.m.offset);

            if (MAP_FAILED == buffers[n_buffers].data[j])
                throw std::runtime_error("mmap");
        }

    }
}

/**
 * @fn      OpenDevice()
 * @brief   Connect the file system of camera device
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::OpenDevice()
{
    struct stat st;

    for(int k=0; k<cam_num; k++){
        if (-1 == stat(device[k].c_str(), &st)) {
            throw std::runtime_error(device[k] + ": cannot identify! " + std::to_string(errno) +  ": " + strerror(errno));
        }

        if (!S_ISCHR(st.st_mode)) {
            throw std::runtime_error(device[k] + " is no device");
        }

        fd[k] = open(device[k].c_str(), O_RDWR /* required */ | O_NONBLOCK, 0);

        if (-1 == fd[k]) {
            throw std::runtime_error(device[k] + ": cannot open! " + std::to_string(errno) + ": " + strerror(errno));
        }
    }
}

/**
 * @fn      CloseDevice()
 * @brief   Deconnect the file system of camera device
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::CloseDevice()
{
    for(int i=0; i<cam_num; i++){
        if (-1 == close(fd[i]))
            throw std::runtime_error("close");

        fd[i] = -1;
    }
}

/**
 * @fn      InitDevice()
 * @brief   Device setting
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::InitDevice()
{
    struct v4l2_capability cap[cam_num];
    struct v4l2_cropcap cropcap;
    struct v4l2_crop crop;
    struct v4l2_format fmt;

    CLEAR(cropcap);
    cropcap.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    crop.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    crop.c = cropcap.defrect; /* reset to default */

    CLEAR(fmt);
    fmt.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    fmt.fmt.pix.width       = xres;
    fmt.fmt.pix.height      = yres;
    fmt.fmt.pix.pixelformat = PIXEL_FORMAT;
    fmt.fmt.pix.field = V4L2_FIELD_ANY;

    for(int i=0; i<cam_num; i++){

        if (-1 == Xioctl(fd[i], VIDIOC_QUERYCAP, &cap[i])) {
            if (EINVAL == errno) {
                throw std::runtime_error(device[i]+ " is no V4L2 device");
            } else {
                throw std::runtime_error("VIDIOC_QUERYCAP");
            }
        }

        if (!(cap[i].capabilities & V4L2_CAP_VIDEO_CAPTURE)) {
            throw std::runtime_error(device[i] + " is no video capture device");
        }

        if (!(cap[i].capabilities & V4L2_CAP_STREAMING)) {
            throw std::runtime_error(device[i] + " does not support streaming i/o");
        }

        /* Select video input, video standard and tune here. */
        Xioctl(fd[i], VIDIOC_CROPCAP, &cropcap);

        if (-1 == Xioctl(fd[i], VIDIOC_S_CROP, &crop)) {
            switch (errno) {
            case EINVAL:
                /* Cropping not supported. */
                break;
            default:
                /* Errors ignored. */
                break;
            }
        }

        if (force_format) {
            if (-1 == Xioctl(fd[i], VIDIOC_S_FMT, &fmt))
                throw std::runtime_error("VIDIOC_S_FMT");

            /* Note VIDIOC_S_FMT may change width and height. */
            xres = fmt.fmt.pix.width;
            yres = fmt.fmt.pix.height;

            stride = fmt.fmt.pix.bytesperline;


        } else {
            /* Preserve original settings as set by v4l2-ctl for example */
            if (-1 == Xioctl(fd[i], VIDIOC_G_FMT, &fmt))
                throw std::runtime_error("VIDIOC_G_FMT");
        }

    }

    Initmmap();
}

/**
 * @fn      UninitDevice()
 * @brief   Uninitailization of Device
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::UninitDevice()
{
    for(int k=0; k<cam_num; k++){
        for (__u32 i = 0; i < n_buffers; ++i){
            if (-1 == munmap(buffers[i].data[k], buffers[i].size))
                throw std::runtime_error("munmap");\
        }
    }

    free(buffers);
}

/**
 * @fn      StartCapturing()
 * @brief   Start capture
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::StartCapturing()
{
    enum v4l2_buf_type type;
    struct v4l2_buffer buf;

    CLEAR(buf);
    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory = V4L2_MEMORY_MMAP;

    type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    for(int k=0; k<cam_num; k++){
        for (__u32 i = 0; i < n_buffers; ++i) {
            buf.index = i;

            if (-1 == Xioctl(fd[k], VIDIOC_QBUF, &buf))
                throw std::runtime_error("VIDIOC_QBUF");
        }

        if (-1 == Xioctl(fd[k], VIDIOC_STREAMON, &type))
            throw std::runtime_error("VIDIOC_STREAMON");
    }
}

/**
 * @fn      StopCapturing()
 * @brief   Stop capture
 * @param   void
 * @return  void
 */
void eCAM130_TRICUTX2::StopCapturing()
{
    enum v4l2_buf_type type;

    type = V4L2_BUF_TYPE_VIDEO_CAPTURE;

    for(int i=0; i<cam_num; i++){
        if (-1 == Xioctl(fd[i], VIDIOC_STREAMOFF, &type))
            throw std::runtime_error("VIDIOC_STREAMOFF");
    }
}

/**
 * @fn      ReadFrame()
 * @brief   Read the frame from buffer
 * @param   void
 * @return  true -> sucess of capture
 *          false -> failure of capture
 */
bool eCAM130_TRICUTX2::ReadFrame()
{
    int i;
    struct v4l2_buffer buf;

    CLEAR(buf);

    buf.type = V4L2_BUF_TYPE_VIDEO_CAPTURE;
    buf.memory = V4L2_MEMORY_MMAP;

    for(i=0; i<cam_num; i++){

        if (-1 == Xioctl(fd[i], VIDIOC_DQBUF, &buf)) {
            switch (errno) {
            case EAGAIN:
//                throw runtime_error("VIDIOC_DQBUF");
                return false;

            case EIO:
                /* Could ignore EIO, see spec. */

                /* fall through */

            default:
                throw std::runtime_error("VIDIOC_DQBUF");
            }
        }
    }

    assert(buf.index < n_buffers);

    frame=buffers[buf.index];

    for(i=0; i<cam_num; i++){
        if (-1 == Xioctl(fd[i], VIDIOC_QBUF, &buf))
            throw std::runtime_error("VIDIOC_QBUF");
    }

    return true;
}

/**
 * @fn      SetParameter(__u32 id, __s32* value)
 * @brief   Set parameter of each camera
 * @param   id : Parameter id of V4L2 library user want to change.
 *               (like V4L2_CID_EXPOSURE_ABSOLUTE, V4L2_CID_BRIGHTNESS)
 * @param   *value : pointer of parameter value.
 * @return  void
 */
void eCAM130_TRICUTX2::SetParameter(__u32 id, __s32* value)
{
    struct v4l2_control ctrl;

    CLEAR(ctrl);
    ctrl.id = id;

    for(int i=0; i<cam_num; i++){
        ctrl.value = value[i];

        if( -1 == Xioctl(fd[i], VIDIOC_S_CTRL, &ctrl) )
            throw std::runtime_error("VIDIOC_S_CTRL");
    }
}

/**
 * @fn      SetParameter(__u32 id, __s32 value)
 * @brief   Set same value for all cameras.
 * @param   id : Parameter id of V4L2 library user want to change.
 *               (like V4L2_CID_EXPOSURE_ABSOLUTE, V4L2_CID_BRIGHTNESS)
 * @param   value : parameter value.
 * @return  void
 */
void eCAM130_TRICUTX2::SetParameter(__u32 id, __s32 value)
{
    struct v4l2_control ctrl;

    CLEAR(ctrl);
    ctrl.id = id;
    ctrl.value = value;

    for(int i=0; i<cam_num; i++){

        if( -1 == Xioctl(fd[i], VIDIOC_S_CTRL, &ctrl) )
            throw std::runtime_error("VIDIOC_S_CTRL");
    }
}

/**
 * @fn        GetParameter(__u32 id)
 * @brief     Get parameter value of each camera
 * @param     id : Parameter id of V4L2 library user want to know.
 * @param     *value : pointer of current parameter value.
 * @return    void
 */
void eCAM130_TRICUTX2::GetParameter(__u32 id, __s32* value)
{
    struct v4l2_control ctrl;

    CLEAR(ctrl);
    ctrl.id = id;

    for(int i=0; i<cam_num; i++){
        if( -1 == Xioctl(fd[i], VIDIOC_G_CTRL, &ctrl) )
            throw std::runtime_error("VIDIOC_G_CTRL");

        value[i] = ctrl.value;
    }
}

}
