# 🎬 Guion Video Loom - Agente IA (2-3 minutos)

**MAI 630 Computer Vision - Atlantis University**

---

## 📋 Estructura del Video

```
Total: 2:45 minutos
├── Intro (0:00 - 0:15)           15 seg
├── Demo Colab (0:15 - 1:15)      60 seg
├── Demo Windows (1:15 - 1:45)    30 seg
├── Generación .exe (1:45 - 2:30) 45 seg
└── Conclusión (2:30 - 2:45)      15 seg
```

---

## 🎯 Antes de Grabar

### ✅ Preparación Técnica

- [ ] Abre Loom (https://www.loom.com)
- [ ] Elige "Start Recording"
- [ ] Selecciona tu pantalla completa
- [ ] Ten **2 ventanas abiertas:**
  1. Google Colab (en navegador)
  2. Terminal/CMD con carpeta `agente_ia_simple`
- [ ] Prueba el micrófono
- [ ] Cierra notificaciones y distracciones

### ✅ Archivos Listos

```
✓ run_agent.py  (en Colab)
✓ requirements.txt
✓ Carpeta agente_ia_simple/ (local)
```

---

## 🎬 GUION DETALLADO

### **[00:00-00:15] INTRO**

**Narración:**
```
"Hola, soy [Tu Nombre] de MAI 630 Computer Vision.
Presento el Agente IA, un prototipo que analiza 
sentimientos y genera respuestas contextuales.

Voy a mostrar:
1. Ejecución en Google Colab
2. Prueba en Windows
3. Generación del ejecutable .exe"
```

**Acciones en pantalla:**
- [ ] Muestra pantalla del escritorio
- [ ] Abre navegador con proyecto

---

### **[00:15-01:15] DEMO GOOGLE COLAB (60 seg)**

#### **Sección A: Setup en Colab [00:15-00:35]**

**Narración:**
```
"Primero, voy a demostrar el agente en Google Colab.
Colab utiliza Linux y Python 3, perfecto para pruebas.
No requiere instalación local."
```

**Acciones:**
- [ ] Abre https://colab.research.google.com
- [ ] Crea nuevo notebook (`+ New notebook`)
- [ ] En primera celda, pega el código:
  ```python
  # Copia aquí el contenido de run_agent.py
  # (o sube el archivo)
  ```
- [ ] Ejecuta celda (Ctrl+Enter)
- [ ] Muestra que "logs/" se crea automáticamente

**Duración:** ~20 seg

---

#### **Sección B: Usar el Agente [00:35-00:55]**

**Narración:**
```
"Ahora interactúo con el agente. Escribo un 
mensaje positivo para demostrar análisis de 
sentimientos en tiempo real."
```

**Acciones:**
- [ ] Elige opción **1** (Conversación interactiva)
- [ ] **Entrada 1** (POSITIVA):
  ```
  Usuario: ¡Hola! Me siento excelente hoy, 
  tengo un sentimiento muy positivo
  ```
- [ ] Pausa de 2-3 seg
- [ ] Muestra respuesta del agente:
  ```
  Agente: ¡Me alegra escuchar eso! 😊 Parece que 
  tienes un sentimiento positivo.
  Sentimiento Detectado: POSITIVO
  ```
- [ ] **Entrada 2** (NEGATIVA):
  ```
  Usuario: La verdad me siento terrible y enojado 
  con la situación actual
  ```
- [ ] Muestra respuesta negativa:
  ```
  Agente: Detecté un sentimiento negativo. 
  ¿En qué puedo ayudarte? 😔
  Sentimiento Detectado: NEGATIVO
  ```
- [ ] **Entrada 3** (NEUTRAL):
  ```
  Usuario: ¿Qué hora es ahora?
  ```
- [ ] Muestra respuesta neutral
- [ ] Escribe **"salir"** para cerrar

**Duración:** ~20 seg

---

#### **Sección C: Generar Reporte [00:55-01:15]**

**Narración:**
```
"Perfecto. Ahora voy a generar un reporte HTML
que muestra las estadísticas de todas las 
interacciones. Opción 3 del menú."
```

**Acciones:**
- [ ] Vuelve al menú (debería mostrar automáticamente)
- [ ] Elige opción **3** (Generar reporte HTML)
- [ ] Muestra mensaje:
  ```
  ✅ Reporte HTML generado: logs/reporte.html
  ```
- [ ] Descarga el reporte:
  ```python
  from google.colab import files
  files.download('logs/reporte.html')
  ```
- [ ] Muestra que se descargó correctamente

**Narración:**
```
"El reporte incluye estadísticas de sentimientos
y un historial de todas las conversaciones.
Ahora pasemos a Windows."
```

**Duración:** ~20 seg

---

### **[01:15-01:45] DEMO WINDOWS LOCAL (30 seg)**

**Narración:**
```
"En Windows, el proceso es idéntico. Solo ejecuto:
python run_agent.py"
```

**Acciones:**
- [ ] Abre Terminal/CMD
- [ ] Navega a carpeta:
  ```bash
  cd "C:\ruta\agente_ia_simple"
  ```
- [ ] Ejecuta:
  ```bash
  python run_agent.py
  ```
- [ ] Muestra menú en Windows
- [ ] Elige opción **1**
- [ ] Haz una conversación rápida (~3 entradas):
  ```
  👤 Tú: Excelente trabajo académico
  🤖 Agente: [respuesta positiva]
  
  👤 Tú: Esto es horrible
  🤖 Agente: [respuesta negativa]
  
  👤 Tú: salir
  ```
- [ ] Muestra que `logs/conversations.csv` se creó

**Narración:**
```
"Los datos se guardan automáticamente en CSV.
Ahora voy a empaquetar esto como ejecutable .exe"
```

**Duración:** ~30 seg

---

### **[01:45-02:30] GENERACIÓN DEL .EXE (45 seg)**

#### **Sección A: Instalación PyInstaller [01:45-01:55]**

**Narración:**
```
"Para crear un .exe, uso PyInstaller. 
Instalo con pip en 30 segundos."
```

**Acciones:**
- [ ] En misma Terminal, ejecuta:
  ```bash
  pip install pyinstaller
  ```
- [ ] Espera a que instale (~10 seg)
- [ ] Muestra "Successfully installed pyinstaller"

**Duración:** ~10 seg

---

#### **Sección B: Comando PyInstaller [01:55-02:10]**

**Narración:**
```
"Ahora genero el ejecutable con este comando:"
```

**Acciones:**
- [ ] Ejecuta:
  ```bash
  pyinstaller --onefile --name AgenteIA run_agent.py
  ```
- [ ] Muestra la ejecución (~10-15 seg)
- [ ] Muestra mensaje:
  ```
  ✓ building 'AgenteIA' completed successfully.
  ```

**Duración:** ~15 seg

---

#### **Sección C: Ubicación y Ejecución [02:10-02:30]**

**Narración:**
```
"El ejecutable está en la carpeta 'dist'.
Voy a abrirlo para demostrar que funciona."
```

**Acciones:**
- [ ] Abre explorador de archivos
- [ ] Navega a `dist/`
- [ ] Muestra archivo `AgenteIA.exe`
- [ ] Hace doble clic para ejecutar
- [ ] Se abre nueva ventana del agente
- [ ] Muestra menú funcionando
- [ ] Haz rápidamente opción **2** (Ver últimas 5):
  ```
  📋 Últimas 5 Interacciones:
  1. [2026-04-26 14:30:45]
     Usuario: Excelente trabajo académico
     Sentimiento: POSITIVO
  ...
  ```
- [ ] Cierra el .exe

**Narración:**
```
"¡Perfecto! El .exe funciona correctamente.
Nota que se ejecuta sin necesidad de Python 
instalado. Esto es lo que hace a PyInstaller 
tan poderoso para distribución."
```

**Duración:** ~20 seg

---

### **[02:30-02:45] CONCLUSIÓN (15 seg)**

**Narración:**
```
"En resumen, el Agente IA:

✓ Procesa entrada de texto natural
✓ Analiza sentimientos (positivo/negativo/neutral)
✓ Genera respuestas contextuales
✓ Registra datos en CSV
✓ Genera reportes HTML
✓ Se ejecuta en Colab, Windows y como .exe

Esto demuestra el ciclo completo de desarrollo,
prueba y despliegue de una aplicación Python.

Gracias por ver. Más información en README.md"
```

**Acciones:**
- [ ] Resume pantalla de escritorio
- [ ] Muestra archivos finales en explorador
- [ ] Termina grabación

**Duración:** ~15 seg

---

## 🎙️ TIPS DE NARRACIÓN

### ✅ Haz esto:
- Habla clara y lentamente
- Haz pausas entre secciones
- Señala elementos importantes con cursor
- Muestra mensajes completos en pantalla

### ❌ Evita esto:
- Hablar muy rápido
- Deslumbrante con mouse
- Cambios muy rápidos de pantalla
- Ruido de fondo

---

## 🎬 GRABACIÓN EN LOOM

### Paso a Paso:

1. **Entra a Loom:** https://www.loom.com
2. **Haz clic:** "Start Recording"
3. **Selecciona:** "Screen" (pantalla completa)
4. **Verifica:** Micrófono activado 🎤
5. **Comienza:** Muestra el desktop
6. **Sigue:** Este guion de arriba
7. **Termina:** Cuando llegues a [02:45]
8. **Descarga o comparte:** Loom te da link automático

### Duración esperada: **2:30 - 3:00 minutos**

---

## 📹 Después de Grabar

### ✅ Checklist Final

- [ ] Video grabado correctamente (sin errores)
- [ ] Audio claro (sin ruido de fondo)
- [ ] Todas las secciones cubiertas
- [ ] Funcionalidad del agente demostrada
- [ ] .exe ejecutable mostrado
- [ ] Duración: 2:30-3:00 min

### 📤 Subir a Portal Académico

1. Ve a Loom → Copia el link del video
2. Sube a portal académico junto con:
   - [ ] Código fuente (run_agent.py)
   - [ ] Documentación (README.md)
   - [ ] Ejecutable (dist/AgenteIA.exe)
   - [ ] Link a video Loom

---

## 📝 Ejemplo de Narración Completa

Si prefieres un script palabra por palabra:

```
[0:00] Hola, soy [Tu Nombre], estudiante de MAI 630
Computer Vision en Atlantis University.

Presento el Agente IA, un sistema que analiza 
sentimientos en texto y genera respuestas contextuales.

Voy a mostrar tres cosas importantes:
Primero, su ejecución en Google Colab.
Segundo, cómo funciona en Windows localmente.
Y tercero, cómo lo convertimos en un ejecutable .exe
que funciona sin Python instalado.

[0:15] Comenzamos en Google Colab...
[abre Colab, crea notebook, copia código]

El agente es muy simple pero funcional.
Analiza sentimientos usando palabras clave
y responde de manera contextual.

[0:35] Voy a escribir un mensaje positivo...
[escribe en terminal]

Como ves, detectó correctamente el sentimiento
positivo y respondió apropiadamente.

Ahora pruebo con un sentimiento negativo...
[segunda entrada]

Funciona perfecto. El agente registra todo en
un archivo CSV automáticamente.

[0:55] Voy a generar un reporte HTML con
estadísticas de todas las interacciones...

[elige opción 3]

Listo. El reporte incluye gráficos y un
historial completo de conversaciones.

[1:15] Ahora voy a Windows, donde el proceso
es idéntico. Solo ejecuto python run_agent.py

[abre Terminal en Windows]
[ejecuta comando]

Ves el mismo menú. La funcionalidad es
exactamente la misma. Los datos se guardan
en la misma estructura CSV.

[1:45] Ahora viene la parte más importante
para la entrega: generar el ejecutable .exe

Uso PyInstaller, que es la herramienta estándar
de Python para empaquetamiento.

[instala PyInstaller]

Una vez instalado, ejecuto este comando...
[pyinstaller --onefile --name AgenteIA run_agent.py]

Espero a que termine...

[2:10] Y aquí está. El ejecutable AgenteIA.exe
en la carpeta dist.

[abre AgenteIA.exe]

Como ves, funciona perfectamente. Puedo
ejecutarlo sin tener Python instalado.
Es un ejecutable Windows estándar.

[2:30] Para resumir:

El Agente IA es un prototipo que demuestra:
- Procesamiento de lenguaje natural básico
- Análisis de sentimientos con diccionarios
- Persistencia de datos en CSV
- Generación de reportes HTML
- Empaquetamiento como ejecutable profesional

Este proyecto combina conceptos de IA, 
ingeniería de software y despliegue en 
un paquete simple pero completo.

Código, documentación y ejecutable están listos
para entrega académica.

Gracias por ver.
```

---

## 🚀 Alternativas si algo sale mal

### Si en Colab falla:
```
Saltate la demo de Colab.
Muestra 2 demos en Windows (una con .py, otra .exe)
```

### Si tarda demasiado PyInstaller:
```
Corta la grabación de esa parte y di:
"Normalmente toma 1-2 minutos..."
Puedes acelerar la grabación 2x en Loom
```

### Si se congela la terminal:
```
Pausa la grabación
Reinicia la terminal
Continúa desde donde dejaste
```

---

**Buena suerte con tu video. ¡Que quede profesional!** 🎬
