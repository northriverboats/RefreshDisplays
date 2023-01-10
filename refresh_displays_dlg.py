# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'refresh_display_dlgyUesMN.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QGroupBox, QLabel,
    QPushButton, QSizePolicy, QWidget)
import refesh_displays_resources_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(536, 547)
        self.pushButton_refresh = QPushButton(Dialog)
        self.pushButton_refresh.setObjectName(u"pushButton_refresh")
        self.pushButton_refresh.setGeometry(QRect(310, 225, 201, 50))
        font = QFont()
        font.setPointSize(14)
        self.pushButton_refresh.setFont(font)
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(20, 20, 271, 511))
        self.groupBox_display_0 = QGroupBox(self.groupBox)
        self.groupBox_display_0.setObjectName(u"groupBox_display_0")
        self.groupBox_display_0.setGeometry(QRect(10, 30, 251, 61))
        self.label_led_0 = QLabel(self.groupBox_display_0)
        self.label_led_0.setObjectName(u"label_led_0")
        self.label_led_0.setGeometry(QRect(10, 30, 21, 21))
        self.label_led_0.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_0.setScaledContents(True)
        self.label_description_0 = QLabel(self.groupBox_display_0)
        self.label_description_0.setObjectName(u"label_description_0")
        self.label_description_0.setGeometry(QRect(40, 30, 81, 16))
        self.groupBox_display_1 = QGroupBox(self.groupBox)
        self.groupBox_display_1.setObjectName(u"groupBox_display_1")
        self.groupBox_display_1.setGeometry(QRect(10, 110, 251, 61))
        self.label_led_1 = QLabel(self.groupBox_display_1)
        self.label_led_1.setObjectName(u"label_led_1")
        self.label_led_1.setGeometry(QRect(10, 30, 21, 21))
        self.label_led_1.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_1.setScaledContents(True)
        self.label_description_1 = QLabel(self.groupBox_display_1)
        self.label_description_1.setObjectName(u"label_description_1")
        self.label_description_1.setGeometry(QRect(40, 30, 111, 16))
        self.groupBox_display_2 = QGroupBox(self.groupBox)
        self.groupBox_display_2.setObjectName(u"groupBox_display_2")
        self.groupBox_display_2.setGeometry(QRect(10, 190, 251, 61))
        self.label_led_2 = QLabel(self.groupBox_display_2)
        self.label_led_2.setObjectName(u"label_led_2")
        self.label_led_2.setGeometry(QRect(10, 30, 21, 21))
        self.label_led_2.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_2.setScaledContents(True)
        self.label_description_2 = QLabel(self.groupBox_display_2)
        self.label_description_2.setObjectName(u"label_description_2")
        self.label_description_2.setGeometry(QRect(40, 30, 81, 16))
        self.groupBox_display_3 = QGroupBox(self.groupBox)
        self.groupBox_display_3.setObjectName(u"groupBox_display_3")
        self.groupBox_display_3.setGeometry(QRect(10, 270, 251, 61))
        self.label_led_4 = QLabel(self.groupBox_display_3)
        self.label_led_4.setObjectName(u"label_led_4")
        self.label_led_4.setGeometry(QRect(10, 30, 21, 21))
        self.label_led_4.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_4.setScaledContents(True)
        self.label_description_4 = QLabel(self.groupBox_display_3)
        self.label_description_4.setObjectName(u"label_description_4")
        self.label_description_4.setGeometry(QRect(40, 30, 91, 16))
        self.groupBox_display_4 = QGroupBox(self.groupBox)
        self.groupBox_display_4.setObjectName(u"groupBox_display_4")
        self.groupBox_display_4.setGeometry(QRect(10, 350, 241, 61))
        self.label_led_5 = QLabel(self.groupBox_display_4)
        self.label_led_5.setObjectName(u"label_led_5")
        self.label_led_5.setGeometry(QRect(10, 30, 21, 21))
        self.label_led_5.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_5.setScaledContents(True)
        self.label_description_5 = QLabel(self.groupBox_display_4)
        self.label_description_5.setObjectName(u"label_description_5")
        self.label_description_5.setGeometry(QRect(40, 30, 151, 16))
        self.groupBox_display_5 = QGroupBox(self.groupBox)
        self.groupBox_display_5.setObjectName(u"groupBox_display_5")
        self.groupBox_display_5.setGeometry(QRect(10, 430, 241, 61))
        self.label_led_6 = QLabel(self.groupBox_display_5)
        self.label_led_6.setObjectName(u"label_led_6")
        self.label_led_6.setGeometry(QRect(10, 30, 21, 21))
        self.label_led_6.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.label_led_6.setScaledContents(True)
        self.label_description_6 = QLabel(self.groupBox_display_5)
        self.label_description_6.setObjectName(u"label_description_6")
        self.label_description_6.setGeometry(QRect(40, 30, 151, 16))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"NRB Refresh Factory Displays", None))
        self.pushButton_refresh.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Factory Displays", None))
        self.groupBox_display_0.setTitle(QCoreApplication.translate("Dialog", u"Display 00", None))
        self.label_led_0.setText("")
        self.label_description_0.setText(QCoreApplication.translate("Dialog", u"Front Office", None))
        self.groupBox_display_1.setTitle(QCoreApplication.translate("Dialog", u"Display 01", None))
        self.label_led_1.setText("")
        self.label_description_1.setText(QCoreApplication.translate("Dialog", u"Outfitting Shop", None))
        self.groupBox_display_2.setTitle(QCoreApplication.translate("Dialog", u"Display 02", None))
        self.label_led_2.setText("")
        self.label_description_2.setText(QCoreApplication.translate("Dialog", u"Paint Shop", None))
        self.groupBox_display_3.setTitle(QCoreApplication.translate("Dialog", u"Display 03", None))
        self.label_led_4.setText("")
        self.label_description_4.setText(QCoreApplication.translate("Dialog", u"Canvas Shop", None))
        self.groupBox_display_4.setTitle(QCoreApplication.translate("Dialog", u"Display 04", None))
        self.label_led_5.setText("")
        self.label_description_5.setText(QCoreApplication.translate("Dialog", u"Samll Fabircation Shop", None))
        self.groupBox_display_5.setTitle(QCoreApplication.translate("Dialog", u"Display 05", None))
        self.label_led_6.setText("")
        self.label_description_6.setText(QCoreApplication.translate("Dialog", u"Large Fabrication Shop", None))
    # retranslateUi

