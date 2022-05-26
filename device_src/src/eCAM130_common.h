/*****************************************************************************
* file : eCAM130_common.h
* author : Mingu Kang
* date : 2019.01.17
* environment : Qt 5.5.1, Ubuntu 16.04 LTS 64bit
* brief : Define Important setting values and header file
* version : 2019.01.17-0.1
*****************************************************************************/

#ifndef ECAM130_COMMON_H
#define ECAM130_COMMON_H

#include <memory>
#include <linux/videodev2.h>

#define V4L2_CID_FRAME_SYNC     (V4L2_CID_AUTO_FOCUS_RANGE+11)
#define MAX_CAM                 6
#define TRIPLE_CAM_MAX          3
#define DEFAULT_COUNT_BUFFER    6

namespace eCAM {

enum HEIGHT{VGA_H=480,HD_H=720,FULL_HD_H=1080,FOUR_K_H=2160};
enum WIDTH{VGA_W=640,HD_W=1280,FULL_HD_W=1920,FOUR_K_W=3840};

/**
 * @struct  buffer
 * @brief   Store data of camera buffer
 */
struct buffer {
    void   *data[MAX_CAM];
    size_t  size;
};

}

#endif // ECAM130_COMMON_H
