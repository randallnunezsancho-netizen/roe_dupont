# Proyecto ROE DuPont - Análisis de Rentabilidad

Este proyecto implementa el análisis del modelo DuPont para calcular y visualizar el Retorno sobre el Patrimonio (ROE) y sus componentes.

## Funcionalidad 1: Cálculo de Ratios Financieros Básicos

Esta primera funcionalidad permite:
- Capturar 4 variables financieras mediante sliders interactivos
- Calcular automáticamente los componentes del modelo DuPont
- Visualizar los resultados de forma clara y profesional

## Requisitos

- Python 3.8 o superior
- Dependencias listadas en `requirements.txt`

## Instalación

1. Crear un entorno virtual (recomendado):
```bash
python -m venv venv
```

2. Activar el entorno virtual:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

## Uso

Ejecutar la aplicación Streamlit:
```bash
streamlit run app.py
```

La aplicación se abrirá automáticamente en tu navegador en `http://localhost:8501`

## Estructura del Proyecto

```
roe_dupont/
├── app.py                      # Aplicación principal Streamlit
├── calculos_financieros.py     # Módulo de cálculos del modelo DuPont
├── requirements.txt            # Dependencias del proyecto
└── README.md                  # Este archivo
```

## Modelo DuPont

El modelo DuPont descompone el ROE en tres componentes:

**ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero**

Donde:
- **Margen Neto** = Utilidad Neta / Ventas
- **Rotación de Activos** = Ventas / Activos Promedio
- **Apalancamiento Financiero** = Activos Promedio / Patrimonio Promedio

## Próximas Funcionalidades

- **Funcionalidad 2**: Visualización 3D del Prisma ROE
- **Funcionalidad 3**: Estados Financieros Simplificados

