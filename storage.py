from models import Task

FILENAME = "tareas.txt"

def cargar_tarea():
    tarea = []
    try:
        with open(FILENAME, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                parts = line.split(" | ", 1)
                if len(parts) != 2:
                    print(f"Línea inválida ignorada: {line}")
                    continue

                status, description = parts
                completed = True if status == "1" else False
                tarea.append(Task(description, completed))
    except FileNotFoundError:
        print("El archivo no extiste, devolvemos la lista sin nada")
    except OSError as error:
        print(f"No se pudo leer el archivo de tareas: {error}")

    return tarea


def guardar_tarea(tarea):
    try:
        with open(FILENAME, "w", encoding="utf-8") as file:
            for item in tarea:
                status = "1" if item.completed else "0"
                file.write(f"{status} | {item.description}\n")
    except OSError as error:
        print(f"No se pudo guardar el archivo de tareas: {error}")



            
