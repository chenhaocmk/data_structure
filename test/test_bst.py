import random

from src.bst import BinarySearchTree
from util.visualizer import print_tree

data = list(range(1, 20))
random.shuffle(data)
tree = BinarySearchTree(data)

print_tree(tree.root, lambda x: [y for y in (x.left, x.right)] if x else [])
