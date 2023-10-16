# projeto par ou impar

#apresentação
print('\033[0;49;34m\n\t\t\t -- Verificador de Número -- \n\n')

#entradas
n1 = int(input('Digite um Número\n'))

#processamento e saida
if n1 % 2 == 0:
    print(f'\n{n1} é par!')
else:
    print(f'\n{n1} é impar!')
