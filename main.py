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

delta = (valor_b**2) - (4 * valor_a * valor_c) # declarando delta

