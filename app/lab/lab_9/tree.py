import pickle

from app.lab.lab_9.node import Node


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, current, key):
        if key < current.value:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert(current.left, key)
        else:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert(current.right, key)

    def is_bst(self):
        return self._is_bst(self.root, float('-inf'), float('inf'))

    def _is_bst(self, node, min_val, max_val):
        if node is None:
            return True
        if not (min_val < node.value < max_val):
            return False
        return self._is_bst(node.left, min_val, node.value) and \
            self._is_bst(node.right, node.value, max_val)

    def save_to_file(self, filename):
        with open(filename, 'wb') as f:
            # noinspection PyTypeChecker
            pickle.dump(self.root, f)

    def load_from_file(self, filename):
        with open(filename, 'rb') as f:
            self.root = pickle.load(f)

    def find_primes(self):
        primes = []
        self._find_primes(self.root, primes)
        return primes

    def _find_primes(self, node, primes):
        if node is not None:
            if is_prime(node.value):
                primes.append(node.value)
            self._find_primes(node.left, primes)
            self._find_primes(node.right, primes)

    def count_non_multiples(self, n):
        count = 0
        return self._count_non_multiples(self.root, n, count)

    def _count_non_multiples(self, node, n, count):
        if node is not None:
            if node.value % n != 0:
                count += 1
            count = self._count_non_multiples(node.left, n, count)
            count = self._count_non_multiples(node.right, n, count)
        return count

    def merge_trees_with_primes(self, other_tree):
        primes = self.find_primes() + other_tree.find_primes()
        new_tree = Tree()
        for prime in primes:
            new_tree.insert(prime)
        new_tree.save_to_file('tree.res')
        return new_tree
