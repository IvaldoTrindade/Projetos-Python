def obter_entrada(mensagem, opcoes_validas):
    entrada = input(mensagem).lower()
    while entrada not in opcoes_validas:
        print('Caminho inválido. Você deve escolher um dos caminhos!')
        entrada = input(mensagem).lower()
    return entrada

def finaliza_jogo(mensagem):
    print(mensagem)
    retorno = obter_entrada("Você deseja jogar novamente? Digite 'sim' ou 'nao': ", ['sim','nao'])
    return retorno == 'nao'    

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

print('Bem vindo à ilha do tesouro!')
print('A sua missão é encontrar o tesouro escondido.')

tesouro = False
while tesouro == False:
    start = obter_entrada("Você está em uma ilha, e tem duas opções de caminho. Qual caminho deseja seguir? Digite 'direita' ou 'esquerda:\n",['direita','esquerda'])
    if start == 'esquerda':
        escolha = obter_entrada("Você chegou ao meio da ilha, e agora existem três opções de caminho. Digite 'esquerda', 'direita' ou 'meio':\n",['esqueda','direita','meio'])
        if escolha == 'esquerda':
            tesouro = finaliza_jogo("Você encontrou com uma onça-pintada. Fim de jogo!")
        elif escolha == 'direita':
            tesouro = finaliza_jogo("Oh não, você foi picado por um escorpião enquanto caminhava. Fim de jogo!")
        elif escolha == 'meio':
            tesouro = finaliza_jogo("Parabéns, você encontrou o tesouro escondido!")
    elif start == 'direita':
        escolha1 = obter_entrada("Você chegou próximo ao lado oeste da ilha, e se deparou com três opções de caminho. Digite 'esquerda', 'direita' ou 'meio':\n",['esqueda','direita','meio'])
        if escolha1 == 'meio':
            tesouro = finaliza_jogo("Você se deparou com uma caverna, e resolveu explorar, mas foi surpreendido por um urso. Fim de jogo!")
        elif escolha1 == 'direita':
            tesouro = finaliza_jogo("Você encontrou uma ponte de madeira, e resolveu atravessá-la, mas pisou em uma madeira podre e acabou caindo. Fim de jogo!")
        elif escolha1 == 'esquerda':
            tentativa = obter_entrada("Você encontrou uma nova estrada com dois caminhos, uma delas pode ser a do tesouro. Digite 'direita' ou 'esquerda:\n",['esquerda','direita'])
            if tentativa == 'direita':
                tesouro = finaliza_jogo('Você foi surpreendido por uma matilha de lobos selvagens. Fim de jogo!')
            elif tentativa == 'esquerda':
                tesouro = finaliza_jogo("Parabéns, você encontrou o tesouro escondido!")
    if tesouro == True:
        print('Muito obrigado por jogar o jogo: ilha do tesouro. Volte sempre que quiser se divertir!')
            
 