#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QtNetwork>
#include <thread>
#include <mutex>
#include <QMessageBox>
#include <condition_variable>
#include <opencv2/opencv.hpp>
#include "signupwindow.h"
#include "capturewindow.h"
#include "eCAM130_TRICUTX2.h"

enum EVENT_ID{SIGN_UP, WORK_IN, WORK_OUT};

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

    void httpUploadFinished2(QNetworkReply *reply);

private:
    Ui::MainWindow *ui;

    SignUpWindow* signup_window;
    CaptureWindow* capture_window;

    QMessageBox msg_box;

    eCAM::eCAM130_TRICUTX2* cam;
    std::thread* capture_thread;
    std::mutex capture_mutex;
    std::condition_variable capture_con;

    QLabel* plabel_frame;
    cv::Mat* frame_yuv;
    cv::Mat* frame_rgb;
    QImage* frame_qimg;
    QPixmap frame_qmap;

    bool save_frame;

    bool process_exit;

    QNetworkRequest network_request;
    QNetworkAccessManager* network_am;

    EVENT_ID event;

    void CameraInit();
    void Capture();

    void sendpost();

protected:
    void closeEvent(QCloseEvent *event);
};

#endif // MAINWINDOW_H
