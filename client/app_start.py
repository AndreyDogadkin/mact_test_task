import sys

from PyQt6.QtWidgets import QApplication

from app.ui.main_window import AppMainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppMainWindow()
    window.show()
    sys.exit(app.exec())
