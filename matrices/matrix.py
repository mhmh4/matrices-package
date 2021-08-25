from exceptions import ZeroConstantException


class Matrix:

    def __init__(self, entries):
        # if not entries or not entries[0]:
        #     ...
        self.entries = entries
        # if not self._entries_has_consistent_row_lengths():
        #     ...

    @property
    def m(self):
        return len(self.entries)

    @property
    def n(self):
        return len(self.entries[0])

    def __add__(self, other):
        if not self.shares_size_with(self, other):
            ...
        result = Matrix.from_dimensions(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __getitem__(self, index):
        return self.entries[index]

    def __repr__(self):
        return "\n".join(str(row) for row in self.entries)

    def __setitem__(self, index, value):
        self.entries[index] = value

    def __sub__(self, other):
        if not Matrix.have_similar_dimensions(self, other):
            ...

    def interchange(self, a, b):
        if a < 0 or a == self.m or b < 0 or b == self.m:
            ...
        self.entries[a], self.entries[b] = self.entries[b], self.entries[a]

    def replace(self, constant, a, b):
        if constant == 0:
            ...
        temp = [constant * x for x in self.entries[a]]
        for j in range(self.n):
            self.entries[b][j] += temp[j]

    def scale(self, constant, i):
        if constant == 0:
            raise ZeroConstantException("Cannot scale a row by a zero.")
        for j in range(self.n):
            self.entries[i][j] *= constant

    def _entries_has_consistent_row_lengths(self):
        for row in self.entries:
            if len(row) != self.n:
                return False
        return True

    def _is_square_matrix(self):
        return self.m == self.n

    @classmethod
    def from_size(cls, n):
        tmp = [0] * n
        return cls(tmp)

    @classmethod
    def from_sizes(cls, m, n):
        tmp = [[0] * n] * m
        return cls(tmp)

    @staticmethod
    def have_similar_dimensions(a, b):
        return (a.m == b.m) and (a.n == b.n)


m = Matrix([[0,1]])
m.scale(0, 0)
print(m)
