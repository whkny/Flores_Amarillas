import eel
import os

# Obtiene la ruta del directorio actual
current_directory = os.getcwd()

# Inicializa Eel con la carpeta actual
eel.init(current_directory)

# Opcional: Exponer funciones de Python para llamarlas desde JavaScript
@eel.expose
def python_function():
    print("¡Función de Python ejecutada!")

# Ejecuta el archivo HTML
eel.start('index.html')  
