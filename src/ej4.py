"""
Dadas las siguientes listas:

frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
Crea conjuntos a partir de estas listas y nómbralos set_frutas1 y set_frutas2.
Encuentra las frutas que están en ambas listas y guárdalas en un nuevo conjunto llamado frutas_comunes.
Encuentra las frutas que están en frutas1 pero no en frutas2 y guárdalas en un conjunto llamado frutas_solo_en_frutas1.
Encuentra las frutas que están en frutas2 pero no en frutas1 y guárdalas en un conjunto llamado frutas_solo_en_frutas2.
"""

def diferenciasFrutas2(listaFrutas1:set, listaFrutas2:set)->set:
    """Encuentra las frutas que están en la listaFrutas2 pero no en la listaFrutas1

    :param listaFrutas1: conjunto con las frutas
    :type listaFrutas1: set
    :param listaFrutas2: conjunto con las frutas
    :type listaFrutas2: set
    :return: conjunto con las frutas que están en listafrutas2 pero no en la lsitaFrutas1
    :rtype: set
    """
    frutas_solo_en_frutas2 = listaFrutas2 - listaFrutas1
    return frutas_solo_en_frutas2

def diferenciasFrutas1(listaFrutas1:set, listaFrutas2:set)->set:
    """Encuentra las frutas que están en la listaFrutas1 pero no en la listaFrutas2

    :param listaFrutas1: conjunto con las frutas
    :type listaFrutas1: set
    :param listaFrutas2: conjunto con las frutas
    :type listaFrutas2: set
    :return: conjunto con las frutas que están en listafrutas1 pero no en la lsitaFrutas2
    :rtype: set
    """
    frutas_solo_en_frutas1 = listaFrutas1 - listaFrutas2
    return frutas_solo_en_frutas1

def encontrarFrutasAmbas(conjuntoFrutas1:set,conjuntoFrutas2:set)->set:
    """Encuentra las frutas que estan en ambos conjuntos

    :param conjuntoFrutas1: conjunto con als frutas
    :type conjuntoFrutas1: set
    :param conjuntoFrutas2: conjunto con las frutas
    :type conjuntoFrutas2: set
    :return: frutas que están en ambos conjuntos
    :rtype: set
    """
    frutasComunes = conjuntoFrutas1 & conjuntoFrutas2
    return frutasComunes
    
def main():
    frutas1 = ["manzana", "pera", "naranja", "plátano", "uva"]
    frutas2 = ["manzana", "pera", "durazno", "sandía", "uva"]
    set_frutas1 = set(frutas1)
    set_frutas2 = set(frutas2)
    interseccionFrutas = encontrarFrutasAmbas(set_frutas1,set_frutas2)
    diferenciaFruta1 = diferenciasFrutas1(set_frutas1,set_frutas2)
    diferenciaFruta2 = diferenciasFrutas2(set_frutas1, set_frutas2)
    
    print(f"Las frutas que están en ambas listas son: {interseccionFrutas}")
    
    print(f"Las frutas que están en la lista 1 pero no en la lista 2 son: {diferenciaFruta1}")
    
    print(f"Las frutas que están en la lista 2 pero no en la lista 1 son: {diferenciaFruta2}")
if __name__ == "__main__":
    main()