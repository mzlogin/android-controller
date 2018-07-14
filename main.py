# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPixmap
from MainWindow import Ui_MainWindow
from adb_util import *


class Wnd(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle('Android Controller')
        self.bindEvents()

        self.setAcceptDrops(True)

        self.adb = AdbUtil()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and str(urls[0].toLocalFile()).endswith('.apk'):
                event.acceptProposedAction()
            else:
                super(QMainWindow, self).dragEnterEvent(event)
        else:
            super(QMainWindow, self).dragEnterEvent(event)

    def dragMoveEvent(self, event):
        super(QMainWindow, self).dragMoveEvent(event)

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            urls = event.mimeData().urls()
            if len(urls) == 1 and str(urls[0].toLocalFile()).endswith('.apk'):
                self.installApk(str(urls[0].toLocalFile()))
                event.acceptProposedAction()
            else:
                super(QMainWindow, self).dropEvent(event)
        else:
            super(QMainWindow, self).dropEvent(event)

    def bindEvents(self):
        self.refreshDeviceButton.clicked.connect(self.onRefreshDevice)
        self.showVirtualKeyButton.clicked.connect(self.onShowVirtualKeys)
        self.screencapButton.clicked.connect(self.onScreencap)
        self.pressMenuButton.clicked.connect(self.onMenuPressed)
        self.homeButton.clicked.connect(self.onHomePressed)
        self.backButton.clicked.connect(self.onBackPressed)
        self.powerButton.clicked.connect(self.onPowerPressed)
        self.volumeUpButton.clicked.connect(self.onVolumeUpPressed)
        self.volumeDownButton.clicked.connect(self.onVolumeDownPressed)
        self.muteButton.clicked.connect(self.onMutePressed)
        self.currentActivityButton.clicked.connect(self.onGetCurrentActivity)

    def onRefreshDevice(self):
        self.deviceListComboBox.clear()
        lst = self.adb.get_device_list()
        if lst is not None:
            self.deviceListComboBox.addItems(lst)

    def onShowVirtualKeys(self):
        if not self.checkCurrentDevice():
            return

        self.adb.show_virtual_keys()

    def onScreencap(self):
        if not self.checkCurrentDevice():
            return

        imageName = 'sc.png'
        if self.adb.screencap(imageName):
            png = QPixmap(imageName)
            png = png.scaledToWidth(self.screencapView.width())
            self.screencapView.setPixmap(png)
        else:
            self.setOutput('截屏失败')

    def onMenuPressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.press_menu()

    def onHomePressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.press_home()

    def onBackPressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.press_back()

    def onPowerPressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.press_power()

    def onVolumeUpPressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.volume_up()

    def onVolumeDownPressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.volume_down()

    def onMutePressed(self):
        if not self.checkCurrentDevice():
            return

        self.adb.mute()

    def onGetCurrentActivity(self):
        if not self.checkCurrentDevice():
            return

        output = self.adb.get_current_focused_activity()
        self.setOutput(output)

    def installApk(self, apk):
        if not self.checkCurrentDevice():
            return

        if self.adb.install_apk(apk):
            self.setOutput('安装应用成功')
        else:
            self.setOutput('安装应用失败')

    def setOutput(self, output):
        self.outputTextEdit.setText(output)

    def checkCurrentDevice(self):
        text = self.deviceListComboBox.currentText()
        if len(text) == 0:
            self.setOutput('no device selected')
            return False
        self.adb.set_device(text)
        return True


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Wnd()
    window.show()
    sys.exit(app.exec_())
