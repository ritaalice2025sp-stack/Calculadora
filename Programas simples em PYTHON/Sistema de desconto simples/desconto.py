# Entrada do valor
valor_inicial = float(input('Qual o valor do produto? '))

# Lógica do desconto
desconto = valor_inicial * 0.05
valor_com_desconto = valor_inicial - desconto

# Resultado
print('O valor incial do produto era de {:.2f} e após recerber 5% de desconto ficou {:.2f}.'.format(valor_inicial, valor_com_desconto))
# Sempre coloco um limite de casas depos da vírgula nos valores que vão aparecer afim de ficar mais limpo.
