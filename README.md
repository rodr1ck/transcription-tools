# Proyecto de Transcripción y Sincronización

Este proyecto contiene scripts en Python para transcribir audios y sincronizar los subtítulos.

## Estructura del Proyecto

- **audio1.mp3** y **audio2.mp3**: Archivos de audio de entrada.
- **audio1.srt** y **audio2.srt**: Archivos de subtítulos de entrada.
- **output_audio1.txt** y **output_audio2.txt**: Archivos de salida de la transcripción.
- **limpiar_subtitulos.py**: Script para limpiar archivos `.srt` y retener solo el texto.
- **transcribir_y_sincronizar_audio1.py** y **transcribir_y_sincronizar_audio2.py**: Scripts para transcribir y sincronizar audio.
- **verificar_torch.py**: Script para verificar la instalación de `torch`.

## Requisitos

##Creación de un Nuevo Entorno Virtual en Windows 11
##Abre PowerShell o Command Prompt.
#Navega a tu directorio de trabajo del proyecto.
#Crea un nuevo entorno virtual ejecutando:
```sh
python -m venv nombre_del_entorno

##Activa el entorno virtual:

#En PowerShell:
```sh
.\nombre_del_entorno\Scripts\Activate

## Instalar las dependencias utilizando el siguiente comando:
```sh
pip install -r requirements.txt

## Uso
# Para ejecutar los scripts, utilizar los siguientes comandos:
```sh
python transcribir_y_sincronizar_audio1.py
python transcribir_y_sincronizar_audio2.py
