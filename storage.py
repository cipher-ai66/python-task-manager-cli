from models import Task

FILENAME = "tareas.txt"

def cargar_tarea():
    tarea = []
    try:
        with open (FILENAME, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                status, description = line.split(" | ")
                completed = True if status == "1" else False
                tarea.append(Task(description, completed))
    except FileNotFoundError:
        print("El archivo no extiste, devolvemos la lista sin nada")
        pass

    return tarea


def guardar_tarea(tarea):
    with open (FILENAME, "w") as file:
        for tarea in tarea:
            status = "1" if tarea.completed else "0"
            file.write(f"{status} | {tarea.description} \n")



            