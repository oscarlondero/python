def identificar_vocal():
    """Identifica si un caracter ingresado por el usuario es una vocal (con o sin acento)."""

    letra = input("Ingrese una letra: ").lower()

    vocales = "aeiouáéíóú"  # Incluimos vocales con acento

    if letra in vocales:
        print(f"La letra ingresada [{letra}] es una vocal.")
    else:
        print("La letra ingresada no es una vocal.")


# Llamada a la función para ejecutar el programa
identificar_vocal()