#ifndef CAPTUREWINDOW_H
#define CAPTUREWINDOW_H

#include <QWidget>

namespace Ui {
class CaptureWindow;
}

class CaptureWindow : public QWidget
{
    Q_OBJECT

public:
    explicit CaptureWindow(QWidget *parent = nullptr);
    ~CaptureWindow();

private:
    Ui::CaptureWindow *ui;
};

#endif // CAPTUREWINDOW_H
