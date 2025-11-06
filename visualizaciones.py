"""
Módulo de Visualizaciones - Prisma 3D ROE DuPont y Estados Financieros

Este módulo contiene las funciones para generar visualizaciones del modelo DuPont:
1. Visualización 3D del prisma que representa la interacción de los tres componentes:
   - Margen Neto
   - Rotación de Activos
   - Apalancamiento Financiero
2. Visualizaciones de Estados Financieros Simplificados:
   - Estado de Resultados (gráfico de barras horizontales)
   - Balance General (gráfico de barras verticales apiladas)

El prisma muestra visualmente cómo estos componentes se combinan para determinar el ROE.
"""

import plotly.graph_objects as go
import numpy as np


def crear_prisma_3d_roe(margen_neto: float, rotacion_activos: float, 
                       apalancamiento: float, roe: float) -> go.Figure:
    """
    Crea una visualización 3D del prisma ROE que muestra la interacción de los tres componentes.
    
    El prisma se construye como un cuboide donde:
    - Eje X: Margen Neto (normalizado a escala 0-1)
    - Eje Y: Rotación de Activos (normalizado a escala razonable)
    - Eje Z: Apalancamiento Financiero (normalizado a escala razonable)
    
    El volumen del prisma representa visualmente el ROE resultante.
    
    Parámetros:
    -----------
    margen_neto : float
        Margen neto expresado como decimal (ej: 0.15 = 15%)
    rotacion_activos : float
        Rotación de activos
    apalancamiento : float
        Apalancamiento financiero
    roe : float
        ROE resultante expresado como decimal
        
    Retorna:
    --------
    go.Figure
        Figura de Plotly con el gráfico 3D del prisma ROE
    """
    
    # Normalización de valores para la visualización 3D
    # Ajustamos las escalas para que el prisma sea visible y proporcional
    
    # Margen neto ya está entre 0 y 1 (o puede ser mayor), lo limitamos a 1 para visualización
    margen_normalizado = min(margen_neto, 1.0) if margen_neto >= 0 else 0.0
    
    # Rotación de activos típicamente está entre 0.5 y 5 veces, normalizamos a escala 0-1
    rotacion_max = 5.0
    rotacion_normalizada = min(rotacion_activos / rotacion_max, 1.0) if rotacion_activos >= 0 else 0.0
    
    # Apalancamiento típicamente está entre 1 y 5 veces, normalizamos a escala 0-1
    apalancamiento_max = 5.0
    apalancamiento_normalizado = min(apalancamiento / apalancamiento_max, 1.0) if apalancamiento >= 0 else 0.0
    
    # Coordenadas de los 8 vértices del prisma rectangular
    # El prisma se extiende desde el origen hasta los valores normalizados
    vertices = np.array([
        [0, 0, 0],                                    # Vértice 0: Origen
        [margen_normalizado, 0, 0],                   # Vértice 1: X
        [margen_normalizado, rotacion_normalizada, 0], # Vértice 2: X-Y
        [0, rotacion_normalizada, 0],                 # Vértice 3: Y
        [0, 0, apalancamiento_normalizado],           # Vértice 4: Z
        [margen_normalizado, 0, apalancamiento_normalizado], # Vértice 5: X-Z
        [margen_normalizado, rotacion_normalizada, apalancamiento_normalizado], # Vértice 6: X-Y-Z (punto final)
        [0, rotacion_normalizada, apalancamiento_normalizado]  # Vértice 7: Y-Z
    ])
    
    # Creamos la figura 3D
    fig = go.Figure()
    
    # Creamos el prisma usando Mesh3d que permite crear sólidos 3D
    # Convertimos las caras en triángulos para Mesh3d
    # Cada cara cuadrada se divide en dos triángulos
    
    # Triangulación de las caras (cada cuadrilátero se divide en 2 triángulos)
    triangulos = [
        # Cara inferior (base)
        [0, 1, 2], [0, 2, 3],
        # Cara superior
        [4, 5, 6], [4, 6, 7],
        # Cara frontal (X)
        [0, 1, 5], [0, 5, 4],
        # Cara trasera
        [2, 3, 7], [2, 7, 6],
        # Cara lateral izquierda (Y)
        [0, 3, 7], [0, 7, 4],
        # Cara lateral derecha
        [1, 2, 6], [1, 6, 5]
    ]
    
    # Aplanamos la lista de triángulos para Mesh3d
    i_mesh = []
    j_mesh = []
    k_mesh = []
    for tri in triangulos:
        i_mesh.extend([tri[0]])
        j_mesh.extend([tri[1]])
        k_mesh.extend([tri[2]])
    
    # Extraemos las coordenadas de los vértices
    x_vertices = vertices[:, 0].tolist()
    y_vertices = vertices[:, 1].tolist()
    z_vertices = vertices[:, 2].tolist()
    
    # Agregamos el prisma como un mesh sólido con colores más visibles
    fig.add_trace(go.Mesh3d(
        x=x_vertices,
        y=y_vertices,
        z=z_vertices,
        i=i_mesh,
        j=j_mesh,
        k=k_mesh,
        opacity=0.85,  # Mayor opacidad para mejor visibilidad
        color='rgba(31, 119, 180, 0.9)',  # Azul más oscuro y contrastante
        flatshading=True,
        lighting=dict(
            ambient=0.5,  # Reducido para mayor contraste
            diffuse=0.8,  # Aumentado para mejor iluminación
            fresnel=0.2,
            specular=0.4,  # Aumentado para más brillo
            roughness=0.2  # Reducido para superficies más lisas
        ),
        lightposition=dict(x=100, y=100, z=100),
        name='Prisma ROE',
        showlegend=False,  # No mostrar en la leyenda
        hovertemplate='<b>Prisma DuPont</b><br>' +
                      'Margen Neto: %{x:.2%}<br>' +
                      'Rotación: %{y:.2f}x<br>' +
                      'Apalancamiento: %{z:.2f}x<br>' +
                      '<extra></extra>'
    ))
    
    # Agregamos bordes visibles alrededor del prisma para mejor definición
    bordes = [
        [0, 1], [1, 2], [2, 3], [3, 0],  # Base inferior
        [4, 5], [5, 6], [6, 7], [7, 4],  # Base superior
        [0, 4], [1, 5], [2, 6], [3, 7]   # Aristas verticales
    ]
    
    for borde in bordes:
        v1, v2 = vertices[borde[0]], vertices[borde[1]]
        fig.add_trace(go.Scatter3d(
            x=[v1[0], v2[0]],
            y=[v1[1], v2[1]],
            z=[v1[2], v2[2]],
            mode='lines',
            line=dict(color='rgba(0, 0, 0, 0.9)', width=4),  # Bordes negros más gruesos
            showlegend=False,
            hoverinfo='skip'
        ))
    
    # Agregamos un punto destacado en el vértice final que representa el ROE
    fig.add_trace(go.Scatter3d(
        x=[margen_normalizado],
        y=[rotacion_normalizada],
        z=[apalancamiento_normalizado],
        mode='markers+text',
        marker=dict(
            size=15,
            color='red',
            symbol='diamond',
            line=dict(width=2, color='darkred')
        ),
        text=[f'ROE: {roe:.1%}'],
        textposition='top center',
        textfont=dict(size=12, color='darkred'),
        name='ROE Resultante',
        showlegend=False,  # No mostrar en la leyenda
        hovertemplate='<b>ROE Resultante: {:.1%}</b><br>'.format(roe) +
                      'Margen Neto: {:.1%}<br>'.format(margen_neto) +
                      'Rotación: {:.2f}x<br>'.format(rotacion_activos) +
                      'Apalancamiento: {:.2f}x<br>'.format(apalancamiento) +
                      '<extra></extra>'
    ))
    
    # Configuración del layout
    fig.update_layout(
        title={
            'text': f'<b>Prisma 3D del Modelo DuPont</b><br><sub>ROE = {roe:.2%}</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 18, 'color': 'black'}  # Título en negro
        },
        scene=dict(
            xaxis=dict(
                title='Margen Neto (normalizado)',
                range=[0, 1.1],
                backgroundcolor='rgba(245, 245, 245, 0.5)',  # Fondo más visible pero claro
                gridcolor='rgba(200, 200, 200, 0.5)',  # Grid más visible
                showbackground=True,
                ticktext=[f'{i*0.2:.0%}' for i in range(6)],
                tickvals=[i*0.2 for i in range(6)],
                titlefont=dict(color='black', size=12),  # Título en negro
                tickfont=dict(color='black', size=14),  # Números en negro
                linecolor='black',  # Línea del eje en negro
                linewidth=3,  # Línea más gruesa
                zerolinecolor='black',  # Línea en cero en negro
                zerolinewidth=2  # Línea cero más gruesa
            ),
            yaxis=dict(
                title='Rotación de Activos (normalizada)',
                range=[0, 1.1],
                backgroundcolor='rgba(245, 245, 245, 0.5)',
                gridcolor='rgba(200, 200, 200, 0.5)',
                showbackground=True,
                ticktext=[f'{i*0.2*rotacion_max:.1f}x' for i in range(6)],
                tickvals=[i*0.2 for i in range(6)],
                titlefont=dict(color='black', size=10),  # Título en negro, tamaño 10
                tickfont=dict(color='black', size=14),  # Números en negro, tamaño 14
                linecolor='black',
                linewidth=3,
                zerolinecolor='black',
                zerolinewidth=2
            ),
            zaxis=dict(
                title='Apalancamiento Financiero (normalizado)',
                range=[0, 1.1],
                backgroundcolor='rgba(245, 245, 245, 0.5)',
                gridcolor='rgba(200, 200, 200, 0.5)',
                showbackground=True,
                ticktext=[f'{i*0.2*apalancamiento_max:.1f}x' for i in range(6)],
                tickvals=[i*0.2 for i in range(6)],
                titlefont=dict(color='black', size=10),  # Título en negro, tamaño 10
                tickfont=dict(color='black', size=14),  # Números en negro, tamaño 14
                linecolor='black',
                linewidth=3,
                zerolinecolor='black',
                zerolinewidth=2
            ),
            aspectmode='cube',
            camera=dict(
                eye=dict(x=1.5, y=1.5, z=1.5)
            )
        ),
        width=1200,  # Ampliado de 900 a 1200
        height=900,  # Ampliado de 700 a 900
        margin=dict(l=0, r=0, t=80, b=0),
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=False  # Ocultar leyenda completamente
    )
    
    return fig


