import pygame, constante, enderecos, funcao
from time import sleep


def creditos():
    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    tela = constante.tela
    pygame.display.set_caption('Créditos')
    clicoumusica = 1
    enderecos.creditosom.play()
    enderecos.creditosom.set_volume(0.4)

    while True:
        clock.tick(20)
        tela.fill((0, 0, 0))
        funcao.mostrartela(tela, enderecos.creditos, constante.larguratexto, constante.alturatexto)
        funcao.mostrartela(tela, enderecos.voltar, 0, 0)
        constante.alturatexto -= 5

        if clicoumusica % 2 != 0:
            botaomusica = funcao.carregarimagem('creditos/imagens/som.png')
            pygame.mixer.unpause()
        else:
            botaomusica = funcao.carregarimagem('creditos/imagens/semsom.png')
            pygame.mixer.pause()
        funcao.mostrartela(tela, botaomusica, 0, 55)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]

                    if funcao.clicoubotao(x, y, 55, 0, 55, 0):
                        funcao.mostrartela(tela, enderecos.voltarpress, 0, 0)
                        pygame.display.update()
                        sleep(0.3)
                        constante.alturatexto = 600
                        constante.larguratexto = 0
                        pygame.mixer.stop()
                        import jogo.alfabeto as jogo
                        jogo.alfabeto()

                    if funcao.clicoubotao(x, y, 55, 0, 111, 55):
                        clicoumusica += 1

        #tempo para ver os nomes---------------
        if constante.alturatexto == -150:
            sleep(3)
        elif constante.alturatexto == -700:
            sleep(3)

        if constante.alturatexto == -1200:
            constante.alturatexto = 600
            constante.larguratexto = 0
            pygame.mixer.stop()
            import jogo.alfabeto as alfabeto
            alfabeto.alfabeto()

        pygame.display.update()
creditos()

