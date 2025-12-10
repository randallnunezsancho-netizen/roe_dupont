import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Calculadora ROE DuPont", layout="wide")

# Estilos personalizados para emular el diseño (opcional pero bueno para "wow")
st.markdown("""
<style>
    .metric-container {
        border: 1px solid #e6e6e6;
        padding: 20px;
        border-radius: 10px;
        background-color: #ffffff;
        text-align: center;
    }
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
    }
    .sub-header {
        font-size: 1.5rem;
        color: #555;
        margin-bottom: 15px;
    }
    .info-box {
        background-color: #e8f4f9;
        padding: 15px;
        border-radius: 10px;
        margin-top: 20px;
        color: #0c5460;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar: Variables Contables
st.sidebar.header("📈 Variables Contables")

utilidad_neta = st.sidebar.slider(
    "Utilidad Neta ($)", 
    min_value=0, 
    max_value=500000, 
    value=90000, 
    step=1000,
    help="Ganancia neta después de impuestos y gastos."
)

ventas = st.sidebar.slider(
    "Ventas ($)", 
    min_value=0, 
    max_value=2000000, 
    value=1020000, 
    step=5000,
    help="Ingresos totales por ventas."
)

activos_promedio = st.sidebar.slider(
    "Activos Promedio ($)", 
    min_value=0, 
    max_value=1000000, 
    value=565000, 
    step=5000,
    help="Valor promedio de los activos de la empresa."
)

patrimonio_promedio = st.sidebar.slider(
    "Patrimonio Promedio ($)", 
    min_value=0, 
    max_value=1000000, 
    value=245000, 
    step=5000,
    help="Valor promedio del patrimonio de los accionistas."
)

# Cálculos del Modelo DuPont
# Evitar división por cero
margen_neto = (utilidad_neta / ventas) * 100 if ventas > 0 else 0
rotacion_activos = ventas / activos_promedio if activos_promedio > 0 else 0
apalancamiento_financiero = activos_promedio / patrimonio_promedio if patrimonio_promedio > 0 else 0
roe = margen_neto * rotacion_activos * apalancamiento_financiero / 100 # Se ajusta porque margen está en %

# Panel Principal
st.title("📊 Rentabilidad Sobre el Patrimonio")
st.markdown("### Descomposición por el Modelo DuPont")

# Mostrar métricas en columnas
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(label="Margen Neto", value=f"{margen_neto:.1f}%", help="Utilidad Neta / Ventas")

with col2:
    st.metric(label="Rotación de Activos", value=f"{rotacion_activos:.1f}", help="Ventas / Activos Promedio")

with col3:
    st.metric(label="Apalancamiento Financiero", value=f"{apalancamiento_financiero:.1f}", help="Activos Promedio / Patrimonio Promedio")

with col4:
    st.metric(label="ROE (Return on Equity)", value=f"{roe:.1f}%", help="Retorno sobre el Patrimonio")

# Sección explicativa
st.markdown("""
<div class="info-box">
    <strong>Fórmula del ROE:</strong> ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero<br><br>
    Esta descomposición del ROE te permite entender qué factores están impulsando la rentabilidad del patrimonio.
</div>
""", unsafe_allow_html=True)
