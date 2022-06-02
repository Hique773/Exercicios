a = [5, 10, 15, 20, 25, 30, 35, 40, 35, 30, 25, 20, 15 , 10, 5]

#print(a[:-1])

if a[0:7:1] == a[14:7:-1]:
    print(f'o conjunto {a} é simétrico.')

teste = input('digite uma palavra\n')
teste = str(teste)


if teste[0::] == teste[::-1]:
    print(f'A palavra {teste} é um palíndromo.')
else:
    print(f'A palavra {teste} não é um palíndromo.')