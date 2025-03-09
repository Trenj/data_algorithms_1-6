class TreeNode:
    def __init__(self, key):
        # Инициализация узла дерева
        self.key = key
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        # Инициализация пустого дерева
        self.root = None

    def insert(self, key):
        # Вставка ключа в дерево
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        # Вспомогательная функция для рекурсивной вставки
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find(self, key):
        # Поиск ключа в дереве
        return self._find(self.root, key)

    def _find(self, node, key):
        # Вспомогательная функция для рекурсивного поиска
        if node is None:
            return None
        if key == node.key:
            return node
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def delete(self, key):
        # Удаление ключа из дерева
        self.root, deleted_node = self._delete(self.root, key)
        return deleted_node

    def _delete(self, node, key):
        # Вспомогательная функция для рекурсивного удаления
        if node is None:
            return node, None

        deleted_node = None
        if key < node.key:
            node.left, deleted_node = self._delete(node.left, key)
        elif key > node.key:
            node.right, deleted_node = self._delete(node.right, key)
        else:
            deleted_node = node
            # Если у узла только один ребёнок или нет детей
            if node.left is None:
                return node.right, deleted_node
            elif node.right is None:
                return node.left, deleted_node

            # Если у узла два ребёнка
            min_larger_node = self._get_min(node.right)
            node.key = min_larger_node.key
            node.right, _ = self._delete(node.right, min_larger_node.key)

        return node, deleted_node

    def _get_min(self, node):
        # Нахождение минимального узла в дереве
        while node.left is not None:
            node = node.left
        return node

    def inorder_traversal(self):
        # Обход дерева по возрастанию (инфиксный обход)
        return self._inorder_traversal(self.root, [])

    def _inorder_traversal(self, node, path):
        # Вспомогательная функция для рекурсивного обхода
        if node:
            self._inorder_traversal(node.left, path)
            path.append(node.key)
            self._inorder_traversal(node.right, path)
        return path


def main():
    bst = BinarySearchTree()
    nodes = [50, 30, 70, 20, 40, 60, 80]

    # Вставка заранее определенных узлов в дерево
    for node in nodes:
        bst.insert(node)

    # Вывод изначального обхода
    print("Изначальный обход дерева по возрастанию:", bst.inorder_traversal())

    # Запрос ключа для поиска и удаления
    key = int(input("Введите ключ для поиска и удаления: "))

    node = bst.find(key)
    if node:
        print(f"Ключ {key} найден в дереве.")
        bst.delete(key)
        print(f"Ключ {key} успешно удален.")
    else:
        print(f"Ключ {key} не найден в дереве.")

    # Вывод обхода после удаления
    print("Обход дерева после удаления:", bst.inorder_traversal())


if __name__ == "__main__":
    main()

"""
Осуществить алгоритм упорядоченного дерева поиска. Найти ключ поиска и удалить его из дерева.
"""