acima_15 = float()
menor = float()
soma = 0

for cont in range(11):
    temperatura = float(input(f"Digite a {cont + 1} temperatura: "))
    soma += temperatura
    if cont == 0:
        maior = temperatura 
        menor = temperatura 

    if  temperatura > maior:
        maior = temperatura
    if  temperatura < menor: 
        menor = temperatura
    if  temperatura > 100:
        acima_100 += 1 
media = soma/cont

print(f"A maior temperatura foi {maior}")
print(f" A menor temperatura é menor {menor}")
print(f" A media das temperaturas é: {media}" )
print (f" A temperatura ultrapassou 100 {acima_100} vezes")