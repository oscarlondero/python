def contar_vocales_consonantes(frase):
    """
    Cuenta la cantidad de vocales y consonantes en una frase.

    Args:
        frase: La frase a analizar (string).

    Returns:
        Una tupla que contiene la cantidad de vocales y consonantes.
    """
    frase = frase.lower()  # Convertir a minúsculas para facilitar la comparación
    vocales = "aeiou"
    cant_vocales = 0
    cant_consonantes = 0

    for letra in frase:
        if letra.isalpha():  # Verificar si es una letra del alfabeto
            if letra in vocales:
                cant_vocales += 1
            else:
                cant_consonantes += 1

    return cant_vocales, cant_consonantes


if __name__ == "__main__":
    frase = input("Ingrese una frase: ")
    vocales, consonantes = contar_vocales_consonantes(frase)
    print(f"La frase contiene {vocales} vocales y {consonantes} consonantes.")