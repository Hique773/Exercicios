from asyncore import read


def soma(x, y):
    """
    Retorna a soma de dois números
    :x: primeiro operando
    :y: segundo opernado
    :return: soma dos operandos
    """
    return x+y

def divisão(x, y):
    """
    Retorna a divisão de dois números
    :x: primeiro operando
    :y: segundo opernado
    :return: quociente dos operandos
    """
    return x/y

numero1 = int(input("Escreva o primeiro número\n"))
numero2 = int(input("Escreva o segundo número\n"))
soma1 = soma(numero1,numero2)

print(f'A soma de {numero1} e {numero2} é: {soma1}')

numero3 = int(input("Escreva o terceiro número\n"))
numero4 = int(input("Escreva o quarto número\n"))
divisao1 = divisão(numero3,numero4)

print(f'A divisão de {numero3} por {numero4} é: {soma1}')

op1 = (soma1**3) * (2*divisao1) 

print(f'A multiplicação do cubo da soma de {numero1} e {numero2} pelo dobro da divisão de {numero3} por {numero4} é igual a: {op1}')