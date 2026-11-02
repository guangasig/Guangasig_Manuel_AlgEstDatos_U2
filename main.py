from utilidades import (
    analizar_prestamos,
    buscar_libro,
    crear_datos_ejemplo,
    crear_socios_y_prestamos_ejemplo,
    obtener_catalogo_ordenado,
    registrar_libro,
    registrar_prestamo,
    registrar_socio,
    socio_esta_registrado,
)


def mostrar_menu():
    """Muestra las opciones disponibles en el sistema."""
    print("\nSISTEMA DE BIBLIOTECA CARUPS")
    print("1. Registrar libro")
    print("2. Buscar libro por codigo")
    print("3. Mostrar catalogo ordenado")
    print("4. Registrar socio")
    print("5. Verificar socio")
    print("6. Mostrar socios registrados")
    print("7. Registrar prestamo por genero")
    print("8. Analizar prestamos")
    print("0. Salir")


def solicitar_texto(mensaje):
    """Solicita un texto obligatorio y elimina espacios exteriores."""
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        print("El valor no puede estar vacio.")


def opcion_registrar_libro(catalogo):
    codigo = solicitar_texto("Codigo del libro: ").upper()
    titulo = solicitar_texto("Titulo: ")
    autor = solicitar_texto("Autor: ")

    if registrar_libro(catalogo, codigo, titulo, autor):
        print("Libro registrado correctamente.")
    else:
        print("Ya existe un libro con ese codigo.")


def opcion_buscar_libro(catalogo):
    codigo = solicitar_texto("Codigo que desea buscar: ").upper()
    libro = buscar_libro(catalogo, codigo)

    if libro is None:
        print("Libro no encontrado.")
    else:
        print(f"Titulo: {libro['titulo']}")
        print(f"Autor: {libro['autor']}")


def opcion_mostrar_catalogo(catalogo):
    libros_ordenados = obtener_catalogo_ordenado(catalogo)

    if not libros_ordenados:
        print("El catalogo esta vacio.")
        return

    print("\nCATALOGO ORDENADO POR CODIGO")
    for codigo, libro in libros_ordenados:
        print(f"{codigo} | {libro['titulo']} | {libro['autor']}")


def opcion_registrar_socio(socios):
    identificador = solicitar_texto("Identificador del socio: ").upper()

    if registrar_socio(socios, identificador):
        print("Socio registrado correctamente.")
    else:
        print("El socio ya esta registrado.")


def opcion_verificar_socio(socios):
    identificador = solicitar_texto("Identificador que desea verificar: ").upper()

    if socio_esta_registrado(socios, identificador):
        print("El socio esta registrado.")
    else:
        print("El socio no esta registrado.")


def opcion_mostrar_socios(socios):
    if not socios:
        print("No existen socios registrados.")
        return

    print("\nSOCIOS REGISTRADOS")
    for identificador in sorted(socios):
        print(identificador)


def opcion_registrar_prestamo(socios, prestamos_novela, prestamos_ciencia):
    identificador = solicitar_texto("Identificador del socio: ").upper()
    genero = solicitar_texto("Genero (novela/ciencia): ").lower()
    resultado = registrar_prestamo(
        socios,
        prestamos_novela,
        prestamos_ciencia,
        identificador,
        genero,
    )

    mensajes = {
        "registrado": "Prestamo registrado correctamente.",
        "socio_no_registrado": "El socio no esta registrado.",
        "genero_invalido": "Genero no valido. Use novela o ciencia.",
        "prestamo_existente": "El socio ya tiene un prestamo de ese genero.",
    }
    print(mensajes[resultado])


def mostrar_identificadores(titulo, identificadores):
    print(f"\n{titulo}")
    if identificadores:
        print(", ".join(sorted(identificadores)))
    else:
        print("Ninguno")


def opcion_analizar_prestamos(prestamos_novela, prestamos_ciencia):
    ambos, solo_novela, total_distintos = analizar_prestamos(
        prestamos_novela,
        prestamos_ciencia,
    )

    mostrar_identificadores("SOCIOS QUE LEEN AMBOS GENEROS", ambos)
    mostrar_identificadores("SOCIOS QUE SOLO LEEN NOVELA", solo_novela)
    mostrar_identificadores("TOTAL DE SOCIOS DISTINTOS CON PRESTAMOS", total_distintos)
    print(f"Cantidad total: {len(total_distintos)}")


def main():
    """Inicia el sistema con libros, socios y prestamos de ejemplo."""
    catalogo = crear_datos_ejemplo()
    socios, prestamos_novela, prestamos_ciencia = (
        crear_socios_y_prestamos_ejemplo()
    )

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opcion: ").strip()

        if opcion == "1":
            opcion_registrar_libro(catalogo)
        elif opcion == "2":
            opcion_buscar_libro(catalogo)
        elif opcion == "3":
            opcion_mostrar_catalogo(catalogo)
        elif opcion == "4":
            opcion_registrar_socio(socios)
        elif opcion == "5":
            opcion_verificar_socio(socios)
        elif opcion == "6":
            opcion_mostrar_socios(socios)
        elif opcion == "7":
            opcion_registrar_prestamo(socios, prestamos_novela, prestamos_ciencia)
        elif opcion == "8":
            opcion_analizar_prestamos(prestamos_novela, prestamos_ciencia)
        elif opcion == "0":
            print("Programa finalizado.")
            break
        else:
            print("Opcion no valida. Intente nuevamente.")


if __name__ == "__main__":
    main()
