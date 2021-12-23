from typing import Literal
from codificacoes import Huffman, LZ77
from codificacoes import Shanon_Fano_v2
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


def main():
    for i,j in enumerate(values):
        print(f"\t [{i+1}] {j}")
    name = values[int(input('Opçao: '))-1]
    print('ficheiro escolhido:', name)
    for i,j in enumerate(temp := ["Huffman", "Lz77", "Shanon"]):
        print(f"\t [{i+1}] {j}")
    try:
        codificacao = temp[int(input('Opçao: '))-1]
        print(f"Codificacao {codificacao}")
    except:
        print('tecla invalida. Mudado par Huffman')
        codificacao = "Huffman"

    for i,j in enumerate(temp := ["Nenhum", "Burrows-Wheeler",
                                  "Delta enconding", "Move to front", "Run Lengh enconding"]):
        print(f"\t [{i}] {j}")
    trans = ["Null", "BTW", "Delta", "MTF", "RLE"][int(input('Opçao: '))]

    nome = compressao(name, codificacao, trans)

    l1 = len(open(f"dataset/{name}", "rb").read())
    l2 = len(open(f"dataset_compressed/{nome}", "rb").read())
    print(f"{l1} caracteres ==> {l2} caracteres")
    print(f"{100 - l2 * 100 / l1}% melhorado")


if __name__ == '__main__':
    main()
    # for i in range(3,-1,-1):
    #     ei = values[i]
    #     print(ei)
    #     name = compressao(ei, "Lz77", "BTW")
    #
    #     # for i in ["BTW", "Delta", "MTF", "RLE"]:
    #     #     name = compressao(ei, "Huffman", i)
    #     l1 = len(open(f"dataset/{ei}", "rb").read())
    #     l2 = len(open(f"dataset_compressed/{name}", "rb").read())
    #     print(f"{l1} ==> {l2}")
    #     print(f"{100 - l2*100/l1}%")
    #
    # # descompressao(name)
    # # print(analyser.is_equal(ei, ei))
