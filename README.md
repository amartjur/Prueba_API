# Script de Saludo según la Hora del Día

## Descripción

Este proyecto contiene un script de Python que imprime un saludo apropiado según la hora actual del día. El saludo se adapta automáticamente basándose en la hora del sistema.

## Funcionalidad

El script determina el saludo según el siguiente esquema:

- **6:01 - 12:00**: "Buenos días"
- **12:01 - 20:00**: "Buenas tardes"
- **20:01 - 6:00**: "Buenas noches"

## Requisitos

- Python 3.x
- Módulo `datetime` (incluido en la biblioteca estándar de Python)

## Instalación

No se requiere instalación adicional. Solo necesitas tener Python 3.x instalado en tu sistema.

## Uso

Para ejecutar el script, simplemente ejecuta el siguiente comando en tu terminal:

```bash
python3 main.py
```

### Ejemplo de salida:

```bash
$ python3 main.py
Buenos días
```

El saludo cambiará automáticamente según la hora en que ejecutes el script.

## Estructura del Proyecto

```
Prueba_API/
├── README.md       # Documentación del proyecto
├── main.py         # Script principal con la lógica de saludo
└── __init__.py     # Archivo de inicialización
```

## Autor

Este proyecto fue creado como parte de una demostración de funcionalidad básica en Python.