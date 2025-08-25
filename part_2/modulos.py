##Podemos importar varios modulos con import
import math
import datetime
from random import randint #Tambien podemos importar una sola funcion
resultado = math.sqrt(64)
print(resultado) #Imprime la raiz del numero

tiempo = datetime.datetime.now()
print(tiempo) #Imprime la fecha y hora actual

randoms = randint(1,20)
print(randoms) #Imprime un numero random del 1 al 20

