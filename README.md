# Conversor Video a Audio y Texto

Esta aplicación convierte un archivo de video a audio y luego transcribe el audio a texto usando Whisper.

## Instalación

1. Instala las dependencias de Python:
   ```
   pip install -r requirements.txt
   ```

2. Instala FFmpeg (requerido):
   ```
   python install_dependencies.py
   ```
   
   Este script detecta tu sistema operativo e instala FFmpeg automáticamente:
   - **macOS**: Usa Homebrew
   - **Linux (Ubuntu/Debian)**: Usa apt-get
   - **Linux (Fedora/RHEL)**: Usa dnf
   - **Linux (Arch)**: Usa pacman
   - **Linux (openSUSE)**: Usa zypper

## Uso

Ejecuta el script con la ruta al archivo de video:

```
python src/main.py ruta/al/video.mp4
```

La aplicación:
- Convierte el video a audio (guarda como .wav en el mismo directorio).
- Transcribe el audio a texto.
- Imprime el texto en la consola.
- Guarda el texto en un archivo .txt con el mismo nombre base.

## Estructura del Proyecto

- `src/converter.py`: Función para extraer audio del video.
- `src/transcriber.py`: Función para transcribir audio a texto.
- `src/main.py`: Script principal.
- `install_dependencies.py`: Script para instalar FFmpeg según el SO.
- `tests/`: Para pruebas unitarias (por implementar).
- `requirements.txt`: Dependencias de Python.

## Notas

- El modelo Whisper usado es 'base'. Puedes cambiarlo en `src/transcriber.py` por 'small', 'medium', etc., para mejor precisión (pero más lento).
- FFmpeg es requerido para procesar archivos de audio.
