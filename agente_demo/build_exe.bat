@echo off
REM ===========================================================================
REM    SCRIPT DE COMPILACION - AGENTE IA A EJECUTABLE .EXE
REM    MAI 630 Computer Vision | Atlantis University
REM ===========================================================================
REM
REM Este script compila el agente de IA en un archivo ejecutable .exe
REM usando PyInstaller.
REM
REM Requisitos:
REM    - Python 3.8+ instalado
REM    - PyInstaller instalado (pip install pyinstaller)
REM
REM Uso:
REM    1. Doble-click en este archivo (.bat)
REM    2. O ejecutar en CMD: build_exe.bat
REM
REM Resultado:
REM    El archivo .exe se encuentra en: dist\run_agent.exe
REM
REM ===========================================================================

echo.
echo ===============================================================================
echo    COMPILANDO AGENTE IA A EJECUTABLE .EXE
echo    MAI 630 Computer Vision
echo ===============================================================================
echo.

REM Verificar si PyInstaller está instalado
python -m pip show pyinstaller >nul 2>&1
if errorlevel 1 (
    echo [!] PyInstaller no está instalado.
    echo [*] Instalando PyInstaller...
    python -m pip install pyinstaller==6.3.0
    if errorlevel 1 (
        echo [ERROR] No se pudo instalar PyInstaller.
        echo [*] Intenta manualmente: pip install pyinstaller
        pause
        exit /b 1
    )
)

echo [OK] PyInstaller detectado.
echo.

REM Limpiar compilaciones anteriores
echo [*] Limpiando compilaciones anteriores...
if exist "build" rmdir /s /q build
if exist "dist" rmdir /s /q dist
if exist "run_agent.spec" del run_agent.spec
echo [OK] Limpieza completada.
echo.

REM Compilar con PyInstaller
echo [*] Compilando run_agent.py a ejecutable .exe...
echo.

python -m PyInstaller ^
    --onefile ^
    --windowed ^
    --name "run_agent" ^
    --add-data "demo_images;demo_images" ^
    --distpath "./dist" ^
    --workpath "./build" ^
    --specpath "./" ^
    run_agent.py

REM Verificar si la compilación fue exitosa
if errorlevel 1 (
    echo.
    echo [ERROR] La compilación falló. Por favor verifica:
    echo   1. Que Python está instalado correctamente
    echo   2. Que PyInstaller está instalado
    echo   3. Que el archivo run_agent.py existe
    echo.
    pause
    exit /b 1
)

echo.
echo ===============================================================================
echo    COMPILACION EXITOSA!
echo ===============================================================================
echo.
echo [OK] Archivo ejecutable generado: dist\run_agent.exe
echo.
echo Pasos siguientes:
echo   1. Navega a la carpeta: dist\
echo   2. Haz doble-click en: run_agent.exe
echo   3. O ejecuta desde terminal: dist\run_agent.exe
echo.
echo Distribución:
echo   - Puedes enviar el archivo dist\run_agent.exe por email
echo   - Puedes comprimirlo en ZIP: dist -> agente_demo.zip
echo   - No requiere Python instalado en la PC destino
echo.
echo Troubleshooting:
echo   - Si obtienes errores de DLL, intenta:
echo     pip install --upgrade opencv-python-headless
echo.
echo ===============================================================================
echo.

pause
