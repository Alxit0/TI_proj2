def bin_compression(seq: str):
    janela = 8
    final = chr(len(seq) % janela)
    for i in range(0, len(seq), janela):
        final += chr(int(seq[i:i+janela], 2))
    return final


def bin_decompression(seq: str):
    final = ""
    for i in seq[1:-1]:
        final += bin(ord(i))[2:].zfill(8)
    final += bin(ord(seq[-1]))[2:].zfill(ord(seq[0]))
    return final


class _PlainNode:
    def __init__(self, key=None, left=None, right=None):
        self.left = left
        self.right = right
        self.key = key


def regenerar_arvore(seq: str, left, right):
    def _tenta(seq1: str):
        nivel = 0
        atual = ''
        resp = []
        for i in seq1[1:-1]:
            if i == left:
                nivel += 1
            elif i == right:
                nivel -= 1
            atual += i
            if nivel == 0:
                resp += atual,
                atual = ''
        return resp
    if len(seq) == 1:
        return _PlainNode(seq)
    splited = _tenta(seq)
    return _PlainNode(None, regenerar_arvore(splited[0], left, right),
                      regenerar_arvore(splited[1], left, right))


def regenera_texto(arv: _PlainNode, seq):
    pointer = arv
    final = ""
    for i in seq:
        if i == '0':
            pointer = pointer.left
        elif i == '1':
            pointer = pointer.right

        if pointer.key is not None:
            final += pointer.key
            pointer = arv
    return final


if __name__ == '__main__':
    a = regenerar_arvore("<a<cb>>", *"<>")
    print(a)
    print(regenera_texto(a, "01010011001000011101011101010000011101010000101000110100100100101101011010010111000000000000000000000000000000000000000000000000010101100001010010100011101101100011110010010111010101001101010100100010010000000111010100100100001010100110101010010001011101101110110100100011011100100000101110000100011100000111011010100110111100101110001110001000101110101110010001101100101111100110010111110111011010010001101110010000010111000010001110000011101101010011011110010111000111000100000001111011010011100110100000111110000100110011011001000010010111100000011011000001001111010100000001111100111110011000001100001001100101010011101100010100111011101011110001000111111110101011001011000101100001011011011100100100101101001110001100111001110101011000111011101111010000000101011010110100000100000110100101100000100001101100001011001110001100110100001010001101010000111111111000110001100000011110111110000111110011101011010010001100000001011010100011011110010011001110001100110100001000001101001011000000100011011111000001111000111111000011110010000100100010110100110010011101100000110011011010010011000111001001110111100"))
