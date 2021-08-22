class Matrix:

    def __init__(self, entries):
        self.entries = entries
        self.m = len(entries)
        self.n = len(entries[0])

    def __getitem__(self, index: int) -> int:
        return self.entries[index]

    def __str__(self) -> str:
        return "\n".join(str(row) for row in self.entries)

    def interchange(self, a: int, b: int) -> None:
        if a < 0 or a == self.m or b < 0 or b == self.m:
            raise IndexError("an index is out of range")
        self.entries[a], self.entries[b] = self.entries[b], self.entries[a]

    def replace(self, c, row1, row2):
        ...

    def scale(self, c: float, i: int) -> None:
        if c == 0:
            ...
        for j in range(self.n):
            self.entries[i][j] *= c

    def _has_equivalent_rows(self) -> bool:
        for row in self.entries:
            if len(row) != self.n:
                return False
        return True

    def _is_square_matrix(self) -> bool:
        return self.m == self.n

    @classmethod
    def from_dimension(cls, n: int):
        tmp = [0] * n
        return cls(tmp)

    @classmethod
    def from_dimensions(cls, m: int, n: int):
        tmp = [[0] * n] * m
        return cls(tmp)


m = Matrix([[1, 2], [3, 4]])

print(m[1][0])
