import re
import sys
import os

def limpiar_srt(archivo_srt, archivo_salida):
    with open(archivo_srt, 'r', encoding='utf-8') as archivo:
        contenido = archivo.read()

    # Eliminar líneas que contienen solo números (los índices)
    contenido = re.sub(r'\n\d+\n', '\n', contenido)
    
    # Eliminar líneas que contienen los tiempos de los subtítulos
    contenido = re.sub(r'\d{1,2}:\d{2}:\d{2},\d{3} --> \d{1,2}:\d{2}:\d{2},\d{3}', '', contenido)
    contenido = re.sub(r'\d{1,2}:\d{2} --> \d{1,2}:\d{2}', '', contenido)
    
    # Eliminar cualquier línea vacía residual
    contenido = re.sub(r'\n\s*\n', '\n', contenido).strip()
    
    # Eliminar números residuales al principio de las líneas
    contenido = re.sub(r'^\d+', '', contenido, flags=re.MULTILINE).strip()

    with open(archivo_salida, 'w', encoding='utf-8') as archivo:
        archivo.write(contenido)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python limpiar_subtitulos.py nombrearchivoentrada.srt")
        sys.exit(1)

    archivo_entrada = sys.argv[1]
    nombre_salida = os.path.splitext(os.path.basename(archivo_entrada))[0]
    archivo_salida = f'output_{nombre_salida}.txt'

    limpiar_srt(archivo_entrada, archivo_salida)
    print(f"Archivo limpio guardado como {archivo_salida}")
