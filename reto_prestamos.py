https://replit.com/join/danxzxgust-julian-emilian1 
'''Calculadora de prestamos:
El reto consiste en un programa que calcule préstamos'''

print("Ingresa lo que se te pide")
prestamos = float(input("Cantidad del péstamo:"))
tasa = float(input("Tasa de intereses anual (%): %"))
años =  float(input("Plazo del péstamo (en años): "))
print(" ")
if tasa <= 5 and años <= 5: 
  print(f"Tu préstamo de {prestamos} es uno tipo de bajo riesgo ")
elif tasa > 5 or años > 5:
  print(f"Tu préstamo de {prestamos} es uno tipo de riesgo moderado ")
else: 
  print(f"Tu préstamo de {prestamos} es uno tipo de riesgo alto ")
