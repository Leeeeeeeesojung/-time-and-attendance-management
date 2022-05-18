#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include "signupwindow.h"
#include "capturewindow.h"

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

private:
    Ui::MainWindow *ui;

    SignUpWindow* signup_window;
    CaptureWindow* capture_window;
};

#endif // MAINWINDOW_H
