num = int(input('Digite um número'))

listRange = list(range(10, 20))
divisores = []

print(listRange)

for number in listRange:
    if num % number == 0:
        divisores.append(number)

print(divisores)