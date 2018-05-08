
class MinHeap(object):
    def __init__(self):
        self.data = []

    def add(self, key):
        self.data.append(key)
        loc = len(self.data) - 1
        while loc and self.data[self._parent(loc)] > self.data[loc]:
            self.data[loc], self.data[self._parent(loc)] = \
                self.data[self._parent(loc)], self.data[loc]
            loc = self._parent(loc)

    def delete(self, index):
        if self._valid_index(index):
            self.modify(index, float('-inf'))
            self.pop_min()

    def modify(self, index, new_val):
        if self._valid_index(index):
            self.data[index] = new_val
            loc = index
            while loc and self.data[self._parent(loc)] > self.data[loc]:
                self.data[loc], self.data[self._parent(loc)] = \
                    self.data[self._parent(loc)], self.data[loc]
                loc = self._parent(loc)

    def get_min(self):
        return self.data[0] if self.data else None

    def pop_min(self):
        if not self.data:
            return None
        else:
            root = self.data.pop(0)
            if self.data:
                self.data = [self.data[-1]] + self.data[:-1]
                self._heapfy(0)
            return root

    def _left_child(self, index):
        if self._valid_index(index):
            left = (index << 1) + 1
            return left if self._valid_index(left) else None
        else:
            raise None

    def _right_child(self, index):
        if self._valid_index(index):
            right = (index << 1) + 2
            return right if self._valid_index(right) else None
        else:
            raise None

    def _parent(self, index):
        if self._valid_index(index):
            return (index-1)//2
        else:
            raise None

    def _heapfy(self, index):
        l, r = self._left_child(index), self._right_child(index)
        smallest = index
        if l and self.data[l] < self.data[index]:
            smallest = l
        if r and self.data[r] < self.data[smallest]:
            smallest = r
        if smallest != index:
            self.data[index], self.data[smallest] = \
                self.data[smallest], self.data[index]
            self._heapfy(smallest)

    def _valid_index(self, index):
        return self.data and 0 <= index < len(self.data)

    def __str__(self):
        return str(self.data)

    def __bool__(self):
        return bool(self.data)

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.data:
            return self.pop_min()
        else:
            raise StopIteration

    def __getattr__(self, item):
        if self._valid_index(item):
            return self.data[item]
        return None
