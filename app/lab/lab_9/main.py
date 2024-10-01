import sys

from PyQt5.QtWidgets import QApplication

from app.lab.lab_9.tree_app import TreeApp

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TreeApp()
    window.show()
    sys.exit(app.exec_())