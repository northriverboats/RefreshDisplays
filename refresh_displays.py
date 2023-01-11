import os
import sys
from PySide2.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton
from PySide2.QtGui import QPixmap, QIcon
from refresh_displays_dlg import Ui_Dialog
from vncdotool import api

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)



class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_refresh.clicked.connect(self.refresh_displays)

        appIcon = QIcon(resource_path("refresh_displays.png"))
        self.setWindowIcon(appIcon)

    def refresh_displays(self, e):
        self.clear_leds()
        self.refresh_display("display00",self.ui.label_led_0)
        self.refresh_display("display01",self.ui.label_led_1)
        self.refresh_display("display02",self.ui.label_led_2)
        self.refresh_display("display03",self.ui.label_led_3)
        self.refresh_display("display04",self.ui.label_led_4)
        self.refresh_display("display05",self.ui.label_led_5)
		
    def closeEvent(self, e):
        e.accept()

    def clear_leds(self):
        self.ui.label_led_0.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.ui.label_led_1.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.ui.label_led_2.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.ui.label_led_3.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.ui.label_led_4.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))
        self.ui.label_led_5.setPixmap(QPixmap(u":/icons/icons/grey-led-off.png"))

    def refresh_display(self, display, led):
        with api.connect(display) as client:
            client.temeout = 5
            try:
                led.setPixmap(QPixmap(u":/icons/icons/blue-led-on.png"))
                QApplication.processEvents()
                client.keyPress('ctrl-w')
                led.setPixmap(QPixmap(u":/icons/icons/green-led-on.png"))
            except api.VNCDoException:
                led.setPixmap(QPixmap(u":/icons/icons/red-led-on.png"))
		

if __name__ == "__main__":
    application = QApplication()
    dialog = Dialog()
    dialog.show()
    sys.exit(application.exec_())
