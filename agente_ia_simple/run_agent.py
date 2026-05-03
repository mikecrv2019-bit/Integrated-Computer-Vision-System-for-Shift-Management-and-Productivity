#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Agente IA - Análisis de Sentimientos y Respuesta Contextual
Proyecto Final I - MAI 630 Computer Vision
Atlantis University 2024-2026

Descripción:
    Agente de inteligencia artificial que:
    - Recibe texto del usuario
    - Analiza sentimiento (positivo, negativo, neutral)
    - Genera respuesta contextual
    - Registra interacciones en CSV
    - Genera reporte en HTML

Uso:
    python run_agent.py
"""

import csv
import os
import datetime
from pathlib import Path
import sys
import random

# ============================================================================
# CONFIGURACIÓN GLOBAL
# ============================================================================

PROJECT_DIR = Path(__file__).parent
LOGS_DIR = PROJECT_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

CSV_FILE = LOGS_DIR / "conversations.csv"
REPORT_FILE = LOGS_DIR / "reporte.html"
LOG_FILE = LOGS_DIR / "agent.log"

# Diccionario de palabras para análisis de sentimientos
PALABRAS_POSITIVAS = {
    'bien', 'excelente', 'genial', 'fantástico', 'perfecto', 'awesome',
    'great', 'good', 'love', 'wonderful', 'amazing', 'bueno', 'muy bien',
    'hermoso', 'feliz', 'contento', 'alegre', 'maravilloso', 'gracias',
    'excellent', 'best', 'super', 'increíble'
}

PALABRAS_NEGATIVAS = {
    'mal', 'terrible', 'horrible', 'peor', 'malo', 'awful', 'hate',
    'bad', 'stupid', 'dumb', 'triste', 'infeliz', 'enojado', 'furioso',
    'decepcionado', 'frustrado', 'odio', 'asco', 'disgusto', 'lástima'
}

RESPUESTAS_POSITIVAS = [
    "¡Me alegra escuchar eso! 😊 Parece que tienes un sentimiento positivo.",
    "Excelente actitud. ¿Hay algo más en lo que pueda ayudarte?",
    "¡Qué buena noticia! Continúa con ese ánimo positivo.",
    "Detecté un sentimiento positivo en tu mensaje. ¡Sigue así!"
]

RESPUESTAS_NEGATIVAS = [
    "Detecté un sentimiento negativo. ¿En qué puedo ayudarte? 😔",
    "Parece que hay algo que no va bien. ¿Qué pasó?",
    "Entiendo tu frustración. Estoy aquí para ayudarte.",
    "Sensé negatividad en tu mensaje. ¿Necesitas apoyo?"
]

RESPUESTAS_NEUTRAL = [
    "Interesante observación. ¿Podrías expandir tu idea?",
    "Entiendo tu punto. ¿Hay algo específico que quieras saber?",
    "Eso es relevante. ¿Necesitas ayuda con algo en particular?",
    "Anotado. ¿Cuál es tu próxima pregunta?"
]

# ============================================================================
# FUNCIONES NÚCLEO
# ============================================================================

def analizar_sentimiento(texto: str) -> str:
    """
    Analiza el sentimiento del texto usando un diccionario simple.

    Args:
        texto: Cadena de texto a analizar

    Returns:
        str: 'positivo', 'negativo' o 'neutral'
    """
    texto_lower = texto.lower()

    # Contar palabras positivas y negativas
    positivos = sum(1 for palabra in PALABRAS_POSITIVAS if palabra in texto_lower)
    negativos = sum(1 for palabra in PALABRAS_NEGATIVAS if palabra in texto_lower)

    if positivos > negativos:
        return 'positivo'
    elif negativos > positivos:
        return 'negativo'
    else:
        return 'neutral'


def generar_respuesta(sentimiento: str, entrada_usuario: str) -> str:
    """
    Genera una respuesta basada en el sentimiento detectado.

    Args:
        sentimiento: 'positivo', 'negativo' o 'neutral'
        entrada_usuario: Texto original del usuario

    Returns:
        str: Respuesta generada
    """
    if sentimiento == 'positivo':
        respuesta = random.choice(RESPUESTAS_POSITIVAS)
    elif sentimiento == 'negativo':
        respuesta = random.choice(RESPUESTAS_NEGATIVAS)
    else:
        respuesta = random.choice(RESPUESTAS_NEUTRAL)

    return respuesta


def registrar_interaccion(entrada: str, sentimiento: str, respuesta: str) -> None:
    """
    Registra la interacción en el archivo CSV.

    Args:
        entrada: Texto del usuario
        sentimiento: Sentimiento detectado
        respuesta: Respuesta generada
    """
    timestamp = datetime.datetime.now()
    fecha = timestamp.strftime("%Y-%m-%d")
    hora = timestamp.strftime("%H:%M:%S")

    # Crear CSV si no existe
    crear_csv_si_no_existe()

    # Agregar fila
    with open(CSV_FILE, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow([fecha, hora, entrada, sentimiento, respuesta])

    # Escribir en log
    with open(LOG_FILE, 'a', encoding='utf-8') as f:
        f.write(f"[{timestamp}] Entrada: {entrada} | Sentimiento: {sentimiento}\n")


def crear_csv_si_no_existe() -> None:
    """Crea el archivo CSV con encabezados si no existe."""
    if not CSV_FILE.exists():
        with open(CSV_FILE, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Fecha', 'Hora', 'Entrada Usuario', 'Sentimiento', 'Respuesta Agente'])


def generar_reporte_html() -> None:
    """Genera un reporte HTML con las estadísticas de la sesión."""
    if not CSV_FILE.exists():
        print("❌ No hay datos para generar reporte.")
        return

    # Leer datos del CSV
    datos = []
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Saltar encabezado
        datos = list(reader)

    if not datos:
        print("❌ No hay datos para generar reporte.")
        return

    # Contar sentimientos
    positivos = sum(1 for fila in datos if len(fila) > 3 and fila[3].lower() == 'positivo')
    negativos = sum(1 for fila in datos if len(fila) > 3 and fila[3].lower() == 'negativo')
    neutrales = sum(1 for fila in datos if len(fila) > 3 and fila[3].lower() == 'neutral')
    total = len(datos)

    # Generar HTML
    html_content = f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte Agente IA - MAI 630</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
            color: #333;
        }}
        .container {{
            max-width: 1000px;
            margin: 0 auto;
            background-color: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #34495e;
            margin-top: 30px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            margin: 20px 0;
        }}
        .stat-box {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 20px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-box.positivo {{
            background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
        }}
        .stat-box.negativo {{
            background: linear-gradient(135deg, #eb3349 0%, #f45c43 100%);
        }}
        .stat-box.neutral {{
            background: linear-gradient(135deg, #fa709a 0%, #fee140 100%);
        }}
        .stat-number {{
            font-size: 32px;
            font-weight: bold;
            margin: 10px 0;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }}
        th {{
            background-color: #34495e;
            color: white;
            padding: 12px;
            text-align: left;
        }}
        td {{
            padding: 12px;
            border-bottom: 1px solid #ddd;
        }}
        tr:hover {{
            background-color: #f9f9f9;
        }}
        .footer {{
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #ddd;
            font-size: 12px;
            color: #7f8c8d;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Reporte de Análisis - Agente IA</h1>
        <p><strong>Proyecto:</strong> MAI 630 Computer Vision - Proyecto Final I</p>
        <p><strong>Fecha de Generación:</strong> {datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</p>

        <h2>Estadísticas Generales</h2>
        <div class="stats">
            <div class="stat-box">
                <div>Total de Interacciones</div>
                <div class="stat-number">{total}</div>
            </div>
            <div class="stat-box positivo">
                <div>Sentimientos Positivos</div>
                <div class="stat-number">{positivos}</div>
            </div>
            <div class="stat-box negativo">
                <div>Sentimientos Negativos</div>
                <div class="stat-number">{negativos}</div>
            </div>
            <div class="stat-box neutral">
                <div>Sentimientos Neutrales</div>
                <div class="stat-number">{neutrales}</div>
            </div>
        </div>

        <h2>Historial de Conversaciones</h2>
        <table>
            <thead>
                <tr>
                    <th>Fecha</th>
                    <th>Hora</th>
                    <th>Entrada Usuario</th>
                    <th>Sentimiento</th>
                    <th>Respuesta Agente</th>
                </tr>
            </thead>
            <tbody>
"""

    # Agregar filas de datos
    for fila in datos:
        if len(fila) >= 5:
            html_content += f"""                <tr>
                    <td>{fila[0]}</td>
                    <td>{fila[1]}</td>
                    <td>{fila[2][:60]}</td>
                    <td><strong>{fila[3].upper()}</strong></td>
                    <td>{fila[4][:60]}</td>
                </tr>
"""

    html_content += """            </tbody>
        </table>

        <div class="footer">
            <p>Este reporte fue generado automáticamente por el Agente IA.</p>
            <p>Archivos: logs/conversations.csv | logs/agent.log</p>
        </div>
    </div>
</body>
</html>
"""

    with open(REPORT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)

    print(f"\n✅ Reporte HTML generado: {REPORT_FILE}")


