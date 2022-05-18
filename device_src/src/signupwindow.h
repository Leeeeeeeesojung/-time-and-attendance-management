#ifndef SIGNUPWINDOW_H
#define SIGNUPWINDOW_H

#include <QWidget>

namespace Ui {
class SignUpWindow;
}

class SignUpWindow : public QWidget
{
    Q_OBJECT

public:
    explicit SignUpWindow(QWidget *parent = nullptr);
    ~SignUpWindow();

private:
    Ui::SignUpWindow *ui;

signals:
    void capture_clicked();

private slots:
    void on_pushButton_capture_clicked();
};

#endif // SIGNUPWINDOW_H
