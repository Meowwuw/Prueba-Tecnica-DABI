from controller import Controlador

class Programa:
    def __init__(self):
        self.controlador = Controlador()

    def ejecutar(self):
        while True:
            print("\nMenú:")
            print("1. Mostrar lista de tareas")
            print("2. Agregar tarea")
            print("3. Marcar tarea como completada")
            print("4. Salir")
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                self.controlador.mostrar_tareas()
            elif opcion == 2:
                self.controlador.agregar_tarea()
            elif opcion == 3:
                self.controlador.marcar_completada()
            elif opcion == 4:
                break
            else:
                print("Opción no válida")

if __name__ == "__main__":
    programa = Programa()
    programa.ejecutar()
