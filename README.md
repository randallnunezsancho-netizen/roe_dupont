# 📊 ROE DuPont Interactivo
### Herramienta Pedagógica de Análisis Financiero

> **Nota Educativa:** Este proyecto ha sido desarrollado con fines exclusivamente pedagógicos para la enseñanza de programación financiera con Python. No debe utilizarse como asesoramiento financiero profesional.

---

## 📖 Descripción General

**ROE DuPont Interactivo** es una aplicación web desarrollada en Python que permite a estudiantes y profesionales visualizar la descomposición del **Retorno sobre el Patrimonio (ROE)** utilizando el modelo DuPont. 

A diferencia de las calculadoras tradicionales, esta herramienta ofrece una experiencia visual inmersiva mediante gráficos interactivos y modelado 3D, facilitando la comprensión intuitiva de cómo tres palancas financieras clave (Margen, Rotación y Apalancamiento) interactúan para generar rentabilidad.

### 🎯 Propósito
El objetivo principal es ilustrar conceptos financieros complejos de manera visual e interactiva, demostrando al mismo tiempo el potencial de Python (Streamlit + Plotly) para la creación de dashboards financieros modernos.

---

## 🚀 Características Principales

El proyecto incluye tres módulos funcionales integrados:

### 1. 🧮 Calculadora de Ratios Financieros
- **Sliders Interactivos:** Ajuste dinámico de 4 variables clave:
  - Utilidad Neta
  - Ventas
  - Activos Promedio
  - Patrimonio Promedio
- **Cálculo Automático:** Determinación en tiempo real de:
  - **Margen Neto:** Eficiencia en costos.
  - **Rotación de Activos:** Eficiencia en el uso de recursos.
  - **Apalancamiento Financiero:** Uso de deuda vs. capital.
  - **ROE:** indicador final de rentabilidad.

### 2. 🧊 Visualización 3D (Prisma DuPont)
- **Gráfico Tridimensional:** Representación del ROE como el volumen de un prisma cuyos lados son los tres componentes del modelo.
- **Interactividad:** El prisma cambia de forma y tamaño en tiempo real según los inputs, permitiendo ver físicamente el impacto de cada variable.

### 3. 📉 Estados Financieros Simplificados
- **Estado de Resultados:** Gráfico de barras horizontales mostrando la relación entre Ventas, Gastos y Utilidad.
- **Balance General:** Gráfico de barras apiladas que visualiza la Ecuación Contable Fundamental (*Activos = Pasivo + Patrimonio*).

---

## ⚙️ Requisitos Técnicos

Para ejecutar este proyecto necesitas tener instalado:

- **Lenguaje:** Python 3.9 o superior.
- **Librerías principales:**
  - `streamlit`: Para la interfaz web.
  - `plotly`: Para los gráficos interactivos 2D y 3D.
  - `pandas` y `numpy`: Para manejo de datos (implícitos).

El archivo `documentos/requirements.txt` contiene las versiones específicas:
```text
streamlit>=1.28.0
numpy>=1.24.0
pandas>=2.0.0
plotly>=5.17.0
```

---

## 🛠️ Instrucciones de Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clonar o Descargar el Proyecto
Asegúrate de tener los archivos en tu carpeta local.

### 2. Crear un Entorno Virtual
Es recomendable usar un entorno virtual para aislar las dependencias:

**Windows:**
```powershell
python -m venv venv
.\venv\Scripts\activate
```

**macOS / Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar Dependencias
Instala las librerías necesarias ejecutando:

```bash
pip install -r requirements.txt
```

---

## ▶️ Guía de Uso

Una vez instalado, ejecuta la aplicación desde la terminal (estando en la carpeta raíz del proyecto):

```bash
streamlit run app.py
```

Esto abrirá automáticamente una pestaña en tu navegador web (usualmente en `http://localhost:8501`) donde podrás:

1. **Ajustar Variables:** Usa la barra lateral izquierda para modificar los valores de Ventas, Utilidad, Activos y Patrimonio.
2. **Analizar Métricas:** Observa cómo cambian los KPIs en la parte superior.
3. **Explorar el Prisma:** Interactúa con el gráfico 3D (zoom, rotación) para entender la composición del ROE.
4. **Revisar Estados:** Consulta los gráficos al final de la página para ver el impacto contable.

---

## 📂 Estructura del Proyecto

A continuación se muestran los archivos clave del proyecto:

```
roe_dupont/
│
├── app.py                      # 🐍 Código fuente principal de la aplicación
├── requirements.txt            # 📦 Lista de dependencias (Movido a raíz)
├── Bitácora_cambios.md         # 📝 Registro de cambios y aprendizajes
├── venv/                       # 🔧 Entorno virtual (no incluido en control de versiones)
│
└── documentos/                 # 📄 Documentación del proyecto
    ├── funcionalidades_proyecto.md # Especificación detallada de funciones
    └── reglasproyecto.mdc      # Reglas de codificación
```

---

## 🎓 Interpretación de Resultados (Modelo DuPont)

La aplicación se basa en la siguiente fórmula fundamental:

$$
ROE = \text{Margen Neto} \times \text{Rotación de Activos} \times \text{Apalancamiento}
$$

1. **Margen Neto (%)**: ¿Cuánto ganamos por cada dólar vendido?  
   *(Refleja eficiencia operativa y estrategia de precios)*
2. **Rotación de Activos (veces)**: ¿Cuántos dólares generamos en ventas por cada dólar invertido en activos?  
   *(Refleja eficiencia en el uso de activos)*
3. **Apalancamiento (veces)**: ¿Cuántos activos controlamos por cada dólar de patrimonio?  
   *(Refleja la estrategia de financiamiento/deuda)*

El gráfico 3D ayuda a visualizar que aumentar cualquiera de estas tres dimensiones incrementa el "volumen" total de rentabilidad para el accionista.

---

## ⚖️ Licencia

Este proyecto es Open Source bajo la licencia **MIT**, permitiendo su uso libre para fines educativos y personales.

**Desarrollado para el curso de Python Financiero & Antigravity.**
