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


def encode(s: str):
    def find_paths(node: Node, path="", d=None):
        if d is None:
            d = {}

        if node.key is not None:
            d[node.key] = path
            return
        find_paths(node.left, path + '0', d)
        find_paths(node.right, path + '1', d)
        return d

    def generate_tree(string: str):
        valores = np.asarray([*string])
        d = {k: j for k, j in zip(*np.unique(valores, return_counts=True, axis=0))}  # achar as contagens
        temp: list[Node] = []
        for i in sorted(d.keys(), key=d.__getitem__):
            temp += Leaf(i, d[i]),

        while len(temp) != 1:
            a = temp.pop()
            b = temp.pop()
            temp += Node(a.value + b.value, a, b),
            temp.sort(key=lambda x: x.value, reverse=True)
        return temp[0]

    def convert(seq):
        a = ""
        for i in range(0, len(seq), 8):
            a += chr(int(seq[i:i + 8], 2))
        return a

    arv = generate_tree(s)
    tabela = find_paths(arv)
    nova_s = ""
    for i in s:
        nova_s += tabela[i]
    return arv, convert(nova_s)
    # return arv, nova_s


def decode(s: str, arv: Node):
    def translate(seq):
        b = ""
        for j in seq:
            b += bin(ord(j))[2:].zfill(8)
        return b

    s = translate(s)
    pointer = arv
    resp = ''
    for i in s:
        if i == '0':
            pointer = pointer.left
        elif i == '1':
            pointer = pointer.right

        if pointer.key is not None:
            resp += pointer.key
            pointer = arv
    return resp


def main():
    arvore, s_encoded = encode("Burrows–Wheeler transform => make easier to compress (rearanges in order to make "
                               "more repeated leters together)")
    print(arvore)
    print(s_encoded)

    print(decode(s_encoded, arvore))


def main1():
    temp = "01011101110"
    print(temp)
    a = ""
    for i in range(0, len(temp), 8):
        a += chr(int(temp[i:i+8], 2))
    print(a)

    b = ""
    for i in a:
        b += bin(ord(i))[2:]
    print(b)


if __name__ == '__main__':
    main()
