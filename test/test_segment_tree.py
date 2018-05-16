from src.segment_tree import SegmentTree
from util.visualizer import print_tree


tree = SegmentTree(list(range(21)))
print_tree(tree.root, lambda x: [y for y in (x.left, x.right)] if x else [])

print(tree.get_sum(0, 0))
print(tree.get_sum(0, 1))
print(tree.get_sum(5, 20))
print(tree.get_sum(1, 20))

print('\n')

tree.update(5, 10)
print_tree(tree.root, lambda x: [y for y in (x.left, x.right)] if x else [])