from typing import Literal
from codificacoes import Huffman as Huf
from codificacoes import LZ77
import analyser
from transformations import btw, delta_encoding, move_to_front
cods = {"Huffman": Huf.HuffmanCompressor(), "Lz77": LZ77.LZ77Compressor()}


def compressao(fich: str, cod: Literal["Huffman", "Lz77"], trans: Literal["BTW", "Delta", "MTF"] = "Null"):
    codificacao = cods[cod]
    if trans != "Null":
        transformacao = {"BTW": btw, "Delta": delta_encoding, "MTF": move_to_front}[trans]

    codificacao.compress('dataset/' + fich, 'dataset_compressed/' + f"{cod}_{trans}_{fich}")
    return f"{cod}_{trans}_{fich}"


def descompressao(fich: str):
    a, b, c = fich.split('_')
    codificacao = cods[a]
    codificacao.decompress(fich, "dataset_decompressed/"+c)


values = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
if __name__ == '__main__':
    ei = values[2]
    name = compressao(ei, "Lz77")
    descompressao(name)
    print(analyser.is_equal(ei, ei))
