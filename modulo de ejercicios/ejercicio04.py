"Crea un programa que pida un número al usuario y muestre su tabla de multiplicar desde 1 hasta 10."

numero = int(input('introduzca el numero a multiplicar: '))
print(f"tabla de multiplicar {numero}: ")
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")