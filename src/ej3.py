"""
El conjunto potencia de un conjunto S es el conjunto de todos los subconjuntos de S.
"""
def conjunto_potencia(subconjunto_s:set)->list:
    """Genera la potencia de un conjunto dado

    :param subconjunto_s: conjunto con los elementos a los que se les va a generar la potencia
    :type subconjunto_s: set
    :return: lista con la potencia del conjunto
    :rtype: list
    """
    conjunto_congelado_lista = list(subconjunto_s)
    lista_potencias = [[]]

    for numero_individual in conjunto_congelado_lista:
        lista_potencias.append([numero_individual])

    for numero in conjunto_congelado_lista:
        lista_tmp = []
        for pares_subconjunto in range(len(conjunto_congelado_lista) -2):
            tmp = subconjunto_s - {numero}
            lista_tmp.append(tmp)
        lista_potencias.append(lista_tmp.copy())
        
    lista_tmp = []

    for numero_en_conjunto in subconjunto_s:
        lista_tmp.append(numero_en_conjunto)

    lista_potencias.append(lista_tmp.copy())

    return lista_potencias

def main():
    subconjunto_s = {6,1,4}
    resultado = conjunto_potencia(subconjunto_s)
    print(resultado)
    
    
if __name__ == "__main__":
    main()