def crear_visualizacion_dupont_completa(margen_neto: float, rotacion_activos: float,
                                       apalancamiento: float, roe: float) -> go.Figure:
    """
    Crea una visualización completa del modelo DuPont que incluye el prisma 3D
    con anotaciones y explicaciones adicionales.
    
    Esta función es un wrapper que mejora la visualización básica con información adicional.
    
    Parámetros:
    -----------
    margen_neto : float
        Margen neto expresado como decimal
    rotacion_activos : float
        Rotación de activos
    apalancamiento : float
        Apalancamiento financiero
    roe : float
        ROE resultante expresado como decimal
        
    Retorna:
    --------
    go.Figure
        Figura de Plotly con el gráfico 3D mejorado
    """
    fig = crear_prisma_3d_roe(margen_neto, rotacion_activos, apalancamiento, roe)
    
    # Agregamos una anotación con la fórmula del ROE debajo del título
    fig.add_annotation(
        text=f'<b>Fórmula DuPont:</b><br>ROE = {margen_neto:.2%} × {rotacion_activos:.2f} × {apalancamiento:.2f} = {roe:.2%}',
        xref='paper',
        yref='paper',
        x=0.5,
        y=0.95,  # Posición debajo del título (cerca de la parte superior)
        showarrow=False,
        font=dict(size=12, color='black'),
        bgcolor='rgba(255, 255, 255, 0.8)',
        bordercolor='black',
        borderwidth=1
    )
    
    return fig


