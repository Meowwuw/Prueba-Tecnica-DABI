from model import ListaTareas, Tarea
from view import Vista

class Controlador:
    def __init__(self):
        self.modelo = ListaTareas()
        self.vista = Vista()

    def agregar_tarea(self):
        descripcion = self.vista.agregar_tarea()
        tarea = Tarea(descripcion)
        self.modelo.agregar_tarea(tarea)

    def mostrar_tareas(self):
        tareas = self.modelo.obtener_tareas()
        self.vista.mostrar_tareas(tareas)

    def marcar_completada(self):
        index = self.vista.marcar_completada()
        self.modelo.marcar_completada(index)
