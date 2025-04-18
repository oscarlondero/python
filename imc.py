import os
def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_imc():
    """Calcula el IMC y lo imprime, con validación de datos."""

    while True:
        try:
            peso = float(input("Ingrese su peso en kilogramos: "))
            if peso <= 0:
                raise ValueError("El peso debe ser un valor positivo.")
            break  # Sale del bucle si la entrada es válida
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

    while True:
        try:
            altura = float(input("Ingrese su altura en metros: "))
            if altura <= 0:
                raise ValueError("La altura debe ser un valor positivo.")
            break
        except ValueError as e:
            print(f"Error: {e}. Por favor, ingrese un número válido.")

    imc = peso / (altura ** 2)
    print(f"Su IMC es: {imc:.2f}")

    # Clasificación del IMC (puede ser ampliada)
    if imc < 18.5:
        print("Clasificación: Bajo peso")
    elif 18.5 <= imc < 25:
        print("Clasificación: Peso normal")
    elif 25 <= imc < 30:
        print("Clasificación: Sobrepeso")
    else:
        print("Clasificación: Obesidad")


limpiar_pantalla()
calcular_imc()