import PySimpleGUI as ps


def tela_ini():
    ps.theme('DarkBrown1')
    layout = [
        [ps.Text(f'{"HEALTHCALC"}'.center(83), font='Monoton 20', background_color='Brown', key='titulo')],
        [ps.Text('HEALTHCALC é um aplicativo voltado para monitoramento '
                 'da sua saúde.\n'
                 'Baseado em cálculos com os dados mais atuais.\n'
                 'Observação: Esse programa não substitui o profissional de saúde!', justification='center')],
        [ps.Text('_' * 61)],
        [ps.Checkbox('IMC', size=(15, 1), font='arial 14', key='imc'), ps.Checkbox('DIETA DO SANGUE', font='arial 14',
                                                                                   key='d.t.s')],
        [ps.Checkbox('GLICEMIA', size=(15, 1), font='arial 14', key='glicemia'), ps.Checkbox('PRESSÃO ARTERIAL',
                                                                                             font='arial 14',
                                                                                             key='p.a')],
        [ps.Text('_' * 61)],
        [ps.Button('Próximo')]
    ]
    return ps.Window('HealthCalc', layout=layout, finalize=True)


def tela2i():
    ps.theme('DarkBrown1')
    layout = [
        [ps.Text(f'{"INDICE DE MASSA CORPORAL"}'.center(35), font='arial 15', background_color='Brown', )],
        [ps.Text('Peso:', size=(12, 1), justification='right', font='arial 12'),
         ps.InputText(size=(5, 0), key='peso', text_color='white', font='arial 11'),
         ps.Text('Altura:', font='arial 12'),
         ps.InputText(size=(5, 0), key='altura', font='arial 11', text_color='white')],
        [ps.Output(size=(42, 8), text_color='white', font='arial 11')],
        [ps.Button('Voltar'), ps.Button('Verificar'), ps.Button('Fechar')]
    ]
    return ps.Window('Índice de Massa Corporal', modal=True, layout=layout, finalize=True)


def tela2g():
    ps.theme('DarkBrown1')
    layout = [
        [ps.Text(f'{"NÍVEL DE GLICEMIA"}'.center(44), font='arial 15', background_color='Brown', )],
        [ps.Text('mgdl:', size=(17, 1), font='arial 12', justification='right'),
         ps.Input(size=(5, 0), key='glic', text_color='white', font='arial 11')],
        [ps.Output(size=(42, 8), text_color='white', font='arial 11')],
        [ps.Button('Voltar'), ps.Button('Verificar'), ps.Button('Fechar')]
    ]
    return ps.Window('Glicemia', layout=layout, modal=True, finalize=True)


def tela2p():
    ps.theme('DarkBrown1')
    layout = [
        [ps.Text(f'{"PRESSÃO ARTERIAL"}'.center(42), font='arial 15', background_color='Brown')],
        [ps.Text('Sistólica:', font='arial 12', size=(12, 1), justification='right'),
         ps.Input(size=(5, 1), key='p1', font='arial 11', text_color='white'),
         ps.Text('Diastólica:', font='arial 12', ),
         ps.Input(size=(5, 0), key='p2', font='arial 11', text_color='white')],
        [ps.Output(size=(42, 8), text_color='white', font='arial 11')],
        [ps.Button('Voltar'), ps.Submit('Verificar'), ps.Button('Fechar')]
    ]
    return ps.Window('Pressão Arterial', layout=layout, modal=True, finalize=True)


def tela2d():
    ps.theme('DarkBrown1')
    layout = [
        [ps.Text(f'{"DIETA DO TIPO SANGUÍNEO"}'.center(61), font='arial 15', background_color='Brown')],
        [ps.Text('Tipo sanguíneo:', font='arial 12', size=(30, 1), justification='right'),
         ps.InputText(size=(5, 1), key='sangue', font='arial 11', text_color='white')],
        [ps.Output(size=(60, 15), key='retorno', text_color='white', font='arial 11')],
        [ps.Button('Voltar'), ps.Submit('Verificar'), ps.Button('Fechar')]
    ]
    return ps.Window('Tipo sanguíneo', layout=layout, modal=True, finalize=True)
