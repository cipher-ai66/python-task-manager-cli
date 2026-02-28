# 📝 Task Manager CLI

Un sencillo pero funcional **gestor de tareas por línea de comandos (CLI)** escrito en Python.  
Este proyecto permite añadir, listar, editar, completar y eliminar tareas directamente desde la terminal.

Es ideal como práctica para desarrollar lógica, modularidad y manejo de archivos durante el aprendizaje de Python.

---

## 🚀 Características

- ➕ Añadir tareas
- 📋 Listar tareas
- ✔️ Marcar tareas como completadas
- ✏️ Editar descripción de una tarea
- 🗑️ Eliminar tareas
- 💾 Guardado automático de tareas en fichero `tareas.txt`
- 🔄 Carga automática de tareas al iniciar el programa

---

## 📂 Estructura del Proyecto
/main.py # Menú principal e interacción con el usuario
/models.py # Definición de la clase Task
/storage.py # Funciones de guardar y cargar tareas desde archivo
tareas.txt # Archivo donde se almacenan las tareas


---

## ▶️ Cómo Ejecutar el Proyecto

Asegúrate de tener **Python 3** instalado.

1. Clona este repositorio:

```bash
git clone https://github.com/cipher-ai66/python-task-manager-cli.git

2. Accede al directorio:
cd python-task-manager-cli

3. Ejecuta la aplicación:

python main.py

4. Uso del Menú

Al arrancar el programa verás el siguiente menú:

Task Manager Propio
1 - Añadir Tarea
2 - Ver todas las tareas
3 - Marcar tarea completada
4 - Borrar Tarea
5 - Guardar y Salir
6 - Editar tarea
Ejemplo de uso

Opción 1 → Añade una nueva tarea

Opción 2 → Muestra todas las tareas

Opción 3 → Marca una tarea como completada

Opción 4 → Elimina una tarea

Opción 6 → Edita una tarea existente

Opción 5 → Guarda todo y cierra la aplicación

Las tareas se guardan automáticamente en el archivo tareas.txt.


Tecnologías y Conceptos Usados

Python 3

Entrada y salida estándar (input, print)

Control de flujo (if, while)

Estructuras de datos (listas)

Programación orientada a objetos (clase Task)

Manejo de archivos (open, lectura y escritura)

Modularización en múltiples archivos .py

🎯 Objetivo Educativo

Este proyecto te ayuda a desarrollar:

Lógica de programación

Organización modular del código

Buenas prácticas básicas de Python

Persistencia de datos en archivo

Construcción de aplicaciones por consola

Estructuras de proyecto reales para un portafolio profesional

🛠️ Mejoras Futuras (Roadmap)

 Filtrar tareas por completadas / pendientes

 Añadir prioridades a las tareas

 Exportar tareas a JSON

 Añadir tests unitarios

 Añadir logs

 Crear interfaz gráfica (Tkinter) o versión web

 Mejorar sistema de IDs de tareas

🤝 Contribuciones

¡Las contribuciones son bienvenidas!

Puedes:

Crear issues

Enviar pull requests

Sugerir nuevas funcionalidades
