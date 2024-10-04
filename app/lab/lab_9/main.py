import sys

from PyQt5.QtWidgets import QApplication

from app.lab.lab_9.tree_app import TreeApp


def main():
    app = QApplication(sys.argv)
    window = TreeApp()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
