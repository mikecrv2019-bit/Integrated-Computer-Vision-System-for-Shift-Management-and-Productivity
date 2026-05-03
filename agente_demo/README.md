# AGENTE DE IA PARA PROCESAMIENTO DE IMÁGENES

## 📋 Información General

**Proyecto:** MAI 630 - Computer Vision  
**Institución:** Atlantis University  
**Título:** Agente de IA para Análisis y Procesamiento de Imágenes de Personas  
**Versión:** 1.0.0  
**Fecha:** 2026  
**Autor:** Estudiante MAI 630  

---

## 🎯 Descripción del Proyecto

Este proyecto implementa un **agente de inteligencia artificial** que:

✅ Carga imágenes de personas desde una carpeta de demostración  
✅ Detecta rostros usando algoritmos de visión por computadora (Haar Cascades)  
✅ Extrae información básica de las imágenes (dimensiones, aspectos de color)  
✅ Procesa imágenes (redimensionamiento, conversión a escala de grises)  
✅ Guarda resultados procesados en una carpeta de salida  
✅ Genera un reporte JSON con todos los análisis realizados  
✅ Se ejecuta desde terminal (interface CLI simple)  
✅ Es convertible a archivo ejecutable .exe para Windows  

---

## 📁 Estructura del Proyecto

```
agente_demo/
│
├── run_agent.py              # Archivo principal del agente
├── requirements.txt          # Dependencias de Python
├── README.md                 # Este archivo (documentación)
├── build_exe.bat            # Script para generar .exe en Windows
│
├── demo_images/             # Carpeta para imágenes de entrada
│   └── (coloca aquí tus imágenes JPG/PNG)
│
└── outputs/                 # Carpeta de resultados (se genera automáticamente)
    ├── faces_*.jpg          # Imágenes con rostros detectados
    ├── resized_*.jpg        # Imágenes redimensionadas
    ├── grayscale_*.jpg      # Imágenes en escala de grises
    └── analysis_report.json # Reporte JSON de análisis
```

---

## 🚀 Instalación y Configuración

### Requisitos Previos

