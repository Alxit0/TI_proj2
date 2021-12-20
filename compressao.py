from typing import Literal
from codificacoes import Huffman as Huf
from codificacoes import LZ77
import analyser
import binarizacao as bins


def compressao(fich: str, cod: Literal["Huffman", "Lz77"], trans: Literal["BTW", "Delta", "MTF"] = "Null"):
    codificacao = {"Huffman": Huf.HuffmanCompressor(), "Lz77": LZ77.LZ77Compressor()}[cod]
    codificacao.compress('dataset/' + fich, 'dataset_compressed/' + f"{cod}_{trans}_{fich}")
    return f"{cod}_{trans}_{fich}"


def decompress(fich: str):
    a, b, c = fich.split('_')
    codificacao = {"Huffman": Huf.HuffmanCompressor(), "Lz77": LZ77.LZ77Compressor()}[a]
    codificacao.decompress("dataset_compressed/"+fich, "dataset_decompressed/"+c)


values = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
if __name__ == '__main__':
    a = Huf.HuffmanCompressor()
    name = compressao(values[0], "Lz77")
    decompress(name)
    print(analyser.is_equal("random.txt", "random.txt"))