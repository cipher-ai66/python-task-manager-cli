from storage import cargar_tarea, guardar_tarea
from models import Task

def menu_opciones():
    print("\n Task Manager Propio")
    print(" 1 - Añadir Tarea")
    print(" 2 - Ver todas las tareas")
    print(" 3 - Marcar tarea completada")
    print(" 4 - Borrar Tarea")
    print(" 5 - Guardar y Salir")


def anadir_tarea(tarea):
    description = input("Introduce la información de la tarea a completar: ").strip()
    if not description:
        print("La tarea no puede estar vacía.")
        return
    tarea.append(Task(description))
    print("Tarea añadida")

def listar_tarea(tarea):
    if not tarea:
        print("Lista vacía, no existen tareas")
        return

    print("\nLista de tareas: ")
    for index, item in enumerate(tarea):
        print(f"{index + 1}. {item}")


def tarea_completada(tarea):
    if not tarea:
        print("No hay tareas a completar o están todas completadas.")
        return
    
    listar_tarea(tarea)

    try:
        eleccion = int(input("Elige la tarea con el número correspondiente a completar: "))
        if 1 <= eleccion <= len(tarea):
            tarea[eleccion - 1].completed = True
        else:
            print("Número inválido")
    except ValueError:
        print("Debes introducir un número")

def eliminar_tarea(tarea):
    if not tarea:
        print("No hay tareas.")
        return
    
    
    listar_tarea(tarea)

    try:
        eliminar = int(input("¿Qué tarea quieres eliminar? elige el número de la lista: "))

        if 1 <= eliminar <= len(tarea):
            tarea_borrada = tarea.pop(eliminar - 1)
            
            print(f"La tarea {tarea_borrada} a sido borrada")
        else:
            print("Ese número no existe en la lista.")
    except ValueError:
        print("Error: Debes introducir un número válido.")


def menu():

    tareas = cargar_tarea()

    while True:
        menu_opciones()
        opciones = input("Elige una opción: ")

        if opciones == "1":
            anadir_tarea(tareas)
        elif opciones == "2":
            listar_tarea(tareas)
        elif opciones == "3":
            tarea_completada(tareas)
        elif opciones == "4":
            eliminar_tarea(tareas)
        elif opciones == "5":
            guardar_tarea(tareas)
            print("Saliendo de la aplicación")
            break
        else:
            print("No has introducido un valor correcto.")
if __name__ == "__main__":
    menu()
        
