import os
import json

def cargar_configuracion():
    with open('config.json', 'r') as archivo:
        configuracion = json.load(archivo)
    return configuracion

def renombrar_archivos(carpeta, palabra):
    # Obtener la lista de archivos en la carpeta
    archivos = os.listdir(carpeta)

    # Filtrar archivos con la extensión .mobi
    archivos_mobi = [archivo for archivo in archivos if archivo.endswith('.mobi')]

    # Renombrar archivos
    for archivo in archivos_mobi:
        numero, extension = archivo.split('.')
        nuevo_nombre = f"{numero}-{palabra}.{extension}"
        ruta_antigua = os.path.join(carpeta, archivo)
        ruta_nueva = os.path.join(carpeta, nuevo_nombre)
        os.rename(ruta_antigua, ruta_nueva)
        print(f"Renombrando: {archivo} -> {nuevo_nombre}")

if __name__ == "__main__":
    configuracion = cargar_configuracion()

    # Llamar a la función para realizar el proceso
    renombrar_archivos(configuracion["carpeta_a_procesar"], configuracion["palabra_a_agregar"])
