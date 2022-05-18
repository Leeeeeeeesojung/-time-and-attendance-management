#include "mainwindow.h"
#include "ui_mainwindow.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);

    signup_window = new SignUpWindow();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::on_pushButton_signup_clicked()
{
    signup_window->show();
}
