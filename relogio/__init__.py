def tempo(tela, tempo, numero):
    print(tempo, numero)
    from funcao import carregarimagem, mostrartela
    mostrartela(tela, carregarimagem(f'numeros/{numero}.png'), 870, 455)
    if tempo >= 3:
        print('tempo')
        numero -= 1
        #tempo = 0
    return numero
