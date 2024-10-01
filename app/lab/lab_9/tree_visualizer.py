from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QMainWindow


class TreeVisualizer(QMainWindow):
    def __init__(self, tree):
        super().__init__()
        self.tree = tree
        self.setWindowTitle('Binary Search Tree Visualizer')
        self.setGeometry(100, 100, 600, 400)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
        if self.tree.root is not None:
            self.draw_node(painter, self.tree.root, self.width() // 2, 50, 200)

    def draw_node(self, painter, node, x, y, offset):
        if node is not None:
            painter.drawEllipse(x - 15, y - 15, 30, 30)
            painter.drawText(x - 10, y + 5, str(node.value))
            if node.left:
                painter.drawLine(x, y, x - offset, y + 50)
                self.draw_node(painter, node.left, x - offset, y + 50, offset // 2)
            if node.right:
                painter.drawLine(x, y, x + offset, y + 50)
                self.draw_node(painter, node.right, x + offset, y + 50, offset // 2)