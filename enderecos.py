from funcao import carregaraudio, carregarimagem


#IMAGENS TELA INICIAL---------------------------------------------------------------------------------------------------
imagemfundoinicial = carregarimagem('imagens/fundo/fundoinicial.png')
logogame = carregarimagem('imagens/jogodoalfabeto.png')
botaoexitinicial = carregarimagem('imagens/botoes/exit.png')
botaoplay = carregarimagem('imagens/botoes/play.png')
botaoexitpressionadoinicial = carregarimagem('imagens/botoes/exitpressionado.png')
botaoplaypressionado = carregarimagem('imagens/botoes/playpressionado.png')

#AUDIOS TELA INICIAL----------------------------------------------------------------------------------------------------
musicafundoinicial = carregaraudio('audios/fundo/musicafundoinicial.ogg')
somplay = carregaraudio('audios/botoes/botao.ogg')

#IMAGENS DENTRO DO GAME-------------------------------------------------------------------------------------------------
imagemfundojogo = carregarimagem('jogo/imagens/fundo/fundojogo.png')
botaoexit = carregarimagem('jogo/imagens/botoes/exit.png')
botaoexitpressionado = carregarimagem('jogo/imagens/botoes/exitpressionado.png')
botaomenu = carregarimagem('jogo/imagens/botoes/menu.png')
botaomenupressionado = carregarimagem('jogo/imagens/botoes/menupressionado.png')
botaocredito = carregarimagem('jogo/imagens/botoes/credito.png')
botaocreditopressionado = carregarimagem('jogo/imagens/botoes/creditopressionado.png')

#AUDIOS DENTRO DO GAME--------------------------------------------------------------------------------------------------
musicafundojogo = carregaraudio('jogo/audios/fundo/musicafundojogo.ogg')
sommenu = carregaraudio('audios/botoes/botao.ogg')
somcredito = carregaraudio('audios/botoes/botao.ogg')

#IMAGENS CREDITOS-------------------------------------------------------------------------------------------------------
creditos = carregarimagem('creditos/imagens/creditos.png')
semsom = carregarimagem('creditos/imagens/semsom.png')
som = som2 = carregarimagem('creditos/imagens/som.png')
voltar = carregarimagem('creditos/imagens/voltar.png')
voltarpress = carregarimagem('creditos/imagens/voltarpress.png')

#AUDIOS CREDITOS--------------------------------------------------------------------------------------------------------
creditosom = carregaraudio('creditos/audios/fundo/creditos.ogg')