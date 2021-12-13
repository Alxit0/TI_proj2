def is_equal(name1: str, name2: str):
    file1 = open(name1, "r")
    file2 = open(name2, "r")
    return file1.readlines() == file2.readlines()