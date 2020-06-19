import pygame, funcao, enderecos
def perdeu():
    pygame.font.init()
    pygame.mixer.init()
    funcao.carregaraudio('derrota/audios/derrota.ogg').play()
    font = pygame.font.get_default_font()
    fonte = pygame.font.SysFont(font, 60)
    texto = 'VOCÊ PERDEU!'
    clicoumenu = clicouexit = 1
    while True:

        clock = pygame.time.Clock()
        clock.tick(30)
        text = fonte.render(texto, 1, (0, 0, 0))
        textRect = text.get_rect()
        textRect.center = (472, 450)
        tela = pygame.display.set_mode((945, 600))
        funcao.mostrartela(tela, funcao.carregarimagem(f'derrota/imagens/fundo.png'), 0, 0)
        tela.blit(text, textRect)
        if clicoumenu % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaomenu, 750, 60)
        else:
            enderecos.sommenu.play()
            funcao.mostrartela(tela, enderecos.botaomenupressionado, 755, 63)
            pygame.display.update()
            import telainicial
            telainicial.telainicial()

        if clicouexit % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaoexit, 750, 145)
        else:
            funcao.mostrartela(tela, enderecos.botaoexitpressionado, 755, 148)
            pygame.display.update()
            quit()

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    x = pygame.mouse.get_pos()[0]
                    y = pygame.mouse.get_pos()[1]
                    if funcao.clicoubotao(x, y, 897, 767, 127, 72):
                        clicoumenu = 2
                        pygame.mixer.stop()
                    if funcao.clicoubotao(x, y, 897, 767, 215, 158):
                        enderecos.sommenu.play()
                        clicouexit = 2