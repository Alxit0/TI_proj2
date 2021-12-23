import numpy as np


def transform(input_name, output_name):
    with open(input_name, 'rb') as f:
        seq_array = np.array([*f.read().decode('u8')])

    compressed_seq = ''
    change = (seq_array[1:] != seq_array[:-1])
    x = np.append(np.where(change), len(seq_array) - 1)
    counter = np.diff(np.append(-1, x))

    for i in range(0, len(counter)):
        compressed_seq = compressed_seq + str(seq_array[x][i]) + str(counter[i])

    with open(output_name, 'wb+') as f:
        f.write(compressed_seq.encode('u8'))

    return compressed_seq


def entropia(a):
    _, cnt = np.unique(list(a), return_counts=True, axis=0)  # achar as contagens
    prob = cnt / len(a)
    return np.sum(-1 * prob * np.log2(prob))


if __name__ == '__main__':
    transform('/Users/alexito_player/PycharmProjects/TI_proj2/algoritmes',
              '/Users/alexito_player/PycharmProjects/TI_proj2/algoritmes_ola.txt')
