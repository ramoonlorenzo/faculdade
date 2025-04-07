codigo = input('Digite o código do produto: ')
descricao = input('Digite a descrição: ')
peso = float(input('Digite o peso do produto: '))
quantidade = int(input('Digite a quantidade: '))
preco_unitario = float(input('Digite o preço unitário: '))


print(f"\nInformações  do produto:")
print(f"Código: {codigo}")
print(f"Descrição: {descricao}")
print(f"Peso: {peso:.2f} kg")
print(f"Quantidade: {quantidade}")
print(f"Preço unitário: R$ {preco_unitario:.2f}")

# A. O preço total (bruto) é obtido multiplicando o preço unitário com a quantidade.

total = preco_unitario * quantidade

# B. O valor do imposto será obtido por meio das seguintes faixas:

if total < 500:
    imposto_aplicado = float(0.05 * total)
    print(f'\nO preço total é R$ {total:.2f}, o imposto cobrado será de 5%')
    print(f'Valor do imposto sobre o preço: R$ {imposto_aplicado:.2f}')
elif total >= 500 and total < 1500:
    imposto_aplicado = float(0.075 * total)
    print(f'\nO preço total é R$ {total:.2f}, o imposto cobrado será de 7,5%')
    print(f'Valor do imposto sobre o preço: R$ {imposto_aplicado:.2f}')
else:
    imposto_aplicado = float(0.10 * total)
    print(f'\nO preço total é R$ {total:.2f}, o imposto cobrado será de 10%')
    print(f'Valor do imposto sobre o preço: R$ {imposto_aplicado:.2f}')

# C. Quando o peso total do produto (peso * quantidade) for maior que 10kg, acrescentar R$50 de custo de frete, caso contrário, o frete será gratuito

peso_total = peso * quantidade

if peso_total > 10:
    frete = 50
    print(f'Custo do frete: R$ {frete:.2f}')
else:
    frete = 0
    print('Frete é gratuito')

# D. O preço final será obtido somando o preço total (bruto) com o valor do imposto e o custo do frete.

preco_final = total + imposto_aplicado + frete

print(f'Preço final: R$ {preco_final:.2f}')
