def is_equal(name1: str, name2: str):
    file1 = open(name1, "r").readlines()
    file2 = open(name2, "r").readlines()
    temp = file1 == file2

    #if not temp: see_dif(file1, file2)

    return temp


def em_numeros(*seq):
    for i in zip(*seq):
        print(*map(ord, i))


def see_dif(a, b):
    for i, j in zip(a, b):
        if i != j:
            print(i, j)