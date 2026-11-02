"""Funciones del catalogo de libros de la biblioteca CarUPS."""


def crear_datos_ejemplo():
    """Crea un catalogo con algunos libros para probar las funciones."""
    catalogo = {
        "L001": {"titulo": "Cien anios de soledad", "autor": "Gabriel Garcia Marquez"},
        "L003": {"titulo": "Cosmos", "autor": "Carl Sagan"},
        "L002": {"titulo": "El principito", "autor": "Antoine de Saint-Exupery"},
    }
    return catalogo


def registrar_libro(catalogo, codigo, titulo, autor):
    """Registra un libro si su codigo todavia no existe."""
    # R1 - Verificar y registrar por clave: O(1) promedio.
    if codigo in catalogo:
        return False

    catalogo[codigo] = {"titulo": titulo, "autor": autor}
    return True


def buscar_libro(catalogo, codigo):
    """Busca un libro directamente mediante su codigo."""
    # R1 - Busqueda en un diccionario: O(1) promedio.
    return catalogo.get(codigo)


def obtener_catalogo_ordenado(catalogo):
    """Devuelve los libros ordenados ascendentemente por codigo."""
    # R2 - Ordenar n entradas mediante sorted: O(n log n).
    return sorted(catalogo.items())


def crear_socios_y_prestamos_ejemplo():
    """Crea conjuntos de socios y prestamos para probar el programa."""
    socios = {"S001", "S002", "S003", "S004"}
    prestamos_novela = {"S001", "S002", "S004"}
    prestamos_ciencia = {"S002", "S003"}

    return socios, prestamos_novela, prestamos_ciencia


def registrar_socio(socios, identificador):
    """Registra un socio sin permitir identificadores duplicados."""
    # R3 - Verificar y agregar en un conjunto: O(1) promedio.
    if identificador in socios:
        return False

    socios.add(identificador)
    return True


def socio_esta_registrado(socios, identificador):
    """Verifica si un identificador pertenece al conjunto de socios."""
    # R3 - Verificacion de pertenencia: O(1) promedio.
    return identificador in socios


def registrar_prestamo(
    socios,
    prestamos_novela,
    prestamos_ciencia,
    identificador,
    genero,
):
    """Asocia un socio registrado con un prestamo de novela o ciencia."""
    # Verificacion y registro en conjuntos: O(1) promedio.
    if identificador not in socios:
        return "socio_no_registrado"

    genero = genero.lower()

    if genero == "novela":
        conjunto_destino = prestamos_novela
    elif genero == "ciencia":
        conjunto_destino = prestamos_ciencia
    else:
        return "genero_invalido"

    if identificador in conjunto_destino:
        return "prestamo_existente"

    conjunto_destino.add(identificador)
    return "registrado"


def analizar_prestamos(prestamos_novela, prestamos_ciencia):
    """Calcula interseccion, diferencia y union de los prestamos."""
    # R4 - Operaciones entre conjuntos: O(n + m).
    ambos_generos = prestamos_novela & prestamos_ciencia
    solo_novela = prestamos_novela - prestamos_ciencia
    socios_con_prestamos = prestamos_novela | prestamos_ciencia

    return ambos_generos, solo_novela, socios_con_prestamos


if __name__ == "__main__":
    # Prueba independiente de los requerimientos R1 y R2.
    catalogo = crear_datos_ejemplo()

    print("CATALOGO INICIAL ORDENADO")
    for codigo, libro in obtener_catalogo_ordenado(catalogo):
        print(f"{codigo} | {libro['titulo']} | {libro['autor']}")

    print("\nREGISTRO DE UN LIBRO")
    registrado = registrar_libro(
        catalogo,
        "L004",
        "Don Quijote de la Mancha",
        "Miguel de Cervantes",
    )
    print("Libro registrado:", registrado)

    print("\nBUSQUEDA POR CODIGO L004")
    libro_encontrado = buscar_libro(catalogo, "L004")
    print(libro_encontrado)

    print("\nCATALOGO FINAL ORDENADO")
    for codigo, libro in obtener_catalogo_ordenado(catalogo):
        print(f"{codigo} | {libro['titulo']} | {libro['autor']}")

    # Prueba independiente de los requerimientos R3 y R4.
    socios, prestamos_novela, prestamos_ciencia = (
        crear_socios_y_prestamos_ejemplo()
    )

    print("\nSOCIOS INICIALES")
    print(sorted(socios))

    print("\nREGISTRO DEL SOCIO S005")
    socio_registrado = registrar_socio(socios, "S005")
    print("Socio registrado:", socio_registrado)
    print("S005 esta registrado:", socio_esta_registrado(socios, "S005"))

    print("\nREGISTRO DE PRESTAMOS PARA S005")
    resultado_novela = registrar_prestamo(
        socios,
        prestamos_novela,
        prestamos_ciencia,
        "S005",
        "novela",
    )
    resultado_ciencia = registrar_prestamo(
        socios,
        prestamos_novela,
        prestamos_ciencia,
        "S005",
        "ciencia",
    )
    print("Prestamo de novela:", resultado_novela)
    print("Prestamo de ciencia:", resultado_ciencia)

    ambos, solo_novela, total_distintos = analizar_prestamos(
        prestamos_novela,
        prestamos_ciencia,
    )

    print("\nANALISIS DE PRESTAMOS")
    print("Ambos generos:", sorted(ambos))
    print("Solo novela:", sorted(solo_novela))
    print("Total de socios distintos:", sorted(total_distintos))