def mostrar_menu_principal() -> None:
    """Muestra el menú principal del agente."""
    print("\n" + "="*70)
    print("🤖 AGENTE IA - Análisis de Sentimientos y Respuesta Contextual")
    print("="*70)
    print("Proyecto Final I - MAI 630 Computer Vision | Atlantis University")
    print("="*70)
    print("\nOpciones:")
    print("  1. Iniciar conversación interactiva")
    print("  2. Ver últimas 5 interacciones")
    print("  3. Generar reporte HTML")
    print("  4. Limpiar historial")
    print("  5. Salir")
    print("-"*70)


def mostrar_ultimas_interacciones() -> None:
    """Muestra las últimas 5 interacciones."""
    if not CSV_FILE.exists():
        print("❌ No hay historial registrado aún.")
        return

    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader, None)  # Saltar encabezado
        interacciones = list(reader)

    if not interacciones:
        print("❌ No hay historial registrado aún.")
        return

    print("\n📋 Últimas 5 Interacciones:")
    print("-"*70)
    for i, fila in enumerate(interacciones[-5:], 1):
        if len(fila) >= 5:
            print(f"\n{i}. [{fila[0]} {fila[1]}]")
            print(f"   Usuario: {fila[2]}")
            print(f"   Sentimiento: {fila[3].upper()}")
            print(f"   Respuesta: {fila[4]}")


