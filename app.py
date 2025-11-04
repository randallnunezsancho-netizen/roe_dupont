"""
Aplicación Streamlit - Análisis DuPont (Funcionalidad 1)

Esta aplicación permite calcular y visualizar los componentes del modelo DuPont
a partir de cuatro variables financieras clave:
- Utilidad Neta
- Ventas
- Activos Promedio
- Patrimonio Promedio

El modelo DuPont descompone el ROE en tres componentes multiplicativos:
ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero
"""

import streamlit as st
import pandas as pd
from calculos_financieros import calcular_componentes_dupont


# Configuración de la página
st.set_page_config(
    page_title="Análisis DuPont - ROE",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Título principal
st.title("📊 Análisis DuPont - Modelo de Rentabilidad")
st.markdown("---")

# Descripción del modelo
st.markdown("""
### ¿Qué es el Modelo DuPont?

El **modelo DuPont** descompone el Retorno sobre el Patrimonio (ROE) en tres componentes clave:

1. **Margen Neto**: Eficiencia operativa (Utilidad Neta / Ventas)
2. **Rotación de Activos**: Eficiencia en el uso de activos (Ventas / Activos Promedio)
3. **Apalancamiento Financiero**: Uso de deuda para financiar activos (Activos Promedio / Patrimonio Promedio)

**ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero**
""")

st.markdown("---")

# Sidebar para inputs
st.sidebar.header("📥 Variables de Entrada")
st.sidebar.markdown("Ajuste los valores utilizando los controles deslizantes:")

# Función helper para formatear números con separadores de miles
def formatear_miles(valor):
    """Formatea un número con separadores de miles sin decimales innecesarios."""
    if valor == 0:
        return "0"
    # Convertir a entero si no tiene decimales significativos
    if valor % 1 == 0:
        return f"{int(valor):,}".replace(",", ".")
    else:
        return f"{valor:,.0f}".replace(",", ".")

# Sliders para las 4 variables financieras
# Valores por defecto representan un ejemplo educativo
utilidad_neta = st.sidebar.slider(
    "Utilidad Neta (USD)",
    min_value=0.0,
    max_value=5000000.0,
    value=150000.0,
    step=10000.0,
    help="Utilidad neta después de impuestos del período"
)
st.sidebar.caption(f"Valor actual: **{formatear_miles(utilidad_neta)}** USD")

ventas = st.sidebar.slider(
    "Ventas (USD)",
    min_value=0.0,
    max_value=20000000.0,
    value=1000000.0,
    step=50000.0,
    help="Ventas totales del período"
)
st.sidebar.caption(f"Valor actual: **{formatear_miles(ventas)}** USD")

activos_promedio = st.sidebar.slider(
    "Activos Promedio (USD)",
    min_value=0.0,
    max_value=15000000.0,
    value=500000.0,
    step=25000.0,
    help="Promedio de activos totales (promedio entre inicio y fin de período)"
)
st.sidebar.caption(f"Valor actual: **{formatear_miles(activos_promedio)}** USD")

patrimonio_promedio = st.sidebar.slider(
    "Patrimonio Promedio (USD)",
    min_value=0.0,
    max_value=10000000.0,
    value=250000.0,
    step=25000.0,
    help="Promedio de patrimonio (promedio entre inicio y fin de período)"
)
st.sidebar.caption(f"Valor actual: **{formatear_miles(patrimonio_promedio)}** USD")

# Validación de división por cero
if patrimonio_promedio == 0 or activos_promedio == 0 or ventas == 0:
    st.warning("⚠️ Por favor, ajuste los valores para evitar división por cero en los cálculos.")
    st.stop()

# Cálculo de componentes DuPont
componentes = calcular_componentes_dupont(
    utilidad_neta=utilidad_neta,
    ventas=ventas,
    activos_promedio=activos_promedio,
    patrimonio_promedio=patrimonio_promedio
)

# Sección principal: Visualización de resultados
st.header("📈 Resultados del Análisis DuPont")

# Métricas principales en columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="**Margen Neto**",
        value=f"{componentes['margen_neto']:.2%}",
        help="Utilidad Neta / Ventas"
    )

with col2:
    st.metric(
        label="**Rotación de Activos**",
        value=f"{componentes['rotacion_activos']:.2f}x",
        help="Ventas / Activos Promedio"
    )

with col3:
    st.metric(
        label="**Apalancamiento**",
        value=f"{componentes['apalancamiento']:.2f}x",
        help="Activos Promedio / Patrimonio Promedio"
    )

with col4:
    # ROE con color condicional
    roe_porcentaje = componentes['roe']
    if roe_porcentaje >= 0.15:
        delta_color = "normal"
    elif roe_porcentaje >= 0.10:
        delta_color = "normal"
    else:
        delta_color = "normal"
    
    st.metric(
        label="**ROE (Return on Equity)**",
        value=f"{roe_porcentaje:.2%}",
        help="Margen Neto × Rotación de Activos × Apalancamiento"
    )

# Interpretación del ROE
st.markdown("---")
st.subheader("💡 Interpretación del ROE")

roe_pct = componentes['roe'] * 100

if roe_pct >= 20:
    interpretacion = "**Excelente**: El ROE es muy alto, indicando una rentabilidad superior. Verifique la sostenibilidad de este nivel."
    color = "success"
elif roe_pct >= 15:
    interpretacion = "**Muy Bueno**: El ROE está por encima del promedio del mercado, indicando buena rentabilidad."
    color = "success"
elif roe_pct >= 10:
    interpretacion = "**Adecuado**: El ROE está en un rango aceptable. Analice oportunidades de mejora en los componentes."
    color = "info"
elif roe_pct >= 5:
    interpretacion = "**Bajo**: El ROE está por debajo del promedio. Revise los componentes para identificar áreas de mejora."
    color = "warning"
else:
    interpretacion = "**Muy Bajo**: El ROE requiere atención inmediata. Analice cada componente del modelo DuPont."
    color = "error"

st.info(f"ROE de {roe_pct:.2f}%: {interpretacion}")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray;'>
    <small>Proyecto ROE DuPont - Funcionalidad 1: Cálculo de Ratios Financieros Básicos</small>
</div>
""", unsafe_allow_html=True)

