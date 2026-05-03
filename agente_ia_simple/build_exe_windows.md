# 📦 Guía: Generar Ejecutable .exe en Windows

**MAI 630 Computer Vision - Atlantis University**

---

## 📋 Tabla de Contenidos

1. [Requisitos](#requisitos)
2. [Opción A: Método Manual (Recomendado)](#opción-a-método-manual-recomendado)
3. [Opción B: Script Automatizado](#opción-b-script-automatizado)
4. [Verificación del .exe](#verificación-del-exe)
5. [Troubleshooting](#troubleshooting)

---

## Requisitos

### ✅ Verificar que tienes:

1. **Windows 10/11**
2. **Python 3.8+** instalado y en PATH
3. **Archivos del proyecto:**
   ```
   agente_ia_simple/
   ├── run_agent.py
   └── requirements.txt
   ```

### Verificar Python instalado:

Abre **CMD o PowerShell** y ejecuta:

```bash
python --version
# Esperado: Python 3.8.x o superior
```

Si no funciona, reinstala Python desde [python.org](https://www.python.org/downloads/) ✅ Marca "Add Python to PATH"

---

## Opción A: Método Manual (Recomendado)

### Paso 1: Abre Terminal en la carpeta del proyecto

**En Windows Explorer:**
1. Navega a `agente_ia_simple/`
2. Haz clic en la barra de dirección
3. Escribe `cmd` y presiona Enter

**O manualmente:**
```bash
cd "C:\ruta\a\agente_ia_simple"
```

### Paso 2: Instala PyInstaller

```bash
pip install pyinstaller
```

**Salida esperada:**
```
Successfully installed pyinstaller-6.8.1
```

### Paso 3: Genera el ejecutable

```bash
pyinstaller --onefile --name AgenteIA run_agent.py
```

**Parámetros explicados:**
| Parámetro | Función |
|-----------|---------|
| `--onefile` | Empaqueta todo en UN solo .exe |
| `--name AgenteIA` | Nombre del ejecutable (sin espacios) |
| `run_agent.py` | Script a empaquetar |

### Paso 4: Verifica el resultado

Después de ~1-2 minutos, verás:

```
✓ building 'AgenteIA' completed successfully.
```

El ejecutable está en:
```
agente_ia_simple/dist/AgenteIA.exe
```

---

## Opción B: Script Automatizado

Si prefieres automatizar todo, crea este archivo:

### Archivo: `build_exe.bat`

```batch
@echo off
REM Script automatizado para generar AgenteIA.exe
REM Windows Batch Script

echo.
echo ============================================
echo Generador de Ejecutable - Agente IA
echo MAI 630 Computer Vision
echo ============================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no encontrado en PATH
    echo Instala Python desde https://www.python.org
    pause
    exit /b 1
)

echo ✓ Python detectado
echo.

REM Instalar PyInstaller
echo [1/3] Instalando PyInstaller...
pip install pyinstaller --quiet
if errorlevel 1 (
    echo ERROR: No se pudo instalar PyInstaller
    pause
    exit /b 1
)
echo ✓ PyInstaller instalado
echo.

REM Generar ejecutable
echo [2/3] Generando ejecutable...
pyinstaller --onefile --name AgenteIA run_agent.py
if errorlevel 1 (
    echo ERROR: PyInstaller falló
    pause
    exit /b 1
)
echo ✓ Ejecutable generado
echo.

REM Copiar archivos necesarios
echo [3/3] Finalizando...
if exist "dist\AgenteIA.exe" (
    echo.
    echo ============================================
    echo ✓ ÉXITO: AgenteIA.exe creado
    echo ============================================
    echo.
    echo Ubicación: %cd%\dist\AgenteIA.exe
    echo.
    echo Instrucciones siguientes:
    echo  1. Abre la carpeta 'dist'
    echo  2. Haz doble clic en 'AgenteIA.exe'
    echo  3. El agente se ejecutará sin necesidad de Python
    echo.
    pause
) else (
    echo ERROR: AgenteIA.exe no se creó
    pause
    exit /b 1
)
```

### Uso del script:

1. Copia el contenido anterior en un archivo `build_exe.bat`
2. Guarda en la carpeta `agente_ia_simple/`
3. Haz doble clic en `build_exe.bat`
4. Espera a que termine

---

## Verificación del .exe

### Test 1: ¿Existe el archivo?

```bash
cd agente_ia_simple/dist
dir AgenteIA.exe
```

Deberías ver algo como:
```
26/04/2026  14:35    5,234,567  AgenteIA.exe
```

### Test 2: ¿Funciona?

Opción A (Desde explorador):
1. Abre `agente_ia_simple/dist/`
2. Haz doble clic en `AgenteIA.exe`
3. Debería abrir una terminal

Opción B (Desde CMD):
```bash
cd agente_ia_simple/dist
AgenteIA.exe
```

### Test 3: Prueba de funcionalidad

Una vez abierto el .exe:
```
🤖 AGENTE IA - Análisis de Sentimientos
========================================

Opciones:
  1. Iniciar conversación interactiva
  2. Ver últimas 5 interacciones
  ...

Selecciona una opción (1-5): 1
```

Escribe algo:
```
👤 Tú: Hola! Me siento muy bien
🤖 Agente: ¡Me alegra escuchar eso! 😊
```

✅ Si ves esto, **¡el .exe funciona correctamente!**

---

## Troubleshooting

### ❌ Error: "Python no encontrado"

**Causa:** Python no está en PATH

**Solución:**
1. Desinstala Python
2. Reinstala desde https://www.python.org
3. ✅ **Marca "Add Python to PATH" durante instalación**
4. Reinicia la computadora
5. Intenta de nuevo

### ❌ Error: "pyinstaller no reconocido"

```
'pyinstaller' is not recognized as an internal or external command
```

**Causa:** PyInstaller no instalado globalmente

**Solución:**
```bash
pip install --upgrade pip
pip install pyinstaller
```

### ❌ Error: "ModuleNotFoundError"

```
ModuleNotFoundError: No module named 'xxx'
```

**Causa:** Una librería importada no está disponible

**Solución:**
```bash
pip install -r requirements.txt
```

Luego intenta generar el .exe de nuevo.

### ❌ El .exe se abre y cierra al instante

**Causa:** Probablemente un error en tiempo de ejecución

**Solución:**
1. Ejecuta desde CMD para ver el error:
   ```bash
   cd agente_ia_simple/dist
   AgenteIA.exe
   ```
2. Lee el mensaje de error
3. Corrige en `run_agent.py`
4. Regenera el .exe

### ❌ El .exe es demasiado grande

```
5 MB es normal para --onefile
```

Si supera 100 MB:
- Verifica que no haya archivos grandes en la carpeta
- Usa `--onedir` (menos portátil pero más pequeño):
  ```bash
  pyinstaller --onedir --name AgenteIA run_agent.py
  ```

### ⚠️ Antivirus bloquea el .exe

**Causa:** PyInstaller a veces genera falsos positivos

**Soluciones:**
1. Agrega a excepciones del antivirus
2. O genera en modo "onedir":
   ```bash
   pyinstaller --onedir --name AgenteIA run_agent.py
   ```

---

## Estructura Final

Después de ejecutar `build_exe.bat` o el comando manual:

```
agente_ia_simple/
├── run_agent.py
├── requirements.txt
├── README.md
├── build_exe.bat                ← Script automatizado
├── build.spec                   ← Metadata (generado)
├── dist/
│   └── AgenteIA.exe            ← 🎉 EJECUTABLE FINAL
├── build/                       ← Temporal (puede eliminarse)
└── logs/
    └── conversations.csv        ← Datos generados
```

---

## Distribución

### ¿Cómo compartir el .exe?

```
Para compartir con otros:

1. Copia solo: dist/AgenteIA.exe
2. Envía por email/USB/Drive
3. El receptor hace doble clic
4. ¡Funciona sin Python instalado!
```

### ZIP para entregar:

```bash
# Crear ZIP con todo necesario
powershell -Command "Compress-Archive -Path 'agente_ia_simple' -DestinationPath 'AgenteIA.zip'"
```

Resultado: `AgenteIA.zip` listo para enviar

---

## Parámetros Avanzados de PyInstaller

Si necesitas opciones adicionales:

```bash
# Icono personalizado (requiere .ico)
pyinstaller --onefile --icon=icon.ico --name AgenteIA run_agent.py

# Sin ventana de consola (oculta CMD en background)
pyinstaller --onefile --windowed --name AgenteIA run_agent.py

# Versión del archivo
pyinstaller --onefile --version-file=version.txt --name AgenteIA run_agent.py
```

Ver documentación: https://pyinstaller.org/en/stable/

---

## Resumen Rápido

```bash
# 1. Abre CMD en la carpeta agente_ia_simple/
cd "C:\ruta\al\agente_ia_simple"

# 2. Instala PyInstaller
pip install pyinstaller

# 3. Genera ejecutable
pyinstaller --onefile --name AgenteIA run_agent.py

# 4. Prueba
dist\AgenteIA.exe

# 5. ¡Listo para compartir!
```

---

## Preguntas Frecuentes

**¿El .exe funciona sin Python?**  
✅ Sí, PyInstaller incluye todo lo necesario.

**¿Puedo modificar el script y regenerar?**  
✅ Sí, haz cambios en `run_agent.py` y ejecuta PyInstaller de nuevo.

**¿Se puede ocultar el código?**  
⚠️ No completamente, pero PyInstaller ofusca.

**¿Es seguro ejecutar en otra computadora?**  
✅ Sí, es un ejecutable compilado estándar de Windows.

---

**Próximos pasos:** Ver [GUION_VIDEO.md](GUION_VIDEO.md) para grabar video de demostración.