def limpiar_historial() -> None:
    """Limpia el historial de conversaciones."""
    if not CSV_FILE.exists():
        print("✅ No hay historial para limpiar.")
        return

    respuesta = input("\n⚠️  ¿Estás seguro de que deseas eliminar todo el historial? (s/n): ").lower()
    if respuesta == 's':
        CSV_FILE.unlink()
        print("✅ Historial eliminado.")
    else:
        print("❌ Operación cancelada.")


def ejecutar_conversacion_interactiva() -> None:
    """Ejecuta el agente en modo conversación interactiva."""
    print("\n🎤 Iniciando conversación interactiva...")
    print("(Escribe 'salir' para terminar)\n")

    while True:
        try:
            entrada_usuario = input("👤 Tú: ").strip()

            if entrada_usuario.lower() == 'salir':
                print("\n👋 ¡Hasta luego! Sesión finalizada.")
                break

            if not entrada_usuario:
                print("⚠️  Por favor, escribe algo para continuar.\n")
                continue

            # Procesar entrada
            sentimiento = analizar_sentimiento(entrada_usuario)
            respuesta = generar_respuesta(sentimiento, entrada_usuario)

            # Registrar
            registrar_interaccion(entrada_usuario, sentimiento, respuesta)

            # Mostrar respuesta
            print(f"\n🤖 Agente: {respuesta}")
            print(f"   Sentimiento Detectado: {sentimiento.upper()}\n")

        except KeyboardInterrupt:
            print("\n\n👋 Sesión interrumpida por el usuario.")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """Función principal del programa."""
    crear_csv_si_no_existe()

    while True:
        mostrar_menu_principal()
        opcion = input("Selecciona una opción (1-5): ").strip()

        if opcion == '1':
            ejecutar_conversacion_interactiva()
        elif opcion == '2':
            mostrar_ultimas_interacciones()
        elif opcion == '3':
            generar_reporte_html()
        elif opcion == '4':
            limpiar_historial()
        elif opcion == '5':
            print("\n👋 ¡Gracias por usar el Agente IA! Hasta pronto.")
            sys.exit(0)
        else:
            print("❌ Opción no válida. Intenta de nuevo.")


if __name__ == "__main__":
    main()
