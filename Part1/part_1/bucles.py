print("Numeros del 1 al 10 multiplicados por 2")
for numero in range(1,11):
    print(numero*2)

print("Contador del 0 al 10")
cont=1
while cont<=10:
    print(cont)
    cont+=1

contador=1
##Utilidad Break
while True:
    print(contador)
    contador+=1
    if contador == 33: #Un digito mas del que se imprime
        break

##Utilidad continue
for i in range (1000):
    if i % 2 == 0:
        continue
    print(i) #En este caso solo imprime los numeros impares

for x in range(5):
    pass #No hace nada, es util como para dejarlo para despues agregar algo