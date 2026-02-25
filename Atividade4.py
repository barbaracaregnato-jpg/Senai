nota1 = float(input ("Insira nota 1: "))
nota2 = float(input ("Insira nota 2: "))
nota3 = float(input ("Insira nota 3: "))
nota4 = float(input ("Insira nota 4: "))
media = (nota1+nota2+nota3+nota4)/ 4 
print("A média final é ", media)
if media >= 7: 
    print("Aluno está aprovado")
else:
    print("Aluno está reprovado")