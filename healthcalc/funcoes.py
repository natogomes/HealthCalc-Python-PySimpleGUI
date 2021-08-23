import PySimpleGUI as ps


def imc(peso, altura):
    """
    Calcula o índice de massa corporal (IMC)
    :param peso: Recebe o peso da pessoa.
    :param altura: Recebe a altura da pessoa.
    :return: Retorma um valor de acordo com a condição do resultado do cálculo.
    By: Renato Gomes
    """

    res = peso / (altura ** 2)
    if res < 18.5:
        return f'{res:.1f} = ABAIXO DO PESO\nAdote hábitos saudáveis e procure um profissional\nde saúde!'.replace('.',
                                                                                                                   ',')
    elif res <= 24.9:
        return f'{res:.1f} = PESO NORMAL\nMantenha hábitos saudáveis!'.replace('.', ',')
    elif res <= 29.9:
        return f'{res:.1f} = SOBREPESO\nAdote habitos saudáveis!'.replace('.', ',')
    elif res <= 34.9:
        return f'{res:.1f} = OBESIDA GRAU 1\nAdote hábitos saudáveis e procure um profissional\nde saúde!'.replace('.',
                                                                                                                   ',')
    elif res <= 39.9:
        return f'{res:.1f} = OBESIDADE GRAU 2\nAdote hábitos saudáveis e procure um profissional\nde saúde!'.replace(
            '.', ',')
    elif res >= 40:
        return f'{res:.1f} = OBESIDADE GRAU 3\nAdote hábitos saudáveis e procure um profissional\nde saúde!'.replace(
            '.', ',')


def glicemy(valor):
    """
    Calcula os níveis de glicemia em Jejum de uma pessoa.
    :param valor: Recebe o valor Glicemico da pessoa.
    :return: Retorna uma condição de acordo com o nível glicemico.
    By Renato Gomes.
    """
    if valor <= 70:
        return '>> HIPOGLICEMIA <<\n Adote hábitos de vida saudáveis\n e procure um profissional'
    elif valor < 100:
        return '>> NORMAL <<\n Mantenha hábitos de vida saudáveis'
    elif 100 <= valor <= 125:
        return '>> ALTERADA <<\n Adote hábitos de vida saudáveis\n e procure um profissional'
    elif valor >= 126:
        return '>> DIABETES <<\n Adote hábitos de vida saudáveis\n e procure um profissional'


def presart(max, min):
    """
    Calcula os valores da pressão arterial.
    :param max: Recebe o valor da pressão máxima.
    :param min: Recebe o valor da pressão mínima.
    :return: Retorna o resultado de acordo com a OMS.
    By: Renato Gomes
    """
    if max <= 12 and min <= 8:
        return '>> ÓTIMA <<\nMantenha hábitos de vida saudáveis!'
    elif max < 13 and min < 8.5:
        return '>> NORMAL <<\nMantenha hábitos de vida saudáveis!'
    elif 13 <= max < 14 or 8.5 <= min < 9:
        return '>> LIMÍTROFE OU ALTERADA <<\nAdote hábitos de vida saudáveis\ne procure um profissional de saúde'
    elif 14 <= max < 16 or 9 <= min < 10:
        return '>> HIPERTENSÃO ESTAGIO 1 (Leve) <<\nAdote hábitos de vida saudáveis\ne procure um profissional de saúde'
    elif 16 <= max < 18 or 10 <= min < 11:
        return '>> HIPERTENSÃO ESTAGIO 2 (Moderada) <<\nAdote hábitos de vida saudáveis\ne procure um profissional de ' \
               'saúde '
    elif max >= 18 or min >= 11:
        return '>> HIPERTENSÃO ESTAGIO 3 (Grave) <<\nAdote hábitos de vida saudáveis\ne procure um profissional de ' \
               'saúde '


