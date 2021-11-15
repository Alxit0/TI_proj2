import numpy as np
from matplotlib import pyplot as plt


def get_info(caminho: str):
    with open(caminho, "r") as file:
        a = []
        for i in file.readlines():
            a += list([*i.replace('\n', '\\n')])
    return np.asarray(a)


def entropia(a):
    _, cnt = np.unique(a, return_counts=True, axis=0)  # achar as contagens
    prob = cnt / len(a)
    return np.sum(-1 * prob * np.log2(prob))


def histograma(a, b):
    #  mostra o histograma num grafico de barras
    plt.figure()
    plt.bar(a, b)
    plt.show()
    plt.close()


def histograma_org(a, b, name):
    d = {}
    for i,j in zip(a, b):
        d[i] = j

    plt.figure(name)
    plt.bar(sorted(d.keys(), key=d.__getitem__, reverse=True), sorted(d.values(), reverse=True))
    plt.show()
    plt.close()


values = ["bible.txt", "finance.csv", "jquery-3.6.0.js", "random.txt"]
if __name__ == '__main__':
    for i in values:
        a = get_info("dataset/"+i)
        b, cnt = np.unique(a, return_counts=True, axis=0)  # achar as contagens
        print(i, entropia(a))

        histograma_org(b, cnt, i)


