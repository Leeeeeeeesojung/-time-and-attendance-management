#include "signupwindow.h"
#include "ui_signupwindow.h"

SignUpWindow::SignUpWindow(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::SignUpWindow)
{
    ui->setupUi(this);
}

SignUpWindow::~SignUpWindow()
{
    delete ui;
}
