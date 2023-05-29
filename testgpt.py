def contagem_regressiva(contagem):
    for cont in range(contagem, 0, -1):
        print(cont)

contagem = int(input("Insira o número para contagem regressiva: "))
contagem_regressiva(contagem)