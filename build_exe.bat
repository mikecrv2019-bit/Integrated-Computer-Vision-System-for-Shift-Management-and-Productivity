@echo off
REM AssistantTrack 4D — Compilador a Ejecutable Windows
REM Script para generar .exe con PyInstaller

setlocal enabledelayedexpansion

echo ════════════════════════════════════════════════════════
echo   AssistantTrack 4D — Generador de Ejecutable (.exe)
echo ════════════════════════════════════════════════════════
echo.

REM Verificar que Python está instalado
python --version >nul 2>&1
if errorlevel 1 (
    echo [X] Python no está instalado o no está en el PATH
    echo Por favor instala Python desde https://www.python.org
    pause
    exit /b 1
)

echo [✓] Python detectado
echo.

REM Instalar dependencias
echo [*] Instalando dependencias...
pip install -r requirements.txt
if errorlevel 1 (
    echo [X] Error al instalar dependencias
    pause
    exit /b 1
)

echo [✓] Dependencias instaladas correctamente
echo.

REM Crear directorio de salida
if not exist "dist" mkdir dist
if not exist "build" mkdir build

echo [*] Compilando archivo ejecutable...
echo     Esto puede tomar 1-2 minutos...
echo.

REM Ejecutar PyInstaller
pyinstaller ^
    --onefile ^
    --windowed ^
    --name "AssistantTrack4D" ^
    --icon=assets/icon.ico ^
    --add-data "assets:assets" ^
    --distpath="dist" ^
    --buildpath="build" ^
    --specpath="." ^
    run_agent.py

if errorlevel 1 (
    echo.
    echo [X] Error en la compilación
    pause
    exit /b 1
)

echo.
echo ════════════════════════════════════════════════════════
echo [✓] ¡Compilación exitosa!
echo ════════════════════════════════════════════════════════
echo.
echo El ejecutable se encuentra en:
echo    dist\AssistantTrack4D.exe
echo.
echo Puedes ejecutarlo haciendo doble clic en:
echo    dist\AssistantTrack4D.exe
echo.
echo Instrucciones de distribución:
echo   1. Copia la carpeta "dist" a otra computadora
echo   2. Ejecuta AssistantTrack4D.exe
echo   3. No requiere instalación adicional
echo.
pause
