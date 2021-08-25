# from exceptions import ZeroConstantException


class Matrix:

    def __init__(self, entries):
        if not entries or not entries[0]:
            ...
        self.entries = entries
        if not self._entries_has_consistent_row_dimensions():
            ...

    @property
    def m(self):
        return len(self.entries)

    @property
    def n(self):
        return len(self.entries[0])

    def __add__(self, other):
        if not self._has_similar_dimensions_as(other):
            ...
        result = Matrix.from_dimensions(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __getitem__(self, index):
        return self.entries[index]

    def __mul__(self, other):
        if self.n != self.m:
            ...
        result = Matrix.from_dimensions(self.m, other.n)
        for i in range(self.m):
            for j in range(other.n):
                for k in range(self.n):
                    result[i][j] += self[i][k] * other[k][j]
        return result

    def __repr__(self):
        return "\n".join(str(row) for row in self.entries)

    def __setitem__(self, index, value):
        self.entries[index] = value

    def __sub__(self, other):
        if not Matrix.have_similar_dimensions(self, other):
            ...

    def scale(self, constant, i):
        if constant == 0:
            ...
        for j in range(self.n):
            self.entries[i][j] *= constant

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

    def _valid_row_index(self, index):
        return index >= 0 and index <= self.m

    def _valid_col_index(self, index):
        return index >= 0 and index <= self.n

    def _entries_has_consistent_row_dimensions(self):
        for row in self.entries:
            if len(row) != self.n:
                return False
        return True

    def _is_square_matrix(self):
        return self.m == self.n

    def _has_similar_dimensions_as(self, other):
        return self.m == other.m and self.n == other.n

    @classmethod
    def from_dimension(cls, n):
        tmp = [0] * n
        return cls(tmp)

    @classmethod
    def from_dimensions(cls, m, n):
        tmp = [[0] * n] * m
        return cls(tmp)
