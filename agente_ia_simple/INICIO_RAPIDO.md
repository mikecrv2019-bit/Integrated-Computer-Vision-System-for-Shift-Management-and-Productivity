# 🚀 Inicio Rápido - Agente IA

**Para los impacientes que quieren ver funcionar el agente en 2 minutos**

---

## Windows (Recomendado)

### 1️⃣ Abre Terminal en esta carpeta

```bash
# Si estás en el explorador, escribe cmd en la dirección
# Si no, abre CMD y navega a:
cd "ruta\a\agente_ia_simple"
```

### 2️⃣ Ejecuta el agente

```bash
python run_agent.py
```

### 3️⃣ Prueba

```
Selecciona opción: 1
👤 Tú: Hola! Me siento muy bien
👤 Tú: Esto es terrible
👤 Tú: salir
```

✅ **¡Listo!** Los datos se guardaron en `logs/conversations.csv`

---

## Google Colab (Sin instalación local)

### 1️⃣ Abre un Notebook

https://colab.research.google.com → `+ New Notebook`

### 2️⃣ Pega este código en la primera celda

```python
# Copia todo el contenido de run_agent.py aquí
# O sube el archivo con: from google.colab import files; uploaded = files.upload()
```

### 3️⃣ Ejecuta

```python
!python run_agent.py  # Si subiste el archivo
# o
exec(open('run_agent.py').read())  # Si pegaste el código
```

✅ **¡Listo!** Funciona en Linux también

---

## Generar .exe (Windows)

```bash
# 1. Instala PyInstaller
pip install pyinstaller

# 2. Genera el ejecutable
pyinstaller --onefile --name AgenteIA run_agent.py

# 3. Usa el .exe
dist/AgenteIA.exe
```

El .exe está en `dist/AgenteIA.exe` y **funciona sin Python instalado**.

---

## Archivos Generados

Después de usar el agente, encontrarás:

```
logs/
├── conversations.csv    ← Datos de conversaciones
├── agent.log           ← Registro técnico
└── reporte.html        ← Abre en navegador (bonito)
```

---

## Próximos pasos

1. 📖 Lee `README.md` para documentación completa
2. 📦 Ve `build_exe_windows.md` para empaquetamiento detallado
3. 🎬 Ve `GUION_VIDEO.md` para grabar el video Loom
4. ✅ Completa `CHECKLIST_ENTREGA.md` antes de enviar

---

## Problemas?

| Problema | Solución |
|----------|----------|
| "python not found" | Instala Python desde python.org ✅ marca "Add to PATH" |
| "ModuleNotFoundError" | Ejecuta: `pip install -r requirements.txt` |
| El .exe no se genera | Instala PyInstaller: `pip install pyinstaller` |
| El agente se cierra rápido | Ejecuta desde CMD (no haz doble clic) |

---

**¿Listo? Comienza con `python run_agent.py`** 🚀
