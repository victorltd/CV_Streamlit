import streamlit as st

# Dados dos projetos
PROJECTS = {
    "🛰️ Weather Station for Aerodesign Competition": {
        "description": "An application where competitors of Aerodesign Competition could see meteorological data. Designed and developed in HTML, CSS and JavaScript, using ESP8266 and BMP280 as sensor. Backend implemented on Google Firebase.",
        "github_url": "https://github.com/victorltd/TCC",
        "image": "assets/project1.png"
    },
    "📡 Telemetry System for Aerodesign (F-Carranca)": {
        "description": "Assembly and implementation of embedded telemetry to obtain in-flight data using Arduino, ESP32, and Pixhawk flight controller. Data was processed and shared with other sectors.",
        "github_url": "https://github.com/victorltd/TCC",
        "image": "assets/project2.png"
    },
    "📊 Brazilian Federal Highway (BR) Accident Analysis with Streamlit": {
        "description": "Developed an interactive Streamlit dashboard to analyze open data from the PRF (Brazilian Federal Highway Police) regarding accidents on national highways.",
        "github_url": "https://github.com/victorltd/Streamlit_PRF",
        "image": "assets/project3.png"
    }
}

# Configuração da página
st.set_page_config(page_title="Projects | Victor Augusto", page_icon="🚀")

# Título da página
st.title("Projects & Accomplishments")
st.write("---")

# Layout em colunas para exibir os projetos
columns = st.columns(3)  # Divide a página em 3 colunas

# Itera sobre os projetos e distribui entre as colunas
for index, (project_name, project_details) in enumerate(PROJECTS.items()):
    col = columns[index % 3]  # Alterna entre as colunas
    with col:
        st.image(project_details["image"], use_column_width=True)  # Adiciona a imagem
        st.subheader(project_name)
        st.write(project_details["description"])
        if project_details.get("github_url"):
            st.markdown(f"[View on GitHub]({project_details['github_url']})")
        st.write("")  # Adiciona um pequeno espaço entre os projetos