#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
AssistantTrack 4D — Ejecutable Principal
Sistema de Control Laboral con Computer Vision
"""

import sys
import os

# Configurar encoding UTF-8 para Windows
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Importar el módulo principal
from assistanttrack_4d import main

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[✓] Aplicación cerrada por el usuario.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[✗] Error crítico: {e}")
        sys.exit(1)
