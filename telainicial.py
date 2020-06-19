import pygame, enderecos, funcao, constante, os
os.environ['SDL_VIDEO_CENTERED'] = '1'

def telainicial():
    pygame.init()
    pygame.display.set_caption(' Tela Inicial ')
    clock = pygame.time.Clock()
    tela = pygame.display.set_mode((constante.largura, constante.altura))
    pygame.mixer.init()
    enderecos.musicafundoinicial.play(loops=-1)
    enderecos.musicafundoinicial.set_volume(0.3)
    alturalogo = -200
    clicoumusica = clicouplay = clicouexit = 1


    while True:
        clock.tick(30)
        alturalogo += 10
        funcao.mostrartela(tela, enderecos.imagemfundoinicial, 0, 0)
        funcao.mostrartela(tela, enderecos.logogame, 197, alturalogo)
        pygame.display.update()
        if alturalogo == 70:
            break

    alturabotoes = 600
    while True:
        clock.tick(30)
        alturabotoes -= 10
        funcao.mostrartela(tela, enderecos.imagemfundoinicial, 0, 0)
        funcao.mostrartela(tela, enderecos.logogame, 197, alturalogo)
        funcao.mostrartela(tela, enderecos.botaoplay, 262, alturabotoes)
        funcao.mostrartela(tela, enderecos.botaoexitinicial, 523, alturabotoes)
        pygame.display.update()
        if alturabotoes == 390:
            break

    while True:
        clock.tick(30)
        funcao.mostrartela(tela, enderecos.imagemfundoinicial, 0, 0)
        funcao.mostrartela(tela, enderecos.logogame, 197, 70)


        if clicoumusica % 2 != 0:
            botaomusica = funcao.carregarimagem('imagens/botoes/musicapause.png')
            pygame.mixer.unpause()
        else:
            botaomusica = funcao.carregarimagem('imagens/botoes/musicaplay.png')
            pygame.mixer.pause()
        funcao.mostrartela(tela, botaomusica, 860, 492)

        if clicouexit % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaoexitinicial, 523, 390)
        else:
            funcao.mostrartela(tela, enderecos.botaoexitpressionadoinicial, 526, 393)
            pygame.display.update()
            quit()

        if clicouplay % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaoplay, 262, 390)
        else:
            enderecos.somplay.play()
            funcao.mostrartela(tela, enderecos.botaoplaypressionado, 265, 393)
            pygame.display.update()
            import jogo.alfabeto as jogo
            jogo.alfabeto()
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if funcao.clicoubotao(x, y, 901, 864, 537, 498):
                        clicoumusica += 1
                    if funcao.clicoubotao(x, y, 415, 270, 467, 402):
                        clicouplay = 2
                        pygame.mixer.stop()
                    if funcao.clicoubotao(x, y, 679, 530, 460, 405):
                        enderecos.somplay.play()
                        clicouexit = 2
telainicial()
