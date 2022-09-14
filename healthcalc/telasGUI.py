import PySimpleGUI as ps


def tela_ini():
    """
    -> Cria a janela inicial do programa.
    :return: Sem retorno.
    """
    ps.theme('DarkBrown1')

    introducao = [
        [ps.Text('HEALTHCALC é um aplicativo voltado para monitoramento '
                 'da sua saúde\n'
                 'baseado em cálculos com os dados mais atuais.\n'
                 'Observação: Esse programa não substitui o profissional de saúde!', justification='center',
                 font='arial 12')]
    ]
    checkbox = [
        [ps.Checkbox('IMC', size=(15, 1), pad=((10, 0), 10), font='arial 14', key='imc'),
         ps.Checkbox('DIETA DO SANGUE', pad=((70, 10), 10), font='arial 14', key='d.t.s')],
        [ps.Checkbox('GLICEMIA', size=(15, 1), pad=((10, 0), 10), font='arial 14', key='glicemia'),
         ps.Checkbox('PRESSÃO ARTERIAL', pad=((70, 10), 10), font='arial 14', key='p.a')],
    ]

    layout = [
        [ps.Text(f'{"HEALTHCALC"}'.center(53), font='Monoton 20', background_color='Brown', key='titulo')],
        [ps.Column(introducao)],
        [ps.Frame('', layout=checkbox, pad=(0, 10))],
        [ps.Button('Próximo', font='arial 12', size=(10, 1)),
         ps.CButton('Sair', font='arial 12', size=(6, 1))]
    ]
    return ps.Window('HealthCalc', element_justification='center', layout=layout, size=(552, 300), finalize=True)


def tela_imc():
    """
    -> Cria a janela para consulta do índice de massa corporal.
    :return: Sem retorno.
    """
    ps.theme('DarkBrown1')

    main = [
        [ps.Text('Peso:', size=(0, 1), font='arial 12'),
         ps.InputText(size=(5, 0), key='peso', text_color='white', font='arial 12'),
         ps.Text('Altura:', font='arial 12'),
         ps.InputText(size=(5, 0), key='altura', font='arial 12', text_color='white')],
        [ps.Output(size=(60, 8), text_color='white', font='arial 12', key='saida_imc')],
    ]

    layout = [
        [ps.Text(f'{"INDICE DE MASSA CORPORAL"}'.center(55), font='Monoton 17', background_color='Brown')],
        [ps.Column(main, element_justification='center', pad=(0, 12))],
        [ps.Button('Voltar', font='arial 12', size=(8, 1)),
         ps.Button('Verificar', font='arial 12', size=(10, 1)),
         ps.Button('Fechar', font='arial 12', size=(8, 1))]
    ]
    return ps.Window('Índice de Massa Corporal', size=(552, 300), element_justification='center',
                     modal=True, layout=layout, finalize=True)


def tela_gli():
    """
    -> Cria janela para consulta da glicemia.
    :return: Sem retorno.
    """
    ps.theme('DarkBrown1')

    main = [
        [ps.Text('mgdl:', font='arial 12'),
         ps.Input(size=(5, 0), key='glic', text_color='white', font='arial 12')],
        [ps.Output(size=(60, 8), text_color='white', font='arial 12', key='saida_glic')]
    ]

    layout = [
        [ps.Text(f'{"NÍVEL DE GLICEMIA"}'.center(70), font='Monoton 17', background_color='Brown')],
        [ps.Column(main, element_justification='center', pad=(0, 12))],
        [ps.Button('Voltar', font='arial 12', size=(8, 1)),
         ps.Button('Verificar', font='arial 12', size=(10, 1)),
         ps.Button('Fechar', font='arial 12', size=(8, 1))]
    ]
    return ps.Window('Glicemia', layout=layout, size=(552, 300), element_justification='center',
                     modal=True, finalize=True)


def tela_pa():
    """
    -> Cria a janela para consulta do estado da pressão arterial.
    :return: Sem retorno.
    """
    ps.theme('DarkBrown1')

    main = [
        [ps.Text('Sistólica:', font='arial 12'),
         ps.Input(size=(5, 1), key='p1', font='arial 12', text_color='white'),
         ps.Text('Diastólica:', font='arial 12', ),
         ps.Input(size=(5, 0), key='p2', font='arial 12', text_color='white')],
        [ps.Output(size=(60, 8), text_color='white', font='arial 12', key='saida_p.a')],
    ]

    layout = [
        [ps.Text(f'{"PRESSÃO ARTERIAL"}'.center(70), font='Monoton 17', background_color='Brown')],
        [ps.Column(main, element_justification='center', pad=(0, 12))],
        [ps.Button('Voltar', font='arial 12', size=(8, 1)),
         ps.Button('Verificar', font='arial 12', size=(10, 1)),
         ps.Button('Fechar', font='arial 12', size=(8, 1))]
    ]
    return ps.Window('Pressão Arterial', layout=layout, size=(552, 300), element_justification='center',
                     modal=True, finalize=True)


def tela_sangue():
    """
    -> Cria janela para consulta da dieta de acordo com tipo saguíneo.
    :return: Sem retorno.
    """
    ps.theme('DarkBrown1')

    main = [
        [ps.Text('Tipo sanguíneo:', font='arial 12'),
         ps.InputText(size=(5, 1), key='sangue', font='arial 12', text_color='white')],
        [ps.Output(size=(60, 8), key='saida_dts', text_color='white', font='arial 12')],
    ]

    layout = [
        [ps.Text(f'{"DIETA DO TIPO SANGUÍNEO"}'.center(60), font='Monoton 17', background_color='Brown')],
        [ps.Column(main, element_justification='center', pad=(0, 12))],
        [ps.Button('Voltar', font='arial 12', size=(8, 1)),
         ps.Button('Verificar', font='arial 12', size=(10, 1)),
         ps.Button('Fechar', font='arial 12', size=(8, 1))]
    ]
    return ps.Window('Tipo sanguíneo', layout=layout, modal=True, size=(552, 300), element_justification='center',
                     finalize=True)
