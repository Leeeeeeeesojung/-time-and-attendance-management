#include "signupwindow.h"
#include "ui_signupwindow.h"

SignUpWindow::SignUpWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SignUpWindow)
{
    ui->setupUi(this);

    connect(ui->pushButton_cancel, SIGNAL(clicked()), this, SLOT(close()));
}

SignUpWindow::~SignUpWindow()
{
    delete ui;
}

void SignUpWindow::on_pushButton_capture_clicked()
{
    emit capture_clicked();
}
