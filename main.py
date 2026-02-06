#!/usr/bin/env python3
"""
Script de saludo según la hora del día
- 6:01 - 12:00: "Buenos días"
- 12:01 - 20:00: "Buenas tardes"
- 20:01 - 6:00: "Buenas noches"
"""

from datetime import datetime


def obtener_saludo():
    """
    Obtiene el saludo apropiado según la hora actual del día.
    
    Returns:
        str: El saludo apropiado ("Buenos días", "Buenas tardes", o "Buenas noches")
    """
    ahora = datetime.now()
    hora_actual = ahora.hour
    minuto_actual = ahora.minute
    
    # Convertir a minutos totales desde medianoche para mejor comparación
    minutos_totales = hora_actual * 60 + minuto_actual
    
    # 6:01 - 12:00: "Buenos días"
    if (6 * 60 + 1) <= minutos_totales <= (12 * 60):
        return "Buenos días"
    # 12:01 - 20:00: "Buenas tardes"
    elif (12 * 60 + 1) <= minutos_totales <= (20 * 60):
        return "Buenas tardes"
    # 20:01 - 6:00: "Buenas noches"
    else:
        return "Buenas noches"


if __name__ == "__main__":
    saludo = obtener_saludo()
    print(saludo)
