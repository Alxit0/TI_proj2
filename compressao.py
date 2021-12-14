from codificacoes import Huffman as Huf
from codificacoes import LZ77
import analyser
import binarizacao as bins


values = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
if __name__ == '__main__':
    a = Huf.HuffmanCompressor()
    # f = "bible.txt"
    for f in values:
        f1 = f
        f2 = f
        a.compress(f1)
        a.decompress(f2)
        print(analyser.is_equal("dataset/"+f1, "dataset_decompressed/"+f2))