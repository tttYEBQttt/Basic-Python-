##Tambien se puede usar with para leer el archivo y que se cierre el archivo auto

with open("D:/Python/part_2/datos.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido) 
