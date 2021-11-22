import numpy as np
from matplotlib import pyplot as plt
import btw


def get_info(caminho: str):
    with open(caminho, "r") as file:
        a = []
        for i in file.readlines():
            a += list([*i.replace('\n', '\\n')])
    a = np.asarray(a)
    return a


def entropia(a):
    _, cnt = np.unique(a, return_counts=True, axis=0)  # achar as contagens
    prob = cnt / len(a)
    return np.sum(-1 * prob * np.log2(prob))


def histograma(a, b, name, organizacao=False):
    def normal():
        #  mostra o histograma num grafico de barras
        plt.figure(name)
        plt.bar(a, b)
        plt.show()
        plt.close()

    def organizado():
        d = {}
        for i, j in zip(a, b):
            d[str(i)] = j

        plt.figure(name)
        plt.bar(sorted(d.keys(), key=d.__getitem__, reverse=True), sorted(d.values(), reverse=True))
        plt.show()
        plt.close()

    if organizacao:
        organizado()
    else:
        normal()


def diferenca(letras):
    final = [ord(letras[0])]
    for i in range(len(letras[1:])):
        final += ord(letras[i]) - ord(letras[i-1]),
    return np.asarray(final)


values = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
if __name__ == '__main__':
    i = values[-1]
    a = get_info("dataset/"+i)
    for i in (t := ''.join(a)):
        if i.isalpha() or i == ' ':
            print(end=i)
    print("")

    for i in btw.bwt(t):
        if i.isalpha() or i == ' ':
            print(end=i)
    print("")

    '''print(i, entropia(a))
    b, cnt = np.unique(a, return_counts=True, axis=0)  # achar as contagens
    histograma(b, cnt, i, organizacao=True)'''




