# main.py
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from PyQt5.QtWidgets import QApplication
from database import init_db
from GUI.public_view import PublicView

if __name__ == '__main__':
    init_db()
    app = QApplication(sys.argv)
    window = PublicView()  # hiển thị giao diện công khai trước
    window.show()
    sys.exit(app.exec_())
