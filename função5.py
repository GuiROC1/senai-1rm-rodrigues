def opcao ():
    num1 = int (input("Insira o numero: "))
    num2 = int (input("Insira o numero: "))

def menu (alternativa):
    if alternativa == 1:
        print ("opção 1 selecionada.")
        result1 = num1 + num2

    elif alternativa == 2:
        print ("opção 2 selecionada.")
        result1 = num1 - num2

    elif alternativa == 3:
        print ("opção 3 selecionada.")
        result1 = num1 * num2

    elif alternativa == 4:
        print ("opção 4 selecionada.")
        result1 = num1 / num2

    elif alternativa == 0:
        print ("opção 0 selecionada.")
        sys.exit()

    else:
        print ("opção invalida: ")

while True:
    if opcao == 0:
        break

