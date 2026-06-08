class Node:
    def __init__(self, value, left=None, right=None, height=1):
        self.value = value
        self.left = left
        self.right = right
        self.height = height


def height(node):
    if node is None:
        return 0
    return node.height


def update_height(node):
    if node is not None:
        node.height = 1 + max(height(node.left), height(node.right))


def balance_factor(node):
    if node is None:
        return 0
    return height(node.left) - height(node.right)


def right_rotate(y):
    x = y.left
    t2 = x.right
    x.right = y
    y.left = t2
    update_height(y)
    update_height(x)
    return x


def left_rotate(x):
    y = x.right
    t2 = y.left
    y.left = x
    x.right = t2
    update_height(x)
    update_height(y)
    return y


def avl_insert(root, x):
    if root is None:
        return Node(x)

    if x < root.value:
        root.left = avl_insert(root.left, x)
    elif x > root.value:
        root.right = avl_insert(root.right, x)
    else:
        return root

    update_height(root)
    balance = balance_factor(root)

    if balance > 1 and x < root.left.value:
        return right_rotate(root)

    if balance < -1 and x > root.right.value:
        return left_rotate(root)

    if balance > 1 and x > root.left.value:
        root.left = left_rotate(root.left)
        return right_rotate(root)

    if balance < -1 and x < root.right.value:
        root.right = right_rotate(root.right)
        return left_rotate(root)

    return root


def inorder_values(root):
    if root is None:
        return []
    return inorder_values(root.left) + [root.value] + inorder_values(root.right)


def build_avl(values):
    if values is None:
        return None
    root=None
    for i in values:
        root = avl_insert(root, i)
    return root

def is_avl(root):
    if root is None:
        return True
    def is_bst_valid(root, min_val=float("-inf"), max_val=float("+inf")):
        if root is None:
            return True
        if not (min_val < root.value < max_val):
            return False
        left_check = is_bst_valid(root.left, min_val, root.value)
        right_check = is_bst_valid(root.right, root.value, max_val)
        return left_check and right_check
    def is_avl_valid(root):
        if root is None:
            return True
        if abs(balance_factor(root))>1:
            return False
        return is_avl_valid(root.left) and is_avl_valid(root.right)
    return is_bst_valid(root) and is_avl_valid(root)
        


