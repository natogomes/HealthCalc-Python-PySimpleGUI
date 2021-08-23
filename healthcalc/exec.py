from funcoes import *
from telasGUI import *
import PySimpleGUI as ps

t1, t2 = tela_ini(), None
while True:
    window, event, values = ps.read_all_windows()

    if window == t1 and event == ps.WIN_CLOSED:
        break

    elif window == t1 and event == 'Próximo' and values['imc']:
        t1.hide()
        ps.popup('''VOCÊ SABIA???'
        
    IMC é a sigla para Índice de Massa Corporal,
que é um cálculo que serve para avaliar se a pessoa
está dentro do seu peso ideal em relação à altura.
Assim, de acordo com o valor do resultado de IMC,
a pessoa pode saber se está dentro do peso ideal,
acima ou abaixo do peso desejado.''', font='arial 12', title='Índice de Massa Corporal')
        t2 = tela2i()
        while True:
            window, event, values = ps.read_all_windows()
            if window == t2 and event == 'Voltar':
                window.close()
                t1 = tela_ini()
                break
            elif window == t2 and event == 'Fechar':
                exit()
            if window == t2 and event == ps.WIN_CLOSED:
                exit()
            elif values['peso'] == '' and values['altura'] == '' and event == 'Verificar':
                ps.popup('Informe os valores para obter o resultado!')
                continue
            peso = float(f'{values["peso"]}'.replace(',', '.'))
            altura = float(f'{values["altura"]}'.replace(',', '.'))
            print(f'PESO: {peso}Kg.')
            print(f'ALTURA: {altura}m.')
            print(f'O seu índice de massa corporal é:\n{imc(peso, altura)}')
            print('-' * 66)
            continue

    elif window == t1 and event == 'Próximo' and values['glicemia']:
        t1.hide()
        ps.popup('''VOCÊ SABIA???
        
    A glicemia de jejum ou glicose em jejum, é um
exame de sangue que mede a taxa de glicose na circulação
sanguínea e precisa ser feito após um jejum de 8 a 12 horas
de duração, ou de acordo com a orientação do médico, sem o
consumo de qualquer alimento ou bebida, exceto água.
Este exame é muito utilizado para investigar o diagnóstico
de diabetes, e para monitorar as taxas de açúcar no sangue
de pessoas diabéticas ou com risco para esta doença.''', font='arial 12', title='Glicemia de Jejum')
        t2 = tela2g()
        while True:
            window, event, values = ps.read_all_windows()
            if window == t2 and event == 'Voltar':
                window.close()
                t1 = tela_ini()
                break
            elif window == t2 and event == 'Fechar':
                exit()
            if window == t2 and event == ps.WIN_CLOSED:
                exit()
            elif values['glic'] == '' and event == 'Verificar':
                ps.popup('Informe os valores para obter o resultado!')
                continue
            glic = int(values['glic'])
            print(f'Nível de glicemia: ({glic})\n{glicemy(glic)}')
            print('-' * 66)
            continue

    elif window == t1 and event == 'Próximo' and values['p.a']:
        t1.hide()
        ps.popup('''VOCÊ SABIA???
        
    A medição da pressão arterial identifica a intensidade
com que o fluxo de sangue passa pelas suas artérias.
Para isso, os valores de referência são representados
em milímetros de mercúrio (mmHg), sendo composto por duas
medidas, denominadas como SISTÓLICA e DIASTÓLICA.''', font='arial 12', title='Pressão arterial')
        t2 = tela2p()
        while True:
            window, event, values = ps.read_all_windows()
            if window == t2 and event == 'Voltar':
                window.close()
                t1 = tela_ini()
                break
            elif window == t2 and event == 'Fechar':
                exit()
            if window == t2 and event == ps.WIN_CLOSED:
                exit()
            elif values['p1'] == '' and values['p2'] == '' and event == 'Verificar':
                ps.popup('Informe os valores para obter o resultado!')
                continue
            p1 = float(values['p1'].replace(',', '.').strip())
            p2 = float(values['p2'].replace(',', '.').strip())

            print(f'Estado da sua pressão arteiral:\n'
                  f'Sistólica: ({p1})\n'
                  f'Diastólica: ({p2})\n{presart(p1, p2)}')
            print('-' * 66)
            continue

    elif window == t1 and event == 'Próximo' and values['d.t.s']:
        t1.hide()
        ps.popup('''VOCÊ SABIA???
        
    A dieta do tipo sanguíneo é um tipo de alimentação
em que as pessoas adaptam os alimentos de acordo com 
o seu tipo de sangue, ou seja, se possui sangue do tipo
A, B, AB ou O. 
Essa dieta foi proposta e desenvolvida pelo médico
naturopata Peter d'Adamo e publicada em seu livro
"Eat right for your type" que significa "Alimente-se
corretamente deacordo com seu tipo de sangue",
publicado em 1996 nos Estados Unidos da América.''', font='arial 12', title='Dieta do tipo sanguíneo')
        t2 = tela2d()
        while True:
            window, event, values = ps.read_all_windows()
            if window == t2 and event == 'Voltar':
                window.close()
                t1 = tela_ini()
                break
            elif window == t2 and event == 'Fechar':
                exit()
            elif window == t2 and event == ps.WIN_CLOSED:
                exit()
            elif values['sangue'] == '' and event == 'Verificar':
                ps.popup('Informe os valores para obter o resultado!')
                continue
            s = values['sangue']
            dieta(s)
            print('-' * 93)
            continue

    elif window == t1 and event == 'Próximo':
        ps.popup('Informe uma opção!')


