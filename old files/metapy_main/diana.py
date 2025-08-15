""""""
import os
import subprocess

import pandas as pd


def run_diana_tno(file_directory, filename):
    """
    """
    c1 = 'call "C:\\Program Files\\Diana 10.2\\bin\\diana.exe"'
    c2 = f' -m {filename}'
    command = c1 + c2

    # run
    __ = subprocess.getstatusoutput(file_directory)
    _ = subprocess.getstatusoutput(command)
    _ = subprocess.getstatusoutput('del diana.ff')
    _ = subprocess.getstatusoutput('exit')


def construcao_modelo_nao_linear_tracao(caminho, f_t, f_c, eps):
    """
    """
    ecrsig_updated = f"     ECRSIG {eps[0]} {f_t[0]} {eps[1]} {f_t[1]}\n"
    ecrsig1_updated = f"            {eps[2]} {f_t[2]}\n"
    crkval_updated = f"     CRKVAL {f_t[0]} {f_c}\n"

    # Abertura arquivo e leitura
    with open(caminho, 'r', encoding="utf-8") as arquivo:
        lines = arquivo.readlines()
        for i, line in enumerate(lines):
            if 'CRKVAL' in line:
                lines[i] = crkval_updated
            if 'ECRSIG' in line:
                lines[i] = ecrsig_updated
                lines[i+1] = ecrsig1_updated
                break

    # Escrita no arquivo
    with open(caminho, 'w', encoding="utf-8") as arquivo:
        arquivo.writelines(lines)


def leitura_saida_modelo_nao_linear(caminho, id_x, id_y):
    """
    """
    x_num = []
    y_num = []

    with open(caminho, 'r', encoding="utf-8") as arquivo:
        lines = arquivo.readlines()
        for i, line in enumerate(lines):
            lista = line.split()
            # Leitura translacao nó 6
            if id_x in lista:
                x_num.append(abs(float(lines[i+2].split()[1])))
            # Leitura força nó 4
            if id_y in lista:
                y_num.append(2*abs(float(lines[i+1].split()[1])))

    return x_num, y_num
    