#include <iostream>
#include <QApplication>
#include "mainwindow.h"

int main(int argc, char *argv[])
{
    std::cout<<"commute management"<<std::endl;

    QApplication app(argc, argv);
    MainWindow main_window;
    main_window.show();

    return app.exec();
}
