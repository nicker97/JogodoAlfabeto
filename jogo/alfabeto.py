import pygame, constante, funcao, enderecos, roleta


def alfabeto():
    pygame.display.set_caption(' Jogo do Alfabeto ')
    pygame.font.init()
    clock = pygame.time.Clock()
    tela = pygame.display.set_mode((constante.largura, constante.altura))
    clicoumusica = clicoumenu = clicouexit = clicoucredito = 1
    fruta = roleta.roleta()
    enderecos.musicafundojogo.play(loops=-1)
    enderecos.musicafundojogo.set_volume(0.3)
    musica = True
    numero = 10
    tempo = 0
    texto = ''
    letraclicada = ''
    font = pygame.font.get_default_font()
    fonte = pygame.font.SysFont(font, 60)
    velocidade = constante.velocidade
    letras = []

    for x in range(0, len(fruta)):
        letras.append('_')

    while True:
        numerotracos = 0

        clock.tick(30)
        funcao.mostrartela(tela, enderecos.imagemfundojogo, 0, 0)
        text = fonte.render(texto, 1, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = (500, 500)
        tela.blit(text, textRect)
        texto =''
        funcao.mostrartela(tela, funcao.carregarimagem(f'numeros/{numero}.png'), 259, 532)
        funcao.mostrartela(tela, funcao.carregarimagem(f'frutas/{fruta}.png'), 650, 400)
        tempo += velocidade




        #BOTOES DO MENU.................................................................................................
        if clicoumusica % 2 != 0:
            botaomusica = funcao.carregarimagem('imagens/botoes/musicapause.png')
            pygame.mixer.unpause()
        else:
            botaomusica = funcao.carregarimagem('imagens/botoes/musicaplay.png')
            if musica == False:
                pygame.mixer.pause()
                musica = True
        funcao.mostrartela(tela, botaomusica, 860, 492)

        if clicouexit % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaoexit, 750, 145)
        else:
            funcao.mostrartela(tela, enderecos.botaoexitpressionado, 755, 148)
            pygame.display.update()
            quit()

        if clicoumenu % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaomenu, 750, 60)
        else:
            enderecos.sommenu.play()
            funcao.mostrartela(tela, enderecos.botaomenupressionado, 755, 63)
            pygame.display.update()
            import telainicial
            telainicial.telainicial()

        if clicoucredito % 2 != 0:
            funcao.mostrartela(tela, enderecos.botaocredito, 750, 228)
        else:
            enderecos.somcredito.play()
            funcao.mostrartela(tela, enderecos.botaocreditopressionado, 755, 231)
            pygame.display.update()
            import creditos.creditos as credito
            credito.creditos()

        #LETRAS.........................................................................................................
        #PRIMEIRA FILEIRA DE LETRAS------------------------------
        constante.condA = funcao.clicouletra(constante.condA, 'A', 71, 55)
        constante.condB = funcao.clicouletra(constante.condB, 'B', 171, 55)
        constante.condC = funcao.clicouletra(constante.condC, 'C', 271, 55)
        constante.condD = funcao.clicouletra(constante.condD, 'D', 371, 55)
        constante.condE = funcao.clicouletra(constante.condE, 'E', 471, 55)
        constante.condF = funcao.clicouletra(constante.condF, 'F', 571, 55)
        #SEGUNDA FILEIRA DE LETRAS------------------------------
        constante.condG = funcao.clicouletra(constante.condG, 'G', 71, 147)
        constante.condH = funcao.clicouletra(constante.condH, 'H', 171, 147)
        constante.condI = funcao.clicouletra(constante.condI, 'I', 271, 147)
        constante.condJ = funcao.clicouletra(constante.condJ, 'J', 371, 147)
        constante.condK = funcao.clicouletra(constante.condK, 'K', 471, 147)
        constante.condL = funcao.clicouletra(constante.condL, 'L', 571, 147)
        #TERCEIRA FILEIRA DE LETRAS------------------------------
        constante.condM = funcao.clicouletra(constante.condM, 'M', 71, 239)
        constante.condN = funcao.clicouletra(constante.condN, 'N', 171, 239)
        constante.condO = funcao.clicouletra(constante.condO, 'O', 271, 239)
        constante.condP = funcao.clicouletra(constante.condP, 'P', 371, 239)
        constante.condQ = funcao.clicouletra(constante.condQ, 'Q', 471, 239)
        constante.condR = funcao.clicouletra(constante.condR, 'R', 571, 239)
        #QUARTA FILEIRA DE LETRAS------------------------------
        constante.condS = funcao.clicouletra(constante.condS, 'S', 71, 331)
        constante.condT = funcao.clicouletra(constante.condT, 'T', 171, 331)
        constante.condU = funcao.clicouletra(constante.condU, 'U', 271, 331)
        constante.condV = funcao.clicouletra(constante.condV, 'V', 371, 331)
        constante.condW = funcao.clicouletra(constante.condW, 'W', 471, 331)
        constante.condX = funcao.clicouletra(constante.condX, 'X', 571, 331)
        #QUINTA FILEIRA DE LETRAS------------------------------
        constante.condY = funcao.clicouletra(constante.condY, 'Y', 71, 423)
        constante.condZ = funcao.clicouletra(constante.condZ, 'Z', 171, 423)

        for let in letras:
            if let == '_':
                numerotracos += 1

        if tempo >= 3:
            numero -= 1
            tempo = 0
            if numero < 1:
                pygame.mixer.stop()
                from derrota import perdeu
                constante.numerovitoria = 0
                constante.velocidade = 0.1
                perdeu()

        for i, letra in enumerate(fruta):
            if fruta[i] == letraclicada:
                letras[i] = letraclicada

        for letra in letras:
            texto += letra + ' '

        if numerotracos == 0:
            constante.numerovitoria += 1
            constante.velocidade += 0.1
            if constante.numerovitoria == 3:
                constante.numerovitoria = 0
                constante.velocidade = 0.1
                from vitoria import ganhou
                from time import sleep
                text = fonte.render(texto, 1, (0, 255, 0))
                tela.blit(text, textRect)
                pygame.display.update()
                enderecos.sommenu.play()
                sleep(0.5)
                pygame.mixer.stop()
                ganhou()
            else:
                from time import sleep
                text = fonte.render(texto, 1, (0, 255, 0))
                tela.blit(text, textRect)
                pygame.display.update()
                enderecos.sommenu.play()
                sleep(0.5)
                pygame.mixer.stop()
                alfabeto()

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
                        musica = False
                    if funcao.clicoubotao(x, y, 897, 767, 295, 242):
                        clicoucredito = 2
                        pygame.mixer.stop()
                    if funcao.clicoubotao(x, y, 897, 767, 215, 158):
                        enderecos.sommenu.play()
                        clicouexit = 2
                    if funcao.clicoubotao(x, y, 897, 767, 127, 72):
                        clicoumenu = 2
                        pygame.mixer.stop()

                    constante.condA = funcao.verificaclique(x, y, constante.largurasX[0], constante.alturasX[0], constante.alturas[1], constante.alturas[0]+5)
                    if constante.condA == True:
                        letraclicada = 'A'
                    constante.condB = funcao.verificaclique(x, y, constante.largurasX[1], constante.alturasX[1], constante.alturas[1], constante.alturas[0]+5)
                    if constante.condB == True:
                        letraclicada = 'B'
                    constante.condC = funcao.verificaclique(x, y, constante.largurasX[2], constante.alturasX[2], constante.alturas[1], constante.alturas[0]+5)
                    if constante.condC == True:
                        letraclicada = 'C'
                    constante.condD = funcao.verificaclique(x, y, constante.largurasX[3], constante.alturasX[3], constante.alturas[1], constante.alturas[0]+5)
                    if constante.condD == True:
                        letraclicada = 'D'
                    constante.condE = funcao.verificaclique(x, y, constante.largurasX[4], constante.alturasX[4], constante.alturas[1], constante.alturas[0]+5)
                    if constante.condE == True:
                        letraclicada = 'E'
                    constante.condF = funcao.verificaclique(x, y, constante.largurasX[5], constante.alturasX[5], constante.alturas[1], constante.alturas[0]+5)
                    if constante.condF == True:
                        letraclicada = 'F'
                    constante.condG = funcao.verificaclique(x, y, constante.largurasX[0], constante.alturasX[0], constante.alturas[2], constante.alturas[1]+5)
                    if constante.condG == True:
                        letraclicada = 'G'
                    constante.condH = funcao.verificaclique(x, y, constante.largurasX[1], constante.alturasX[1], constante.alturas[2], constante.alturas[1]+5)
                    if constante.condH == True:
                        letraclicada = 'H'
                    constante.condI = funcao.verificaclique(x, y, constante.largurasX[2], constante.alturasX[2], constante.alturas[2], constante.alturas[1]+5)
                    if constante.condI == True:
                        letraclicada = 'I'
                    constante.condJ = funcao.verificaclique(x, y, constante.largurasX[3], constante.alturasX[3], constante.alturas[2], constante.alturas[1]+5)
                    if constante.condJ == True:
                        letraclicada = 'J'
                    constante.condK = funcao.verificaclique(x, y, constante.largurasX[4], constante.alturasX[4], constante.alturas[2], constante.alturas[1]+5)
                    if constante.condK == True:
                        letraclicada = 'K'
                    constante.condL = funcao.verificaclique(x, y, constante.largurasX[5], constante.alturasX[5], constante.alturas[2], constante.alturas[1]+5)
                    if constante.condL == True:
                        letraclicada = 'L'
                    constante.condM = funcao.verificaclique(x, y, constante.largurasX[0], constante.alturasX[0], constante.alturas[3], constante.alturas[2]+5)
                    if constante.condM == True:
                        letraclicada = 'M'
                    constante.condN = funcao.verificaclique(x, y, constante.largurasX[1], constante.alturasX[1], constante.alturas[3], constante.alturas[2]+5)
                    if constante.condN == True:
                        letraclicada = 'N'
                    constante.condO = funcao.verificaclique(x, y, constante.largurasX[2], constante.alturasX[2], constante.alturas[3], constante.alturas[2]+5)
                    if constante.condO == True:
                        letraclicada = 'O'
                    constante.condP = funcao.verificaclique(x, y, constante.largurasX[3], constante.alturasX[3], constante.alturas[3], constante.alturas[2]+5)
                    if constante.condP == True:
                        letraclicada = 'P'
                    constante.condQ = funcao.verificaclique(x, y, constante.largurasX[4], constante.alturasX[4], constante.alturas[3], constante.alturas[2]+5)
                    if constante.condQ == True:
                        letraclicada = 'Q'
                    constante.condR = funcao.verificaclique(x, y, constante.largurasX[5], constante.alturasX[5], constante.alturas[3], constante.alturas[2]+5)
                    if constante.condR == True:
                        letraclicada = 'R'
                    constante.condS = funcao.verificaclique(x, y, constante.largurasX[0], constante.alturasX[0], constante.alturas[4], constante.alturas[3]+5)
                    if constante.condS == True:
                        letraclicada = 'S'
                    constante.condT = funcao.verificaclique(x, y, constante.largurasX[1], constante.alturasX[1], constante.alturas[4], constante.alturas[3]+5)
                    if constante.condT == True:
                        letraclicada = 'T'
                    constante.condU = funcao.verificaclique(x, y, constante.largurasX[2], constante.alturasX[2], constante.alturas[4], constante.alturas[3]+5)
                    if constante.condU == True:
                        letraclicada = 'U'
                    constante.condV = funcao.verificaclique(x, y, constante.largurasX[3], constante.alturasX[3], constante.alturas[4], constante.alturas[3]+5)
                    if constante.condV == True:
                        letraclicada = 'V'
                    constante.condW = funcao.verificaclique(x, y, constante.largurasX[4], constante.alturasX[4], constante.alturas[4], constante.alturas[3]+5)
                    if constante.condW == True:
                        letraclicada = 'W'
                    constante.condX = funcao.verificaclique(x, y, constante.largurasX[5], constante.alturasX[5], constante.alturas[4], constante.alturas[3]+5)
                    if constante.condX == True:
                        letraclicada = 'X'
                    constante.condY = funcao.verificaclique(x, y, constante.largurasX[0], constante.alturasX[0], constante.alturas[5], constante.alturas[4]+5)
                    if constante.condY == True:
                        letraclicada = 'Y'
                    constante.condZ = funcao.verificaclique(x, y, constante.largurasX[1], constante.alturasX[1], constante.alturas[5], constante.alturas[4]+5)
                    if constante.condZ == True:
                        letraclicada = 'Z'

        pygame.display.update()
