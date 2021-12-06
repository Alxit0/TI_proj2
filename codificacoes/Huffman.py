import numpy as np


class leaf:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"<{self.key},{self.value}>"


class tree_node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right
        self.value = left.value + right.value

    def __str__(self):
        return f"){self.left} {self.right}("

    def get_paths(self):pass


def encode(string: str):
    valores = np.asarray([*string])
    d = {i: j for i, j in zip(*np.unique(valores, return_counts=True, axis=0))}  # achar as contagens
    temp = []
    for i in sorted(d.keys(), key=d.__getitem__):
        temp += leaf(i, d[i]),
    while len(temp) != 1:
        a = temp.pop()
        b = temp.pop()
        temp += tree_node(a, b),
        temp.sort(key=lambda x: x.value, reverse=True)

    print(*map(str, temp))


if __name__ == '__main__':
    encode("banana")
    print(type(leaf('a', 0)))
