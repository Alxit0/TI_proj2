import analyser
import binarizacao as bins


class _Node:

    left_sep = "<"
    right_sep = ">"

    def __init__(self, value=None, key=None, left=None, right=None):
        self.value = value
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        if self.key is None:
            return f"{self.left_sep}{self.left}{self.right}{self.right_sep}"
        else:
            return str(self.key)


def _generate_tree(seq: str):
    # obter as contagens
    conts = {}
    for i in seq:
        if i in conts:
            conts[i] += 1
        else:
            conts[i] = 1
    print(">>> Contagens concluidas")
    nodes = []
    for i in sorted(conts, key=conts.__getitem__):
        nodes += _Node(conts[i], i),

    while len(nodes) != 1:
        a, b = nodes[:2]
        nodes = nodes[2:]
        nodes.insert(0, _Node(a.value + b.value, None, b, a))
        nodes = sorted(nodes, key=lambda x: x.value)
    print(">>> Arvore concluida")
    # print(nodes)
    return nodes[0]


def _find_paths(node: _Node, path="", d=None):
    if d is None:
        d = {}

    if node.key is not None:
        d[node.key] = path
        return
    _find_paths(node.left, path + '0', d)
    _find_paths(node.right, path + '1', d)
    return d


def _binarizacao(seq: str, paths: dict):
    final = ''
    for i in seq:
        final += paths[i]
    print(">>> Binarizacao completa")
    return final


class HuffmanCompressor:
    def __init__(self):
        pass

    def compress(self, input_file_path, output_file_path=None):

        if output_file_path is None:
            output_file_path = "dataset_compressed/" + input_file_path
        print("="*20, f"Decompress of {input_file_path}", "="*20)
        data = ""
        with open(input_file_path, "r")as file:
            for i in file.readlines():
                data += i
        arv = _generate_tree(data)

        psths = _find_paths(arv)

        seps = []
        for i in range(1, 255):
            if chr(i) not in psths:
                seps += chr(i)
            if len(seps) == 2:
                break
        _Node.left_sep, _Node.right_sep = seps
        # _Node.left_sep, _Node.right_sep = "<", ">"
        tam_arv = str(arv).count('\n')
        seq = _binarizacao(data, psths)
        # print(seq)
        string = (str(tam_arv) + _Node.left_sep + _Node.right_sep + str(arv) + '\n').encode("u8")
        with open(output_file_path, "bw+")as file:
            file.write(string + bins.bin_compression(seq))
        # print(str(tam_arv) + _Node.left_sep + _Node.right_sep + str(arv))
        # print(bins.bin_compression(seq))

        # print("=="*100)
        # print(bins.bin_decompression(bins.bin_compression(seq).decode("u8")))

    def decompress(self, input_file_path, output_file_path=None):
        input_file_path = "dataset_compressed/" + input_file_path
        print("=" * 20, f"Decompress of {input_file_path}", "=" * 20)
        arv = ""
        data = ""
        with open(input_file_path, "br")as file:
            line = file.readline().decode("u8")
            arv += line[1:]
            for _ in range(int(line[0])):
                arv += file.readline().decode("u8")

            for i in file.readlines():
                data += i.decode("u8")
        # print(arv)
        # print(data)

        l, r = arv[:2]
        # print(arv[2:])
        arv = bins.regenerar_arvore(arv[2:], l, r)
        # print(data)
        # print(bins.bin_decompression(data)[-10:])
        texto = bins.regenera_texto(arv, bins.bin_decompression(data))
        # print(bins.bin_decompression(data))
        # print(analyser.em_numeros(data))
        # print(texto)
        with open(output_file_path, "w+")as file:
            file.write(texto)


if __name__ == '__main__':
    a = HuffmanCompressor()
    a.compress("algoritmes", "algoritmes_decompressed")

    analyser.em_numeros("abcdefg")
