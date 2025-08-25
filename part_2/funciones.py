##Palbra clave : def ##Siempre poner : 

def tuki ():
    x= 1
    y= 10
    a = x+y
    print(a)

tuki() #Simplemente se llama a la funcion

##Las funciones pueden aceptar parametros y argumentos
listen = "Timeless" #Tambnien podemos poner el argumento directamente al llamr a la funcion

def cancion(song):
    print(f"Tu cancion es: {song}")

cancion(listen) #Al llamar a la funcion le proporcionamos el argumento al parametro

##Tambien podemos utilizar el return para devolver valores a partir de los argumentos dados a los parametros
def resta(num1,num2):
    return num1-num2
resultado = resta(3,9) #En este caso se llama a la funcion y se guarda en otra variable para poder imprimir
print(resultado)

##Funciones lambda , son funciones sin nombre y para cosas pequeñas (Una linea)
Number = lambda s : (s/2)+5 #Se coloca la palabra lambda junto a un parametro y posteriormente el proceso a realizar
print(Number(24)) #se imprime con un print y como si llamaras a una funcion pasandole el argumento al parametro

##Las funciones declaradas dentro de las funciones son variables locales, mientras que las que esten afuera seran globales

##Tambien podemos hacer un parametro que acepte varios argumentos

def prom(*nums): #Se coloca * para que acepte varios argumentos, lo que crea una tupla para ello
    suma = sum(nums)
    cantidad =  len(nums)
    prom = suma / cantidad
    return prom
print(f"Promedio = {prom(10,9,8,10,8,10)}") #Se puede imprimir de estas dos formas
print("Promedio =", prom(10,9,8,10,8,10))