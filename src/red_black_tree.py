from util.tree_node import TreeNode
import util.tree_util as util
from src.bst import BinarySearchTree


class RedBlackTreeNode(TreeNode):
    BLACK = 'black'
    RED = 'red'

    def __init__(self, color=RED, val=None):
        super(RedBlackTreeNode, self).__init__(val)
        self.color = color
        self.parent = None

    def __str__(self):
        return str((self.color, self.val))


class RedBlackTree(BinarySearchTree):
    def __init__(self, arr=None):
        super(RedBlackTree, self).__init__(arr)

    def add(self, val):
        if self.get(val):
            raise ValueError('Value already exist in {name}: {val}'.
                             format(name=self.__class__.__name__, val=val))
        else:
            self.length += 1
            if not self.root:
                self.root = RedBlackTreeNode(RedBlackTreeNode.BLACK, val)
                return
            else:
                node = RedBlackTreeNode(RedBlackTreeNode.RED, val)

                # add the node as a red leaf first
                curr = self.root
                while curr:
                    if node.val > curr.val:
                        if not curr.right:
                            curr.right, node.parent = node, curr
                            break
                        else:
                            curr = curr.right
                    else:
                        if not curr.left:
                            curr.left, node.parent = node, curr
                            break
                        else:
                            curr = curr.left

                # 5 cases been discussed here
                self._add_case_1(node)

    def _add_case_1(self, node):
        """
        Case 1: node at root position with no parent

        It will be colored as black and tree becomes valid
        """
        if not node.parent:
            node.color = RedBlackTreeNode.BLACK
            self.root = node
        else:
            self._add_case_2(node)

    def _add_case_2(self, node):
        """
        Case 2: node's parent colored black

        Tree is still valid
        """
        if node.parent.color == RedBlackTreeNode.BLACK:
            return
        else:
            self._add_case_3(node)

    def _add_case_3(self, node):
        """
        Case 3: node's parent and uncle are all red

        We color node's parent and uncle as black
        We color node's grandparent as red
        Then we treat the grandparent as newly added node and go though who process
        from the beginning
        """
        if util.uncle(node) and util.uncle(node).color == RedBlackTreeNode.RED:
            node.parent.color = RedBlackTreeNode.BLACK
            util.uncle(node).color = RedBlackTreeNode.BLACK
            util.grandparent(node).color = RedBlackTreeNode.RED
            self._add_case_1(util.grandparent(node))
        else:
            self._add_case_4(node)

    def _add_case_4(self, node):
        """
        Case 4: node's parent is red and uncle is black(or None)

        We try to make node, parent and grandparent to be aligned on same side
        That is, node and parent is both left/right child of parent and grandparent
        We can use left/right rotation to make it happen
        After rotation we make node left/right child to be node
        """
        if node == node.parent.right and node.parent == util.grandparent(node).left:
            util.left_rotate(node.parent)
            node = node.left
        elif node == node.parent.left and node.parent == util.grandparent(node).right:
            util.right_rotate(node.parent)
            node = node.right

        self._add_case_5(node)

    def _add_case_5(self, node):
        """
        Case 5: We color node's grandparent to red and node's parent to black
        Then do a left/right rotation to make it valid
        """
        util.grandparent(node).color = RedBlackTreeNode.RED
        node.parent.color = RedBlackTreeNode.BLACK

        (util.left_rotate, util.right_rotate)[node.parent.left == node](util.grandparent(node))

    def delete(self, val):
        pass
