'''
Programa que debe recibir un archivo como entrada, analizarlo y devolver info.
por pantalla.

Entrada: Un archivo 'txt' con lineas en este formato
    [ID]=[Lista de numero separados por comas] [ORDENAR | BUSCAR] [argumentos]

Salida: Por consola en este formato
    identificador = [ID]
    Datos = [Array List]
    funciones = [lista de funciones]
    salida de la función = [SALIDA BUSCAR | ORDENAR]
'''

from tkinter import Tk
from tkinter.filedialog import askopenfilename
import re as regex


def open_file():
    Tk().withdraw()
    return askopenfilename()


def clear_ops(ops_list: list):
    ops_return = []
    op_regex = regex.compile('(BUSCAR|ORDENAR)(\s\d)?')
    for op in ops_list:
        if (type(op) is str) and (op != None) and (op != '\n') and (
                op != '') and (op != ' '):
            ops_return.append(op_regex.findall(op)[0])
    return ops_return


def execute_op(op: tuple, data: list):
    if op[0] == 'ORDENAR':
        data.sort()
        print('Datos ordenados: {}'.format(data))
    if op[0] == 'BUSCAR':
        if int(op[1]) in data:
            print('{} encontrado'.format(int(op[1])))
        else:
            print('{} no encontrado'.format(int(op[1])))


if __name__ == '__main__':
    file_data = open(open_file(), 'r')
    file_rows = file_data.readlines()

    for row in file_rows:
        split_row = row.split('=', 1)
        print('Identificador: {}'.format(split_row.pop(0)))

        split_op = regex.split('(BUSCAR\s\d$)|(ORDENAR,?)', split_row[0])

        num_regex = regex.compile('\d+,?')
        clear_numbers = list(
            map(lambda string: int(string.strip(',')),
                num_regex.findall(split_op.pop(0))))

        print('Datos: {}'.format(clear_numbers))
        ops = clear_ops(split_op)
        for op in ops:
            execute_op(op, clear_numbers)
        print()
