#Escribir un programa que acceda a un fichero de internet mediante su url y muestre por pantalla el número
#de palabras que contiene.

import urllib.request

def contar_palabras(url):
    cont = 0
    file = urllib.request.urlopen(url)
    for line in file:
        for i in line.decode("utf-8"):
            cont += 1
    print("La URL tiene", cont, "palabras.")

fichero = input("Escribe una URL: ")
contar_palabras(fichero)
