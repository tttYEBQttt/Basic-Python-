##Con w usamos para escribir en el archivo, cuando se escribe se borra lo anterior

archivo = open("D:/Python/part_2/datos.txt", "w") #En caso de que el archivo no exista, se creara
archivo.write("FOSTER THE PEOPLE")
archivo.close()