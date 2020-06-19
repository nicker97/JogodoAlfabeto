from pygame import mixer, image
from constante import tela

def mostrartela(nomedatela, caminhoimagem, posx, posy):
    nomedatela.blit(caminhoimagem, (posx, posy))

def carregarimagem(caminhoimagem):
    imagem = image.load(caminhoimagem)
    return imagem

def carregaraudio(caminhoaudio):
    mixer.init()
    audio = mixer.Sound(caminhoaudio)
    return audio

def clicoubotao(x, y, posxmaior, posxmenor, posymaior, posymenor):
    if posxmaior > x > posxmenor and posymaior > y > posymenor:
        clicoubotao = True
        return clicoubotao

def clicouletra(condicao, letra, posx, posy):
    if condicao == True:
        carregaraudio(f'jogo/audios/letras/{letra}.ogg').play()
        mostrartela(tela, carregarimagem(f'jogo/imagens/letraspressionadas/{letra}press.png'), posx, posy)
        condicao = False
        return condicao
    else:
        mostrartela(tela, carregarimagem(f'jogo/imagens/letras/{letra}.png'), posx-6, posy)

def verificaclique(x, y, posXmaior, posXmenor, posYmaior, posYmenor):
    if clicoubotao(x, y, posXmaior, posXmenor, posYmaior, posYmenor):
        condicao = True
        return condicao

def sortearfruta():
    from random import randint
    frutas = ['cereja', 'pessego', 'pera', 'abacate', 'abacaxi', 'melancia', 'morango', 'laranja', 'goiaba', 'banana', 'kiwi', 'uva']
    indice = randint(0, len(frutas) - 1)
    fruta = frutas[indice]
    return fruta
