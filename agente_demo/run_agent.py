#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
=============================================================================
    AGENTE DE IA PARA PROCESAMIENTO DE IMAGENES - MAI 630
    Proyecto Final I | Atlantis University
=============================================================================

Descripcion:
    Agente de IA que carga imagenes de personas desde la carpeta demo_images/,
    realiza analisis basico (deteccion de rostros, informacion de imagen) y
    guarda resultados procesados en outputs/.

Requisitos:
    - Python 3.8+
    - OpenCV (cv2)
    - Pillow
    - NumPy

Uso:
    python run_agent.py

Autor: MAI 630 Computer Vision
Fecha: 2026
=============================================================================
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import json

try:
    import cv2
    import numpy as np
    from PIL import Image
except ImportError as e:
    print("\n[ERROR] Importacion fallida: %s" % e)
    print("\nInstala las dependencias con:")
    print("   pip install -r requirements.txt")
    sys.exit(1)


class ImageProcessingAgent:
    """Agente de IA para analisis y procesamiento de imagenes de personas."""

    def __init__(self, demo_folder='demo_images', output_folder='outputs'):
        """
        Inicializa el agente.

        Args:
            demo_folder (str): Ruta de la carpeta con imagenes de demostracion
            output_folder (str): Ruta de la carpeta para guardar resultados
        """
        self.demo_folder = Path(demo_folder)
        self.output_folder = Path(output_folder)

        try:
            self.cascade_path = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
            self.face_cascade = cv2.CascadeClassifier(self.cascade_path)

            if self.face_cascade.empty():
                raise ValueError("No se pudo cargar el modelo Haar Cascade")

        except Exception as e:
            print("\n[ERROR] Inicializando Haar Cascade: %s" % e)
            raise

        try:
            self.demo_folder.mkdir(parents=True, exist_ok=True)
            self.output_folder.mkdir(parents=True, exist_ok=True)
        except Exception as e:
            print("\n[ERROR] Creando carpetas: %s" % e)
            raise

        self.analysis_log = []

        print("\n" + "="*80)
        print("  AGENTE DE IA - ANALISIS DE IMAGENES DE PERSONAS")
        print("  MAI 630 Computer Vision | Atlantis University")
        print("="*80)
        print("\n[INFO] Carpeta de entrada: %s" % self.demo_folder.absolute())
        print("[INFO] Carpeta de salida:  %s" % self.output_folder.absolute())
        print()

    def get_image_info(self, image_path):
        """Extrae informacion basica de una imagen."""
        img = cv2.imread(str(image_path))
        if img is None:
            return None

        height, width, channels = img.shape
        file_size_mb = os.path.getsize(image_path) / (1024 * 1024)

        return {
            'width': width,
            'height': height,
            'channels': channels,
            'aspect_ratio': round(width / height, 2),
            'size_mb': round(file_size_mb, 3),
            'color_space': 'BGR'
        }

    def detect_faces(self, image_path):
        """Detecta rostros en la imagen usando Haar Cascades."""
        img = cv2.imread(str(image_path))
        if img is None:
            return None, 0

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )

        img_with_faces = img.copy()
        for (x, y, w, h) in faces:
            cv2.rectangle(img_with_faces, (x, y), (x+w, y+h), (0, 255, 0), 2)

        return img_with_faces, len(faces)

    def process_image(self, image_path):
        """Procesa una imagen: redimensiona y convierte a escala de grises."""
        img = cv2.imread(str(image_path))
        if img is None:
            return None, None

        max_dimension = 800
        height, width = img.shape[:2]
        if max(height, width) > max_dimension:
            scale = max_dimension / max(height, width)
            new_width = int(width * scale)
            new_height = int(height * scale)
            img_resized = cv2.resize(img, (new_width, new_height))
        else:
            img_resized = img

        gray = cv2.cvtColor(img_resized, cv2.COLOR_BGR2GRAY)

        return img_resized, gray

    def save_image(self, image, filename):
        """Guarda una imagen procesada en la carpeta outputs/."""
        output_path = self.output_folder / filename
        success = cv2.imwrite(str(output_path), image)
        return output_path if success else None

    def create_test_image(self):
        """Crea una imagen de prueba simple si no hay imagenes."""
        test_image_path = self.demo_folder / 'test_image.jpg'

        print("\n[AVISO] No se encontraron imagenes en demo_images/")
        print("[INFO] Creando imagen de prueba automaticamente...\n")

        img = np.zeros((400, 400, 3), dtype=np.uint8)

        cv2.rectangle(img, (50, 50), (350, 350), (0, 255, 0), 3)
        cv2.circle(img, (150, 150), 30, (0, 0, 255), -1)
        cv2.circle(img, (250, 150), 30, (0, 0, 255), -1)
        cv2.rectangle(img, (150, 220), (250, 260), (255, 0, 0), 3)
        cv2.putText(img, 'Test Image', (120, 350),
                   cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        cv2.imwrite(str(test_image_path), img)
        print("[OK] Imagen de prueba creada: %s\n" % test_image_path.name)
        return True

    def analyze_image(self, image_path):
        """Realiza analisis completo de una imagen."""
        filename = Path(image_path).name
        print("\n[PROCESANDO] Analizando: %s" % filename)
        print("-" * 80)

        info = self.get_image_info(image_path)
        if info is None:
            print("[ERROR] No se pudo cargar la imagen: %s" % filename)
            return None

        print("\n[INFO] INFORMACION DE LA IMAGEN:")
        print("   - Dimensiones: %dx%d pixeles" % (info['width'], info['height']))
        print("   - Relacion de aspecto: %s" % info['aspect_ratio'])
        print("   - Canales de color: %d" % info['channels'])
        print("   - Tamano de archivo: %s MB" % info['size_mb'])
        print("   - Espacio de color: %s" % info['color_space'])

        img_with_faces, face_count = self.detect_faces(image_path)
        print("\n[DETECCION] ROSTROS DETECTADOS:")
        print("   - Total de rostros: %d" % face_count)

        if img_with_faces is not None:
            face_filename = "faces_%s.jpg" % Path(filename).stem
            self.save_image(img_with_faces, face_filename)
            print("   - Imagen guardada: %s" % face_filename)

        img_resized, gray = self.process_image(image_path)
        if img_resized is not None:
            resized_filename = "resized_%s.jpg" % Path(filename).stem
            gray_filename = "grayscale_%s.jpg" % Path(filename).stem

            self.save_image(img_resized, resized_filename)
            self.save_image(gray, gray_filename)

            print("\n[PROCESAMIENTO] RESULTADOS:")
            print("   - Imagen redimensionada: %s" % resized_filename)
            print("   - Imagen en escala de grises: %s" % gray_filename)
            print("   - Nuevas dimensiones: %dx%d" % (img_resized.shape[1], img_resized.shape[0]))

        analysis_record = {
            'timestamp': datetime.now().isoformat(),
            'image': filename,
            'dimensions': "%dx%d" % (info['width'], info['height']),
            'faces_detected': face_count,
            'files_generated': 3
        }
        self.analysis_log.append(analysis_record)

        print("\n" + "-" * 80)
        return analysis_record

    def process_all_images(self):
        """Procesa todas las imagenes en la carpeta demo_images/."""
        image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.tiff'}
        image_files = [
            f for f in self.demo_folder.iterdir()
            if f.suffix.lower() in image_extensions
        ]

        if not image_files:
            self.create_test_image()

            image_files = [
                f for f in self.demo_folder.iterdir()
                if f.suffix.lower() in image_extensions
            ]

        if not image_files:
            print("\n[ERROR] No se pueden procesar imagenes.")
            print("\n[INFO] Coloca imagenes JPG/PNG en: %s" % self.demo_folder.absolute())
            return False

        print("\n[OK] Se encontraron %d imagen(es) para procesar\n" % len(image_files))

        for image_path in sorted(image_files):
            self.analyze_image(image_path)

        return True

    def save_analysis_report(self):
        """Guarda un reporte JSON de todos los analisis realizados."""
        if not self.analysis_log:
            return

        report_path = self.output_folder / 'analysis_report.json'
        report = {
            'timestamp': datetime.now().isoformat(),
            'total_images_processed': len(self.analysis_log),
            'analyses': self.analysis_log
        }

        with open(report_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=4, ensure_ascii=False)

        print("\n[OK] Reporte de analisis guardado: %s" % report_path.name)

    def print_summary(self):
        """Imprime un resumen final del procesamiento."""
        print("\n" + "="*80)
        print("  RESUMEN FINAL")
        print("="*80)
        print("\n[OK] Imagenes procesadas: %d" % len(self.analysis_log))
        print("[INFO] Resultados guardados en: %s" % self.output_folder.absolute())

        if self.analysis_log:
            total_faces = sum(record['faces_detected'] for record in self.analysis_log)
            print("[INFO] Rostros detectados en total: %d" % total_faces)
            print("[INFO] Archivos generados: %d" % (len(self.analysis_log) * 3))

        print("\n" + "="*80)


def print_system_info():
    """Imprime informacion del sistema para diagnostico."""
    print("\n" + "-"*80)
    print("[INFO] INFORMACION DEL SISTEMA:")
    print("-"*80)
    print("Python version: %s" % sys.version)
    print("OpenCV version: %s" % cv2.__version__)
    print("NumPy version: %s" % np.__version__)
    print("-"*80 + "\n")


def main():
    """Funcion principal del agente."""
    try:
        print_system_info()

        agent = ImageProcessingAgent()

        if agent.process_all_images():
            agent.save_analysis_report()
            agent.print_summary()
            print("\n[OK] PROCESO COMPLETADO EXITOSAMENTE\n")
            return 0
        else:
            print("\n[AVISO] No se procesaron imagenes\n")
            return 1

    except KeyboardInterrupt:
        print("\n\n[INFO] Proceso interrumpido por el usuario.")
        return 1

    except Exception as e:
        print("\n[ERROR CRITICO] %s" % e)
        print("\nDetalles tecnicos:")
        import traceback
        traceback.print_exc()

        print("\n[INFO] Soluciones posibles:")
        print("   1. Verifica las dependencias: pip install -r requirements.txt")
        print("   2. Coloca imagenes en: demo_images/")
        print("   3. Asegura de tener Python 3.8+")
        print("   4. Si el error persiste, contacta al profesor\n")
        return 1


if __name__ == '__main__':
    sys.exit(main())
