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

    def set_black(self):
        self.color = RedBlackTreeNode.BLACK

    def set_red(self):
        self.color = RedBlackTreeNode.RED

    def is_black(self):
        return self.color == RedBlackTreeNode.BLACK

    def is_red(self):
        return self.color == RedBlackTreeNode.RED


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
            node.set_black()
            self.root = node
        else:
            self._add_case_2(node)

    def _add_case_2(self, node):
        """
        Case 2: node's parent colored black

        Tree is still valid
        """
        if node.parent.is_black():
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
        if util.uncle(node) and util.uncle(node).is_red():
            node.parent.set_black()
            util.uncle(node).set_black()
            util.grandparent(node).set_red()
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

    @staticmethod
    def _add_case_5(node):
        """
        Case 5: We color node's grandparent to red and node's parent to black
        Then do a left/right rotation to make it valid
        """
        util.grandparent(node).set_red()
        node.parent.set_black()

        (util.left_rotate, util.right_rotate)[node.parent.left == node](util.grandparent(node))

    def delete(self, val):
        node = self.get(val)
        if not node:
            raise ValueError('Value not found in {name}: {val}'.format(
                name=self.__class__.__name__, val=val))
        elif not self.root:
            raise ValueError('Root not found in tree')
        else:
            self.length -= 1
            # If node has two child, we do a value change on node
            # And the problem becomes deleting a node with at most one non-null child
            if node.left and node.right:
                curr = node.left
                while curr.right:
                    curr = curr.right
                node.val = curr.val

                # now we are deleting curr instead of node
                node = curr

            child = node.left if node.left else node.right
            if not node.parent and not node.left and not node.right:
                self.root = node
                return
            elif not node.parent:
                if child:
                    child.parent = None,
                    self.root = child
                    child.set_black()
                return
            else:
                if node == node.parent.left:
                    node.parent.left = child
                else:
                    node.parent.right = child

            if child:
                child.parent = node.parent

            # if node is red then child must be black and tree is still valid
            if node.is_red():
                return
            else:
                # if node is black and child is red we just need to color child as black
                if child and child.is_red():
                    child.set_black()
                else:
                    # if node is black and child is black
                    # 6 cases been discussed here
                    self._delete_case_1(child)

    def _delete_case_1(self, node):
        """
        Case 1: node is root

        The tree is valid, we are done
        """
        if not node.parent:
            self._delete_case_2(node)
        else:
            return

    def _delete_case_2(self, node):
        """
        Case 2: node's sibling is red

        We want to give node a black sibling
        - we color sibling as black and parent as red
        - left/right rotate node's parent
        - further processing will be done in case 4
        """
        if util.sibling(node).is_red():
            if node == node.parent.left:
                util.sibling(node).set_black()
                node.parent.set_red()

                if node == node.parent.left:
                    util.left_rotate(node.parent)
                else:
                    util.right_rotate(node.parent)

        self._delelte_case_3(node)

    def _delete_case_3(self, node):
        """
        Case 3: node's sibling/parent/nephews are all black

        We color node's sibling as red and restart from case 1 for parent
        """
        sibling = util.sibling(node)
        if all([node.parent.is_black(),
                not sibling.left or sibling.left.is_black(),
                not sibling.right or sibling.right.is_black()]):
            sibling.set_red()
            self._delete_case_1(node.parent)
        else:
            self._delete_case_4(node)

    def _delete_case_4(self, node):
        """
        Case 4: node's sibling&nephews are black, parent is red

        We simply color node's sibling red and parent to black
        """
        sibling = util.sibling(node)
        if all([node.parent.is_red(),
                not sibling.left or sibling.left.is_black(),
                not sibling.right or sibling.right.is_black()]):
            sibling.set_red()
            node.parent.set_black()
        else:
            self._delete_case_5(node)

    def _delete_case_5(self, node):
        """
        Case 5: node's sibling is black.
        - node is right child and sibling's left/right child is red/black
        - node is left child and sibling's right/left child is red/black

        We do left/right rotation and it's done
        """
        sibling = util.sibling(node)
        if node == node.parent.left and sibling.right.is_black() \
                and sibling.left.is_red():
            sibling.set_red()
            sibling.left.set_black()
            util.right_rotate(sibling)
            return
        elif node == node.parent.right and sibling.left.is_black() \
                and sibling.right.is_red():
            sibling.set_red()
            sibling.right.set_black()
            util.left_rotate(sibling)
            return

        self._delete_case_6(node)

    @staticmethod
    def _delete_case_6(node):
        """
        Case 6: node's sibling is black
        - node is left child and sibling's left/right child is black/right
        - node is right child and sibling's right/left child is black/red

        We do left/right rotation on node's parent then switch color of parent/sibling
        Then set sibling's left child to black
        """
        sibling = util.sibling(node)
        sibling.color = node.parent.color
        node.parent.set_black()

        if node == node.parent.left:
            sibling.right.set_black()
            util.left_rotate(node.parent)
        else:
            sibling.left.set_black()
            util.right_rotate(node.parent)
