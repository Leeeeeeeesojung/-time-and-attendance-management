#include "capturewindow.h"
#include "ui_capturewindow.h"

CaptureWindow::CaptureWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::CaptureWindow)
{
    ui->setupUi(this);
}

CaptureWindow::~CaptureWindow()
{
    delete ui;
}
