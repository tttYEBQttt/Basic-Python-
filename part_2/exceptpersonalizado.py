##Tenemos primero que definir la condicion para el except

def funcion (numero) :
    if numero % 2!=0:
        raise Exception ("El numero no es par") #Se utiliza raise para dar de alta la excepcion 
    else:
        print("El numero es par")

try: 
    funcion(11)
except Exception as x: #Se usa el as para renombrar la excepcion
    print("Error: ", x)
finally:
    print("Ingrese otro valor")

try: 
    funcion(4)
except Exception as x:
    print("Error: ", x)
finally:
    print("Hecho")