def dieta(san):
    sangue = str(san).strip().upper()

    if sangue == 'O+O-':
        print(f'  São carnívoros com aparelho intestinal forte\n'
              'e necessitam comer proteínas animais diariamente,\n'
              'caso contrário, estão propensos a desenvolver doenças\n'
              'gástricas como úlceras e gastrites devido a alta\n'
              'produção de sucos gástricos.\n')
        print('ALIMENTOS POSITIVOS:\n'
              'CARNES: bovina, carneiro, vitela, cordeiro\n'
              'PEIXES: bacalhau, badejo, sardinha, linguado, salmão\n'
              'LATICÍNEOS: Queijo de leite de cabra, queijo de soja\n'
              'FRUTAS: ameixa, nozes, figo, semente de abóbora\n'
              'VERDURAS: abóbora, brócolis, espinafre, alface romana, acelga, salsa\n'
              'CEREAIS: Evitar\n'
              'OUTROS: azeite de oliva\n\n'
              'ALIMENTOS NEUTROS:\n'
              'CARNES: frango e peru\n'
              'PEIXES: atum, camarão, lagosta\n'
              'LATICÍNEOS: mussarela, manteiga, queijo minas\n'
              'FRUTAS: noz pecãn, castanhas, avelã, pinha\n'
              'VERDURAS: abobrinha, agrião, inhame\n'
              'CEREAIS: farelo de arroz, farinha de trigo integral\n'
              'OUTROS: óleo de canola\n\n'
              'ALIMENTOS NEGATIVOS:\n'
              'CARNES: carne de porco e derivados, como presunto e bacon\n'
              'PEIXES: caviar, salmão defumado, polvo\n'
              'LATICÍNEOS: creme de leite, iogurte, leite (integral ou magro),\n'
              'a maioria dos queijos, sorvete\n'
              'FRUTAS: laranja, morango, côco, amora, amendoim,\n'
              'castanha do pará, pistache, castanha de caju, abacate\n'
              'VERDURAS: berinjela, champignon, milho, repolho\n'
              'CEREAIS: aveia, trigo, cuscuz e pão branco\n'
              'OUTROS: óleo de milho, óleo de amendoim')

    elif sangue == 'A-A+':
        print('  São vegetarianos com aparelho intestinal sensível\n'
              'e têm dificuldades para digerir proteínas de origem\n'
              'animal, pois sua produção de suco gástrico é mais limitada.\n')
        print('ALIMENTOS POSITIVOS:\n'
              'CARNES: evitar carnes vermelhas\n'
              'PEIXES: bacalhau, salmão vermelho, salmão, sardinha, truta\n'
              'LATICÍNEOS: queijo de soja, tofu\n'
              'FRUTAS: abacaxi, ameixa, cereja, figo, limão, amora, damasco\n'
              'VERDURA: abóbora moranga, alface romana, acelga,\n'
              'brócolis, cenoura, acelga, alcachofra, cebola\n'
              'CEREAIS: farinhas de centeio, arroz, soja,\n'
              'aveia, pão de farinha de soja\n'
              'OUTROS: alho, molho de soja, missô, melaço de cana, \n'
              'gengibre, chá verde, café normal, vinho tinto\n\n'
              'ALIMENTOS NEUTROS:\n'
              'CARNES: frango e peru\n'
              'PEIXES: atum, pescada\n'
              'LATICÍNEOS: iogurte, mussarela, ricota, iogurte c/\n'
              'frutas, coalhada, queijo minas\n'
              'FRUTAS: melão, passas, pêra, maçã, morango, uva, pêssego, goiaba, kiwi\n'
              'VERDURAS: agrião, chicória, milho, beterraba\n'
              'CEREAIS: fubá de milho, flocos de milho, cevada\n'
              'OUTROS: açúcar branco, chocolate, alecrim, mostarda (seca),\n'
              'noz-moscada, manjericão, açúcar mascavo, manjericão, orégano,\n'
              'canela, hortelã, salsa, salvi\n\n'
              'ALIMENTOS NEGATIVOS:\n'
              'CARNES: bovina, carneiro, cordeiro, pato, porco\n'
              'e derivados, vitela\n'
              'PEIXES: mexilhões, lagostim, salmão defumado,\n'
              'caviar, ostra, lagosta, camarão, caranguejo.\n'
              'LATICÍNEOS: creme de leite, sorvete, leite magro e\n'
              'integral, manteiga, requeijão\n'
              'FRUTAS: caqui, carambola, côco\n'
              'VERDURAS: repolho, tomate, inhame, batata, berinjela, batata doce\n'
              'CEREAIS: Creme e germe de trigo, farinha de trigo integral,\n'
              'pão preto, pão integral, farinha branca, granola\n'
              'OUTROS: alcaparras, gelatina pura, pimenta em grão, vinagre,\n'
              'cerveja, licor, chá preto, refrigerante.\n')

    elif sangue == 'B-B+':
        print('  Podem tolerar dieta mais variadas é o único tipo\n'
              ' de sangue que tolera bem laticínios em geral.\n')
        print('ALIMENTOS POSITIVOS:\n'
              'CARNES: carneiro, cordeiro, coelho, veado.\n'
              'PEIXES: bacalhau, salmão, linguado, badejo, caviar, sardinha.\n'
              'LATICÍNEOS: iogurte, mussarela, coalhada, leite, queijo, ovos, ricota.\n'
              'FRUTAS: abacaxi, bananas, mamão, uvas, ameixa fresca.\n'
              'VERDURAS: batata doce, cenoura, berinjela, inhame,\n'
              'beterraba, brócolis, couve, repolho.\n'
              'CEREAIS: arroz integral, aveia integral.\n'
              'OUTROS: gengibre, salsa, açafrão, hortelã,\n'
              'pimenta, ginseng, gengibre, sálvia.\n\n'
              'ALIMENTOS NEUTROS:\n'
              'CARNES: carne bovina, peru, vitela.\n'
              'PEIXES: arenque, truta, atum, lula.\n'
              'LATICÍNEO: leite soja, queijo parmesão,\n'
              'queijo soja, manteiga, requeijão, leite integral.\n'
              'FRUTAS: morango, laranja, kiwi, passas, pêra.\n'
              'VERDURAS: abóbora, agrião, alface, acelga, aipo, cogumelos, espinafre.\n'
              'CEREAIS: granola.\n'
              'OUTROS: café, vinho branco, cerveja, chá preto,\n'
              'chá de amora, hortelã, camomila.\n\n'
              'ALIMENTOS NEGATIVOS:\n'
              'CARNES: frango, pato, porco, presunto.\n'
              'PEIXES: lagosta, camarão, anchova, caranguejo, polvo,\n'
              'ostra, polvo, mexilhão.\n'
              'LATICÍNEOS: queijo fundido e roquefort, sorvete com leite.\n'
              'FRUTAS: caqui, carambola, coco.\n'
              'VERDURAS: alcachofra, azeitonas, tomate, broto de feijão, milho verde.\n'
              'CEREAIS: farinha de trigo, milho, centeio.\n'
              'OUTROS: canela, maisena, pimenta branca e do reino,\n'
              'gelatina pura, refrigerantes, bebidas destiladas.\n')

    elif sangue == 'AB':
        print('  Necessitam de uma dieta equilibrada contendo um pouco de tudo.\n')
        print('ALIMENTOS POSITIVOS:\n'
              'CARNES: carneiro, coelho, cordeiro e peru.\n'
              'PEIXES: atum, bacalhau, cavala, sardinha, garoupa, truta.\n'
              'LATICÍNEOS: coalhada, iogurte, mussarela, ricota, queijo cottage.\n'
              'FRUTAS: abacaxi, ameixa, cereja, figo, limão, kiwi, uva, framboesa.\n'
              'VERDURAS: aipo, alho, beterraba, berinjela, brócolis, couve-flor, pepino.\n'
              'CEREAIS: arroz, farinha de centeio, de trigo, aveia.\n'
              'OUTROS: curry, alho, missô, gengibre, camomila.\n\n'
              'ALIMENTOS NEUTROS:\n'
              'CARNES: faisão, fígado.\n'
              'PEIXES: arenque, linguado, carpa.\n'
              'LATICÍNEOS: leite e queijo de soja, leite desnatado, requeijão.\n'
              'FRUTAS: ameixa seca, pêra, passas, mamão, maçã, pêssego.\n'
              'VERDURAS: broto de bambu, cebolinha, escarola, agrião, vagem.\n'
              'CEREAIS: cevada, germe de trigo, granola.\n'
              'OUTROS: açafrão, mel, açúcar, melaço, chocolate, vinho.\n\n'
              'ALIMENTOS NEGATIVOS:\n'
              'CARNES: bovina, frango, porco, presunto e vitela,\n'
              'PEIXES: anchova, camarão, caranguejo, lagosta, linguado,\n'
              'ostra, mexilhão, siri.\n'
              'LATICÍNEOS: leite integral, creme de leite, queijo parmesão, brie,\n'
              'provolone, roquefort, manteiga.\n'
              'FRUTAS: banana, caqui, goiaba, laranja, manga.\n'
              'VERDURAS: alcachofra, milho verde, nabo, pimentão, rabanete.\n'
              'CEREAIS: farinha de cevada, de milho, trigo sarraceno,\n'
              'cereais matinais, amido de milho.\n'
              'OUTROS: alcaparras, tapioca, vinagre, mel de milho, anis,\n'
              'maisena, malte de cevada, pimenta do reino e vermelha.\n')





