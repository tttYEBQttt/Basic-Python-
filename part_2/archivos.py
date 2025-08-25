##Podemos abrir archivos en diferentes modos, como lectura ("r"), escritura ("w") o anexar ("a")

##Utiizamos open() para abrir el archivo y close() para cerrarlo
archivo = open("D:/Python/part_2/datos.txt", "r") #Si no abre el archivo, poner directamente la direccion
contenido = archivo.read()
print(contenido)
archivo.close() #Siempre cerrar el archivo

