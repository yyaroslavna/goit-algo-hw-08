class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_sum(root):
    if root is None:
        return 0

    return root.value + tree_sum(root.left) + tree_sum(root.right)


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(7)

print("Сума всіх значень:", tree_sum(root))
