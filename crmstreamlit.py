import streamlit as st
import pandas as pd

# Carregar os dados do CRM (substituir pelo caminho correto do arquivo ou integrar a um banco de dados)
data = {
    "ID": ["OP001", "OP002", "OP003"],
    "Nome": ["Carla Patricia", "Elton e Jordana", "Juliana Vzinha"],
    "Tipo de Oportunidade": ["Venda", "Parceria Comercial", "Parceria Comercial"],
    "Fase": ["Proposta Aprovada", "Lead Em Potencial", "Lead Em Potencial"],
    "Produto/Solução": ["Home Equity", "Home Equity", "Home Equity"],
    "Valor Estimado (R$)": [550000, 600000, 300000],
    "Etapa no Funil": ["Fechado", "Aguardando Contato", "Aguardando Contato"],
    "Responsável": ["Adriele Valêncio", "Bruno Cordeiro", "Bruno Cordeiro"],
    "Probabilidade (%)": [90, 70, 60]
}

df = pd.DataFrame(data)

# Configuração do layout do Streamlit
st.set_page_config(page_title="CRM - Allcap", layout="wide")

# Título do Dashboard
st.title("📊 CRM de Oportunidades - Allcap")

# Filtro de status do funil de vendas
status_selecionado = st.sidebar.selectbox("Filtrar por Status:", df["Fase"].unique())

# Aplicar filtro
filtro_df = df[df["Fase"] == status_selecionado]

# Exibir o DataFrame filtrado
st.dataframe(filtro_df, use_container_width=True)

# Seção de detalhes
st.subheader("📌 Detalhes da Oportunidade")
selecionado = st.selectbox("Selecione uma Oportunidade:", df["ID"])
detalhes = df[df["ID"] == selecionado].iloc[0]

st.write(f"**Nome:** {detalhes['Nome']}")
st.write(f"**Produto/Solução:** {detalhes['Produto/Solução']}")
st.write(f"**Valor Estimado:** R$ {detalhes['Valor Estimado (R$)']:,}")
st.write(f"**Responsável:** {detalhes['Responsável']}")

# Gráfico de probabilidade de fechamento
st.subheader("🔮 Probabilidade de Fechamento")
st.progress(int(detalhes["Probabilidade (%)"]))
