"""
Test
"""

import sys

from PyQt6.QtWidgets import QApplication, QMainWindow

from .main_window_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    """Test"""

    def __init__(self):
        """MainWindow constructor.
        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(lambda: self.ui.label.setText("Pushed"))


def test_window():
    """Quick test"""
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    test_window()
