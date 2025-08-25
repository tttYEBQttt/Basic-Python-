conjunto = {1,2,3,4,5,6} #Tambien se puede poner como conjunto = se([1,2,3,4,5,6])
conjuntotwo = set([6,7,8,9,10,11])

print(conjunto)
print(conjuntotwo)

union = conjunto | conjuntotwo #Une los valores de ambos conjuntos
print(union)

interseccion = conjunto & conjuntotwo #Imprime los valores iguales de ambos conjuntos
print(interseccion)

diferencia = conjunto - conjuntotwo #imprime el primer conjunto menos los valores iguales del segundo
print(diferencia)

diferencia_simetrica = conjunto ^ conjuntotwo #Imprime los dos conjuntos menos los valores iguales
print(diferencia_simetrica)

conjunto.add(7) #Añadir un nuevo valor al conjunto
print(conjunto)

conjunto.remove(3) #Remueve un elemento del conjunto, si no exite, genera error
print(conjunto)

conjunto.discard(4) #Remueve un elemento pero si no existe en el conjunto no pasa nada
print(conjunto)

conjuntotwo.clear() #Elimina todos los elementos del conjunto
print(conjuntotwo)


