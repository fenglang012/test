import sys

import Ui_main_windows

from tkinter import dialog

from PyQt5.QtWidgets import (QApplication, QDialog, QMainWindow, QMessageBox)

from PyQt5.uic import loadUi



class Window(QMainWindow, Ui_main_windows.Ui_MainWindow):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.connectSignalsSlots()

    def connectSignalsSlots(self):
        self.action_Exit.triggered.connect(self.close)
        self.action_Find_Replace.triggered.connect(self.findAndReplace)

    def findAndReplace(self):
        dialog = FindReplaceDialog(self)
        dialog.exec()

class FindReplaceDialog(QDialog):
    def __init__(self, parent = None):
        super().__init__(parent)
        loadUi("sample_editor/ui/find_replace.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec())