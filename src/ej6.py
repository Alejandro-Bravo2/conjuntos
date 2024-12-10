# Aqui lo que se hace es devolver los valores que estén en ambos conjuntos


def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1 & conjunto2

def main():
    vocales = {'a', 'e', 'i', 'o', 'u'}
    consonantes = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}
    resultado = interseccion_conjuntos(vocales, consonantes)
    print(resultado)

if __name__ == "__main__":
    main()
# No devolverá nada porque en las consonantes no están las vocales