- **Python 3.8 o superior** (descargar desde [python.org](https://www.python.org))
- **pip** (gestor de paquetes de Python)
- Una terminal (CMD, PowerShell en Windows; bash en macOS/Linux)

### Paso 1: Clonar o Descargar el Proyecto

```bash
# Descargar el proyecto y navegar a la carpeta
cd agente_demo
```

### Paso 2: Instalar Dependencias

```bash
# Instalar todas las librerías necesarias
pip install -r requirements.txt
```

**Nota:** Si encuentras problemas con `opencv-python`, intenta:
```bash
pip install --upgrade opencv-python
```

### Paso 3: Agregar Imágenes de Prueba

1. Copia imágenes de personas (JPG o PNG) a la carpeta `demo_images/`
2. Asegúrate de que las imágenes contengan rostros claros para mejor detección
3. Las imágenes pueden ser de diferentes tamaños

---

## ▶️ Ejecución del Agente

### Desde Terminal (Opción Básica)

```bash
python run_agent.py
```

### Salida Esperada

```
================================================================================
  AGENTE DE IA - ANÁLISIS DE IMÁGENES DE PERSONAS
  MAI 630 Computer Vision | Atlantis University
================================================================================

✅ Se encontraron 2 imagen(es) para procesar

📸 Analizando: persona1.jpg
--------------------------------------------------------------------------------

📊 INFORMACIÓN DE LA IMAGEN:
   • Dimensiones: 800x600 píxeles
   • Relación de aspecto: 1.33
   • Canales de color: 3
   • Tamaño de archivo: 0.125 MB
   • Espacio de color: BGR

👤 DETECCIÓN DE ROSTROS:
   • Rostros detectados: 1
   • Imagen con rostros guardada: faces_persona1.jpg

⚙️  PROCESAMIENTO:
   • Imagen redimensionada guardada: resized_persona1.jpg
   • Imagen en escala de grises guardada: grayscale_persona1.jpg
   • Nuevas dimensiones: 800x600

================================================================================
  RESUMEN FINAL
================================================================================

✅ Imágenes procesadas: 2
📁 Resultados guardados en: C:\...\agente_demo\outputs
👤 Rostros detectados en total: 2
📄 Archivos generados: 6

================================================================================
```

---

## 📊 Componentes del Agente

### Clase: `ImageProcessingAgent`

La clase principal implementa los siguientes métodos:

#### `__init__(demo_folder, output_folder)`
Inicializa el agente, crea carpetas necesarias y carga el modelo Haar Cascade.

#### `get_image_info(image_path)`
Extrae información de la imagen:
- Dimensiones (ancho × alto)
- Número de canales de color
- Relación de aspecto
- Tamaño en MB

#### `detect_faces(image_path)`
Detecta rostros usando Haar Cascades de OpenCV.
- Retorna la imagen con rectángulos dibujados
- Cuenta el número de rostros detectados

#### `process_image(image_path)`
Procesa la imagen:
1. Redimensiona a máximo 800 píxeles de ancho/alto
2. Convierte a escala de grises

#### `analyze_image(image_path)`
Método principal que orquesta todos los análisis:
1. Extrae información básica
2. Detecta rostros
3. Procesa la imagen
4. Registra los resultados

#### `save_analysis_report()`
Genera un archivo `analysis_report.json` con todos los análisis.

---

## 🔧 Tecnologías Utilizadas

| Librería | Propósito |
|----------|-----------|
| **OpenCV (cv2)** | Procesamiento de imágenes, detección de rostros |
| **NumPy** | Operaciones matemáticas en arrays |
| **Pillow** | Manipulación de imágenes |
| **JSON** | Almacenamiento de reportes |
| **Pathlib** | Manejo de rutas de archivo |

---

## 📝 Logs y Reportes

### Reporte JSON (`analysis_report.json`)

Cada ejecución genera un reporte estructurado:

```json
{
    "timestamp": "2026-04-26T14:30:45.123456",
    "total_images_processed": 2,
    "analyses": [
        {
            "timestamp": "2026-04-26T14:30:45.100000",
            "image": "persona1.jpg",
            "dimensions": "800x600",
            "faces_detected": 1,
            "files_generated": 3
        },
        {
            "timestamp": "2026-04-26T14:30:46.200000",
            "image": "persona2.jpg",
            "dimensions": "1024x768",
            "faces_detected": 2,
            "files_generated": 3
        }
    ]
}
```

---

## 🌐 Ejecución en Google Colab

### Paso 1: Crear un Notebook

1. Abre [Google Colab](https://colab.research.google.com)
2. Crea un nuevo notebook

### Paso 2: Instalar Dependencias

```python
!pip install opencv-python Pillow numpy
```

### Paso 3: Clonar o Descargar el Proyecto

```python
# Opción A: Si está en un repositorio Git
!git clone <URL_DEL_REPOSITORIO>
%cd agente_demo

# Opción B: Subir archivo ZIP manualmente
from google.colab import files
files.upload()  # Selecciona tu archivo agente_demo.zip
!unzip agente_demo.zip
%cd agente_demo
```

### Paso 4: Cargar Imágenes de Prueba

```python
# Crear carpeta si no existe
import os
os.makedirs('demo_images', exist_ok=True)

# Subir imágenes manualmente
from google.colab import files
print("Sube tus imágenes de personas:")
uploaded = files.upload()

# Mover al directorio demo_images
for filename in uploaded.keys():
    os.rename(filename, f'demo_images/{filename}')
```

### Paso 5: Ejecutar el Agente

```python
!python run_agent.py
```

### Paso 6: Descargar Resultados

```python
# Comprimir resultados
!zip -r outputs.zip outputs/

# Descargar
from google.colab import files
files.download('outputs.zip')
```

---

## 🔨 Compilación a .exe para Windows

### ⚠️ Importante
Google Colab usa **Linux**, no puede generar .exe nativo de Windows.  
**Debes ejecutar estos comandos en una PC con Windows.**

### Requisito: PyInstaller

```bash
pip install pyinstaller==6.3.0
```

### Opción 1: Script Automático (Recomendado)

Crea un archivo `build_exe.bat` en la carpeta `agente_demo/`:

```batch
@echo off
REM Compilar run_agent.py a ejecutable .exe
REM Uso: double-click en build_exe.bat o ejecutar en CMD

echo Compilando agente a ejecutable .exe...
pyinstaller --onefile --windowed --icon=icon.ico run_agent.py

echo.
echo ========================================
echo Compilacion completada!
echo El archivo .exe se encuentra en:
echo   agente_demo\dist\run_agent.exe
echo ========================================
pause
```

**Guardar este contenido como `build_exe.bat`**

### Opción 2: Comando Manual

```bash
# Abrir CMD en la carpeta agente_demo/
cd C:\ruta\a\agente_demo

# Compilar
pyinstaller --onefile --windowed --add-data "demo_images:demo_images" run_agent.py
```

### Parámetros de PyInstaller Explicados

| Parámetro | Función |
|-----------|---------|
| `--onefile` | Genera un único .exe (en lugar de múltiples archivos) |
| `--windowed` | Sin ventana de consola (oculta la terminal) |
| `--add-data` | Incluye carpetas adicionales (demo_images) |
| `--icon=icon.ico` | Añade un icono personalizado (opcional) |

### Resultado Final

Después de ejecutar PyInstaller, encontrarás:

```
agente_demo/
├── run_agent.py
├── requirements.txt
├── build_exe.bat
├── build/              # Archivos temporales
├── dist/
│   └── run_agent.exe   ← ARCHIVO EJECUTABLE (puede distribuirse)
└── run_agent.spec      # Especificación de PyInstaller
```

### Distribución del .exe

✅ El archivo `dist/run_agent.exe` puede ejecutarse en cualquier PC Windows  
✅ No requiere Python instalado  
✅ Incluye todas las dependencias necesarias  
✅ Puedes comprimir `dist/` en un ZIP para enviar  

---

## 🎬 Guion para Video Loom (2-3 minutos)

Ver archivo: **GUION_VIDEO_LOOM.md**

---

## 🐛 Solución de Problemas

### Error: `ModuleNotFoundError: No module named 'cv2'`

```bash
# Solución:
pip install --upgrade opencv-python
```

### Error: `ImportError: DLL load failed`

En Windows, puede deberse a librerías faltantes:
```bash
pip install --upgrade opencv-python-headless
```

### Las imágenes no se cargan

Verificaciones:
1. ¿Están las imágenes en la carpeta `demo_images/`?
2. ¿Son formatos válidos? (JPG, PNG, BMP, TIFF)
3. ¿Tienen permisos de lectura?

### Rostros no se detectan

- Los Haar Cascades funcionan mejor con rostros frontales
- Intenta con imágenes de mejor calidad
- Ajusta los parámetros de `detectMultiScale()` en el código

### El .exe no funciona

1. Verifica que Python está en la `PATH`
2. Ejecuta el script `.py` primero para verificar que funciona
3. Re-compila con: `pyinstaller --clean --onefile run_agent.py`

---

## 📚 Referencias Académicas

### Bibliografía
- **OpenCV Documentation:** https://docs.opencv.org
- **Haar Cascades:** Viola-Jones Object Detection Framework
- **Computer Vision:** Szeliski, R. (2010). Computer Vision: Algorithms and Applications

### Recursos
- [OpenCV Tutorials](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
- [PyInstaller Documentation](https://pyinstaller.org)
- [Google Colab Guide](https://colab.research.google.com/notebooks/welcome.ipynb)

---

## ✅ Checklist de Entrega

- [ ] Código `run_agent.py` funciona en terminal
- [ ] `requirements.txt` contiene todas las dependencias
- [ ] Carpeta `demo_images/` contiene imágenes de prueba
- [ ] Carpeta `outputs/` se crea automáticamente
- [ ] Reporte JSON se genera correctamente
- [ ] Proyecto probado en Google Colab
- [ ] `.exe` generado exitosamente en Windows
- [ ] Documentación `README.md` completa
- [ ] Video Loom grabado (2-3 minutos)
- [ ] Proyecto comprimido en ZIP para entregar

---

## 📧 Contacto y Soporte

**Institución:** Atlantis University  
**Curso:** MAI 630 - Computer Vision  
**Año:** 2026  

---

**Versión 1.0.0** | Última actualización: 2026-04-26
