from PyQt5.QtWidgets import QMainWindow, QLineEdit, QPushButton, QLabel

from app.lab.lab_9.tree import Tree
from app.lab.lab_9.tree_visualizer import TreeVisualizer


# noinspection SpellCheckingInspection
class TreeApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.tree2 = None
        self.visualizer = None
        self.tree = Tree()
        self.setWindowTitle('Binary Search Tree')
        self.setGeometry(100, 100, 400, 300)

        self.input_box = QLineEdit(self)
        self.input_box.setPlaceholderText('Введите числа через пробел')
        self.input_box.setGeometry(50, 50, 300, 30)

        self.button_add = QPushButton('Создать дерево', self)
        self.button_add.setGeometry(50, 100, 150, 30)
        # noinspection PyUnresolvedReferences
        self.button_add.clicked.connect(self.create_tree)

        self.button_check_bst = QPushButton('Проверить BST', self)
        self.button_check_bst.setGeometry(50, 150, 150, 30)
        # noinspection PyUnresolvedReferences
        self.button_check_bst.clicked.connect(self.check_bst)

        self.result_label = QLabel(self)
        self.result_label.setGeometry(50, 200, 300, 30)

        self.button_draw = QPushButton('Нарисовать дерево', self)
        self.button_draw.setGeometry(50, 250, 150, 30)
        # noinspection PyUnresolvedReferences
        self.button_draw.clicked.connect(self.draw_tree)

    def create_tree(self):
        sequence = list(map(int, self.input_box.text().split()))
        for num in sequence:
            self.tree.insert(num)
        self.tree.save_to_file('tree.dat')

    def check_bst(self):
        is_bst = self.tree.is_bst()
        self.result_label.setText(f'Это BST: {is_bst}')

    def draw_tree(self):
        self.visualizer = TreeVisualizer(self.tree)
        self.visualizer.show()

    def merge_trees(self):
        new_tree = self.tree.merge_trees_with_primes(self.tree2)
        self.result_label.setText('Дерево объединено и сохранено в tree.res')
