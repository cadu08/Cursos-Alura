print("*********************************")
print("Bem vindo no jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):

    print("Tentativa {} de {}".format(rodada, total_de_tentativas))

    chute = input("Digite o seu numero: ")
    chute = int(chute)

    print("Você digitou ", chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto

    if chute == numero_secreto:
        print("você acertou")
        total_de_tentativas = 4
    elif maior:
        print("você errou. O seu chute foi maior que o número secreto!")
    elif menor:
        print("Você errou. O seu chute foi menor que o número secreto!")

    rodada = rodada + 1

print("Fim do jogo")