def crear_estado_resultados(ventas: float, utilidad_neta: float) -> go.Figure:
    """
    Crea un gráfico de barras horizontales que representa el Estado de Resultados simplificado.
    
    Muestra tres componentes principales:
    - Ventas (azul claro)
    - Gastos (rosa claro) - calculado como Ventas - Utilidad Neta
    - Utilidad Neta (verde claro)
    
    Parámetros:
    -----------
    ventas : float
        Ventas totales del período
    utilidad_neta : float
        Utilidad neta después de impuestos
        
    Retorna:
    --------
    go.Figure
        Figura de Plotly con el gráfico de barras horizontales del Estado de Resultados
    """
    # Calcular gastos como diferencia entre ventas y utilidad neta
    gastos = ventas - utilidad_neta
    
    # Datos para el gráfico
    # En Plotly con barras horizontales, por defecto el orden se muestra de ABAJO a ARRIBA
    # Para invertir y mostrar Ventas arriba, Gastos medio, Utilidad Neta abajo:
    # Usamos categoryorder='array' con autorange='reversed' O simplemente invertimos el orden
    categorias = ['Utilidad Neta', 'Gastos', 'Ventas']
    valores = [utilidad_neta, gastos, ventas]
    
    # Colores según la imagen de referencia (orden invertido para que coincida con el orden de categorias)
    # Verde claro para Utilidad Neta, Rosa claro para Gastos, Azul claro para Ventas
    colores = ['rgba(144, 238, 144, 0.8)', 'rgba(255, 182, 193, 0.8)', 'rgba(173, 216, 230, 0.8)']
    
    # Crear el gráfico de barras horizontales
    fig = go.Figure()
    
    fig.add_trace(go.Bar(
        y=categorias,
        x=valores,
        orientation='h',
        marker=dict(
            color=colores,
            line=dict(color='rgba(0, 0, 0, 0.3)', width=1)
        ),
        text=[f'${val:,.0f}'.replace(',', '.') for val in valores],
        textposition='inside',  # Etiquetas dentro de las barras
        textfont=dict(size=12, color='black'),
        hovertemplate='<b>%{y}</b><br>Monto: $%{x:,.0f}<extra></extra>',
        name=''
    ))
    
    # Configurar el layout del gráfico
    fig.update_layout(
        title={
            'text': '<b>Estado de Resultados</b><br><sub>Año terminado 31 de Diciembre, 20X5</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': 'black'}
        },
        xaxis=dict(
            title='Monto ($)',
            titlefont=dict(size=12, color='rgba(0, 0, 0, 0.7)'),
            tickfont=dict(size=11, color='rgba(0, 0, 0, 0.7)'),
            gridcolor='rgba(0, 0, 0, 0.1)',
            linecolor='rgba(0, 0, 0, 0.7)',
            linewidth=1,
            # Ajustar el rango máximo para que muestre hasta 1M o un poco más
            range=[0, max(ventas * 1.05, 1000000)]
        ),
        yaxis=dict(
            title='',
            tickfont=dict(size=12, color='black'),
            linecolor='rgba(0, 0, 0, 0.7)',
            linewidth=1,
            categoryorder='array',
            categoryarray=categorias,
            autorange='reversed'  # Invertir el orden para que Ventas quede arriba
        ),
        height=300,
        width=800,
        margin=dict(l=120, r=50, t=80, b=50),
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=False
    )
    
    return fig


