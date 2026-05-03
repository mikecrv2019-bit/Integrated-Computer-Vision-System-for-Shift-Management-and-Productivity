# INSTRUCCIONES PASO A PASO - GOOGLE COLAB Y WINDOWS

## 📌 Tabla de Contenidos

1. [Ejecución en Google Colab](#google-colab)
2. [Compilación a .exe en Windows](#windows-exe)
3. [Troubleshooting](#troubleshooting)

---

# 🌐 Google Colab

## ¿Por qué Google Colab?

✅ No requiere instalación de Python  
✅ Acceso a GPU gratis  
✅ Ambiente Linux (no genera .exe, pero sí prototipos)  
✅ Fácil compartir y colaborar  
✅ Descargar resultados directamente  

## ❌ Limitaciones en Colab

- No genera .exe nativo de Windows (usa Linux)
- Las interfaces gráficas funcionan limitadamente
- El .exe debe generarse en Windows nativo

## Paso 1: Preparar el Proyecto

### 1.1 Crear un Notebook en Colab

```python
# Abrir Google Colab
# URL: https://colab.research.google.com

# Crear nuevo notebook
# Menú: Archivo > Nuevo notebook
```

### 1.2 Descargar el Proyecto

**Opción A: Desde un repositorio Git**

```python
!git clone <URL_DEL_REPOSITORIO>
%cd agente_demo
!ls -la
```

**Opción B: Subir manualmente**

```python
from google.colab import files

print("📁 Selecciona el archivo agente_demo.zip")
uploaded = files.upload()

# Descomprimirzip
import zipfile
for filename in uploaded.keys():
    with zipfile.ZipFile(filename, 'r') as zip_ref:
        zip_ref.extractall('/content/')

# Navegar a la carpeta
import os
os.chdir('/content/agente_demo')
!pwd
```

---

## Paso 2: Instalar Dependencias

```python
# Instalar las librerías necesarias
!pip install opencv-python Pillow numpy

# Verificar instalación
import cv2
import numpy as np
from PIL import Image
print("✅ Todas las librerías instaladas correctamente")
```

---

## Paso 3: Preparar Imágenes de Prueba

### Opción A: Subir Imágenes Manualmente

```python
from google.colab import files
import os

# Crear carpeta si no existe
os.makedirs('demo_images', exist_ok=True)

print("📸 Sube tus imágenes de personas (JPG/PNG):")
uploaded = files.upload()

# Mover archivos a demo_images/
for filename in uploaded.keys():
    if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp')):
        os.rename(filename, f'demo_images/{filename}')
        print(f"✅ {filename} movido a demo_images/")
```

### Opción B: Descargar Imágenes de Internet

```python
import urllib.request
import os

os.makedirs('demo_images', exist_ok=True)

# Descargar imagen de ejemplo (persona del repositorio de OpenCV)
url = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/26/Camponotus_flavomarginatus_ant.jpg/440px-Camponotus_flavomarginatus_ant.jpg"
urllib.request.urlretrieve(url, 'demo_images/sample1.jpg')

print("✅ Imagen descargada a demo_images/")

# Verificar
!ls -la demo_images/
```

---

## Paso 4: Ejecutar el Agente

```python
# Ejecutar el agente
!python run_agent.py
```

**Salida esperada:**

```
================================================================================
  AGENTE DE IA - ANÁLISIS DE IMÁGENES DE PERSONAS
  MAI 630 Computer Vision | Atlantis University
================================================================================

✅ Se encontraron 1 imagen(es) para procesar

📸 Analizando: sample1.jpg
--------------------------------------------------------------------------------

📊 INFORMACIÓN DE LA IMAGEN:
   • Dimensiones: 440x441 píxeles
   • Relación de aspecto: 1.0
   • Canales de color: 3
   • Tamaño de archivo: 0.042 MB
   • Espacio de color: BGR

👤 DETECCIÓN DE ROSTROS:
   • Rostros detectados: 0
   • Imagen con rostros guardada: faces_sample1.jpg

⚙️  PROCESAMIENTO:
   • Imagen redimensionada guardada: resized_sample1.jpg
   • Imagen en escala de grises guardada: grayscale_sample1.jpg
   • Nuevas dimensiones: 440x441
```

---

## Paso 5: Visualizar Resultados

```python
# Listar archivos generados
!ls -la outputs/

# Ver las imágenes procesadas
from IPython.display import Image, display
import os

print("🖼️  IMÁGENES PROCESADAS:\n")
for filename in os.listdir('outputs/'):
    if filename.endswith('.jpg'):
        print(f"\n📷 {filename}")
        display(Image(f'outputs/{filename}'))

# Ver el reporte JSON
import json
with open('outputs/analysis_report.json', 'r') as f:
    report = json.load(f)
    print("\n📋 REPORTE DE ANÁLISIS:")
    print(json.dumps(report, indent=2, ensure_ascii=False))
```

---

## Paso 6: Descargar Resultados

```python
# Crear ZIP con los resultados
import shutil

# Comprimir la carpeta outputs
shutil.make_archive('agente_demo_resultados', 'zip', '.', 'outputs')

# Descargar
from google.colab import files
files.download('agente_demo_resultados.zip')

print("✅ Archivo descargado: agente_demo_resultados.zip")
```

---

## Paso 7: Descargar Proyecto Completo

```python
# Crear ZIP del proyecto completo
import shutil

shutil.make_archive('agente_demo_completo', 'zip', '../', 'agente_demo')

# Descargar
from google.colab import files
files.download('agente_demo_completo.zip')

print("✅ Proyecto completo descargado: agente_demo_completo.zip")
```

---

## Notebook Completo (Copy-Paste)

```python
# ===========================================================================
# AGENTE DE IA EN GOOGLE COLAB - NOTEBOOK COMPLETO
# MAI 630 Computer Vision
# ===========================================================================

# PASO 1: Instalar dependencias
print("📥 Instalando dependencias...")
!pip install opencv-python Pillow numpy -q

# PASO 2: Descargar proyecto (opción git)
print("📁 Descargando proyecto...")
!git clone <URL_DEL_REPOSITORIO> agente_demo 2>/dev/null || echo "Ya existe"
%cd agente_demo

# PASO 3: Preparar imágenes
import os
os.makedirs('demo_images', exist_ok=True)

# Descargar imagen de ejemplo
print("📸 Descargando imagen de ejemplo...")
!wget -q https://upload.wikimedia.org/wikipedia/commons/thumb/7/7e/Curve_25519.svg/1024px-Curve_25519.svg.png -O demo_images/sample.png || echo "Sube tus propias imágenes"

# PASO 4: Ejecutar agente
print("\n⚙️  Ejecutando agente...\n")
!python run_agent.py

# PASO 5: Mostrar resultados
import json
print("\n📋 REPORTE GENERADO:")
with open('outputs/analysis_report.json', 'r') as f:
    print(json.dumps(json.load(f), indent=2, ensure_ascii=False))

# PASO 6: Descargar resultados
from google.colab import files
import shutil

shutil.make_archive('agente_demo_resultados', 'zip', '.', 'outputs')
print("\n📥 Descargando resultados...")
files.download('agente_demo_resultados.zip')

print("\n✅ COMPLETADO!")
```

---

# 🪟 Windows - Compilación a .exe

## ¿Por qué compilar a .exe?

✅ Ejecutable independiente (sin Python)  
✅ Distribución simple a otros usuarios  
✅ Aspecto profesional  
✅ Puede usarse en cualquier PC Windows  

## ⚠️ Requisitos

- **PC con Windows** (Windows 7, 10, 11)
- **Python 3.8+** instalado (https://www.python.org)
- **PyInstaller** instalado
- **El proyecto funciona** en terminal (python run_agent.py)

---

## Paso 1: Verificar Python

```bash
# Abrir CMD o PowerShell
python --version

# Debería mostrar Python 3.8 o superior
# Ejemplo: Python 3.11.7
```

**Si Python no se reconoce:**
1. Reinstalar Python desde https://www.python.org
2. ✅ Marcar: "Add Python to PATH"
3. Reiniciar la terminal

---

## Paso 2: Navegar a la Carpeta del Proyecto

```bash
# Abrir CMD en la carpeta agente_demo
# Opción A: Usar cd
cd C:\ruta\a\agente_demo

# Opción B: Shift + Right-click en la carpeta > "Open PowerShell here"
```

---

## Paso 3: Instalar PyInstaller

```bash
pip install pyinstaller==6.3.0
```

**Verificar instalación:**
```bash
pyinstaller --version
# Debería mostrar: 6.3.0
```

---

## Paso 4: Opción A - Usar Script Automático (Recomendado)

```bash
# El archivo build_exe.bat está incluido en el proyecto
# Simplemente doble-click o ejecutar:

build_exe.bat
```

**¿Qué hace el script?**
- Verifica PyInstaller
- Limpia compilaciones anteriores
- Compila run_agent.py a .exe
- Muestra el resultado en dist/run_agent.exe

---

## Paso 4: Opción B - Comando Manual

```bash
# Compilar a un único archivo .exe
pyinstaller --onefile --windowed ^
    --name "run_agent" ^
    --add-data "demo_images;demo_images" ^
    --distpath "./dist" ^
    --workpath "./build" ^
    run_agent.py
```

**Nota:** En PowerShell, usa backtick (`) al final de línea:
```powershell
pyinstaller --onefile --windowed `
    --name "run_agent" `
    --add-data "demo_images;demo_images" `
    --distpath "./dist" `
    --workpath "./build" `
    run_agent.py
```

---

## Paso 5: Verificar el Resultado

```bash
# Navegar a la carpeta dist
cd dist

# Verificar que existe run_agent.exe
dir

# Ejecutar el .exe (requiere imágenes en demo_images/)
run_agent.exe
```

---

## Paso 6: Distribuir el .exe

### Opción A: Archivo Individual

```
Copiar: dist/run_agent.exe
Enviar por email o USB
```

### Opción B: Carpeta Completa

```bash
# Copiar toda la carpeta dist/ con:
# - run_agent.exe
# - demo_images/ (con imágenes)
# - Se puede ejecutar desde cualquier lado
```

### Opción C: Archivo ZIP

```bash
# Crear ZIP de distribución
powershell -Command "Compress-Archive -Path dist -DestinationPath agente_demo_windows.zip"

# O usando 7-Zip, WinRAR, etc.
```

---

## Paso 7: Instalación en Otra PC

```bash
# En la PC destino:
# 1. Descargar agente_demo_windows.zip
# 2. Descomprimir
# 3. Navegar a: agente_demo/dist/
# 4. Doble-click en run_agent.exe
# 5. ✅ Funciona sin Python instalado
```

---

# Troubleshooting

## Google Colab

### Error: ModuleNotFoundError: No module named 'cv2'

```python
!pip install --upgrade opencv-python
```

### Error: Namespace 'cv' has no attribute

```python
# Desinstalar y reinstalar
!pip uninstall opencv-python -y
!pip install opencv-python
```

### Las imágenes no aparecen

```python
# Verificar que están en demo_images/
import os
print(os.listdir('demo_images'))

# Si está vacío, subirlas manualmente
from google.colab import files
files.upload()
```

### Error de memoria

```python
# Colab a veces limita la memoria
# Solución: Procesar imágenes más pequeñas
# O reiniciar el runtime: Runtime > Restart runtime
```

---

## Windows

### Error: PyInstaller no reconocido

```bash
# Solución: Instalar nuevamente
pip install --upgrade pyinstaller

# O usar la ruta completa
python -m PyInstaller --version
```

### Error: DLL not found

```bash
# Solución: Reinstalar OpenCV
pip uninstall opencv-python -y
pip install opencv-python
```

### El .exe no se abre

```bash
# Ejecutar desde terminal para ver el error
cd dist
run_agent.exe
```

### Error: "demo_images" no encontrado

```bash
# El .exe necesita una carpeta demo_images/ cerca
# Estructura correcta:
agente_demo/
├── run_agent.exe
├── demo_images/
│   └── (imágenes aquí)
└── outputs/
```

### PyInstaller genera un .exe pero no funciona

```bash
# Limpiar y recompilar
rmdir /s build dist *.spec
pyinstaller --onefile --windowed run_agent.py

# Si aún falla, probar con OpenCV headless
pip install opencv-python-headless
```

---

## Error General: Traceback

Si ves un error tipo:

```
Traceback (most recent call last):
  File "run_agent.py", line ...
  ...
```

**Soluciones:**
1. Verificar que Python está instalado: `python --version`
2. Verificar que las dependencias están instaladas: `pip list`
3. Reinstalar las dependencias: `pip install -r requirements.txt`
4. Verificar que hay imágenes en `demo_images/`

---

## Contacto y Soporte

Si encuentras problemas:
1. Verifica todos los pasos de este documento
2. Revisa los logs de error completos
3. Contacta al profesor del curso MAI 630
4. Consulta la documentación de OpenCV y PyInstaller

---

**Versión 1.0** | 2026 | MAI 630 Computer Vision
