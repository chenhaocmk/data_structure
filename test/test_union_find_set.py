from src.union_find_set import UnionFindCollection

my_union_find_set = UnionFindCollection()

for i in range(1, 21):
    my_union_find_set.add_relation(i)
print(my_union_find_set)

for i in range(1, 21)[::2]:
    my_union_find_set.add_relation(i, i+1)
    print(my_union_find_set)

for i in range(1, 21):
    print(i, my_union_find_set.get_ancestor(i))
print(my_union_find_set)