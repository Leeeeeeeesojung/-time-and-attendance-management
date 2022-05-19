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

void SignUpWindow::closeEvent(QCloseEvent* event)
{
    signup_info.name = ui->lineEdit_name->text();
    signup_info.mail = ui->lineEdit_mail->text();
    signup_info.password = ui->lineEdit_password->text();
    signup_info.position = ui->lineEdit_position->text();
    signup_info.deparment = ui->lineEdit_department->text();
}
