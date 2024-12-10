def pregunta()->list:
    """ Entrada datos

    :return: Listas con los alumnados de primaria y secundaria.
    :rtype: list
    """ 
    nombres_primaria = ""
    nombres_secundaria = ""
    alumnado_primaria = []
    alumnado_secundaria = []
    while nombres_primaria != "x":
        nombres_primaria = input("Dime el nombre del alumno de primaria: ")
        alumnado_primaria.append(nombres_primaria)
    while nombres_secundaria != "x":
        nombres_secundaria = input("Dime el nombre del alumno de secundaria: ")
        alumnado_secundaria.append(nombres_secundaria)
    return alumnado_primaria, alumnado_secundaria

def nombres_no_repetidos(alumnado_primaria:list, alumnado_secundaria:list) -> list:
    """ comprobar los nombres que no se repiten

    :param alumnado_primaria: lista con los nombres de los alumnos de primaria
    :type alumnado_primaria: list
    :param alumnado_secundaria: lista con los nombres de los alumnos de secundaria
    :type alumnado_secundaria: list
    
    :return: listas con los nombres que no se repiten de primaria y secundaria
    :rtype: dict
    """
    lista_no_repetidos_primaria = []
    lista_no_repetidos_secundaria = []
    for i in alumnado_primaria:
        if i not in lista_no_repetidos_primaria:
            lista_no_repetidos_primaria.append(i)
    for i in alumnado_secundaria:
        if i not in lista_no_repetidos_secundaria:
            lista_no_repetidos_secundaria.append(i)
    return lista_no_repetidos_primaria, lista_no_repetidos_secundaria

def nombres_repetidos(alumnado_primaria:list, alumnado_secundaria:list)->dict:
    """comprobar nombres repetidos y cantidad de veces

    :param alumnado_primaria: lista con los nombres de los alumnos de primaria
    :type alumnado_primaria: list
    :param alumnado_secundaria: lista con los nombres de los alumnos de secundaria
    :type alumnado_secundaria: list
    :return: diccionarios con los nombres repetidos de primaria y secundaria por separado.s
    :rtype: dict
    """
    lista_repetidos = []
    repeticiones_primaria = {}
    repeticiones_secundaria = {}
    contador = 0
    for i in alumnado_primaria:
        if i in lista_repetidos:
            if i not in repeticiones_primaria:
                repeticiones_primaria[i] = 2
            else:
                tmp = repeticiones_primaria[i]
                contador = tmp + 1
                repeticiones_primaria[i] = contador
            lista_repetidos.append(i)
        else:
            lista_repetidos.append(i)
    lista_repetidos =[]
    for i in alumnado_secundaria:
        if i in lista_repetidos:
            if i not in repeticiones_secundaria:
                repeticiones_secundaria[i] = 2
            else:
                tmp = repeticiones_secundaria[i]
                contador = tmp + 1
                repeticiones_secundaria[i] = contador
            lista_repetidos.append(i)
        else:
            lista_repetidos.append(i)
    return repeticiones_primaria, repeticiones_secundaria

def comprobar_si_repiten(alumnado_primaria, alumnado_secundaria)->list:
    """Lista con los nombres de primaria incluidos en secundaria

    :param alumnado_primaria: lista con los nombres de los alumnos de primaria
    :type alumnado_primaria: list
    :param alumnado_secundaria: lista con los nombres de los alumnos de secundaria
    :type alumnado_secundaria: list
    :return: lista con los nombres de primaria incluidos en secundaria
    :rtype: dict
    """
    alumnados_repetidos = []
    for i in alumnado_primaria:
        if i in alumnado_secundaria:
            alumnados_repetidos.append(i)
    return alumnados_repetidos

def comprobacion_total(alumnado_primaria, alumnado_secundaria):
    tmp = True
    contador = 0
    while contador < len(alumnado_primaria) and tmp:
        tmp = alumnado_primaria[contador] in alumnado_secundaria
        contador += 1
    return tmp


def main():
    alumnado_primaria, alumnado_secundaria = pregunta()
    lista_no_repetidos_primaria, lista_no_repetidos_secundaria = nombres_no_repetidos(alumnado_primaria,alumnado_secundaria)
    repeticiones_primaria, repeticiones_secundaria = nombres_repetidos(alumnado_primaria, alumnado_secundaria)
    alumnados_repetidos = comprobar_si_repiten(alumnado_primaria, alumnado_secundaria)
    igualdad_clases = comprobacion_total(alumnado_primaria, alumnado_secundaria)

    # IMPRIMIR ALUMNOS NO REPETIDOS
    print("\n Alumnos no repetidos")
    for i in range(len(lista_no_repetidos_primaria)):
        print(f"El nombre del alumno de primaria llamado: {lista_no_repetidos_primaria[i]} no se repite más veces")
    for i in range(len(lista_no_repetidos_secundaria)):
        print(f"El nombre del alumno de secundaria llamado: {lista_no_repetidos_secundaria[i]} no se repite más veces")
    # IMPRIMIR ALUMNOS REPETIDOS
    print("\n Alumnos repetidos")

    for i in repeticiones_primaria.keys():
        print(f"El alumno de primaria llamado: {i} se ha repetido {repeticiones_primaria[i]} veces")

    for i in repeticiones_secundaria.keys():
        print(f"El alumno de secundaria llamado: {i} se ha repetido {repeticiones_secundaria[i]} veces")

    # IMPRIMIR NOMBRES DE PRIMARIA NO REPETIDOS EN SECUNDARIA
    print("\n Nombres de primaria no repetidos en secundaria")
    for i in alumnados_repetidos:
        print(f"El nombre de alumno: {i} se repite también en secundaria")

    # IMPRIMIR SI LOS NOMBRES DE PRIMARIA SON IGUALES A LOS DE SECUNDARIA
    print("\n")
    if igualdad_clases:
        print("Todos los nombres de la clase de primaria están incluidos en la clase de secundaria")
    else:
        print("Los nombres de la clase primaria no están incluidos en la clase de secundaria")

if __name__ == '__main__':
    main()