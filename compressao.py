from typing import Literal
from codificacoes import Huffman, LZ77
from codificacoes import Shanon_Fano_v2
import analyser
from transformations import btw, delta_encoding, move_to_front, rle
cods = {"Huffman": Huffman.HuffmanCompressor(), "Lz77": LZ77.LZ77Compressor(),
        "Shanon": Shanon_Fano_v2.ShanonFannoCompressor()}


def compressao(fich: str, cod: Literal["Huffman", "Lz77", "Shanon"], trans: Literal["BTW", "Delta", "MTF", "RLE"] = "Null"):
    codificacao = cods[cod]
    new_name = 'dataset/' + fich
    if trans != "Null":
        transformacao = {"BTW": btw, "Delta": delta_encoding, "MTF": move_to_front,
                         "RLE": rle}[trans]
        new_name = 'dataset_transformado/' + f"{trans}_{fich}"
        transformacao.transform('dataset/' + fich, new_name)

    codificacao.compress(new_name, 'dataset_compressed/' + f"{cod}_{trans}_{fich}")
    return f"{cod}_{trans}_{fich}"


def descompressao(fich: str):
    a, b, c = fich.split('_')
    codificacao = cods[a]
    codificacao.decompress(fich, "dataset_decompressed/"+c)


values = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
if __name__ == '__main__':
    ei = values[1]
    name = compressao(ei, "Shanon")

    for i in ["BTW", "Delta", "MTF", "RLE"]:
        name = compressao(ei, "Huffman", i)
        l1 = len(open(f"dataset/{ei}", "r").read())
        l2 = len(open(f"dataset_compressed/{name}", "r").read())
        print(f"{l1} ==> {l2}")
        print(f"{100 - l2*100/l1}%")

    # descompressao(name)
    # print(analyser.is_equal(ei, ei))
