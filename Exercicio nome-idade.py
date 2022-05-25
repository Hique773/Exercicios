from mailbox import NotEmptyError
idade = input('digite sua idade\n')
nome = input('digite seu nome\n')

print(f'Bem vindo {nome}, fico feliz em saber que tem {idade} anos.')

#no comando **f'Bem vindo {nome}, fico feliz em saber que tem {idade} anos.'**, o "f" tem a função de formatar a string para aceitar a inserção de variáveis 
#poderia ser escrito **'Bem vindo', nome, 'fico feliz em saber que tem', idade, 'anos.'**