def crear_balance_general(activos_promedio: float, patrimonio_promedio: float) -> go.Figure:
    """
    Crea un gráfico de barras verticales apiladas que representa el Balance General simplificado.
    
    Muestra dos barras comparativas:
    - Activos (verde claro) - barra única
    - Deuda + Patrimonio (barra apilada):
      - Patrimonio (azul claro) - parte inferior
      - Deuda (rosa claro) - parte superior
    
    Parámetros:
    -----------
    activos_promedio : float
        Promedio de activos totales
    patrimonio_promedio : float
        Promedio de patrimonio
        
    Retorna:
    --------
    go.Figure
        Figura de Plotly con el gráfico de barras verticales apiladas del Balance General
    """
    # Calcular deuda como diferencia entre activos y patrimonio
    deuda = activos_promedio - patrimonio_promedio
    
    # Si la deuda es negativa, establecerla en 0 (caso teórico donde patrimonio excede activos)
    if deuda < 0:
        deuda = 0
    
    # Colores según la imagen de referencia
    # Verde claro para Activos, Azul claro para Patrimonio, Rosa claro para Deuda
    color_activos = 'rgba(144, 238, 144, 0.8)'
    color_patrimonio = 'rgba(173, 216, 230, 0.8)'
    color_deuda = 'rgba(255, 182, 193, 0.8)'
    
    # Crear el gráfico de barras verticales
    fig = go.Figure()
    
    # Calcular total para mostrar en la parte superior
    total_pasivo = patrimonio_promedio + deuda
    
    # Con barmode='stack', las barras con el mismo valor de x se apilarán automáticamente
    # Activos tiene x='Activos' (barra simple)
    # Patrimonio y Deuda tienen x='Deuda + Patrimonio' (se apilarán)
    
    # Barra de Activos (barra única)
    fig.add_trace(go.Bar(
        x=['Activos'],
        y=[activos_promedio],
        name='Activos',
        marker=dict(
            color=color_activos,
            line=dict(color='rgba(0, 0, 0, 0.3)', width=1)
        ),
        text=[f'${activos_promedio:,.0f}'.replace(',', '.')],
        textposition='outside',
        textfont=dict(size=12, color='black'),
        hovertemplate='<b>Activos</b><br>Monto: $%{y:,.0f}<extra></extra>',
        showlegend=False
    ))
    
    # Barra apilada de Deuda + Patrimonio
    # Primero agregamos Patrimonio (parte inferior) - se apilará primero
    fig.add_trace(go.Bar(
        x=['Deuda + Patrimonio'],
        y=[patrimonio_promedio],
        name='Patrimonio',
        marker=dict(
            color=color_patrimonio,
            line=dict(color='rgba(0, 0, 0, 0.3)', width=1)
        ),
        text=[f'${patrimonio_promedio:,.0f}'.replace(',', '.')],
        textposition='inside',
        textfont=dict(size=11, color='black'),
        hovertemplate='<b>Patrimonio</b><br>Monto: $%{y:,.0f}<extra></extra>',
        showlegend=False
    ))
    
    # Luego agregamos Deuda (parte superior) - se apila sobre el patrimonio automáticamente
    fig.add_trace(go.Bar(
        x=['Deuda + Patrimonio'],
        y=[deuda],
        name='Deuda',
        marker=dict(
            color=color_deuda,
            line=dict(color='rgba(0, 0, 0, 0.3)', width=1)
        ),
        text=[f'${deuda:,.0f}'.replace(',', '.') if deuda > 0 else ''],
        textposition='inside',
        textfont=dict(size=11, color='black'),
        hovertemplate='<b>Deuda</b><br>Monto: $%{y:,.0f}<extra></extra>',
        showlegend=False
    ))
    
    # Configurar el layout del gráfico
    max_valor = max(activos_promedio, total_pasivo)
    
    fig.update_layout(
        title={
            'text': '<b>Balance General</b><br><sub>Al 31 de Diciembre, 20X5</sub>',
            'x': 0.5,
            'xanchor': 'center',
            'font': {'size': 16, 'color': 'black'}
        },
        xaxis=dict(
            title='',
            tickfont=dict(size=12, color='black'),
            linecolor='rgba(0, 0, 0, 0.7)',
            linewidth=1
        ),
        yaxis=dict(
            title='Monto ($)',
            titlefont=dict(size=12, color='rgba(0, 0, 0, 0.7)'),
            tickfont=dict(size=11, color='rgba(0, 0, 0, 0.7)'),
            gridcolor='rgba(0, 0, 0, 0.1)',
            linecolor='rgba(0, 0, 0, 0.7)',
            linewidth=1,
            # Ajustar el rango máximo para que muestre hasta 400k o un poco más
            range=[0, max(max_valor * 1.05, 400000)]
        ),
        barmode='stack',  # Usamos 'stack' para apilar Patrimonio y Deuda
        # Las barras con el mismo x se apilarán automáticamente
        height=400,
        width=600,
        margin=dict(l=60, r=50, t=80, b=60),
        paper_bgcolor='white',
        plot_bgcolor='white',
        showlegend=False
    )
    
    # Agregar anotación con el total de Deuda + Patrimonio en la parte superior de la barra apilada
    fig.add_annotation(
        x='Deuda + Patrimonio',
        y=total_pasivo,
        text=f'${total_pasivo:,.0f}'.replace(',', '.'),
        showarrow=False,
        font=dict(size=12, color='black'),
        yshift=15
    )
    
    return fig

