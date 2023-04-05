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
