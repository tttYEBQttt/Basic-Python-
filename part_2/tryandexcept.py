##Contiene el código que puede generar una excepción
try:
    ##Código que puede generar una excepción, se puede tener varios except
    resultado = 10 / 0  # División por cero
    print(resultado)
except ZeroDivisionError:
    print("Error: División por cero")
except ValueError:
    print("Error: Valor inválido")
finally: #finally siempre se ejecutara 
    print("Hola Mundo")
