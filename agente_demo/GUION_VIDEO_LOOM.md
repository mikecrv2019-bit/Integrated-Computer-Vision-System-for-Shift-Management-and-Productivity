# GUION PARA VIDEO LOOM - AGENTE DE IA (2-3 minutos)

## 📝 Información General del Video

**Duración:** 2-3 minutos  
**Plataforma:** Loom (https://www.loom.com)  
**Audiencia:** Profesor/evaluador de MAI 630  
**Propósito:** Demostración funcional del agente de IA  

---

## 🎬 Estructura del Video

### FASE 1: Introducción (0:00 - 0:15)

**Audio:**
> "Buenos días. Presento el Agente de IA para Análisis de Imágenes, desenvolvimiento del Proyecto Final I del curso MAI 630 Computer Vision de Atlantis University."

**Pantalla:**
- Mostrar la carpeta del proyecto en el explorador de archivos
- Señalar la estructura: `run_agent.py`, `requirements.txt`, `demo_images/`, `outputs/`

**Duración:** 15 segundos

---

### FASE 2: Instalación de Dependencias (0:15 - 0:45)

**Audio:**
> "Primero, necesitamos instalar las dependencias necesarias. Esto incluye OpenCV para procesamiento de imágenes, NumPy para operaciones matemáticas y Pillow para manipulación de imágenes."

**Pantalla:**
- Abrir terminal/CMD
- Mostrar el archivo `requirements.txt`
- Ejecutar comando:
  ```bash
  pip install -r requirements.txt
  ```
- Mostrar la instalación en progreso

**Nota sobre Loom:** 
- Si la instalación es lenta, puedes acelerar el video o usar fade-out/fade-in

**Duración:** 30 segundos

---

### FASE 3: Preparación de Imágenes de Prueba (0:45 - 1:15)

**Audio:**
> "Colocamos imágenes de personas en la carpeta demo_images. El agente detectará rostros, extraerá información de las imágenes y generará resultados procesados."

**Pantalla:**
- Abrir carpeta `demo_images/`
- Mostrar 2-3 imágenes de personas (pueden ser públicas: stock photos, etc.)
- Cerrar y regresar a la vista principal del proyecto

**Nota:**
- Usa imágenes claras donde se vean rostros frontales
- Puede usar: https://unsplash.com, https://pixabay.com (imágenes libres)

**Duración:** 30 segundos

---

### FASE 4: Ejecución del Agente (1:15 - 2:00)

**Audio:**
> "Ahora ejecutamos el agente desde la terminal con el comando: python run_agent.py"

**Pantalla:**
1. Abrir terminal en la carpeta del proyecto
2. Ejecutar:
   ```bash
   python run_agent.py
   ```
3. Mostrar la salida completa con:
   - Encabezado del agente
   - Análisis de cada imagen
   - Información extraída (dimensiones, rostros detectados)
   - Archivos generados
   - Resumen final

**Duración:** 45 segundos

**Punto de énfasis:**
- Mostrar que detectó los rostros
- Mencionar los archivos generados: `faces_*.jpg`, `resized_*.jpg`, `grayscale_*.jpg`

---

### FASE 5: Visualización de Resultados (2:00 - 2:30)

**Audio:**
> "Los resultados se guardan automáticamente en la carpeta outputs. Podemos ver las imágenes procesadas: rostros detectados con rectángulos verdes, versiones redimensionadas y escala de grises."

**Pantalla:**
1. Abrir carpeta `outputs/`
2. Mostrar los archivos generados:
   - `faces_*.jpg` (con rectángulos verdes alrededor de rostros)
   - `resized_*.jpg` (imagen redimensionada)
   - `grayscale_*.jpg` (imagen en blanco y negro)
   - `analysis_report.json` (reporte de análisis)

3. Doble-click en una imagen para abrir y mostrar brevemente
4. Abrir `analysis_report.json` en editor de texto para mostrar el reporte

**Duración:** 30 segundos

---

### FASE 6: Compilación a .exe (2:30 - 2:50) [OPCIONAL]

**Audio:**
> "El proyecto puede compilarse a un ejecutable .exe para Windows usando PyInstaller. Simplemente ejecutamos el script build_exe.bat, que genera un archivo .exe independiente que no requiere Python instalado."

**Pantalla:**
1. Mostrar el archivo `build_exe.bat` en el explorador
2. Doble-click para ejecutar (o ejecutar en terminal)
3. Mostrar el proceso de compilación
4. Mostrar la carpeta `dist/` con el archivo `run_agent.exe`

**Duración:** 20 segundos

---

### FASE 7: Conclusión (2:50 - 3:00)

**Audio:**
> "El agente de IA es funcional, modular y listo para producción. Puede ejecutarse en terminal, compilarse a .exe, y funciona en Google Colab. Gracias por su atención."

**Pantalla:**
- Volver a la carpeta principal del proyecto
- Mostrar el nombre del archivo `run_agent.py` como cierre

**Duración:** 10 segundos

---

## 🎯 Checklist de Grabación

### Antes de Grabar:
- [ ] Tener todas las carpetas y archivos listos
- [ ] Tener imágenes de prueba en `demo_images/`
- [ ] Haber ejecutado el script al menos una vez (para verificar que funciona)
- [ ] Limpiar la pantalla (no mostrar archivos sensibles)
- [ ] Ajustar el zoom de la terminal para que sea legible
- [ ] Tener el micrófono funcionando correctamente

### Configuración de Loom:
- [ ] Calidad: 1080p o 720p (mínimo)
- [ ] Audio: micrófono limpio, sin ruidos de fondo
- [ ] Pantalla: capturar toda la pantalla o región específica
- [ ] Cámara web: opcional (NO incluir si afecta calidad)

### Durante la Grabación:
- [ ] Hablar claro y a velocidad moderada
- [ ] Hacer clic lentamente para que se vea bien
- [ ] No saltar entre ventanas rápidamente
- [ ] Pausar brevemente entre fases para dar tiempo al espectador

### Después de Grabar:
- [ ] Editar (si es necesario):
  - Acelerar fases lentas (instalación, compilación)
  - Añadir títulos/transiciones
  - Añadir música de fondo (opcional)
- [ ] Probar el video completo
- [ ] Obtener enlace compartible de Loom
- [ ] Incluir enlace en la entrega final

---

## 📊 Guion Detallado con Tiempos

```
00:00 - 00:15  | Introducción del proyecto
               | "Buenos días. Presento el Agente de IA para Análisis de Imágenes,
               |  desenvolvimiento del Proyecto Final I de MAI 630..."

00:15 - 00:45  | Instalación de dependencias
               | "Primero, instalamos las dependencias..."
               | [Mostrar: pip install -r requirements.txt]

00:45 - 01:15  | Preparación de datos
               | "Colocamos imágenes en demo_images..."
               | [Mostrar carpeta con imágenes]

01:15 - 02:00  | Ejecución del agente
               | "Ejecutamos: python run_agent.py"
               | [Mostrar salida completa]

02:00 - 02:30  | Visualización de resultados
               | "Los resultados se guardan en outputs..."
               | [Mostrar imágenes procesadas]

02:30 - 02:50  | Compilación a .exe (opcional)
               | "Compilamos a .exe usando PyInstaller..."
               | [Mostrar build_exe.bat]

02:50 - 03:00  | Conclusión
               | "El agente es funcional, modular y listo para producción..."
               | [Pantalla final]
```

---

## 🎤 Notas de Audio - Versión Completa

### Introducción (0:00 - 0:15):
> "Buenos días. Presento el Agente de IA para Análisis de Imágenes, desenvolvimiento del Proyecto Final I del curso MAI 630 Computer Vision de Atlantis University. Este agente procesa imágenes de personas, detecta rostros, extrae información y genera reportes automáticamente."

### Instalación (0:15 - 0:45):
> "El primer paso es instalar las dependencias del proyecto. Utilizamos OpenCV para visión por computadora, NumPy para operaciones numéricas y Pillow para manipulación de imágenes. Ejecutamos pip install -r requirements.txt y esperamos a que todas las librerías se instalen correctamente."

### Datos (0:45 - 1:15):
> "Para el demo, colocamos imágenes de personas en la carpeta demo_images. El agente analizará automáticamente todas las imágenes que coloquemos aquí. Detectará rostros utilizando el algoritmo Haar Cascades, que es robusto y eficiente para este tipo de tarea."

### Ejecución (1:15 - 2:00):
> "Ahora ejecutamos el agente desde la terminal. El comando es simple: python run_agent.py. El agente comienza su procesamiento: lee cada imagen, extrae información como dimensiones y número de canales, detecta rostros y dibuja rectángulos alrededor de ellos, redimensiona las imágenes y las convierte a escala de grises. Todo se procesa automáticamente."

### Resultados (2:00 - 2:30):
> "Todos los resultados se guardan en la carpeta outputs. Aquí podemos ver las imágenes procesadas: primero, las imágenes con los rostros detectados marcados con rectángulos verdes. Segundo, las imágenes redimensionadas al tamaño óptimo. Tercero, las versiones en escala de grises. También se genera un reporte JSON con todos los análisis realizados."

### Compilación (2:30 - 2:50):
> "Opcionalmente, el proyecto puede compilarse a un ejecutable independiente para Windows usando PyInstaller. Simplemente ejecutamos el script build_exe.bat. El proceso genera un archivo .exe que no requiere Python instalado en la computadora. Perfecto para distribución y demostración."

### Conclusión (2:50 - 3:00):
> "El agente de IA es completamente funcional, modular, escalable y listo para producción. Puede ejecutarse en terminal, compilarse a .exe, funciona en Google Colab y en cualquier sistema con Python. Gracias por su atención."

---

## 🎬 Recomendaciones Técnicas de Loom

### Configuración Óptima:
```
Resolución:     1920x1080 (Full HD)
Frames:         30 fps
Audio:          48kHz, estéreo
Formato:        MP4
```

### Edición en Loom (después de grabar):
1. **Cortadas:** Eliminar partes innecesarias
2. **Velocidad:** Acelerar fases lentas (instalación)
3. **Títulos:** Añadir entre fases principales
4. **Música:** Tema de fondo profesional (opcional)
5. **Subtítulos:** Auto-generados por Loom

### Compartir:
- Obtener enlace directo
- Permitir comentarios
- Descargar como MP4 para respaldar
- Incluir en presentación final

---

## 📋 Formato de Entrega Final

**Título del Video:**
> "MAI 630 Computer Vision - Agente de IA para Análisis de Imágenes | Proyecto Final I"

**Descripción (para plataforma académica):**
> "Demostración funcional del Agente de IA para Procesamiento de Imágenes. Muestra: instalación de dependencias, ejecución del agente, análisis de imágenes con detección de rostros, generación de reportes y compilación a ejecutable .exe. Desenvolvimiento del Proyecto Final I del curso MAI 630 Computer Vision."

**Duración:**
> 2 minutos 50 segundos a 3 minutos

**Tags:**
> #MAI630 #ComputerVision #AIAgent #ImageProcessing #OpenCV #Python #AtlantisUniversity

---

## ✅ Checklist Final

- [ ] Video grabado en Loom
- [ ] Audio claro y a buen volumen
- [ ] Duración entre 2-3 minutos
- [ ] Todas las fases incluidas
- [ ] Edición completada
- [ ] Enlace de Loom obtenido
- [ ] Descripción añadida
- [ ] Video descargado como MP4 (respaldo)
- [ ] Enlace incluido en documentación README.md
- [ ] Listo para presentación final

---

**Versión 1.0** | 2026
