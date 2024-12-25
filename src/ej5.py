"""
Dado el conjunto de números enteros:

numeros = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
Crea un conjunto pares que contenga los números pares del conjunto numeros.
Crea un conjunto multiplos_de_tres que contenga los números que son múltiplos de tres del conjunto numeros.
Encuentra la intersección entre los conjuntos pares y multiplos_de_tres y guárdala en un conjunto llamado pares_y_multiplos_de_tres.
"""


def multiplos(numeros:set)->set:
    """Devuelve los multiplos de 2 y de 3

    :param numeros: Conjunto de numeros
    :type numeros: set
    :return: Conjunto de pares y conjunto de multiplos de 3
    :rtype: set
    """
    multiplos_de_dos = set()
    multiplos_de_tres = set()
    for i in numeros:
        if i % 2 == 0 and i % 3 == 0:
            multiplos_de_dos.add(i)
            multiplos_de_tres.add(i)
        elif i % 2 == 0:
            multiplos_de_dos.add(i)
        elif i % 3 == 0:
            multiplos_de_tres.add(i)
    return multiplos_de_dos, multiplos_de_tres

def interseccion_conjuntos(conjunto1:set, conjunto2:set)->set:
    """Hacemos la intersection de los dos conjuntos

    :param conjunto1: Conjunto de pares
    :type conjunto1: set
    :param conjunto2: Conjunto de multiplos de 3
    :type conjunto2: set
    :return: Conjunto con los valores que están en ambos conjuntos
    :rtype: set
    """
    return conjunto1 & conjunto2

def main():
    numeros = {1,2,3,4,5,6,7,8,9,10}
    multiplos_de_dos, multiplos_de_tres = multiplos(numeros)
    pares_y_multiplos_de_tres = interseccion_conjuntos(multiplos_de_dos, multiplos_de_tres)
    print(f"Los numeros que son pares y multiplos de 3 son: {pares_y_multiplos_de_tres}")
    
if __name__ == "__main__":
    main()