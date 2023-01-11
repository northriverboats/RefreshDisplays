# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'refresh_displays_dlg.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import icons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(506, 397)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 461, 321))
        self.groupBox_display_0 = QGroupBox(self.groupBox)
        self.groupBox_display_0.setObjectName(u"groupBox_display_0")
        self.groupBox_display_0.setGeometry(QRect(20, 30, 191, 71))
        self.label_led_0 = QLabel(self.groupBox_display_0)
        self.label_led_0.setObjectName(u"label_led_0")
        self.label_led_0.setGeometry(QRect(20, 30, 21, 21))
        self.label_led_0.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_0.setScaledContents(True)
        self.label_display_0 = QLabel(self.groupBox_display_0)
        self.label_display_0.setObjectName(u"label_display_0")
        self.label_display_0.setGeometry(QRect(50, 30, 131, 16))
        self.groupBox_display_1 = QGroupBox(self.groupBox)
        self.groupBox_display_1.setObjectName(u"groupBox_display_1")
        self.groupBox_display_1.setGeometry(QRect(20, 120, 191, 71))
        self.label_led_1 = QLabel(self.groupBox_display_1)
        self.label_led_1.setObjectName(u"label_led_1")
        self.label_led_1.setGeometry(QRect(20, 30, 21, 21))
        self.label_led_1.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_1.setScaledContents(True)
        self.label_display_1 = QLabel(self.groupBox_display_1)
        self.label_display_1.setObjectName(u"label_display_1")
        self.label_display_1.setGeometry(QRect(50, 30, 131, 16))
        self.groupBox_display_2 = QGroupBox(self.groupBox)
        self.groupBox_display_2.setObjectName(u"groupBox_display_2")
        self.groupBox_display_2.setGeometry(QRect(20, 210, 191, 71))
        self.label_led_2 = QLabel(self.groupBox_display_2)
        self.label_led_2.setObjectName(u"label_led_2")
        self.label_led_2.setGeometry(QRect(20, 30, 21, 21))
        self.label_led_2.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_2.setScaledContents(True)
        self.label_display_2 = QLabel(self.groupBox_display_2)
        self.label_display_2.setObjectName(u"label_display_2")
        self.label_display_2.setGeometry(QRect(50, 30, 131, 16))
        self.groupBox_display_3 = QGroupBox(self.groupBox)
        self.groupBox_display_3.setObjectName(u"groupBox_display_3")
        self.groupBox_display_3.setGeometry(QRect(240, 30, 191, 71))
        self.label_led_3 = QLabel(self.groupBox_display_3)
        self.label_led_3.setObjectName(u"label_led_3")
        self.label_led_3.setGeometry(QRect(20, 30, 21, 21))
        self.label_led_3.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_3.setScaledContents(True)
        self.label_display_3 = QLabel(self.groupBox_display_3)
        self.label_display_3.setObjectName(u"label_display_3")
        self.label_display_3.setGeometry(QRect(50, 30, 131, 16))
        self.groupBox_display_4 = QGroupBox(self.groupBox)
        self.groupBox_display_4.setObjectName(u"groupBox_display_4")
        self.groupBox_display_4.setGeometry(QRect(240, 120, 191, 71))
        self.label_led_4 = QLabel(self.groupBox_display_4)
        self.label_led_4.setObjectName(u"label_led_4")
        self.label_led_4.setGeometry(QRect(20, 30, 21, 21))
        self.label_led_4.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_4.setScaledContents(True)
        self.label_display_4 = QLabel(self.groupBox_display_4)
        self.label_display_4.setObjectName(u"label_display_4")
        self.label_display_4.setGeometry(QRect(50, 30, 131, 16))
        self.groupBox_display_5 = QGroupBox(self.groupBox)
        self.groupBox_display_5.setObjectName(u"groupBox_display_5")
        self.groupBox_display_5.setGeometry(QRect(240, 210, 191, 71))
        self.label_led_5 = QLabel(self.groupBox_display_5)
        self.label_led_5.setObjectName(u"label_led_5")
        self.label_led_5.setGeometry(QRect(20, 30, 21, 21))
        self.label_led_5.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_5.setScaledContents(True)
        self.label_display_5 = QLabel(self.groupBox_display_5)
        self.label_display_5.setObjectName(u"label_display_5")
        self.label_display_5.setGeometry(QRect(50, 30, 131, 16))
        self.pushButton_refresh = QPushButton(Dialog)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setGeometry(QRect(374, 352, 111, 31))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"NRB Refresh Factory Displays", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Factory Displays", None))
        self.groupBox_display_0.setTitle(QCoreApplication.translate("Dialog", u"Display 00", None))
        self.label_led_0.setText("")
        self.label_display_0.setText(QCoreApplication.translate("Dialog", u"Reception Area", None))
        self.groupBox_display_1.setTitle(QCoreApplication.translate("Dialog", u"Display 01", None))
        self.label_led_1.setText("")
        self.label_display_1.setText(QCoreApplication.translate("Dialog", u"Outfitting Shop", None))
        self.groupBox_display_2.setTitle(QCoreApplication.translate("Dialog", u"Display 02", None))
        self.label_led_2.setText("")
        self.label_display_2.setText(QCoreApplication.translate("Dialog", u"Paint Shop", None))
        self.groupBox_display_3.setTitle(QCoreApplication.translate("Dialog", u"Display 03", None))
        self.label_led_3.setText("")
        self.label_display_3.setText(QCoreApplication.translate("Dialog", u"Canvas Shop", None))
        self.groupBox_display_4.setTitle(QCoreApplication.translate("Dialog", u"Display 04", None))
        self.label_led_4.setText("")
        self.label_display_4.setText(QCoreApplication.translate("Dialog", u"Small Fab Shop", None))
        self.groupBox_display_5.setTitle(QCoreApplication.translate("Dialog", u"Display 05", None))
        self.label_led_5.setText("")
        self.label_display_5.setText(QCoreApplication.translate("Dialog", u"Commercial Fab Shop", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Dialog", u"Refresh Displays", None))
    # retranslateUi

