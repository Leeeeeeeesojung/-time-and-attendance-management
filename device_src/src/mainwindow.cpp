#include "mainwindow.h"
#include "ui_mainwindow.h"
#include <iostream>
#include <unistd.h>
#include <QMessageBox>

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

    /*Set network*/
    network_am = new QNetworkAccessManager(this);
    network_am->setParent(this);
    connect(network_am, SIGNAL(finished(QNetworkReply*)), this, SLOT(httpUploadFinished2(QNetworkReply*)));
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
    event = EVENT_ID::SIGN_UP;
    signup_window->show();
}

void MainWindow::signup_capture_clicked()
{
    capture_window->showMaximized();
    capture_con.notify_one();
}

void MainWindow::on_pushButton_work_in_clicked()
{
    event = EVENT_ID::WORK_IN;
    capture_window->showMaximized();
    capture_con.notify_one();
}

void MainWindow::on_pushButton_work_out_clicked()
{
    event = EVENT_ID::WORK_OUT;
    capture_window->showMaximized();
    capture_con.notify_one();
}

void MainWindow::Capture()
{
    eCAM::buffer frame_buf;
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
//                frame_qmap.save("face.bmp");
                save_frame = false;
                break;
            }
        }while(true);
    }while(true);
}

void MainWindow::Save_Frame()
{
     msg_box.setText("Send data...");
     msg_box.show();

    save_frame = true;
    signup_window->close();
    frame_qmap.save("face.bmp");

#ifdef QT_DEBUG
    std::cout<<signup_window->signup_info.name.toStdString()<<std::endl;
    std::cout<<signup_window->signup_info.mail.toStdString()<<std::endl;
    std::cout<<signup_window->signup_info.password.toStdString()<<std::endl;
    std::cout<<signup_window->signup_info.position.toStdString()<<std::endl;
    std::cout<<signup_window->signup_info.deparment.toStdString()<<std::endl;
#endif

    sendpost();
}

void MainWindow::closeEvent(QCloseEvent *event)
{
    /*Exit capture thread*/
    process_exit = true;
    capture_con.notify_one();
    sleep(1);
}

//http finished slot
void MainWindow::httpUploadFinished2(QNetworkReply *reply)
{
    reply->open(QIODevice::ReadOnly);

    if (reply->error() == QNetworkReply::NoError){
        msg_box.close();

        QString str = (QString)reply -> readAll();
        QJsonDocument jsonResponse = QJsonDocument::fromJson(str.toUtf8());
        QJsonObject jsonObj = jsonResponse.object();

        if(jsonObj["response"] == "1"){
            QMessageBox::StandardButton reply;
            reply = QMessageBox::question(this, "info", "Wellcome!! \t "+jsonObj["username"].toString()+"\n"+jsonObj["datetime"].toString(),
                    QMessageBox::Yes|QMessageBox::No);
            if (reply == QMessageBox::Yes) {
                qDebug() << "Yes was clicked";
                QApplication::quit();
            } else {
                qDebug() << "Yes was not clicked";
            }
            //QMessageBox::information(this,"send","success");
        }else{
            QMessageBox::information(this,"send","fail");
        }
    }else{
        QString error_code = reply->errorString();
        msg_box.setText(error_code);
//        QMessageBox::information(this,"send",reply->errorString());
        std::cerr<<error_code.toStdString()<<std::endl;
    }
        //        this->close();
}

//Send data to DB
void MainWindow::sendpost()
{
    QNetworkRequest network_request;
    QNetworkReply *reply;

    QHttpMultiPart* http_multi_part =
            new QHttpMultiPart(QHttpMultiPart::FormDataType);
    QString username = signup_window->signup_info.name;
    QFile *file = new QFile("./face.bmp");

    switch (event){
    case EVENT_ID::WORK_IN:
    {
        QHttpPart text_part;
        text_part.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"text\""));
        text_part.setBody("face0");
        QHttpPart image_part;
        image_part.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("image/bmp"));
        image_part.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("multipart/form-data; name=\"image\"; filename=\"face0.bmp\""));
        image_part.setRawHeader("Content-Transfer-Encoding","binary");

        /*Input image data*/
