"""#"___________________________________________"
valor_a_pagar = float(input("Quanto você tem? (Digite o valor em reais:)"))

preco_gasolina = float(input("Qual o preço atual do litro da Gasolina?"))

preco_alcool = float(input("Qual o preço atual do litro do Álcool?"))

resultado_gasolina = (valor_a_pagar/preco_gasolina)

resultado_alcool = (valor_a_pagar/preco_alcool)

media = (preco_gasolina*0.7)

print( "A quantidade de Gasolina que esse valor pode comprar é {:.2f} L e de Alcool é {:.2f} L" .format(resultado_gasolina , resultado_alcool))

quest2 = input("Com essas informações da pra saber se é mais rentavel abastecer com alcool ou gasolina com base no consumo dos dois combustiveis, sabia disso? sim ou não?:")
if(media < preco_alcool):
  print("Melhor abastecer com Gasolina")
else: 
  print("Melhor abastecer com Alcool")

#print(f'{resultado_gasolina:,.2f}',"L")
#print(f'{resultado_alcool:,.2f}',"L")
#print(f'R${media:,.2f}')
"""

"""#"___________________________________________"
  
idade = int(input("Quantos anos você tem?: "))

if(idade < 65):
  print("Como sua idade é {} anos, o valor da sua passagem será R$5,50" .format(idade))
else: 
  print("Como sua idade é {} anos, o valor da sua passagem será R$3,90" .format(idade))
"""
"""#"____________________________________________________"

idade = int(input("Quantos anos você tem?: "))

if(idade < 65):
  valor_bil = 5,50
else:
  valor_bil = 3,90

print("Como sua idade é {} anos, o valor da sua passagem será R$ {}" .format(idade,valor_bil))
"""

"""#"__________________________________________________________"
x = 10
y = 10

if(x==y):
  print("São Iguais")
  print("x = y",x==y)
print("x =",x,"y =",y)

"""

#"_____________________________________________________________"

maca = int(input("Quantas Maçãs você deseja comprar?: "))

if (maca < 12):
  preco = 1.50
elif (maca >= 24):
  preco = 1.00
else:
  preco = 1.10

total = float(maca*preco)

print("Como sua compra foi de {} Maçãs, o valor unitario será R$ {:.2f} e sua compra total será R$ {:.2f}." .format(maca,preco,total))

