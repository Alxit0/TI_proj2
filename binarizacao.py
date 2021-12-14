def bin_compression(seq: str):
    janela = 8
    final = chr(len(seq) % janela)
    if final == chr(0):
        final = chr(8)
    for i in range(0, len(seq), janela):
        temp = int(seq[i:i+janela], 2)
        final += chr(temp)
        # if temp == 92: final += chr(92)
    return final.encode("u8")


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
