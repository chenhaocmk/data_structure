import collections


class UnionFindCollection(object):
    def __init__(self):
        self.elements = dict()

    def all_sets(self):
        res = collections.defaultdict(set)
        for key, val in self.elements.items():
            res[val].add(key)
        return res

    def __str__(self):
        return str(self.all_sets())

    def __repr__(self):
        return self.__str__()

    def __contains__(self, item):
        return item in self.elements

    def add_relation(self, a, b=None):
        if a is None:
            print('Nothing been done when trying to add None to collection')
            return
        elif b is None:
            if a in self.elements:
                print('Nothing been done when trying to add existed single element to collection')
            else:
                self.elements[a] = a
        else:
            self._union(a, b)

    def _union(self, a, b):
        res_a, res_b = self.get_ancestor(a), self.get_ancestor(b)
        if res_a != res_b:
            self.elements[a] = res_b

    def get_ancestor(self, x):
        assert x in self.elements, 'Element should be in collections already: %s' % x
        if self.elements[x] != x:
            self.elements[x] = self.get_ancestor(self.elements[x])
        return self.elements[x]

    def in_same_set(self, x, y):
        assert x in self.elements, 'Element not found in collection: %s' % x
        assert y in self.elements, 'Element not found in collection: %s' % y

        return self.get_ancestor(x) == self.get_ancestor(y)
