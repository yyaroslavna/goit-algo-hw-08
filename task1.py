class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_min(root):
    if root is None:
        return None
    while root.left is not None:
        root = root.left
    return root.value


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Найменше значення:", find_min(root))
