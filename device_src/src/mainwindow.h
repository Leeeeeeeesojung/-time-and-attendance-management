#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <opencv2/opencv.hpp>
#include "signupwindow.h"
#include "capturewindow.h"
#include "eCAM130_TRICUTX2.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = nullptr);
    ~MainWindow();

private slots:
    void on_pushButton_signup_clicked();
    void on_pushButton_work_in_clicked();
    void on_pushButton_work_out_clicked();

    void signup_capture_clicked();
    void Save_Frame();

private:
    Ui::MainWindow *ui;

    SignUpWindow* signup_window;
    CaptureWindow* capture_window;

    eCAM::eCAM130_TRICUTX2* cam;
    std::thread* capture_thread;
    std::mutex capture_mutex;
    std::condition_variable capture_con;

    QLabel* plabel_frame;
    cv::Mat* frame_yuv;
    cv::Mat* frame_rgb;
    QImage* frame_qimg;

    bool save_frame;

    bool process_exit;

    void CameraInit();
    void Capture();

protected:
    void closeEvent(QCloseEvent *event);
};

#endif // MAINWINDOW_H
