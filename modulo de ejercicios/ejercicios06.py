"Crea un programa que pida un número al usuario y determine si es un número primo."
numero = int(input('ingrese un numero: '))

es_primo = True

if numero < 2:
    es_primo = False
else:   
    for i in range(2, int(numero ** 0.5) +1):
      if numero % 1 == 0:
         es_primo = False
         break
    
if es_primo:
    print(f"{numero} es un numero primo.: ")
else:
    print(f"{numero} no es un numero primo.: ")