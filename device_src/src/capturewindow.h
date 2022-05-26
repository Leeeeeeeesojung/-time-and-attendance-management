#ifndef CAPTUREWINDOW_H
#define CAPTUREWINDOW_H

#include <QWidget>
#include <QLabel>

namespace Ui {
class CaptureWindow;
}

class CaptureWindow : public QWidget
{
    Q_OBJECT

public:
    explicit CaptureWindow(QWidget *parent = nullptr);
    ~CaptureWindow();

    QLabel* plabel_frame;

private:
    Ui::CaptureWindow *ui;

    bool eventFilter(QObject *object, QEvent *event);

signals:
    void face_capture();
};

#endif // CAPTUREWINDOW_H
