#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
    VERIFICADOR DE DEPENDENCIAS - AGENTE IA
    MAI 630 Computer Vision | Atlantis University
=============================================================================
"""

import sys
import platform
import os

if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

print("\n" + "="*80)
print("  VERIFICADOR DE DEPENDENCIAS - AGENTE DE IA")
print("="*80 + "\n")

print("Python: %s" % sys.version)
print("Sistema: %s %s\n" % (platform.system(), platform.release()))

# Verificar Python version
python_version = sys.version_info
if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
    print("[ERROR] Python 3.8+ requerido. Tienes: %d.%d" % (python_version.major, python_version.minor))
    sys.exit(1)
else:
    print("[OK] Python %d.%d - Correcto" % (python_version.major, python_version.minor))

print("\n" + "-"*80)
print("VERIFICANDO DEPENDENCIAS:")
print("-"*80 + "\n")

# Dependencias necesarias
dependencies = {
    'cv2': 'OpenCV',
    'numpy': 'NumPy',
    'PIL': 'Pillow',
    'json': 'JSON (built-in)',
    'pathlib': 'Pathlib (built-in)',
}

all_ok = True

for module, name in dependencies.items():
    try:
        if module == 'PIL':
            import PIL
            print("[OK] %-20s - Instalado" % name)
        else:
            __import__(module)
            print("[OK] %-20s - Instalado" % name)
    except ImportError as e:
        print("[ERROR] %-20s - NO INSTALADO" % name)
        all_ok = False

print("\n" + "-"*80)
print("VERIFICANDO MODULOS ESPECIFICOS:")
print("-"*80 + "\n")

# Verificar OpenCV
try:
    import cv2
    print("[OK] OpenCV detectado:")
    print("   Version: %s" % cv2.__version__)
    cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
    cascade = cv2.CascadeClassifier(cascade_path)
    if cascade.empty():
        print("   [ERROR] Haar Cascade NO encontrado")
        all_ok = False
    else:
        print("   [OK] Haar Cascade detectado")
except Exception as e:
    print("[ERROR] Error con OpenCV: %s" % e)
    all_ok = False

# Verificar NumPy
try:
    import numpy as np
    print("[OK] NumPy detectado:")
    print("   Version: %s" % np.__version__)
except Exception as e:
    print("[ERROR] Error con NumPy: %s" % e)
    all_ok = False

# Verificar Pillow
try:
    from PIL import Image
    print("[OK] Pillow detectado:")
    print("   Version: Instalada")
except Exception as e:
    print("[ERROR] Error con Pillow: %s" % e)
    all_ok = False

print("\n" + "-"*80)
print("VERIFICANDO ESTRUCTURA DEL PROYECTO:")
print("-"*80 + "\n")

from pathlib import Path

project_files = {
    'run_agent.py': 'Archivo principal del agente',
    'requirements.txt': 'Dependencias del proyecto',
    'README.md': 'Documentacion',
}

for filename, description in project_files.items():
    file_path = Path(filename)
    if file_path.exists():
        size = os.path.getsize(file_path) / 1024
        print("[OK] %-25s - %s (%.1f KB)" % (filename, description, size))
    else:
        print("[ERROR] %-25s - NO ENCONTRADO" % filename)
        all_ok = False

# Verificar carpetas
folders = {
    'demo_images': 'Carpeta para imagenes de entrada',
    'outputs': 'Carpeta para resultados',
}

for folder, description in folders.items():
    folder_path = Path(folder)
    if folder_path.exists():
        file_count = len(list(folder_path.glob('*')))
        print("[OK] %-25s - %s (%d archivos)" % (folder + '/', description, file_count))
    else:
        print("[AVISO] %-25s - Sera creada automaticamente" % (folder + '/'))

print("\n" + "="*80)
if all_ok:
    print("[OK] TODAS LAS DEPENDENCIAS ESTAN INSTALADAS CORRECTAMENTE")
    print("\nPuedes ejecutar el agente con:")
    print("    python run_agent.py")
else:
    print("[ERROR] HAY PROBLEMAS CON ALGUNAS DEPENDENCIAS")
    print("\nSOLUCION:")
    print("    Instala las dependencias con:")
    print("    pip install -r requirements.txt")

print("\n" + "="*80 + "\n")

sys.exit(0 if all_ok else 1)
