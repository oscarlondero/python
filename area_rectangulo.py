import os


def area_rectangulo():
  while True:
    try:
      base = float(input("Ingrese la base del rectángulo: "))
      altura = float(input("Ingrese la altura del rectángulo: "))
      if base <= 0 or altura <= 0:
        print("Error: La base y la altura deben ser valores positivos.")
      else:
        break
    except ValueError:
      print("Error: Ingrese valores numéricos válidos.")
  return base * altura

def limpiar_pantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')


limpiar_pantalla()
area = area_rectangulo()
print(f"El área del rectángulo es: {area}")