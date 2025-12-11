# 📝 Bitácora de Cambios - Proyecto ROE DuPont

Este documento registra la evolución del desarrollo del proyecto, detallando los cambios realizados por funcionalidad y los aprendizajes clave obtenidos durante el proceso de codificación asistida.

---

## 📅 11 de Diciembre, 2025

### 📚 Documentación Final
- **Descripción del Cambio:** Creación de un `README.md` profesional y pedagógico. Se movió el archivo a la raíz del proyecto para mejorar la visibilidad.
- **Aprendizaje:** La documentación técnica debe equilibrar las instrucciones de instalación con el contexto "de negocio" (financiero en este caso) para que el proyecto sea comprensible tanto para desarrolladores como para estudiantes.

### 📉 Funcionalidad 3: Estados Financieros Simplificados
- **Descripción del Cambio:** Implementación de gráficos de barras horizontales y apiladas para representar el Estado de Resultados y el Balance General.
- **Aprendizaje:** La visualización de datos contables requiere "limpieza" visual. Usar colores consistentes (verde para activos, azul para patrimonio) ayuda a reforzar la ecuación contable mentalmente en el usuario.

---

## 📅 10 de Diciembre, 2025

### 🧊 Funcionalidad 2: Visualización 3D (Prisma ROE)
- **Descripción del Cambio:** Desarrollo del gráfico tridimensional con `plotly.graph_objects`. Se modeló un prisma cuyos ejes (x, y, z) representan los tres componentes del DuPont.
- **Aprendizaje Clave:** Durante la generación del gráfico 3D complejo, el modo "Agente" inicial tuvo dificultades para alinear perfectamente los vértices. **Aprendizaje:** Fue más efectivo utilizar el comando/modo **/ask** o chat para iterar sobre el código específico de Plotly, en lugar de esperar que el agente resolviera toda la lógica geométrica en un solo intento.

### 🏗️ Funcionalidad 1: Cálculo de Ratios Básicos
- **Descripción del Cambio:** Configuración inicial de la app en Streamlit. Creación de sliders inputs y la lógica matemática para Margen Neto, Rotación de Activos y Apalancamiento.
- **Aprendizaje:** Streamlit es ideal para prototipado rápido financiera. Separar la lógica de cálculo de la interfaz (inputs) desde el principio facilita mantener el código ordenado.

### 🚀 Inicio del Proyecto
- **Descripción del Cambio:** Definición de la estructura de carpetas, entorno virtual (`venv`) y archivo `requirements.txt`.
- **Aprendizaje:** Establecer una estructura de proyecto sólida desde el día 0 evita problemas de importación y dependencias más adelante.
