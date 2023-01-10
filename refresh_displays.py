import sys
from PySide6.QtWidgets import QApplication, QDialog
from PySide6.QtGui import QPixmap
from refresh_displays_dlg import Ui_Dialog

class Dialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_refresh.clicked.connect(self.refresh_displays)


    def refresh_displays(self, e):
        self.ui.label_led_0.setPixmap(QPixmap(u":/icons/icons/red-led-on.png"))
        self.ui.label_led_1.setPixmap(QPixmap(u":/icons/icons/green-led-on.png"))
        self.ui.label_led_2.setPixmap(QPixmap(u":/icons/icons/blue-led-on.png"))

    def closeEvent(self, e):
        e.accept()


if __name__ == "__main__":
    application = QApplication()
    dialog = Dialog()
    dialog.show()
    sys.exit(application.exec())
