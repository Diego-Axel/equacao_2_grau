############################################################
######   PROGRAMA RESOLVEDOR DE EQUAÇÃO DO 2º GRAU    ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RN                    ######
############################################################


from math import sqrt # Importando a biblioteca math, em específico o SQRT para a dar a raiz quadrada
import interface

resp = True
while resp:
    interface.titulo()
    print()
    # PEDINDO OS VALORES QUE SERÃO ATRIBUIDOS DE: A, B E C ->
    verificador = True
    while verificador:
        try:
            valor_a = float(input("--- Digite o valor de A: "))  
            print()
            verificador = False
        except ValueError:
            print("Por favor, coloque um número! Tente novamente.")
    verificador = True
    while verificador:
        try:
            valor_b = float(input("--- Digite o valor de B: "))
            print()
            verificador = False
        except ValueError:
            print("Por favor, coloque um número! Tente novamente.")
    verificador = True
    while verificador:
        try:
            valor_c = float(input("--- Digite o valor de C: "))
            print()
            verificador = False
        except ValueError:
            print("Por favor, coloque um número! Tente novamente.")
    print()

    interface.titulo()
    print()
    print(f"A: {valor_a} | B: {valor_b} | C: {valor_c}")
    print()
    # EQUAÇÃO APÓS DADO OS VALORES DE A, B E C:
    print(f"Sua equação é {valor_a}x² {valor_b}x {valor_c} = 0") 
    print()

    # CAUCULANDO O VALOR DE DELTA(A)
    print("A fórmula de BASKARA é: A(DELTA) = B² - 4ac")
    print("-----------------------------------------------")
    print("Passando suas informações para a fórmula, temos:")
    print(f"A(DELTA) = {valor_b}² - 4 x {valor_a} x {valor_c}")
    print()

    delta = (valor_b**2) - (4 * valor_a * valor_c) # DECLARANDO DELTA

    print(f"O valor de Delta é: {delta}")
    print()

    # CONDICONIAS: 
    if delta > 0:
        print("Delta é maior que 0, então o valor de X1 e X2 serão diferente: ") 
        print()

        # CAUCULANDO O VALOR DE X1 E X2 
        print("Agora iremos achar o valor de X1 e X2. A formula para chegar no valor deles é: X = -b +- RA/2a. X1 sera atriuido o sinal +(positivo) e x2 o sinal -(negativo)")
        print()

        # X1 ->
        x1 = (-valor_b + (sqrt(delta)))/(2*valor_a)
        print(f"O valor de X1 é = {x1}")

        # X2 ->
        x2 = (-valor_b - (sqrt(delta)))/(2*valor_a)
        print(f"O valor de X2 é = {x2}")
        print()
    elif delta == 0:
        print("Delta é igual a 0, então X1 e X2 serão iguais")
        print()
    
        # CAUCULANDO O VALOR DE X1 E X2   
        print("Agora iremos achar o valor de X1 e X2. A formula para chegar no valor deles é: X = -b +- RA/2a. X1 sera atriuido o sinal +(positivo) e x2 o sinal -(negativo)")
        print()

        # X1 ->
        x1 = (-valor_b + (sqrt(delta)))/(2*valor_a)
        print(f"O valor de X1 é = {x1}")

        # X2 ->
        x2 = (-valor_b - (sqrt(delta)))/(2*valor_a)
        print(f"O valor de X2 é = {x2}")
        print()
    else:
        print("Delta é < 0 (NEGATIVO)")
        print("NÃO EXISTE RAIZ PARA DELTA NEGATIVO!")
        print()
    interface.confirmacao()
    resp = input("Digite sua resposta: ")
    resp = resp.upper()
    if (resp == "SIM") or (resp == "S"):
        print()
    else:
        resp = False
        print()    
print("FIM DO PROGRAMA, ATÉ BREVE.") 
