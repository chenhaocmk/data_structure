

def grandparent(node):
    return node.parent.parent if node and node.parent else None


def uncle(node):
    gp = grandparent(node)
    if not gp:
        return None
    else:
        return gp.left if gp.right == node.parent else gp.right


def left_rotate(node):
    if not node or not node.right:
        raise ValueError('Invalid left rotate')
    else:
        parent, right_child = node.parent, node.right
        if parent:
            is_left = parent.left == node
        node.right = right_child.left
        if right_child.left:
            right_child.left.parent = node
        node.parent, right_child.left = right_child, node
        right_child.parent = parent
        if parent:
            if is_left:
                parent.left = right_child
            else:
                parent.right = right_child


def right_rotate(node):
    if not node or not node.left:
        raise ValueError('Invalid right rotate')
    else:
        parent, left_child = node.parent, node.left
        if parent:
            is_left = parent.left == node
        node.left = left_child.right
        if left_child.right:
            left_child.right.parent = node
        node.parent, left_child.right = left_child, node
        left_child.parent = parent
        if parent:
            if is_left:
                parent.left = left_child
            else:
                parent.right = left_child
