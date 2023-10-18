import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QDialog, QApplication


class MyForm(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi('layout.ui', self)

        self.show()

    def displayFare(self):
        fare = 0
        if self.ui.radioFirst.isChecked():
            fare = 8000
        elif self.ui.radioBuisness.isChecked():
            fare = 4000
        elif self.ui.radioEconomy.isChecked():
            fare = 1500
        self.ui.priceLabel.setText("Cena lotu wynosi: "+ str(fare) +" zł")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyForm()
    w.show()
    sys.exit(app.exec())