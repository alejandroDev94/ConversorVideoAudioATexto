#!/usr/bin/env python3
"""
Script para instalar dependencias del sistema (FFmpeg) de forma genérica
según el sistema operativo.
"""

import platform
import subprocess
import sys

def check_ffmpeg():
    """Verifica si FFmpeg está instalado."""
    try:
        subprocess.run(['ffmpeg', '-version'], capture_output=True, check=True)
        print("✓ FFmpeg ya está instalado")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def install_ffmpeg():
    """Instala FFmpeg según el sistema operativo."""
    system = platform.system()

    if check_ffmpeg():
        return True

    print("FFmpeg no está instalado. Intentando instalar...")

    try:
        if system == "Darwin":  # macOS
            print("Sistema: macOS")
            # Intenta con Homebrew primero
            try:
                subprocess.run(['brew', '--version'], capture_output=True, check=True)
                subprocess.run(['brew', 'install', 'ffmpeg'], check=True)
                print("✓ FFmpeg instalado con Homebrew")
            except (subprocess.CalledProcessError, FileNotFoundError):
                print("✗ Homebrew no está instalado")
                print("Instala Homebrew desde: https://brew.sh")
                print("O instala FFmpeg manualmente")
                return False

        elif system == "Linux":
            print("Sistema: Linux")
            # Detecta el gestor de paquetes
            distro_commands = [
                (['apt-get', 'update'], ['apt-get', 'install', '-y', 'ffmpeg']),  # Debian/Ubuntu
                (['dnf', 'install', '-y', 'ffmpeg'], None),  # Fedora/RHEL
                (['pacman', '-S', '--noconfirm', 'ffmpeg'], None),  # Arch
                (['zypper', 'install', '-y', 'ffmpeg'], None),  # openSUSE
            ]

            installed = False
            for install_cmd, update_cmd in distro_commands:
                if update_cmd:
                    try:
                        subprocess.run(update_cmd[0:2], capture_output=True, check=True)
                        subprocess.run(install_cmd, check=True)
                        print(f"✓ FFmpeg instalado")
                        installed = True
                        break
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        continue
                else:
                    try:
                        subprocess.run(install_cmd, check=True)
                        print(f"✓ FFmpeg instalado")
                        installed = True
                        break
                    except (subprocess.CalledProcessError, FileNotFoundError):
                        continue

            if not installed:
                print("✗ No se pudo instalar FFmpeg automáticamente")
                print("Intenta instalar manualmente: sudo apt-get install ffmpeg")
                return False

        elif system == "Windows":
            print("Sistema: Windows")
            print("✗ Descarga FFmpeg desde: https://ffmpeg.org/download.html")
            print("O usa: choco install ffmpeg (si tienes Chocolatey)")
            return False
        else:
            print(f"✗ Sistema operativo no reconocido: {system}")
            return False

        # Verifica que FFmpeg se instaló correctamente
        if check_ffmpeg():
            return True
        else:
            print("✗ FFmpeg se instaló pero no se puede encontrar en PATH")
            return False

    except Exception as e:
        print(f"✗ Error al instalar FFmpeg: {e}")
        return False

if __name__ == "__main__":
    if not install_ffmpeg():
        sys.exit(1)
    print("\n✓ Todas las dependencias están instaladas")
    sys.exit(0)

