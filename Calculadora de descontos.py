produto = int(input ('Digite o valor do produto: '))
desconto = int(input ('Digite o percentual de desconto: '))
desconto = desconto / 100
valor_desconto = produto * desconto
produto = produto - valor_desconto
print (f'o valor do desconto é de: {valor_desconto}')
print (f'o valor do produto com desconto é de: {produto}')

