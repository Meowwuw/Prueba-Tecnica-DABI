class ListaTareas:
    def __init__(self):
        self.tareas = []

    def agregar_tarea(self, tarea):
        self.tareas.append(tarea)

    def obtener_tareas(self):
        return self.tareas

    def marcar_completada(self, index):
        self.tareas[index].completada = True

class Tarea:
    def __init__(self, descripcion):
        self.descripcion = descripcion
        self.completada = False

class Vista:
    def mostrar_tareas(self, tareas):
        print("Lista de tareas:")
        for tarea in tareas:
            estado = "Completada" if tarea.completada else "Pendiente"
            print(f"{tarea.descripcion} ({estado})")

    def agregar_tarea(self):
        descripcion = input("Ingrese la descripción de la tarea: ")
        return descripcion

    def marcar_completada(self):
        index = int(input("Ingrese el índice de la tarea que desea marcar como completada: "))
        return index

