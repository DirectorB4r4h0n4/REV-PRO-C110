import random

class Dados:
    def tirar_dado(self):
        respuesta = "y"

        while respuesta == "y":
            # Generar un número aleatorio entre 1 y 6 para simular el lanzamiento de un dado
            resultado = random.randint(1, 6)

            # Imprimir la representación visual del dado según el resultado obtenido
            if resultado == 1:
                print("  _____\n |     |\n |  *  |\n |     |\n  ‾‾‾‾‾")
            elif resultado == 2:
                print("  _____\n |*    |\n |     |\n |    *|\n  ‾‾‾‾‾")
            elif resultado == 3:
                print("  _____\n |*    |\n |  *  |\n |    *|\n  ‾‾‾‾‾")
            elif resultado == 4:
                print("  _____\n |*   *|\n |     |\n |*   *|\n  ‾‾‾‾‾")
            elif resultado == 5:
                print("  _____\n |*   *|\n |  *  |\n |*   *|\n  ‾‾‾‾‾")
            elif resultado == 6:
                print("  _____\n |*   *|\n |*   *|\n |*   *|\n  ‾‾‾‾‾")

            # Preguntar al usuario si desea tirar el dado nuevamente
            respuesta = input("¿Quieres tirar el dado nuevamente? (y/n): ").lower()

            # Salir del bucle si la respuesta es "n"
            if respuesta != "y":
                print("¡Hasta luego!")

# Crear un objeto de la clase Dados
juego_de_dados = Dados()

# Llamar al método tirar_dado para iniciar el juego
juego_de_dados.tirar_dado()
