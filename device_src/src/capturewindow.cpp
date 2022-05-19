#include "capturewindow.h"
#include "ui_capturewindow.h"
#include <QMouseEvent>
#include <iostream>

CaptureWindow::CaptureWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CaptureWindow)
{
    ui->setupUi(this);

    plabel_frame = ui->label_frame;
    ui->label_frame->installEventFilter(this);
}

CaptureWindow::~CaptureWindow()
{
    delete ui;
}

bool CaptureWindow::eventFilter(QObject *object, QEvent *event)
{
    /*save and exit capture when clicked frame image*/
    if( (object == ui->label_frame) && (event->type() == QMouseEvent::MouseButtonPress) ){
        std::cout<<"Capture"<<std::endl;
        emit face_capture();
        this->close();
    }

    return QWidget::eventFilter(object,event);
}
