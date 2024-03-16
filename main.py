############################################################
######   PROGRAMA RESOLVEDOR DE EQUAÇÃO DO 2º GRAU    ######
######                   DIÊGO AXEL                   ######
######                    CAICÓ-RM                    ######
############################################################


from math import sqrt # Importando a biblioteca math, em específico o SQRT para a dar a raiz quadrada

print("-----------------------------------------------")
print("|  PROGRAMA RESOLVEDOR DE EQUAÇÃO DO 2º GRAU  |" )
print("-----------------------------------------------")
print("") # espaços

# PEDINDO OS VALORES QUE SERÃO ATRIBUIDOS DE: A, B E C ->
valor_a = float(input("Digite o valor de A: "))  
valor_b = float(input("Digite o valor de B: "))
valor_c = float(input("Digite o valor de C: "))
print("")

# EQUAÇÃO APÓS DADO OS VALORES DE A, B E C:
print("Sua equação é %.2fx² %.2fx  %.2f = 0"%(valor_a,valor_b,valor_c)) 
print("")

# CAUCULANDO O VALOR DE DELTA(A)
print("A fórmula de BASKARA é: A(DELTA) = B² - 4ac")
print("-----------------------------------------------")
print("Passando suas informações para a fórmula, temos:")
print("A(DELTA) = %.2f² - 4 x %.2f x %.2f"%(valor_b,valor_a,valor_c))
print("")

delta = (valor_b**2) - (4 * valor_a * valor_c) # DECLARANDO DELTA

print("O valor de Delta é: %.2f"%delta)
print("")

# CONDICONIAS: 
if delta > 0:
    print("Delta é maior que 0, então o valor de X1 e X2 serão diferente: ") 
    print("")

    # CAUCULANDO O VALOR DE X1 E X2 
    print("Agora iremos achar o valor de X1 e X2. A formula para chegar no valor deles é: X = -b +- RA/2a. X1 sera atriuido o sinal +(positivo) e x2 o sinal -(negativo)")
    print("")

    # X1 ->
    x1 = float((-valor_b + (sqrt(delta)))/(2*valor_a))
    print("O valor de X1 é = %.2f"%x1)

    # X2 ->
    x2 = float((-valor_b - (sqrt(delta)))/(2*valor_a))
    print("O valor de X2 é = %.2f"%x2)
    print("")

elif delta == 0:
    print("Delta é igual a 0, então X1 e X2 serão iguais")
    print("")
   
    # CAUCULANDO O VALOR DE X1 E X2   
    print("Agora iremos achar o valor de X1 e X2. A formula para chegar no valor deles é: X = -b +- RA/2a. X1 sera atriuido o sinal +(positivo) e x2 o sinal -(negativo)")
    print("")

    # X1 ->
    x1 = float((-valor_b + (sqrt(delta)))/(2*valor_a))
    print(f"O valor de X1 é = {x1}")

    # X2 ->
    x2 = float((-valor_b - (sqrt(delta)))/(2*valor_a))
    print(f"O valor de X2 é = {x2}")
    print("")


else:
    print("Delta é < 0 (NEGATIVO)")
    print("NÃO EXISTE RAIZ PARA DELTA NEGATIVO!")
    print("")


print("FIM DO PROGRAMA") 

# END