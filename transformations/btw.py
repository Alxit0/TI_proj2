def transform(input_name, output_name):
    with open(output_name, 'wb+') as file:
        file.write(b'')
    with open(input_name, 'r') as f:
        # s = f.read()
        for s in f.readlines():
            """Apply Burrows–Wheeler transform to input string."""
            # assert "\002" not in s and "\003" not in s, "Input string cannot contain STX and ETX characters"
            # s = "\002" + s + "\003"  # Add start and end of text marker
            table = sorted(s[i:] + s[:i] for i in range(len(s)))  # Table of rotations of string
            last_column = [row[-1:] for row in table]  # Last characters of each row

            with open(output_name, 'ab+') as file:
                file.write("".join(last_column).encode('u8'))
            # return "".join(last_column)  # Convert list of characters into string


def detransform(r: str) -> str:
    """Apply inverse Burrows–Wheeler transform."""
    table = [""] * len(r)  # Make empty table
    for i in range(len(r)):
        table = sorted(r[i] + table[i] for i in range(len(r)))  # Add a column of r
    s = [row for row in table if row.endswith("\003")][0]  # Find the correct row (ending in ETX)
    return s.rstrip("\003").strip("\002")  # Get rid of start and end markers


def main():
    pass


if __name__ == '__main__':
    print(transform('/Users/alexito_player/PycharmProjects/TI_proj2/algoritmes',
                    '/Users/alexito_player/PycharmProjects/TI_proj2/algoritmes_oal.txt'))
