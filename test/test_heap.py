import random

from src.heap import MinHeap

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
for i in h:
    print(i)
