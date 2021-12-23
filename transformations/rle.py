import numpy as np


def transform(seq_array):
    compressed_seq = ''
    change = (seq_array[1:] != seq_array[:-1])
    x = np.append(np.where(change), len(seq_array) - 1)
    counter = np.diff(np.append(-1, x))

    for i in range(0, len(counter)):
        compressed_seq = compressed_seq + str(seq_array[x][i]) + str(counter[i])

    return compressed_seq


def entropia(a):
    _, cnt = np.unique(list(a), return_counts=True, axis=0)  # achar as contagens
    prob = cnt / len(a)
    return np.sum(-1 * prob * np.log2(prob))


if __name__ == '__main__':
    str_array = np.array(['A', 'A', 'B', 'C', 'C', 'C', 'C', 'C'])
    print(transform(str_array))
    print(entropia(transform(str_array)))
