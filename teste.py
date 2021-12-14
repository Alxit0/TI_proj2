class ola:
    def __init__(self):
        self.o = 1
        self.a = 2

    def sum(self):
        return self.o + self.a


def main1():
    with open("ola", "bw+") as file:
        file.write(chr(10).encode("u8"))
        file.write(chr(13).encode("u8"))

    with open("ola", "br") as file:
        a = ""
        for i in file.readlines():
            a += i.decode("u8")

    print(*map(ord, a))


if __name__ == '__main__':
    print("0".zfill(4))
