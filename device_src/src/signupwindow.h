#ifndef SIGNUPWINDOW_H
#define SIGNUPWINDOW_H

#include <QWidget>

typedef struct _PersonInfo{
    QString name;
    QString mail;
    QString password;
    QString position;
    QString deparment;
}PersonInfo;

namespace Ui {
class SignUpWindow;
}

class SignUpWindow : public QWidget
{
    Q_OBJECT

public:
    explicit SignUpWindow(QWidget *parent = nullptr);
    ~SignUpWindow();

    PersonInfo signup_info;

private:
    Ui::SignUpWindow *ui;

signals:
    void capture_clicked();

private slots:
    void on_pushButton_capture_clicked();

protected:
    void closeEvent(QCloseEvent *);
};

#endif // SIGNUPWINDOW_H
