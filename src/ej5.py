# Basicamente lo que se hace es usar el modulo y lo divididimos entre 2
# y si el resto es 0 entonces es par y si no es impar
# Luego cojemos y lo metemos en un conjunto y lo devolvemos

# Y con los multiplos de 3 lo mismo


def multiplos(numeros:set)->set:
    """Devuelve los multiplos de 2 y de 3

    :param numeros: Conjunto de numeros
    :type numeros: set
    :return: Conjunto de pares y conjunto de multiplos de 3
    :rtype: set
    """
    conjunto_pares = set()
    conjunto_multiplos_3 = set()
    for i in numeros:
        if i % 2 == 0 and i % 3 == 0:
            conjunto_pares.add(i)
            conjunto_multiplos_3.add(i)
        elif i % 2 == 0:
            conjunto_pares.add(i)
        elif i % 3 == 0:
            conjunto_multiplos_3.add(i)
    return conjunto_pares, conjunto_multiplos_3

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
    conjunto_pares, conjunto_multiplos_3 = multiplos(numeros)
    resultado = interseccion_conjuntos(conjunto_pares, conjunto_multiplos_3)
    print(resultado)
    
if __name__ == "__main__":
    main()