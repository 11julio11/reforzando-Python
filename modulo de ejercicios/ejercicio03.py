"Escribe un programa que pida tres números al usuario y determine cuál es el mayor de los tres."

usuario1 = int(input('ingrese su primer numero: '))
usuario2 = int(input('ingrese su segundo numero: '))
usuario3 = int(input('ingrese su tercer numero: '))

numero_mayor = max(usuario1,usuario2,usuario3)

print('el mumero mayor es: ', numero_mayor)