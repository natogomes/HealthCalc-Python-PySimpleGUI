import PySimpleGUI as ps


def valid_str(valor):
    """
    -> Faz a validação do valor para saber se é uma string.
    :param valor: Valor de entrada string.
    :return: Retorna True ou False.
    """
    valido = False
    while not valido:
        entrada = str(valor).replace(',', '.').strip().upper()
        if entrada.isnumeric() or entrada == '':
            ps.Popup('ERRO! Digite um valor válido', font='arial 12', title='ERRO!')
            break
        else:
            valido = True
            return valido


def valid_int(valor):
    """
    -> Faz a validação do valor para saber se é um número inteiro.
    :param valor: Valor de entrada número inteiro.
    :return: Retorna True ou False.
    """
    valido = False
    while not valido:
        try:
            entrada = int(valor)
        except:
            ps.Popup('ERRO! Digite um número Inteiro válido!', font='arial 12', title='ERRO!')
            break
        else:
            valido = True
            return valido


def valid_float(valor1, valor2):
    """
    -> Faz a validação para saber se o valor é float.
    :param valor1: Primeiro valor tem que estar no tipo float.
    :param valor2: Segundo valor tem quee estar no tipo float.
    :return: Retorna True ou False.
    """
    valido = False
    while not valido:
        try:
            entrada1 = float(valor1)
            entrada2 = float(valor2)
        except:
            ps.Popup('ERRO! Digite um valor válido!', font='arial 12', title='ERRO!')
            break
        else:
            valido = True
            return valido
