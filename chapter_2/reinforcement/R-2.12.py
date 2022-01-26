# Implement the mul method for the Vector class of Section 2.3.3, so that the expression v 3 returns a new vector
# with coordinates that are 3 times the respective coordinates of v.

class Vector:
    def __init__(self, d):
        self._coords = [0] * d

    def __len__(self):
        return len(self._coords)

    def __getitem__(self, j):
        return self._coords[j]

    def __setitem__(self, j, val):
        self._coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __mul__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] * 3

    def __eq__(self, other):
        return self._coords == other._coords

    def __ne__(self, other):
        return not self == other

    def __str__(self):
        return "<" + str(self._coords)[1:-1] + ">"


v = Vector(5)
v[1] = 23
v[-1] = 45
print(v[4])
u = v + v
print(u)
total = 0
for entry in v:
    total += entry