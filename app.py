import streamlit as st
import plotly.graph_objects as go

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

st.markdown("---")
st.header("🔮 Visualización 3D del ROE")
st.markdown("Prisma 3D del ROE - Análisis DuPont")

col_viz, col_data = st.columns([3, 1])

with col_viz:
    # Definir vértices del cubo
    # Vértices: (x, y, z)
    # 0: 0,0,0
    # 1: M,0,0
    # 2: M,R,0
    # 3: 0,R,0
    # 4: 0,0,A
    # 5: M,0,A
    # 6: M,R,A
    # 7: 0,R,A
    
    x_nodes = [0, margen_neto, margen_neto, 0, 0, margen_neto, margen_neto, 0]
    y_nodes = [0, 0, rotacion_activos, rotacion_activos, 0, 0, rotacion_activos, rotacion_activos]
    z_nodes = [0, 0, 0, 0, apalancamiento_financiero, apalancamiento_financiero, apalancamiento_financiero, apalancamiento_financiero]
    
    # Definir caras (triángulos)
    # i, j, k son índices de los vértices
    i_idx = [0, 0, 4, 4, 0, 0, 2, 2, 0, 0, 1, 1]
    j_idx = [1, 2, 5, 6, 1, 5, 3, 7, 3, 7, 2, 6]
    k_idx = [2, 3, 6, 7, 5, 4, 7, 6, 7, 4, 6, 5]
    
    fig = go.Figure(data=[
        go.Mesh3d(
            x=x_nodes,
            y=y_nodes,
            z=z_nodes,
            # i, j, k definen los triángulos que forman las caras
            # Para un cubo son 12 triángulos (2 por cara * 6 caras)
            i = [0, 0,  4, 4,  0, 0,  3, 3,  0, 0,  1, 1],
            j = [1, 2,  5, 6,  1, 5,  2, 6,  3, 7,  2, 6],
            k = [2, 3,  6, 7,  5, 4,  6, 7,  7, 4,  6, 5],
            color='#FFD700',
            opacity=0.9,
            flatshading=True,
            name='ROE Prisma'
        )
    ])
    
    # Configurar diseño 3D
    fig.update_layout(
        scene = dict(
            xaxis = dict(title='Margen Neto (%)', range=[0, 30], backgroundcolor="white", gridcolor="lightgrey"),
            yaxis = dict(title='Rotación de Activos', range=[0, 4], backgroundcolor="white", gridcolor="lightgrey"),
            zaxis = dict(title='Apalancamiento', range=[0, 6], backgroundcolor="white", gridcolor="lightgrey"),
            aspectmode='manual',
            aspectratio=dict(x=1, y=1, z=1)
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=500
    )
    
    st.plotly_chart(fig, use_container_width=True)

with col_data:
    st.subheader("📊 Resultado")
    st.metric("ROE (%)", f"{roe:.1f}%")
    
    st.markdown(f"""
    <div style="background-color: #f0f8ff; padding: 20px; border-radius: 10px; border-left: 5px solid #007bff;">
        <h4 style="color: #004085; margin-top:0;">Dimensiones del Prisma:</h4>
        <ul style="list-style-type: none; padding-left: 0; color: #333; font-size: 1.1em;">
            <li style="margin-bottom: 15px;">• <strong>Margen:</strong><br><span style="font-size: 1.5rem; font-weight: bold;">{margen_neto:.1f}%</span></li>
            <li style="margin-bottom: 15px;">• <strong>Rotación:</strong><br><span style="font-size: 1.5rem; font-weight: bold;">{rotacion_activos:.1f}</span></li>
            <li style="margin-bottom: 0px;">• <strong>Apalancamiento:</strong><br><span style="font-size: 1.5rem; font-weight: bold;">{apalancamiento_financiero:.1f}</span></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

