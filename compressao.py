from codificacoes import Huffman as huf
from codificacoes import LZ77
import analyser


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


if __name__ == '__main__':
    a = huf.HuffmanCompressor()
    a.compress("algoritmes", "algoritmes_comp")
    a.decompres("algoritmes_comp.txt", "algoritmes_decompressed")

    print(analyser.is_equal("algoritmes", "algoritmes_decompressed"))
