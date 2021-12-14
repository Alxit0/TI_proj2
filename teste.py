from codificacoes import LZ77


class ola:
    def __init__(self):
        self.o = 1
        self.a = 2

    def sum(self):
        return self.o + self.a


def main1():
    with open("ola", "bw+") as file:
        file.write("Ola Eu sou o Alexandre Silva Regalado".encode("u8"))

    with open("ola", "br") as file:
        a = ""
        for i in file.readlines():
            a += i.decode("u8")

    print(a)


if __name__ == '__main__':
    a = LZ77.LZ77Compressor()