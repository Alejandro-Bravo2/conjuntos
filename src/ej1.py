""" 
Suponer una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, 
la cual contiene tuplas con información de cada venta: (cliente, día del mes, monto, domicilio 
del cliente). Ejemplo:

[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol 218"),
("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
("Jorge Russo", 15, 958, "Mirasol 218")]
Escribir una función que reciba como parámetro una lista con 
el formato mencionado anteriormente y retorne los domicilios de
cada cliente al cual se le debe enviar una factura de compra. Notar 
que cada cliente puede haber hecho más de una compra en el mes, por lo
que la función debe retornar una estructura que contenga cada domicilio una sola vez.
"""
def preguntarClientes()->list:
    """Funcion encargada de preguntar por los datos del usuario y los agrupa en una lista

    :return: listas con los datos del usuario divididos en: nombre, dia, porte, domicilio
    :rtype: list
    """
    datosCliente = ""
    listaClientes = []
    while datosCliente != "salir":
        datosCliente = input("Cual es el nombre de su cliente / Escriba salir para parar el programa => ")
        if datosCliente == "salir":
            return listaClientes
        try:
            dia = int(input("En que día del mes se realizó la compra => "))
            if dia > 31 or dia < 0:
                raise("EL CAMPO DIA SOLO PUEDE ESTAR EN EL RANGO DE VALORES 0..31")
            porte = int(input("Cuanto ha costado la compra => "))
            if porte < 0:
                raise("EL CAMPO DE PORTE TIENE QUE SER MAYOR A 0")
        except ValueError:
            raise("LOS CAMPOS DE NÚMEROS NO PUEDEN SER CARÁCTERES")
        domiciolio = input("A que domicilio se ha mandado el pedido => ")
        valoresTMP = []
        valoresTMP.append(datosCliente)
        valoresTMP.append(dia)
        valoresTMP.append(porte)
        valoresTMP.append(domiciolio)
        
        valoresCliente = tuple(valoresTMP)
        listaClientes.append(valoresCliente)


def domicilioPorCliente(listaClientes:list)->dict:
    """Funcion encargada de leer la lista y añadir a un diccionario los clientes y su domicilio, PERO AQUELLOS DOMICILIOS QUE 
    NO SE HAYAN DUPLICADO

    :param listaClientes: lista con los clientes y sus datos
    :type listaClientes: list
    :return: diccionario con clave el nombre del cliente y valor el domicilio
    :rtype: dict
    """
    diccionarioClientes = {}
    for cliente, dia, porte, domicilio in listaClientes:
        if not domicilio in diccionarioClientes.values():
            diccionarioClientes[cliente] = domicilio
    return diccionarioClientes

def main():
    listaClientes = preguntarClientes()
    diccioanrioClientes = domicilioPorCliente(listaClientes)
    for cliente in diccioanrioClientes:
        print(f"El usuario {cliente} ha realizado un pedido al domicilio: {diccioanrioClientes[cliente]}")
    
if __name__ == "__main__":
    main()