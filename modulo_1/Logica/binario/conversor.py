def string_para_binario(nome):
    result = ' '.join(format(ord(c), 'b') for c in nome)
    return result


def binario_para_string(codigo_binario):
    grupos_de_bits = [codigo_binario[
        i:i+8] for i in range(0, len(codigo_binario), 8)]

    caracteres = [chr(int(bits, 2)) for bits in grupos_de_bits]

    resultado = ''.join(caracteres)

    return resultado

if __name__ == '__main__':
    print(string_para_binario('maxwell'))
    print(binario_para_string(
        '1101101 1100001 1111000 1110111 1100101 1101100 1101100'))
'''
bit = 0 ou 1
byte = 8 bits
kilobyte = 1024 bytes
megabyte = 1024 kilobytes
gigabyte = 1024 megabytes
terabyte = 1024 gigabytes

100 mbps
'''

