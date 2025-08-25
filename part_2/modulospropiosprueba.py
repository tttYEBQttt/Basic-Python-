##Importamos nuestro modulo por su nombre
import modulospropios

a = int(input("Ingrese un valor: "))
b = int(input("Ingrese otro valor: "))

producto = modulospropios.calcular_multiplicacion(a,b)
print(producto) #Imprime el producto de los dos numeros dados

tuki = modulospropios.name("GOJO") #No necesita print