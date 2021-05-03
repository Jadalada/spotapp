# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assets/mainframe.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import Qt
from spotfuncs import *
import time


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__(parent)
        self.setMouseTracking(True)

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        self.usize = QtCore.QSize(90, 90)
        self.osize = QtCore.QSize(35, 35)
        MainWindow.resize(700, 700)
        MainWindow.setStyleSheet("background-color: rgb(30, 30, 30);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.duration_label = QtWidgets.QLabel(self.centralwidget)
        self.duration_label.setGeometry(QtCore.QRect(75, 515, 60, 16))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(14)
        self.duration_label.setFont(font)
        self.duration_label.setStyleSheet("color:rgb(255, 255, 255); background-color:rgba(0,0,0,0) ")
        self.duration_label.setObjectName("duration_label")
        self.duration_slider = QtWidgets.QSlider(self.centralwidget)
        self.duration_slider.setGeometry(QtCore.QRect(75, 490, 550, 25))
        self.duration_slider.setStyleSheet("background-color:rgba(0,0,0,0)")
        self.duration_slider.setMaximum(100)
        self.duration_slider.setSingleStep(1)
        self.duration_slider.setProperty("value", 50)
        self.duration_slider.setSliderPosition(50)
        self.duration_slider.setOrientation(QtCore.Qt.Horizontal)
        self.duration_slider.setObjectName("duration_slider")

        self.artistname = QtWidgets.QLabel(self.centralwidget)
        self.artistname.setGeometry(QtCore.QRect(150, 341, 400, 25))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(18)
        self.artistname.setFont(font)
        self.artistname.setMouseTracking(True)
        self.artistname.setAccessibleDescription("")
        self.artistname.setStyleSheet("background-color:rgba(108,108,108,50) ")
        self.artistname.setText(
            "<html><head/><body><p><span style=\" color:#6c6c6c;\">artist_name_placeholder</span></p></body></html>")
        self.artistname.setScaledContents(False)
        self.artistname.setAlignment(QtCore.Qt.AlignCenter)
        self.artistname.setObjectName("artistname")
        self.songname = QtWidgets.QLabel(self.centralwidget)
        self.songname.setGeometry(QtCore.QRect(150, 300, 400, 33))
        font = QtGui.QFont()
        font.setFamily("Avenir")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.songname.setFont(font)
        self.songname.setMouseTracking(True)
        self.songname.setAccessibleDescription("")
        self.songname.setStyleSheet("background-color:rgba(108,108,108,50) ")
        self.songname.setText(
            "<html><head/><body><p><span style=\" color:#ffffff;\">song_name_placeholder</span></p></body></html>")
        self.songname.setScaledContents(False)
        self.songname.setAlignment(QtCore.Qt.AlignCenter)
        self.songname.setObjectName("songname")

        # BACK BUTTON
        self.b_back = QtWidgets.QPushButton(self.centralwidget)
        self.b_back.setGeometry(QtCore.QRect(150, 380, 100, 100))
        self.b_back.setAcceptDrops(False)
        self.b_back.setAccessibleDescription("")
        self.b_back.setAutoFillBackground(False)
        self.b_back.setText("")
        self.b_back.setCheckable(False)
        self.b_back.setDefault(False)
        self.b_back.setFlat(True)
        self.b_back.setObjectName("b_back")
        self.b_back.setIcon(QtGui.QIcon('assets/back.png'))
        self.b_back.setIconSize(self.osize)
        self.b_back.setStyleSheet("background-color:rgba(0,0,0,0) ")

        # PLAY OR PAUSE BUTTON
        self.b_playpause = QtWidgets.QPushButton(self.centralwidget)
        self.b_playpause.setGeometry(QtCore.QRect(300, 380, 100, 100))
        self.b_playpause.setAcceptDrops(False)
        self.b_playpause.setAccessibleDescription("")
        self.b_playpause.setAutoFillBackground(False)
        self.b_playpause.setText("")
        self.b_playpause.setCheckable(False)
        self.b_playpause.setDefault(False)
        self.b_playpause.setFlat(True)
        self.b_playpause.setObjectName("b_playpause")
        self.b_playpause.setIcon(QtGui.QIcon('assets/play.png'))
        self.b_playpause.setIconSize(self.usize)
        self.b_playpause.setStyleSheet("background-color:rgba(0,0,0,0) ")

        # SEEK BUTTON
        self.b_forward = QtWidgets.QPushButton(self.centralwidget)
        self.b_forward.setGeometry(QtCore.QRect(450, 380, 100, 100))
        self.b_forward.setAcceptDrops(False)
        self.b_forward.setAccessibleDescription("")
        self.b_forward.setAutoFillBackground(False)
        self.b_forward.setText("")
        self.b_forward.setCheckable(False)
        self.b_forward.setDefault(False)
        self.b_forward.setFlat(True)
        self.b_forward.setObjectName("b_forward")
        self.b_forward.setIcon(QtGui.QIcon('assets/forward.png'))
        self.b_forward.setIconSize(self.osize)
        self.b_forward.setStyleSheet("background-color:rgba(0,0,0,0) ")

        # SHUFFLE BUTTON
        self.b_shuffle = QtWidgets.QPushButton(self.centralwidget)
        self.b_shuffle.setGeometry(QtCore.QRect(220, 520, 100, 100))
        self.b_shuffle.setAcceptDrops(False)
        self.b_shuffle.setAccessibleDescription("")
        self.b_shuffle.setAutoFillBackground(False)
        self.b_shuffle.setText("")
        self.b_shuffle.setCheckable(False)
        self.b_shuffle.setDefault(False)
        self.b_shuffle.setFlat(True)
        self.b_shuffle.setObjectName("b_shuffle")
        self.b_shuffle.setIcon(QtGui.QIcon('assets/shuffle.png'))
        self.b_shuffle.setIconSize(self.osize)
        self.b_shuffle.setStyleSheet("background-color:rgba(0,0,0,0) ")

        # REPEAT BUTTON
        self.b_repeat = QtWidgets.QPushButton(self.centralwidget)
        self.b_repeat.setGeometry(QtCore.QRect(380, 520, 100, 100))
        self.b_repeat.setAcceptDrops(False)
        self.b_repeat.setAccessibleDescription("")
        self.b_repeat.setAutoFillBackground(False)
        self.b_repeat.setText("")
        self.b_repeat.setCheckable(False)
        self.b_repeat.setDefault(False)
        self.b_repeat.setFlat(True)
        self.b_repeat.setObjectName("b_repeat")
        self.b_repeat.setIcon(QtGui.QIcon('assets/repeat.png'))
        self.b_repeat.setIconSize(self.osize)
        self.b_repeat.setStyleSheet("background-color:rgba(0,0,0,0) ")

        # ALBUM ART
        self.albumart = QtWidgets.QLabel(self.centralwidget)
        self.albumart.setGeometry(QtCore.QRect(50, 50, 600, 600))
        self.albumart.setText("")
        self.albumart.setObjectName("albumart")

        # BLUR EFFECT
        self.blur = QtWidgets.QGraphicsBlurEffect()
        self.blur.setBlurRadius(5)
        self.albumart.setGraphicsEffect(self.blur)

        self.albumart.raise_()
        self.duration_label.raise_()
        self.duration_slider.raise_()
        self.b_back.raise_()
        self.b_playpause.raise_()
        self.b_forward.raise_()
        self.b_shuffle.raise_()
        self.b_repeat.raise_()
        self.artistname.raise_()
        self.songname.raise_()

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # DEFINE FUNCTIONS
        sn = get_song_name
        an = get_artists
        dur = get_duration
        durs = get_progress_percent

        # SONG NAME THREAD
        self.workersn = SWorker(sn, 1)
        self.workersn.start()
        self.workersn.update.connect(self.update_sn)

        # ARTIST NAME THREAD
        self.workeran = SWorker(an, 1)
        self.workeran.start()
        self.workeran.update.connect(self.update_an)

        # DURATION THREAD
        self.workerdur = SWorker(dur, 0.5)
        self.workerdur.start()
        self.workerdur.update.connect(self.update_dur)

        # DURATION THREAD
        self.workerdurs = SWorker(durs, 0.5)
        self.workerdurs.start()
        self.workerdurs.update.connect(self.update_durs)

        # ALBUM ART THREAD
        self.workeraa = SWorker(get_album_img, 2)
        self.workeraa.start()
        self.workeraa.update.connect(self.update_img)

        # UPDATE FUNCTIONS FOR CONNECTING SLOTS-SIGNALS

    def update_sn(self, val):
        self.songname.setText(f"<html><head/><body><p><span style=\" color:white;\">{val}</span></p></body></html>")

    def update_an(self, val):
        self.artistname.setText(f"<span style=color:#FBFCF8;>{val}</span>")

    def update_dur(self, val):
        self.duration_label.setText(f"<span style=color:white;>{val}</span>")

    def update_durs(self, val):
        self.duration_slider.setValue(int(val))

    def update_img(self, val):
        val = get_album_img()
        image = QtGui.QImage()
        try:
            image.loadFromData(val)
            pix = QtGui.QPixmap(image)
            self.albumart.setPixmap(pix)
        except TypeError:
            self.albumart.setPixmap(QtGui.QPixmap('assets/unknown.png'))

    # this un-needingly resets ui elements but app breaks if i delete
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.duration_label.setText(_translate("MainWindow", "0:00"))

    def enterEvent(self, event):
        print("Mouse")
        return QtWidgets.enterEvent(self, event)


# WORKER CLASS FOR CREATING QThread(s) TO UPDATE GUI
class SWorker(QThread):
    update = pyqtSignal(str)

    def __init__(self, func, timerest, parent=None):
        super().__init__(parent)  # need to call super() or app breaks idk
        self.func = func
        self.timerest = timerest

    def run(self):
        while True:
            n = str(self.func())
            self.update.emit(n)
            time.sleep(self.timerest)  # TIME SLEEP SET TO 0.9 INSTEAD OF 1 CAUSE APP BREAKS IF I DONT


# WORKER CLASS FOR MOUSE
class MWorker(QThread):
    update = pyqtSignal()
