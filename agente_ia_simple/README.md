# 🤖 Agente IA - Análisis de Sentimientos y Respuesta Contextual

**Proyecto Final I - MAI 630 Computer Vision**  
Atlantis University 2024-2026

---

## 📋 Contenido

1. [Objetivo del Proyecto](#objetivo)
2. [Funcionamiento del Agente](#funcionamiento)
3. [Estructura del Proyecto](#estructura)
4. [Ejecución en Google Colab](#ejecución-en-google-colab)
5. [Ejecución en Windows (Local)](#ejecución-en-windows-local)
6. [Empaquetamiento como .exe](#empaquetamiento-como-exe)
7. [Limitaciones Técnicas](#limitaciones-técnicas)
8. [Evidencia Esperada para Entrega](#evidencia-esperada)

---

## Objetivo

Desarrollar un **prototipo de agente de inteligencia artificial** que demuestre:

- ✅ **Procesamiento de entrada natural** (NLP básico)
- ✅ **Análisis de sentimientos** (positivo, negativo, neutral)
- ✅ **Generación de respuestas contextuales**
- ✅ **Almacenamiento persistente** de interacciones (CSV)
- ✅ **Generación de reportes** (HTML)
- ✅ **Empaquetamiento como ejecutable** (.exe para Windows)

Este prototipo sirve como base académica para entender:
- Pipelines de procesamiento de texto
- Máquinas de estados para conversaciones
- Logging y persistencia de datos
- Despliegue de aplicaciones Python

---

## Funcionamiento

### Arquitectura General

```
┌─────────────────────────────────────────────────────────┐
│                    ENTRADA DEL USUARIO                  │
│              (Texto en línea de comandos)               │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            ANÁLISIS DE SENTIMIENTOS                     │
│  • Tokenización simple (palabras clave)                 │
│  • Búsqueda en diccionarios (+/-)                       │
│  • Clasificación: positivo/negativo/neutral             │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│          GENERACIÓN DE RESPUESTA                        │
│  • Selección aleatoria de plantilla                     │
│  • Contextualización según sentimiento                  │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            ALMACENAMIENTO EN CSV + LOG                  │
│  • Timestamp (fecha, hora)                             │
│  • Entrada usuario + Sentimiento + Respuesta           │
│  • Archivo: logs/conversations.csv                      │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
┌─────────────────────────────────────────────────────────┐
│            SALIDA AL USUARIO                            │
│       (Terminal + HTML Report opcional)                 │
└─────────────────────────────────────────────────────────┘
```

### Flujo de Ejecución

1. **Menú Principal**: Usuario elige acción
2. **Conversación Interactiva**: Entrada → Análisis → Respuesta → Registro
3. **Visualización**: Historial de últimas 5 interacciones
4. **Reportes**: Generación de HTML con estadísticas
5. **Mantenimiento**: Limpiar historial

---

## Estructura

```
agente_ia_simple/
├── run_agent.py              # Script principal
├── requirements.txt          # Dependencias Python
├── README.md                 # Este archivo
├── build_exe_windows.md      # Instrucciones empaquetamiento
├── GUION_VIDEO.md            # Guion para video Loom
├── .gitignore                # Ignorar archivos en Git
└── logs/                      # Creado automáticamente
    ├── conversations.csv      # Historial de conversaciones
    ├── agent.log              # Log técnico
    └── reporte.html           # Reporte HTML generado
```

---

## Ejecución en Google Colab

### Ventajas
- ✅ No requiere instalación local
- ✅ Incluye todas las librerías estándar de Python
- ✅ Perfecto para pruebas y desarrollo
- ✅ Documentación clara paso a paso

### Desventajas
- ❌ **Corre en Linux** (no genera .exe)
- ❌ Los archivos se pierden al cerrar la sesión
- ❌ No tiene interfaz gráfica (solo terminal)

### Pasos en Google Colab

#### **Paso 1: Cargar el archivo en Colab**

```python
# Opción A: Subir desde tu computadora
from google.colab import files
uploaded = files.upload()  # Selecciona run_agent.py
```

Alternativa rápida: Copia y pega el contenido de `run_agent.py` en una celda:

```python
# Pega aquí el contenido completo de run_agent.py
```

#### **Paso 2: Ejecutar el agente**

```bash
!python run_agent.py
```

O con el contenido pegado directamente:

```python
# Si pegaste el código en la celda anterior, solo ejecuta:
exec(open('run_agent.py').read())
```

#### **Paso 3: Interactuar**

```
🤖 AGENTE IA - Análisis de Sentimientos y Respuesta Contextual
===============================================================

Opciones:
  1. Iniciar conversación interactiva
  2. Ver últimas 5 interacciones
  3. Generar reporte HTML
  4. Limpiar historial
  5. Salir

Selecciona una opción (1-5): 1

🎤 Iniciando conversación interactiva...
(Escribe 'salir' para terminar)

👤 Tú: Hola, me siento excelente hoy
🤖 Agente: ¡Me alegra escuchar eso! 😊 Parece que tienes un sentimiento positivo.
   Sentimiento Detectado: POSITIVO
```

#### **Paso 4: Descargar archivos (opcional)**

```python
from google.colab import files
files.download('logs/conversations.csv')
files.download('logs/reporte.html')
```

---

## Ejecución en Windows (Local)

### Requisitos

- **Python 3.8+** instalado
- **Terminal (CMD o PowerShell)**
- Archivos del proyecto

### Pasos

#### **Paso 1: Instalar dependencias**

```bash
pip install -r requirements.txt
```

*(Nota: Solo instala PyInstaller, las demás son librerías estándar)*

#### **Paso 2: Ejecutar el agente**

```bash
python run_agent.py
```

#### **Paso 3: Usar el menú**

```
🤖 AGENTE IA - Análisis de Sentimientos y Respuesta Contextual
===============================================================

Opciones:
  1. Iniciar conversación interactiva
  2. Ver últimas 5 interacciones
  3. Generar reporte HTML
  4. Limpiar historial
  5. Salir

Selecciona una opción (1-5): 1
```

#### **Paso 4: Ver archivos generados**

Los archivos se guardan automáticamente en:
```
agente_ia_simple/logs/
├── conversations.csv  (datos)
├── agent.log          (técnico)
└── reporte.html       (abre en navegador)
```

---

## Empaquetamiento como .exe

**⚠️ Importante:** Solo funciona en **Windows**. No en Colab (Linux).

Ver archivo: **[build_exe_windows.md](build_exe_windows.md)**

### Resumen rápido

```bash
# 1. Instalar PyInstaller (en Windows)
pip install pyinstaller

# 2. Empaquetar
pyinstaller --onefile --name AgenteIA run_agent.py

# 3. Ejecutable generado en:
dist/AgenteIA.exe
```

---

## Limitaciones Técnicas

### Google Colab
| Aspecto | Limitación |
|--------|-----------|
| **OS** | Linux (no Windows) |
| **Generador .exe** | ❌ Imposible (PyInstaller requiere Windows) |
| **Persistencia** | ❌ Archivos se pierden al cerrar sesión |
| **Interfaz** | Solo terminal |
| **.exe** | No genera |

**Solución:** Descargar archivos con `files.download()` y generar .exe en Windows local.

### Windows Local
| Aspecto | Ventaja |
|--------|--------|
| **Ejecución directa** | ✅ `python run_agent.py` |
| **Generación .exe** | ✅ PyInstaller funciona |
| **Persistencia** | ✅ Datos se guardan en carpeta `logs/` |
| **Portabilidad** | ✅ El .exe funciona sin Python instalado |

---

## Evidencia Esperada para Entrega

### 📁 Archivos a Entregar

```
agente_ia_simple/
├── ✅ run_agent.py              # Script ejecutable
├── ✅ requirements.txt          # Deps (solo PyInstaller)
├── ✅ README.md                 # Documentación
├── ✅ build_exe_windows.md      # Instrucciones .exe
├── ✅ GUION_VIDEO.md            # Guion Loom
├── ✅ .gitignore
├── ✅ logs/
│   ├── conversations.csv        # Historial ejemplo
│   ├── agent.log                # Log ejemplo
│   └── reporte.html             # Reporte HTML ejemplo
└── ✅ dist/
    └── AgenteIA.exe             # Ejecutable final
```

### 📹 Video Loom (2-3 minutos)

Grabar demostrando:

1. **Ejecución en Google Colab**
   - Cargar archivo
   - Ejecutar `python run_agent.py`
   - Interactuar con el agente
   - Generar reporte HTML

2. **Ejecución en Windows (local)**
   - `python run_agent.py`
   - Demostrar menú
   - Realizar conversación
   - Mostrar archivos CSV/HTML

3. **Generación del .exe**
   - `pip install pyinstaller`
   - `pyinstaller --onefile --name AgenteIA run_agent.py`
   - Ejecutar `dist/AgenteIA.exe`
   - Demostrar que funciona sin Python instalado

Ver guion detallado en: **[GUION_VIDEO.md](GUION_VIDEO.md)**

### 📊 Reporte Esperado (logs/conversations.csv)

```csv
Fecha,Hora,Entrada Usuario,Sentimiento,Respuesta Agente
2026-04-26,14:30:45,Hola me siento muy bien hoy,positivo,¡Me alegra escuchar eso! 😊
2026-04-26,14:31:12,Las cosas no van tan mal,negativo,Entiendo tu frustración. Estoy aquí...
2026-04-26,14:32:00,¿Qué hora es?,neutral,Interesante observación. ¿Podrías expandir...
```

### 🎯 Checklist de Validación

- [ ] `python run_agent.py` ejecuta sin errores
- [ ] Menú funciona (opciones 1-5)
- [ ] Análisis de sentimientos clasifica correctamente
- [ ] CSV se crea en `logs/conversations.csv`
- [ ] HTML reporte se genera correctamente
- [ ] Funciona en Google Colab
- [ ] Funciona en Windows (Python)
- [ ] `.exe` se genera con PyInstaller
- [ ] `.exe` ejecuta sin Python instalado
- [ ] Video Loom grabado (2-3 min)

---

## Tecnologías Usadas

- **Python 3.8+** — Lenguaje principal
- **csv** — Almacenamiento de datos
- **pathlib** — Gestión de rutas multiplataforma
- **datetime** — Timestamps
- **HTML5/CSS3** — Generación de reportes
- **PyInstaller** — Empaquetamiento .exe

---

## Autor

**Proyecto desarrollado para:** MAI 630 Computer Vision  
**Institución:** Atlantis University 2024-2026  
**Fecha:** 2026-04-26

---

**Preguntas frecuentes:**

> ¿Por qué no usa APIs externas?  
→ Para que funcione offline y sin credenciales. Ideal para prototipos académicos.

> ¿Por qué el análisis de sentimientos es simple?  
→ Suficiente para demostrar el concepto. Proyectos avanzados usarían NLTK/spaCy/Transformers.

> ¿Puedo modificar las respuestas?  
→ Sí, edita `RESPUESTAS_POSITIVAS`, `RESPUESTAS_NEGATIVAS`, `RESPUESTAS_NEUTRAL` en `run_agent.py`.

> ¿Qué hago si el .exe no funciona?  
→ Ver [build_exe_windows.md](build_exe_windows.md) - Troubleshooting.
