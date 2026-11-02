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
