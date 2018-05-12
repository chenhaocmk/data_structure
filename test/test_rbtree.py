import random

from src.red_black_tree import RedBlackTree
from util.visualizer import print_tree

my_list = list(range(21))
random.shuffle(my_list)

tree = RedBlackTree(my_list)
print_tree(tree.root, lambda x: [y for y in (x.left, x.right)] if x else [])