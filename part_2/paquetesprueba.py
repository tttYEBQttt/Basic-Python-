##Importamos el paquete creado
import paquete.operaciones #Tambien podemos importar directamente los modulos

a = int(input("Ingrese un valor: ")) 
b = int(input("Ingrese otro valor: "))

sum = paquete.operaciones.suma(a,b)
resta = paquete.operaciones.resta(a,b)
mult = paquete.operaciones.multiplicacion(a,b)

print(f"La suma es: {sum} , La resta es : {resta} , La multiplicacion es: {mult}") #Imprime los 3 valores