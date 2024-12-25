"""
Dado el conjunto de letras:

vocales = {'a', 'e', 'i', 'o', 'u'}
Crea un conjunto consonantes que contenga las letras del alfabeto que no son vocales.
Crea un conjunto letras_comunes que contenga las letras que están tanto en el conjunto vocales como en el conjunto consonantes.
"""

def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1 & conjunto2

def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', "ñ", 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    letras_comunes = interseccion_conjuntos(vocales, consonantes)
    print(letras_comunes)

if __name__ == "__main__":
    main()
# devuelve conjunto vacio porque las volcales no estan en las consonantes, he leido el ejercicio 8 veces y creo
# que lo que querías era interseccion porque dices que contenga las letras que estan tanto en vocales como en consonantes 
# pero se me hace raro porque como devuelve algo vacio pues alomejor me he confudido pero si lo que querías era que usara
# el metodo de union lo unico que habria que hacer es cambiar el & por |