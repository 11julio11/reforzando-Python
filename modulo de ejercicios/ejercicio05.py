"Escribe un programa que reciba una cadena de texto y cuente cuántas vocales hay en ella."

cadena_de_texto = input('ingrese una cadena de texto: ')
vocales = "aeiouAEIOU"
contador = 0 

for letras in cadena_de_texto:
    if letras in vocales:
        contador += 1
    
print("Número de vocales en la cadena:", contador)
