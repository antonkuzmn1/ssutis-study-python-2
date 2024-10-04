from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QLabel, QPushButton

from app.lab.lab_9.tree import Tree


# noinspection PyUnresolvedReferences,SpellCheckingInspection
class TreeApp(QWidget):
    def __init__(self):
        super().__init__()
        self.label_n = None
        self.n_edit = None
        self.save_button = None
        self.count_non_multiples_button = None
        self.prime_tree_button = None
        self.insert_button2 = None
        self.check_bst_button = None
        self.insert_button = None
        self.label_result = None
        self.label_input2 = None
        self.label_input = None
        self.result_edit = None
        self.input_edit2 = None
        self.input_edit = None
        self.tree = Tree()
        self.tree2 = Tree()
        self.result_tree = None
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.input_edit = QLineEdit(self)
        self.input_edit2 = QLineEdit(self)
        self.result_edit = QLineEdit(self)
        self.result_edit.setReadOnly(True)

        self.n_edit = QLineEdit(self)

        self.label_input = QLabel("Введите последовательность для 1-го дерева:", self)
        self.label_input2 = QLabel("Введите последовательность для 2-го дерева:", self)
        self.label_n = QLabel("Введите значение n:", self)
        self.label_result = QLabel("Результат:", self)

        self.insert_button = QPushButton("Вставить последовательность в 1-е дерево", self)
        self.insert_button2 = QPushButton("Вставить последовательность во 2-е дерево", self)
        self.check_bst_button = QPushButton("Проверить 1-е дерево на BST", self)
        self.prime_tree_button = QPushButton("Построить дерево из простых чисел", self)
        self.count_non_multiples_button = QPushButton("Посчитать элементы, не кратные n", self)
        self.save_button = QPushButton("Сохранить дерево", self)

        self.insert_button.clicked.connect(self.insert_sequence)
        self.insert_button2.clicked.connect(self.insert_sequence2)
        self.check_bst_button.clicked.connect(self.check_bst)
        self.prime_tree_button.clicked.connect(self.build_prime_tree)
        self.count_non_multiples_button.clicked.connect(self.count_non_multiples)
        self.save_button.clicked.connect(self.save_tree)

        layout.addWidget(self.label_input)
        layout.addWidget(self.input_edit)
        layout.addWidget(self.insert_button)

        layout.addWidget(self.label_input2)
        layout.addWidget(self.input_edit2)
        layout.addWidget(self.insert_button2)

        layout.addWidget(self.label_n)
        layout.addWidget(self.n_edit)

        layout.addWidget(self.label_result)
        layout.addWidget(self.result_edit)

        layout.addWidget(self.check_bst_button)
        layout.addWidget(self.prime_tree_button)
        layout.addWidget(self.count_non_multiples_button)
        layout.addWidget(self.save_button)

        layout.setContentsMargins(0, 400, 0, 0)

        self.setLayout(layout)
        self.setWindowTitle('Binary Search Tree')
        self.setGeometry(100, 100, 800, 600)
        self.show()

    def insert_sequence(self):
        sequence = self.input_edit.text().split()
        for value in sequence:
            self.tree.insert(int(value))
        self.update()

    def insert_sequence2(self):
        sequence = self.input_edit2.text().split()
        for value in sequence:
            self.tree2.insert(int(value))
        self.update()

    def check_bst(self):
        is_bst = self.tree.is_bst()
        self.result_edit.setText(f"Это дерево {'является' if is_bst else 'не является'} деревом поиска")
        self.update()

    def build_prime_tree(self):
        self.result_tree = self.tree.build_tree_from_primes(self.tree2)
        self.result_tree.save_tree("tree.res")
        self.update()

    def count_non_multiples(self):
        try:
            n = int(self.n_edit.text())
            count = self.tree.count_non_multiples(n)
            self.result_edit.setText(f"Количество элементов: {count}")
        except ValueError:
            self.result_edit.setText("Ошибка: Введите корректное значение для n")
        self.update()

    def save_tree(self):
        self.tree.save_tree("tree.dat")
        self.result_edit.setText("Дерево сохранено")

    def paintEvent(self, event):
        """Отрисовка деревьев"""
        painter = QPainter(self)
        if self.tree.root:
            painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
            self.tree.visualize(painter, self.tree.root, 300, 50, 100)
        if self.result_tree and self.result_tree.root:
            painter.setPen(QPen(Qt.blue, 2, Qt.SolidLine))
            self.result_tree.visualize(painter, self.result_tree.root, 600, 50, 100)