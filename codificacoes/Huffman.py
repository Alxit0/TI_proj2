import numpy as np
# classes
if True:
    class Node:
        def __init__(self, value=0, left=None, right=None, key=None):
            self.left = left
            self.right = right
            self.value = value
            self.key = key

        def __str__(self):
            return f"){self.left},{self.right}("

        def get_type(self):
            return "normal"


    class Leaf(Node):
        def __init__(self, key, value):
            super().__init__(value)
            self.key = key

        def __str__(self):
            return f"<{self.key},{self.value}>"

        def get_type(self):
            return "leaf"


def find_paths(node: Node, path="", d=None):
    if d is None:
        d = {}

    if node.key is not None:
        d[node.key] = path
        print(node.key, path)
        return
    find_paths(node.left, path+'0', d)
    find_paths(node.right, path+'1', d)
    return d


def generate_tree(string: str):
    valores = np.asarray([*string])
    d = {i: j for i, j in zip(*np.unique(valores, return_counts=True, axis=0))}  # achar as contagens
    temp: list[Node] = []
    for i in sorted(d.keys(), key=d.__getitem__):
        temp += Leaf(i, d[i]),

    while len(temp) != 1:
        a = temp.pop()
        b = temp.pop()
        temp += Node(a.value + b.value, a, b),
        temp.sort(key=lambda x: x.value, reverse=True)

    print(*map(str, temp))
    return temp[0]


def encode(s: str):
    arv = generate_tree(s)
    tabela = find_paths(arv)
    nova_s = ""
    for i in s:
        nova_s += tabela[i]
    return arv, tabela, nova_s


if __name__ == '__main__':
    a, t, s_encoded = encode("banana")
    print(s_encoded)

