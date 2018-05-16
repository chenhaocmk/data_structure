from util.tree_node import TreeNode


class SegmentTreeNode(TreeNode):
    def __init__(self, val, start, end):
        super(SegmentTreeNode, self).__init__(val)
        self.start = start
        self.end = end

    def __str__(self):
        return '(val: {val}, start: {start}, end: {end})'.format(
            val=self.val, start=self.start, end=self.end)

    def contains_index(self, index):
        return self.start <= index < self.end


class SegmentTree(object):
    def __init__(self, arr):
        self.arr = arr
        self.length = len(self.arr)

        self.root = self._build_segment_tree(0, self.length)

    def _build_segment_tree(self, start, end):
        if start == end:
            return None
        elif end - start == 1:
            return SegmentTreeNode(self.arr[start], start, end)
        else:
            mid = (start+end)//2 + (start+end) % 2
            left_child = self._build_segment_tree(start, mid)
            right_child = self._build_segment_tree(mid, end)

            val = sum([x.val for x in (left_child, right_child) if x])
            node = SegmentTreeNode(val, start, end)
            node.left, node.right = left_child, right_child
            return node

    def get_sum(self, start, end):
        if not 0 <= start <= end <= self.length-1:
            raise ValueError('Invalid index range')
        else:
            return self._get_subtree_sum(self.root, start, end)

    def _get_subtree_sum(self, node, start, end):
        if start > node.end or end < node.start:
            return 0
        elif node.start == start and node.end == end+1:
            return node.val
        elif node.start + 1 == node.end:
            return node.val
        elif end < node.left.end:
            return self._get_subtree_sum(node.left, start, end)
        elif start >= node.right.start:
            return self._get_subtree_sum(node.right, start, end)
        else:
            return self._get_subtree_sum(node.left, start, node.left.end-1) + \
                    self._get_subtree_sum(node.right, node.right.start, end)

    def update(self, index, val):
        if not 0 <= index < self.length:
            raise ValueError('Invalid index')
        else:
            diff = val - self.arr[index]
            self.arr[index] = val
            self._update_subtree(self.root, index, diff)

    def _update_subtree(self, node, index, diff):
        if not node or not node.contains_index(index):
            return
        else:
            node.val += diff
            self._update_subtree(node.left, index, diff)
            self._update_subtree(node.right, index, diff)
