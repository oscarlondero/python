def convertir_temperatura():
    """Convierte una temperatura de Celsius a Fahrenheit y Kelvin."""

    while True:
        try:
            celsius = float(input("Ingrese la temperatura en grados Celsius: "))
            break  # Sale del bucle si la entrada es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    print(f"\nTemperatura ingresada: {celsius} °C")
    print(f"Temperatura en Fahrenheit: {fahrenheit:.2f} °F")
    print(f"Temperatura en Kelvin: {kelvin:.2f} K")


# Llamada a la función para ejecutar el programa
convertir_temperatura()