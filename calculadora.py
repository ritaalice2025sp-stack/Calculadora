escolha = (input('Escolha uma das operações matemáticas para calcular: '
      '\n1- Somar\n'
      '2- Multiplicar\n'
      '3- Subtrair\n'
      '4- Dividir\n'
      '5- Potência\n'
      'Opção: '))

if escolha == '1':
    n1 = float(input('Digite o primeiro número que deseja somar: '))
    n2 = float(input('Digite o segundo número que deseja somar: '))
    soma = n1 + n2
    print(f'O resultado da sua soma é {soma}')

elif escolha == '2':
    n1 = float(input('Digite o primeiro número que deseja subtrair: '))
    n2 = float(input('Digite o segundo número que deseja subtrair: '))
    sub = n1 - n2
    print(f'O resultado da sua subtração é {sub}')

elif escolha == '3':
    n1 = float(input('Digite o primeiro número que deseja multiplicar: '))
    n2 = float(input('Digite o segundo número que deseja multiplicar: '))
    multiplicar = n1 * n2
    print(f'O resultado da sua multiplicação é {multiplicar}')

elif escolha == '4':
    n1 = float(input('Digite o número que deseja dividir: '))
    n2 = float(input('Digite o divisor: '))
    dividir = n1 / n2
    print(f'O resultado da sua divisão é {dividir}')

elif escolha == '5':
    n1 = float(input('Digite o primeiro número que deseja a potenciação: '))
    n2 = float(input('Digite o segundo número que deseja a potenciação: '))
    potencia = n1 ** n2
    print(f'O resultado da sua potência é {potencia}')

else:
    print('Inválido')


