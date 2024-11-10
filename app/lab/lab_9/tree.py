import math

from app.lab.lab_9.node import Node


# noinspection SpellCheckingInspection
def is_prime(num):
    """Проверка, является ли число простым."""
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


# noinspection SpellCheckingInspection
class Tree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        """Вставка элемента в дерево"""
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, current_node, value):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(current_node.left, value)
        elif value > current_node.value:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(current_node.right, value)

    def in_order(self, node=None, values=None):
        """Обход дерева в порядке возрастания"""
        if values is None:
            values = []
        if node is None:
            node = self.root
        if node.left:
            self.in_order(node.left, values)
        values.append(node.value)
        if node.right:
            self.in_order(node.right, values)
        return values

    def is_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """Проверка, является ли дерево деревом поиска"""
        if node is None:
            node = self.root
        if not node:
            return True
        if node.value <= min_val or node.value >= max_val:
            return False
        return (self.is_bst(node.left, min_val, node.value) and
                self.is_bst(node.right, node.value, max_val))

    def count_non_multiples(self, n, node=None):
        if node is None:
            node = self.root

        if node is None:
            return 0

        count = 0
        if node.value % n != 0:
            count += 1

        if node.left is not None:
            count += self.count_non_multiples(n, node.left)
        if node.right is not None:
            count += self.count_non_multiples(n, node.right)

        return count

    def save_tree(self, filename):
        """Сохранение дерева в файл"""
        with open(filename, 'w') as f:
            values = self.in_order()
            f.write(' '.join(map(str, values)))

    def load_tree(self, filename):
        """Загрузка дерева из файла"""
        with open(filename, 'r') as f:
            values = map(int, f.read().split())
            for value in values:
                self.insert(value)

    def build_tree_from_primes(self, other_tree):
        """Построение нового дерева из простых чисел двух деревьев."""
        new_tree = Tree()
        self_primes = [v for v in self.in_order() if is_prime(v)]
        other_primes = [v for v in other_tree.in_order() if is_prime(v)]

        for value in self_primes + other_primes:
            new_tree.insert(value)

        return new_tree

    def visualize(self, painter, node=None, x=300, y=50, offset=100):
        """Рекурсивная отрисовка дерева с помощью QPainter."""
        if node is None:
            node = self.root
        if node:
            painter.drawText(x, y, str(node.value))
            if node.left:
                painter.drawLine(x, y, x - offset, y + 50)
                self.visualize(painter, node.left, x - offset, y + 50, offset // 2)
            if node.right:
                painter.drawLine(x, y, x + offset, y + 50)
                self.visualize(painter, node.right, x + offset, y + 50, offset // 2)