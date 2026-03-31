#Crea una función que reciba una palabra y retorne la cadena invertida.

def invertir(palabra):
    return palabra[:: -1]

texto = input("ingresa una palabra: ")

resultado = invertir(texto)

print("palabra invertida:", resultado)