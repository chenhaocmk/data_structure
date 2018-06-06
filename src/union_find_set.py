import collections


class UnionFindCollection(object):
    def __init__(self):
        self.elements = dict()
        self.depth = dict()

    def all_sets(self):
        res = collections.defaultdict(set)
        for item in self.elements:
            res[self.get_ancestor(item)].add(item)
        return res

    def __str__(self):
        return str(self.all_sets())

    def __repr__(self):
        return self.__str__()

    def __contains__(self, item):
        return item in self.elements

    def add(self, x):
        assert x not in self.elements, 'Element already exists: %s' % str(x)
        self.elements[x] = x
        self.depth[x] = 1

    def union(self, a, b):
        if a not in self.elements:
            self.add(a)
        if b not in self.elements:
            self.add(b)

        res_a, res_b = self.get_ancestor(a), self.get_ancestor(b)
        if res_a != res_b:
            if self.depth[res_a] > self.depth[res_b]:
                self.elements[res_b] = res_a
                self.depth[res_a] += self.depth[res_b]
            else:
                self.elements[res_a] = res_b
                self.depth[res_b] += self.depth[res_a]

    def get_ancestor(self, x):
        assert x in self.elements, 'Element should be in collections already: %s' % x
        if self.elements[x] != x:
            self.elements[x] = self.get_ancestor(self.elements[x])
        return self.elements[x]

    def in_same_set(self, x, y):
        assert x in self.elements, 'Element not found in collection: %s' % x
        assert y in self.elements, 'Element not found in collection: %s' % y

        return self.get_ancestor(x) == self.get_ancestor(y)
