from util.tree_node import TreeNode


class BinarySearchTree(object):
    def __init__(self, arr=None):
        self.root = None
        self.length = 0
        if isinstance(arr, list):
            for i in arr:
                self.add(i)

    def __len__(self):
        return self.length

    def get(self, val):
        # BFS search
        if not self.root:
            return False

        tmp = [self.root]
        for node in tmp:
            if node.val == val:
                return node
            else:
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
        return False

    def add(self, val):
        if self.get(val):
            raise ValueError('Value already exist in BST: %s' % val)
        else:
            if not self.root:
                self.root = TreeNode(val)
            else:
                self._add_helper(self.root, val)
            self.length += 1

    def _add_helper(self, node, val):
        if not node:
            raise ValueError("Unable to attach node to None")
        else:
            if node.val > val:
                if not node.left:
                    node.left = TreeNode(val)
                else:
                    self._add_helper(node.left, val)
            elif node.val < val:
                if not node.right:
                    node.right = TreeNode(val)
                else:
                    self._add_helper(node.right, val)
            else:
                raise ValueError('Node with value %s already exist in tree' % val)

    def delete(self, val):
        if not self.get(val):
            raise ValueError('Value not found in BST: %s' % val)
        else:
            self.length -= 1
            return self._delete_helper(self.root, val)

    def _delete_helper(self, node, val):
        if not node:
            return None
        elif val != node.val:
            (node.left, node.right)[val > node.val] = self._delete_helper((node.left, node.right)[val > node.val], val)
            return node
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            curr = node.right
            while curr and curr.left:
                curr = curr.left
            node.val = curr.val
            node.right = self._delete_helper(node.right, node.val)
            return node

    def __len__(self):
        return self.length
