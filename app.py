import streamlit as st

# ============================================================
# CONFIGURACIÓN DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Predicción de Depósitos a Plazo",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================
# TÍTULO PRINCIPAL
# ============================================================

st.title("🏦 Sistema Inteligente de Predicción de Depósitos a Plazo")

st.markdown("""
### Bienvenido

Esta aplicación utiliza técnicas de **Machine Learning** para estimar la probabilidad
de que un cliente acepte la oferta de un **depósito a plazo** durante una campaña de
telemarketing bancario.

El objetivo es ayudar a priorizar los clientes con mayor probabilidad de contratación,
permitiendo optimizar los recursos comerciales y maximizar el beneficio esperado de la campaña.
""")

st.divider()

# ============================================================
# DESCRIPCIÓN GENERAL
# ============================================================

col1, col2 = st.columns(2)

with col1:

    st.subheader("🎯 Objetivo")

    st.info("""
Identificar clientes con alta probabilidad de contratar un depósito a plazo
mediante un modelo predictivo basado en aprendizaje automático.
""")

with col2:

    st.subheader("🧠 Modelo utilizado")

    st.success("""
**Regresión Logística Balanceada**

Pipeline de Machine Learning compuesto por:

- OneHotEncoder
- StandardScaler
- SelectKBest
- SelectFromModel
- Logistic Regression

La clasificación utiliza un **threshold optimizado**
para maximizar el beneficio esperado.
""")

st.divider()

# ============================================================
# FUNCIONALIDADES
# ============================================================

st.subheader("📌 Funcionalidades")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
### 📋 Predicción individual

Permite ingresar manualmente la información
de un cliente para estimar su probabilidad
de contratar un depósito a plazo.

Incluye:

- Probabilidad estimada
- Clasificación
- Recomendación comercial
""")

with col2:

    st.markdown("""
### 📂 Predicción masiva

Permite cargar un archivo CSV o Excel con
múltiples clientes para realizar predicciones
de forma automática.

Incluye:

- Predicción por cliente
- Probabilidad
- Descarga de resultados

*(Disponible próximamente.)*
""")

st.divider()

# ============================================================
# INFORMACIÓN DEL PROYECTO
# ============================================================

st.subheader("📊 Información del proyecto")

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "Modelo",
        "Regresión Logística"
    )

with col2:

    st.metric(
        "Variables de entrada",
        "20"
    )

with col3:

    st.metric(
        "Variable objetivo",
        "Depósito a plazo"
    )

st.divider()

# ============================================================
# MENSAJE FINAL
# ============================================================

st.info("""
👈 Utilice el menú lateral para acceder a las diferentes funcionalidades de la aplicación.
""")