//        QFile *file = new QFile("./face.bmp");
        file->open(QIODevice::ReadOnly);
        image_part.setBodyDevice(file);
        file->setParent(http_multi_part);
        http_multi_part->append(text_part);
        http_multi_part->append(image_part);

        QUrl url("http://61.78.103.36:8000/myuser/login/");
//        QNetworkRequest request(url);
        network_request.setUrl(url);
        break;
    }
    case 2:
    {
//            QHttpMultiPart *multiPart = new QHttpMultiPart(QHttpMultiPart::FormDataType);
        QHttpPart text_part;
//        QHttpPart text2,text3;
//        QByteArray by1 = user_name.toUtf8();
//        QByteArray by2 = e_mail.toUtf8(),by3 = pass_word.toUtf8(),by4;
        text_part.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"text\""));
        text_part.setBody(username.toUtf8());

        QHttpPart image_part;
        image_part.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("image/bmp"));
        image_part.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("multipart/form-data; name=\"image\"; filename=\"face0.bmp\""));
        image_part.setRawHeader("Content-Transfer-Encoding","binary");

        /*Input image data*/
//        QFile *file = new QFile("./face.bmp");
        file->open(QIODevice::ReadOnly);
        image_part.setBodyDevice(file);
        file->setParent(http_multi_part);
        http_multi_part->append(text_part);
        http_multi_part->append(image_part);

        QUrl url("http://61.78.103.36:8000/myuser/logout/");
        network_request.setUrl(url);
//        QNetworkRequest request(url);

//        QNetworkAccessManager manager;
//        QNetworkReply *reply = am->post(request, multiPart);
//        multiPart->setParent(reply);

        break;
    }

    case EVENT_ID::SIGN_UP:
    {
//        QHttpMultiPart* http_multi_part = new QHttpMultiPart(QHttpMultiPart::FormDataType);

        /*Input user information*/
        QHttpPart info_part[6];
        info_part[0].setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"text\";"));
        info_part[0].setBody(username.toLatin1());
        info_part[1].setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"username\";"));
        info_part[1].setBody(signup_window->signup_info.name.toLatin1());
        info_part[2].setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"email\";"));
        info_part[2].setBody(signup_window->signup_info.mail.toLatin1());
        info_part[3].setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"password\";"));
        info_part[3].setBody(signup_window->signup_info.password.toLatin1());
        info_part[4].setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"position\";"));
        info_part[4].setBody(signup_window->signup_info.position.toLatin1());
        info_part[5].setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("form-data; name=\"department\";"));
        info_part[5].setBody(signup_window->signup_info.deparment.toLatin1());

        /*Input image data*/
        QHttpPart image_part;
        image_part.setHeader(QNetworkRequest::ContentTypeHeader, QVariant("image/bmp"));
        image_part.setHeader(QNetworkRequest::ContentDispositionHeader, QVariant("multipart/form-data; name=\"image\"; filename=\""+username+".bmp\""));
        image_part.setRawHeader("Content-Transfer-Encoding","binary");
//        QFile* img_file = new QFile("./face.bmp");
        file->open(QIODevice::ReadOnly);
        image_part.setBodyDevice(file);
        file->setParent(http_multi_part);
        for(int i = 0 ; i < 6 ; i++)
            http_multi_part->append(info_part[i]);
        http_multi_part->append(image_part);

        /*Send user data for sign up*/
        QUrl url("http://61.78.103.36:8000/myuser/register/");
//        QNetworkRequest request(url);
        network_request.setUrl(url);
//        QNetworkAccessManager manager;
//        QNetworkReply *reply = network_am->post(request, http_multi_part);
//        http_multi_part->setParent(reply);

        break;
    }
    }

    QNetworkAccessManager manager;
    reply = network_am->post(network_request, http_multi_part);
    http_multi_part->setParent(reply);

}
