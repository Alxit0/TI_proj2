# Instead of always transmitting an "original" dictionary, it is simpler to just agree on an initial set.
# Here we use the 256 possible values of a byte:
common_dictionary = list(range(256))


def transform(input_name, output_name):
    with open(input_name, 'r')as f:
        plain_text = f.read()
    # Change to bytes for 256.
    plain_text = plain_text.encode('utf-8')

    # Changing the common dictionary is a bad idea. Make a copy.
    dictionary = common_dictionary.copy()

    # Transformation
    compressed_text = list()  # Regular array
    rank = 0

    # Read in each character
    for c in plain_text:
        rank = dictionary.index(c)  # Find the rank of the character in the dictionary [O(k)]
        compressed_text.append(rank)  # Update the encoded text

        # Update the dictionary [O(k)]
        dictionary.pop(rank)
        dictionary.insert(0, c)

    # final = b''.join(chr(i) for i in compressed_text)
    with open(output_name, 'wb+') as f:
        f.write(b''.join(chr(i).encode('u8') for i in compressed_text))

    # return compressed_text


if __name__ == '__main__':
    transform('/Users/alexito_player/PycharmProjects/TI_proj2/algoritmes',
              '/Users/alexito_player/PycharmProjects/TI_proj2/algoritmes_ola.txt')