#Código de calculadora colaborativa
#Eu vou escrever a função e adicionar a soma;
#vai ficar para vocês as outras operações
#é uma calculadora básica!

#Função de soma:
def soma (a, b):
    return a + b

#Função de subtração:
def subtração (a, b):
    return a - b

#Função de multiplicação:
def multiplicacao (a, b):
    return a * b
#Função de divisão:



num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
operador = input("Digite o operador [+, -, *, /]: ")
calc = 0


#Soma:
if operador == "+":
    calc = soma(num1, num2)

#Subtração:
elif operador == "-":
    calc = subtração(num1, num2)

#Multiplicação:
elif operador == "*":
    calc = multiplicacao(num1, num2)
#Divisão:

#Quando o usuário errar [else]:
else:
    print("Operador não identificado!")

print(f"{num1} {operador} {num2} = {calc}")