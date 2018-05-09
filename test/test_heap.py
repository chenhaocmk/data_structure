import random

from src.heap import MinHeap
from util import visualizer as vis

h = MinHeap()
my_list = list(range(1, 20))
random.shuffle(my_list)
for i in my_list:
    h.add(i)
    print(list(enumerate(h.data)))

for i in h:
    print(i)

for i in my_list:
    h.add(i)
    print(list(enumerate(h.data)))

h.modify(10, -2)
h.modify(9, -1)

func = lambda x: [y for y in (h._left_child(x), h._right_child(x)) if y]
vis.print_tree(0, func, h.__getattr__)