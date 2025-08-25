Alumno={"Nombre":"Raul Ascencio", "Edad": 18, "Codigo" :2223334543, "Correo": "Ascencio3340@gmail.com"}

##Imprimir ciertos valores
print(Alumno["Codigo"])
print(Alumno["Nombre"])

print(Alumno.keys()) #Imprime directamente las keys
print(Alumno.values()) #Imprime los valores de las keys
print(Alumno.items()) #Imprime las key y sus valores en pareja

Alumno.update({"Promedio": 89}) #Agregar una nueva key juntop a su valor
print(Alumno)