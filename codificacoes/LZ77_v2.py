class lz77:
    """
       Esta classe comprime uma sequêencia de caracteres usando
       o algoritmo LZ77 como descrito em

       Esta é uma implementação didática, para exemplificar
       o funcionamento do algoritmo, e não possui nenhum tipo de
       otimização, por isso seu desempenho em situações reais
       deve ser muito abaixo do esperado.
    """
    def __init__(self, window_size = 65535, buffer_size=255):
        """
           Carrega os parâmetros de tamanho de janela e buffer
           de look-ahead
        """
        self.window_size = window_size
        self.buffer_size = buffer_size

    def encode(self, str):
        """
            Aplica o algoritmo LZ77 na cadeia de entrada, gerando
            uma lista de "tuplas" na saída. Cada tupla corresponde
            a (posição, tamanho, literal) onde posição é a posição
            relativa da cadeia encontrada na janela, tamanho é o
            tamanho dessa cadeia e literal é o símbolo que segue
            a cadeia nessa sequência.
        """
        print('-'*100)
        ret = []
        i = 0
        autal = 1
        tot = len(str)
        while i < len(str):
            if autal == int(100 - (len(str) - i) * 100 / tot):
                autal += 1
                print(end='#')
            begin_window = i-self.window_size
            if begin_window < 0:
                begin_window = 0
            window = str[begin_window:i]
            buffer = str[i:i+self.buffer_size]
            tuple = (0, 0, str[i])
            # Este "loop" é o "coração" do algoritmo. Aqui procuramos
            # a maior sequência dentro da janela (window) que case
            # com o início do buffer. A implementação atual simplesmente
            # procura por ocorrências de substrings cada vez menores
            # do buffer até encontrar alguma. Implementações mais
            # eficientes usariam um dicionário de prefixos, uma trie
            # ou uma tabela de espalhamento.
            for size in range(len(buffer), 0, -1):
                index = window.rfind(buffer[0:size])
                if index >= 0:
                    literal = '' # a string vazia representa
                                 # o final do arquivo.
                    if i + size < len(str):
                        literal = str[i+size]
                    tuple = (len(window)-index-1, size, literal)
                    break
            i = i + tuple[1] + 1
            ret = ret + [tuple]
        print('#')
        return ret

    def decode(self, list):
        """
            A decodificação é extremamente simples: basta copiar a
            subsequência indicada pela tupla para o final da sequência
            de saída e acrescentar o novo carácter literal.
        """
        ret = ''
        for tuple in list:
            pos = len(ret) - tuple[0] - 1
            ret = ret + ret[pos:pos+tuple[1]] + tuple[2]
        return ret


if __name__ == '__main__':
    with open("/Users/alexito_player/PycharmProjects/TI_proj2/dataset/random.txt", "r") as f:
        r = f.read()
    print(len(r))
    print(len(lz77().encode(r)))
