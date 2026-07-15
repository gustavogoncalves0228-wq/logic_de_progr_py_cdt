'''
COMO FRITAR UM OVO;

Primeiro passo:Ligar o fogo
Sengundo passo:Ter uma panela ou frigideira
Terceiro passo:Ter oleo ou manteiga 
Quarto passo: Colocar oleo ou manteiga na panela ou na frigideira
Quinto passo: Esperar o oleo ou a manteiga esquentar 
Sexto passo: Quebrar o Ovo na Panela, Ou quebrar o Ovo em um Copo ou Prato, para nao ter risco de cair casca de ovo.
setimo passo: Colocar na panela ou na frigideira 
oitavo passo : Esperar fritar na panela ate o ponto que voce preferir 
'''





def fritar_ovo(tipo_gema):
    print('🍳 Fritando ovo - Sistema Simles🍳')
    print('1. ligar o fogo')
    print('2. Ter uma frigideira')
    print('3. Ter oleo ou manteiga')
    print('4. oleo ou manteiga na frigideira')
    print('5. esperar o oleo ou manteiga esquentar')
    print('6. quebrar o ovo')
    print('7. colocar na panela ou na frigideira')
    print('8. esperar fritar')
    print('9. virar o lado')
    print('10. tirar da frigideira no ponto que voce preferir')

    if tipo_gema.lower() == 'mole':
        resultado = 'Ovo frito com gema mole'
    else:
        resultado = 'ovo frito com gema firme'
            
    return resultado 

meu_almoco = fritar_ovo('mole')
print(f'meu almoco esta: (ovo frito com gema mole)')