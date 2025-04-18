import os
def calcular_area_cuadrado():
    """Calcula el área de un cuadrado, validando la entrada del usuario."""

    while True:
        try:
            lado = float(input("Ingresa la longitud del lado del cuadrado: "))
            if lado <= 0:
                print("Error: La longitud del lado debe ser un número positivo.")
            else:
                break  # Salir del bucle si la entrada es válida
        except ValueError:
            print("Error: Ingresa un número válido para la longitud del lado.")

    area = lado * lado
    print(f"El área del cuadrado con lado {lado} es: {area}")

# Función para preguntar si se desea calcular otra área
def preguntar_otra_vez():
    """Pregunta al usuario si desea calcular el área de otro cuadrado."""

    while True:
        respuesta = input("¿Deseas calcular el área de otro cuadrado? (sí/no): ").lower()
        if respuesta == "sí" or respuesta == "si":
            return True
        elif respuesta == "no":
            return False
        else:
            print("Error: Por favor, ingresa 'sí' o 'no'.")

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')



# Programa principal
while True:
    
    limpiar_pantalla()
    calcular_area_cuadrado()
    if not preguntar_otra_vez():
        break  # Salir del bucle principal si el usuario no quiere continuar

print("¡Programa finalizado!")