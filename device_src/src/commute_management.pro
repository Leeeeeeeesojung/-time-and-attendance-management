QT += core gui widgets

CONFIG += c++11

SOURCES += \
    capturewindow.cpp \
    eCAM130_TRICUTX2.cpp \
    main.cpp \
    mainwindow.cpp \
    signupwindow.cpp

FORMS += \
    capturewindow.ui \
    mainwindow.ui \
    signupwindow.ui

HEADERS += \
    capturewindow.h \
    eCAM130_TRICUTX2.h \
    eCAM130_common.h \
    mainwindow.h \
    signupwindow.h

LIBS += `pkg-config opencv --libs` \
-lv4l2 \
-lusb-1.0 -ludev
