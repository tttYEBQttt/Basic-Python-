Comidas = ["Sushi", "Pescado", "Pollo", "Papa"]

print(Comidas[-1]) 
print(Comidas[-2]) 
print(Comidas[-3]) 
print(Comidas[-4]) #Se imprimen a la inversa

Comidas.append("Hamburguesa") #Agrega al final el elemento
print(Comidas)

Comidas.insert(3,"Mango") #Agrega el elemento al lugar indicado al inicio 
print(Comidas)

Comidas.remove("Papa") #Remueve el elemento
print(Comidas)

Comida_eliminada=Comidas.pop(0) #Recorta el elemento de la lista y se guarda en una variable
print(Comidas)
print(Comida_eliminada)

Comidas.sort() #Ordena de manera ascendente
print(Comidas)

Comidas.reverse() #Invierte la fila
print(Comidas)