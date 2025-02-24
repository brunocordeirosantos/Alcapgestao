import streamlit as st
import pandas as pd

# Função para carregar dados do CRM a partir da planilha existente
def load_data():
    try:
        df = pd.read_csv("crm_data.csv")  # Nome do arquivo CSV que armazena os dados
    except FileNotFoundError:
        df = pd.DataFrame(columns=["ID", "Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado", "Tipo de Oportunidade",
                                   "Fase", "Tipo de Cliente", "Segmento de Mercado do Cliente", "Produto/Solução Específica",
                                   "Valor Estimado (R$)", "Prazo Desejado (meses)", "Taxa de Juros (Estimativa)", "Etapa no Funil de Vendas",
                                   "Data da Última Interação", "Próxima Ação", "Responsável pela Oportunidade", "Probabilidade de Fechamento (%)",
                                   "Valor Total (R$)", "Data de Fechamento", "Notas/Comentários Adicionais", "Histórico de Interações"])
    return df

# Carregar dados existentes
df = load_data()

# Interface do Streamlit
st.set_page_config(page_title="CRM - Allcap", layout="wide")

# Título do Dashboard
st.title("📊 CRM de Oportunidades - Allcap")

# Exibir as oportunidades cadastradas
st.subheader("📌 Oportunidades Registradas")
st.dataframe(df, use_container_width=True)

# Seção de detalhes da oportunidade
st.subheader("🔍 Detalhes da Oportunidade")
selecionado = st.selectbox("Selecione uma Oportunidade:", df["ID"])
detalhes = df[df["ID"] == selecionado].iloc[0]

st.write(f"**Nome:** {detalhes['Nome']}")
st.write(f"**Contato:** {detalhes['Contato']}")
st.write(f"**E-mail:** {detalhes['E-mail']}")
st.write(f"**Telefone:** {detalhes['Telefone']}")
st.write(f"**Cidade:** {detalhes['Cidade']}, {detalhes['Estado']}")
st.write(f"**Tipo de Oportunidade:** {detalhes['Tipo de Oportunidade']}")
st.write(f"**Fase:** {detalhes['Fase']}")
st.write(f"**Produto/Solução:** {detalhes['Produto/Solução Específica']}")
st.write(f"**Valor Estimado:** R$ {detalhes['Valor Estimado (R$)']:,}")
st.write(f"**Taxa de Juros Estimada:** {detalhes['Taxa de Juros (Estimativa)']}")
st.write(f"**Etapa no Funil:** {detalhes['Etapa no Funil de Vendas']}")
st.write(f"**Data da Última Interação:** {detalhes['Data da Última Interação']}")
st.write(f"**Próxima Ação:** {detalhes['Próxima Ação']}")
st.write(f"**Responsável:** {detalhes['Responsável pela Oportunidade']}")
st.write(f"**Probabilidade de Fechamento:** {detalhes['Probabilidade de Fechamento (%)']}%")
st.write(f"**Valor Total Estimado:** R$ {detalhes['Valor Total (R$)']:,}")
st.write(f"**Data Prevista de Fechamento:** {detalhes['Data de Fechamento']}")
st.write(f"**Notas/Comentários:** {detalhes['Notas/Comentários Adicionais']}")
st.write(f"**Histórico de Interações:** {detalhes['Histórico de Interações']}")

# Gráfico de probabilidade de fechamento
st.subheader("📈 Probabilidade de Fechamento")
st.progress(int(detalhes["Probabilidade de Fechamento (%)"]))
