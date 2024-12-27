# This Python file uses the following encoding: utf-8
import sys
from datetime import datetime
from PySide6.QtWidgets import QApplication, QMainWindow
import PySide6.QtGui as QtGui
import PySide6.QtCore as QtCore

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        fontClock = QtGui.QFont()
        fontClock.setPointSize(32)
        fontDate = QtGui.QFont()
        fontDate.setPointSize(16)
        time = datetime.now()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.label.setStyleSheet("font-weight: bold")
        self.ui.label.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label.setFont(fontClock)
        self.ui.label.setText(time.strftime('%I:%M %p'))

        self.ui.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.label_2.setFont(fontDate)
        self.ui.label_2.setText(time.strftime('%A %B %d'))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
