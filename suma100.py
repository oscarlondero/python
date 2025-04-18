def sumar_hasta_cien():
    """
    Este programa solicita al usuario que ingrese números hasta que la suma de los números ingresados alcance o supere 100.
    """
    suma = 0
    while suma < 100:
        try:
            numero = int(input("Ingrese un número entero: "))
            suma += numero
            print(f"Suma actual: {suma}")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    print(f"La suma total ({suma}) ha alcanzado o superado 100.")


if __name__ == "__main__":
    sumar_hasta_cien()