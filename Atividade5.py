contador=0
soma=0
while contador < 4:
    contador+= 1
    nota = float(input (f"Insira a {contador} nota: "))
    soma+=nota

media = soma/contador
print("A média final é ", media)
if media >= 7: 
    print("Aluno está aprovado")
else:
    print("Aluno está reprovado")   