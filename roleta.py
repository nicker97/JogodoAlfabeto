import pygame, funcao
from time import sleep
def roleta():
    pygame.font.init()
    pygame.mixer.init()
    funcao.carregaraudio('roleta/audios/fundo.ogg').play()
    font = pygame.font.get_default_font()
    fonte = pygame.font.SysFont(font, 60)
    texto = 'ADIVINHE O NOME DA FRUTA:'
    tempo = 0
    while True:
        tempo += 0.1
        clock = pygame.time.Clock()
        clock.tick(30)
        text = fonte.render(texto, 1, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (472, 100)
        tela = pygame.display.set_mode((945, 600))
        fruta = funcao.sortearfruta()
        funcao.mostrartela(tela, funcao.carregarimagem(f'roleta/imagens/fundo.png'), 0, 0)
        tela.blit(text, textRect)
        funcao.mostrartela(tela, funcao.carregarimagem(f'roleta/imagens/{fruta}.png'), 265, 120)
        pygame.display.update()
        if tempo > 7:
            funcao.mostrartela(tela, funcao.carregarimagem(f'frutas/{fruta}.png'), 265, 120)
            sleep(0.5)
            return fruta.upper()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
