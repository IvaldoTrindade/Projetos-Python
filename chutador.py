import random

jogar = True
while True:
    while jogar:
        numero = random.randrange(1, 100)
        print(numero)
        while True:
            chute = int(input('Chute um número entre 1 e 100: '))
            if chute > numero:
                print("Chute um número mais baixo!")
            elif chute < numero:
                print('Chute um número mais alto!')
            else:
                print(f'Parabéns! O número aleatório é o {numero}')
                parar = input('Deseja continuar jogando? (s) ou (n): ')
                if parar not in ('s'):
                    jogar = False
                    print('-----------------------------\nEncerrando o jogo...\n-----------------------------')
                break 
