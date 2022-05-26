/*****************************************************************************
* file : eCAM130_TRICUTX2.h
* author : Mingu Kang
* date : 2019.02.08
* environment : Qt 5.5.1, Ubuntu 16.04 LTS 64bit
* brief : eCAM130_TRICUTX2 class, eCAM namespace
* version : 2019.01.17-0.1
*****************************************************************************/

#ifndef ECAM130_TRICUTX2_H
#define ECAM130_TRICUTX2_H

#include <string>
#include <linux/videodev2.h>
#include "eCAM130_common.h"

namespace eCAM{

/**
 * @class   eCAM130_TRICUTX2
 * @brief   eCAM130_TRICUTX2 setting and controls
 * @version 0.1
 */
class eCAM130_TRICUTX2
{
public:
    eCAM130_TRICUTX2(){}
    eCAM130_TRICUTX2(int cam_num, size_t width, size_t height, __u32 buffer_count = DEFAULT_COUNT_BUFFER);
    ~eCAM130_TRICUTX2();

    void Open(int cam_num, size_t width, size_t height, __u32 buffer_count = DEFAULT_COUNT_BUFFER);
    void Close();
    void Uninitialize();
    void StartCapturing();
    void StopCapturing();

    const eCAM::buffer GetFrame();

    void SetParameter(__u32 id, __s32* value);
    void SetParameter(__u32 id, __s32 value);
    void GetParameter(__u32 id, __s32* value);

private:
    void Initialize(int cam_num);

    int Xioctl(int fh, unsigned long int request, void *arg);
    void Initmmap();

    void OpenDevice();
    void CloseDevice();

    void InitDevice();
    void UninitDevice();

    bool ReadFrame();

    int cam_num;
    std::string device[TRIPLE_CAM_MAX];
    int fd[TRIPLE_CAM_MAX];

    struct eCAM::buffer *buffers;
    struct eCAM::buffer frame;
    unsigned int n_buffers;

    size_t xres;
    size_t yres;
    size_t stride;
     __u32 buffer_count;

    bool force_format = true;
};

}
#endif // ECAM130_TRICUTX2_H
