#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <unistd.h>

#define CAM_NUM             1
#define CAM_WIDTH           eCAM::FULL_HD_W
#define CAM_HEIGHT          eCAM::FULL_HD_H

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow), process_exit(false), save_frame(false)
{
    ui->setupUi(this);

    signup_window = new SignUpWindow();
    capture_window = new CaptureWindow();

    connect(signup_window, SIGNAL(capture_clicked()), this, SLOT(signup_capture_clicked()));
    connect(capture_window, SIGNAL(face_capture()), this, SLOT(Save_Frame()));

    /*Camera setting*/
    cam = new eCAM::eCAM130_TRICUTX2();
    cam->Open(CAM_NUM, CAM_WIDTH, CAM_HEIGHT);
    CameraInit();
    cam->StartCapturing(); //capture start

    /*Frame image*/
    frame_yuv = new cv::Mat(CAM_HEIGHT, CAM_WIDTH, CV_8UC2);
    frame_rgb = new cv::Mat(CAM_HEIGHT, CAM_WIDTH, CV_8UC3);
    frame_qimg = new QImage(frame_rgb->data, frame_rgb->cols, frame_rgb->rows,
                            QImage::Format_RGB888);
    plabel_frame = capture_window->plabel_frame;

    /*Start capture thread*/
    capture_thread = new std::thread( [&](){Capture();} );
    capture_thread->detach();
}

MainWindow::~MainWindow()
{
    delete signup_window;
    delete  capture_window;
    delete cam;
    delete capture_thread;
    delete ui;
}

void MainWindow::CameraInit()
{
    /*Parameter of camera setting*/
    cam->SetParameter(V4L2_CID_BRIGHTNESS, 0);
    cam->SetParameter(V4L2_CID_CONTRAST, 4);
    cam->SetParameter(V4L2_CID_SATURATION, 18);
    cam->SetParameter(V4L2_CID_GAMMA, 220);
    cam->SetParameter(V4L2_CID_GAIN, 1);
    cam->SetParameter(V4L2_CID_SHARPNESS, 16);
    cam->SetParameter(V4L2_CID_FRAME_SYNC, 1);
    cam->SetParameter(V4L2_CID_EXPOSURE_ABSOLUTE, 290);
    cam->SetParameter(V4L2_CID_AUTO_WHITE_BALANCE, 0);
    cam->SetParameter(V4L2_CID_WHITE_BALANCE_TEMPERATURE, 6000);
    cam->SetParameter(V4L2_CID_PAN_ABSOLUTE, 0);
    cam->SetParameter(V4L2_CID_TILT_ABSOLUTE, 0);
    cam->SetParameter(V4L2_CID_ZOOM_ABSOLUTE, 100);
    cam->SetParameter(V4L2_CID_HFLIP, 1);
    cam->SetParameter(V4L2_CID_VFLIP, 0);
}

void MainWindow::on_pushButton_signup_clicked()
{
    signup_window->show();
}

void MainWindow::signup_capture_clicked()
{
    capture_window->showMaximized();
    capture_con.notify_one();
}

void MainWindow::on_pushButton_work_in_clicked()
{
    capture_window->showMaximized();
    capture_con.notify_one();
}

void MainWindow::on_pushButton_work_out_clicked()
{
    capture_window->showMaximized();
    capture_con.notify_one();
}

void MainWindow::Capture()
{
    eCAM::buffer frame_buf;
    QPixmap frame_qmap;
    QTransform frame_trans;

    std::unique_lock<std::mutex> capture_lock(capture_mutex);
    frame_trans.rotate(90);

    do{
        capture_con.wait(capture_lock);

        if(process_exit){
            cam->Close();
            break;
        }

        do{
            /*Get frame*/
            frame_buf = cam->GetFrame();

            /*Convert color space of frame image*/
            memcpy(frame_yuv->data, frame_buf.data[0], frame_buf.size);
            cv::cvtColor(*frame_yuv, *frame_rgb, CV_YUV2RGB_UYVY);

            /*Show frame*/
            frame_qmap = QPixmap::fromImage(*frame_qimg).transformed(frame_trans);
            frame_qmap = frame_qmap.scaled(plabel_frame->width(),
                                                plabel_frame->height());
            plabel_frame->setPixmap(frame_qmap);

            /*save image*/
            if(save_frame){
                frame_qimg->save("image.jpg");
                save_frame = false;
                break;
            }
        }while(true);
    }while(true);
}

void MainWindow::Save_Frame()
{
    save_frame = true;
}

void MainWindow::closeEvent(QCloseEvent *event)
{
    /*Exit capture thread*/
    process_exit = true;
    capture_con.notify_one();
    sleep(1);
}
