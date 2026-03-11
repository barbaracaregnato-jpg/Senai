soma = 0 
acima_15 = 0
acima_20 = 0
acima_200 = 0
sobrecarga = False
alerta = False
for i in range(8):
  corrente = float(input(f"Digite a {i+1} medição de corrente(A): "))
  soma += corrente 

  if corrente > 15:
    acima_15 += 1
  if corrente > 20:
    sobrecarga = True
    acima_20 += 1
  if corrente > 200:
    alerta = True
    acima_200 += 1
media = soma/ 8
print("Medições acima de de 15 (A)", acima_15)
print("Média da corrente: ", media)
if sobrecarga:
  print(f"Houve sobrecarga no motor {acima_20} vezes")
if alerta:
  print(f"ALERTA: Medição ultrapassou 200 {acima_200} vezes")


    
    

