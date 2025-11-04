"""
Módulo de Cálculos Financieros - Modelo DuPont

Este módulo contiene las funciones para calcular los componentes del modelo DuPont
y el ROE (Return on Equity).

Modelo DuPont descompone el ROE en tres componentes:
1. Margen Neto = Utilidad Neta / Ventas
2. Rotación de Activos = Ventas / Activos Promedio
3. Apalancamiento Financiero = Activos Promedio / Patrimonio Promedio

ROE = Margen Neto × Rotación de Activos × Apalancamiento Financiero
"""


def calcular_margen_neto(utilidad_neta: float, ventas: float) -> float:
    """
    Calcula el margen neto de utilidad.
    
    Parámetros:
    -----------
    utilidad_neta : float
        Utilidad neta del período
    ventas : float
        Ventas totales del período
        
    Retorna:
    --------
    float
        Margen neto expresado como decimal (ej: 0.15 = 15%)
        
    Ejemplo:
    --------
    >>> calcular_margen_neto(150000, 1000000)
    0.15
    """
    if ventas == 0:
        return 0.0
    return utilidad_neta / ventas


def calcular_rotacion_activos(ventas: float, activos_promedio: float) -> float:
    """
    Calcula la rotación de activos.
    
    Parámetros:
    -----------
    ventas : float
        Ventas totales del período
    activos_promedio : float
        Promedio de activos totales
        
    Retorna:
    --------
    float
        Rotación de activos (veces que se rotan los activos)
        
    Ejemplo:
    --------
    >>> calcular_rotacion_activos(1000000, 500000)
    2.0
    """
    if activos_promedio == 0:
        return 0.0
    return ventas / activos_promedio


def calcular_apalancamiento_financiero(activos_promedio: float, patrimonio_promedio: float) -> float:
    """
    Calcula el apalancamiento financiero.
    
    Parámetros:
    -----------
    activos_promedio : float
        Promedio de activos totales
    patrimonio_promedio : float
        Promedio de patrimonio
        
    Retorna:
    --------
    float
        Multiplicador de apalancamiento financiero
        
    Ejemplo:
    --------
    >>> calcular_apalancamiento_financiero(500000, 250000)
    2.0
    """
    if patrimonio_promedio == 0:
        return 0.0
    return activos_promedio / patrimonio_promedio


def calcular_roe(margen_neto: float, rotacion_activos: float, apalancamiento: float) -> float:
    """
    Calcula el ROE (Return on Equity) usando el modelo DuPont.
    
    Parámetros:
    -----------
    margen_neto : float
        Margen neto de utilidad (como decimal)
    rotacion_activos : float
        Rotación de activos
    apalancamiento : float
        Apalancamiento financiero
        
    Retorna:
    --------
    float
        ROE expresado como decimal (ej: 0.30 = 30%)
        
    Ejemplo:
    --------
    >>> calcular_roe(0.15, 2.0, 2.0)
    0.6
    """
    return margen_neto * rotacion_activos * apalancamiento


def calcular_componentes_dupont(utilidad_neta: float, ventas: float, 
                                activos_promedio: float, patrimonio_promedio: float) -> dict:
    """
    Calcula todos los componentes del modelo DuPont a partir de las variables base.
    
    Parámetros:
    -----------
    utilidad_neta : float
        Utilidad neta del período
    ventas : float
        Ventas totales del período
    activos_promedio : float
        Promedio de activos totales
    patrimonio_promedio : float
        Promedio de patrimonio
        
    Retorna:
    --------
    dict
        Diccionario con todos los componentes calculados:
        - margen_neto: Margen neto (decimal)
        - rotacion_activos: Rotación de activos
        - apalancamiento: Apalancamiento financiero
        - roe: Return on Equity (decimal)
    """
    margen_neto = calcular_margen_neto(utilidad_neta, ventas)
    rotacion_activos = calcular_rotacion_activos(ventas, activos_promedio)
    apalancamiento = calcular_apalancamiento_financiero(activos_promedio, patrimonio_promedio)
    roe = calcular_roe(margen_neto, rotacion_activos, apalancamiento)
    
    return {
        'margen_neto': margen_neto,
        'rotacion_activos': rotacion_activos,
        'apalancamiento': apalancamiento,
        'roe': roe
    }

