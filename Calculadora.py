print ("CALCULADORA")

sair = False
while sair == False:

    while True:
        try:
            num1 = int(input("Insira o primeiro número: "))
            break
        except:
            print("Número inválido!")
        
    while True:
        operador = input("Insira o operador (+-*/): ")
        if operador in "+-*/":
            break
        else:
            print("Operador inválido!")

    while True:
        try:
            num2 = int(input("Insira o segundo número: "))
            break
        except:
            print("Número inválido")
        
    resultado = eval(str(num1) + operador + str(num2)) # eval("4+5")
    print("Resultado: " + str(resultado))

    teste = input("Deseja sair (s/n)?").lower()
    if teste == "s":
        sair = True
