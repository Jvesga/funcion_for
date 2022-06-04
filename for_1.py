# sumar los numeros del 1 al 10 con while
suma = 0
contador = 1 
while contador <= 10:
    suma = suma + contador
    # contador = contador + 1
    contador += 1
print(" La suma es " + str(suma))

# sumar los numeros del 1 
suma = 0
lista = [1,2,3,4,5,6,7,8,9,10]
for contador in lista:
    suma = suma + contador
print(" La suma es " + str(suma))