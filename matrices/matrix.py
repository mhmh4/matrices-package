from exceptions import *


class Matrix:

    def __init__(self, entries):
        if not entries or not entries[0]:
            raise EmptyMatrixException("matrix entries cannot be empty")
        self.entries = entries
        if not self._entries_has_consistent_row_dimensions():
            raise InconsistentRowDimensionsException(
                "all rows must be of the same length")

    @property
    def m(self):
        return len(self.entries)

    @property
    def n(self):
        return len(self.entries[0])

    def __add__(self, other):
        if not self._has_similar_dimensions_as(other):
            raise InvalidDimensionsException(
                "dimensions of both matrices must be similar")
        result = Matrix.from_dimensions(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                result[i][j] = self[i][j] + other[i][j]
        return result

    def __eq__(self, other):
        return self.entries == other.entries

    def __getitem__(self, index):
        return self.entries[index]

    def __mul__(self, other):
        if self.n != other.m:
            raise InvalidDimensionsException(
                "number of columns of the first matrix must be equal "
                "to the number of rows of the second matrix"
            )
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
        if not self._has_similar_dimensions_as(other):
            raise InvalidDimensionsException(
                "dimensions of both matrices must be similar")
        result = Matrix.from_dimensions(self.m, self.n)
        for i in range(self.m):
            for j in range(self.n):
                result[i][j] = self[i][j] - other[i][j]
        return result

    def scale(self, constant, i):
        if constant == 0:
            raise ZeroConstantException("cannot scale a row by zero")
        if not self._valid_row_index(i):
            raise BadIndexException("index is out of range")
        for j in range(self.n):
            self.entries[i][j] *= constant

    def interchange(self, a, b):
        if not self._valid_row_index(a) or not self._valid_row_index(b):
            raise BadIndexException("an index is out of range")
        self.entries[a], self.entries[b] = self.entries[b], self.entries[a]

    def replace(self, constant, a, b):
        if constant == 0:
            raise ZeroConstantException("cannot multiply a row by zero")
        if not self._valid_row_index(a) or not self._valid_row_index(b):
            raise BadIndexException("an index is out of range")
        temp = [constant * x for x in self.entries[a]]
        for j in range(self.n):
            self.entries[b][j] += temp[j]

    def transpose(self):
        self.entries = [[*x] for x in zip(*self.entries)]

    def _valid_row_index(self, index):
        return index >= 0 and index < self.m

    def _entries_has_consistent_row_dimensions(self):
        for row in self.entries:
            if len(row) != self.n:
                return False
        return True

    def _has_similar_dimensions_as(self, other):
        return self.m == other.m and self.n == other.n

    @classmethod
    def from_dimension(cls, n):
        tmp = [[0 for _ in range(n)]]
        return cls(tmp)

    @classmethod
    def from_dimensions(cls, m, n):
        tmp = [[0 for _ in range(n)] for _ in range(m)]
        return cls(tmp)
