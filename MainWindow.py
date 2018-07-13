# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\main-window.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(610, 760)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(430, 20, 160, 491))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.deviceListComboBox = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.deviceListComboBox.setObjectName("deviceListComboBox")
        self.verticalLayout.addWidget(self.deviceListComboBox)
        self.refreshDeviceButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.refreshDeviceButton.setObjectName("refreshDeviceButton")
        self.verticalLayout.addWidget(self.refreshDeviceButton)
        self.showVirtualKeyButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.showVirtualKeyButton.setObjectName("showVirtualKeyButton")
        self.verticalLayout.addWidget(self.showVirtualKeyButton)
        self.screencapButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.screencapButton.setObjectName("screencapButton")
        self.verticalLayout.addWidget(self.screencapButton)
        self.pressMenuButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pressMenuButton.setObjectName("pressMenuButton")
        self.verticalLayout.addWidget(self.pressMenuButton)
        self.homeButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.homeButton.setObjectName("homeButton")
        self.verticalLayout.addWidget(self.homeButton)
        self.backButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.backButton.setObjectName("backButton")
        self.verticalLayout.addWidget(self.backButton)
        self.powerButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.powerButton.setObjectName("powerButton")
        self.verticalLayout.addWidget(self.powerButton)
        self.volumeUpButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.volumeUpButton.setObjectName("volumeUpButton")
        self.verticalLayout.addWidget(self.volumeUpButton)
        self.volumeDownButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.volumeDownButton.setObjectName("volumeDownButton")
        self.verticalLayout.addWidget(self.volumeDownButton)
        self.muteButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.muteButton.setObjectName("muteButton")
        self.verticalLayout.addWidget(self.muteButton)
        self.currentActivityButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.currentActivityButton.setObjectName("currentActivityButton")
        self.verticalLayout.addWidget(self.currentActivityButton)
        self.outputTextEdit = QtWidgets.QTextEdit(self.verticalLayoutWidget)
        self.outputTextEdit.setObjectName("outputTextEdit")
        self.verticalLayout.addWidget(self.outputTextEdit)
        self.screencapView = QtWidgets.QLabel(self.centralwidget)
        self.screencapView.setGeometry(QtCore.QRect(20, 10, 381, 741))
        self.screencapView.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.screencapView.setObjectName("screencapView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.refreshDeviceButton.setText(_translate("MainWindow", "刷新设备列表"))
        self.showVirtualKeyButton.setText(_translate("MainWindow", "显示虚拟按键"))
        self.screencapButton.setText(_translate("MainWindow", "截屏"))
        self.pressMenuButton.setText(_translate("MainWindow", "MENU"))
        self.homeButton.setText(_translate("MainWindow", "HOME"))
        self.backButton.setText(_translate("MainWindow", "BACK"))
        self.powerButton.setText(_translate("MainWindow", "电源键"))
        self.volumeUpButton.setText(_translate("MainWindow", "音量+"))
        self.volumeDownButton.setText(_translate("MainWindow", "音量-"))
        self.muteButton.setText(_translate("MainWindow", "静音"))
        self.currentActivityButton.setText(_translate("MainWindow", "当前Activity"))
        self.screencapView.setText(_translate("MainWindow", "截图显示区"))

