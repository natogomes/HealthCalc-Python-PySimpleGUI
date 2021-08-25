import PySimpleGUI as ps


def valid_str(valor):
    valido = False
    while not valido:
        entrada = str(valor).replace(',', '.').strip().upper()
        if entrada.isnumeric() or entrada == '':
            ps.Popup('ERRO! Digite um número Inteiro válido!', title='ERRO!')
            break
        else:
            valido = True
            return valido


def valid_int(valor):
    valido = False
    while not valido:
        try:
            entrada = int(valor)
        except:
            ps.Popup('ERRO! Digite um número Inteiro válido!', title='ERRO!')
            break
        else:
            valido = True
            return valido


def valid_float(valor1, valor2):
    valido = False
    while not valido:
        try:
            entrada1 = float(valor1)
            entrada2 = float(valor2)
        except:
            ps.Popup('ERRO! Digite um número Inteiro válido!', title='ERRO!')
            break
        else:
            valido = True
            return valido
