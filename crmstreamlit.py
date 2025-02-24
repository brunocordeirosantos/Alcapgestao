import streamlit as st
import pandas as pd

# URL do CSV no GitHub
github_url = "https://raw.githubusercontent.com/brunocordeirosantos/Alcapgestao/main/CRM_Clientes_Allcap_Trust%20-%20CRM%20(1).csv"

def load_data():
    try:
        df = pd.read_csv(github_url, delimiter=',', encoding='utf-8', dtype=str)
        df.fillna("", inplace=True)  # Preenchendo valores nulos
        return df
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return pd.DataFrame()

# Carregar dados
df = load_data()

st.title("📊 CRM de Oportunidades - Allcap")
st.subheader("Gerencie suas oportunidades de forma eficiente")

# Seção para exibir e editar oportunidades
st.markdown("### 📋 Oportunidades Registradas")
if not df.empty:
    selected_id = st.selectbox("Selecione uma Oportunidade para Editar", df["ID"])
    oportunidade = df[df["ID"] == selected_id].iloc[0]

    # Criando campos editáveis
    col1, col2 = st.columns(2)
    with col1:
        nome = st.text_input("Nome do Cliente", oportunidade["Nome "])
        contato = st.text_input("Contato", oportunidade["Contato "])
        email = st.text_input("E-mail", oportunidade["E-mail "])
        telefone = st.text_input("Telefone", oportunidade["Telefone"])
        cidade = st.text_input("Cidade", oportunidade["Cidade"])
        estado = st.text_input("Estado", oportunidade["Estado "])
    
    with col2:
        tipo_oportunidade = st.selectbox("Tipo de Oportunidade", df["Tipo de Oportunidade"].unique(), index=list(df["Tipo de Oportunidade"]).index(oportunidade["Tipo de Oportunidade"]))
        fase = st.selectbox("Fase", df["Fase"].unique(), index=list(df["Fase"]).index(oportunidade["Fase"]))
        tipo_cliente = st.selectbox("Tipo de Cliente", df["Tipo de Cliente"].unique(), index=list(df["Tipo de Cliente"]).index(oportunidade["Tipo de Cliente"]))
        valor_estimado = st.text_input("Valor Estimado (R$)", oportunidade["Valor Estimado (R$)"])
        etapa_funnel = st.text_input("Etapa no Funil de Vendas", oportunidade["Etapa no Funil de Vendas"])
        proxima_acao = st.text_input("Próxima Ação", oportunidade["Próxima Ação"])
    
    # Botão para salvar alterações
    if st.button("Salvar Alterações"):
        df.loc[df["ID"] == selected_id, ["Nome ", "Contato ", "E-mail ", "Telefone", "Cidade", "Estado ", "Tipo de Oportunidade", "Fase", "Tipo de Cliente", "Valor Estimado (R$)", "Etapa no Funil de Vendas", "Próxima Ação"]] = [
            nome, contato, email, telefone, cidade, estado, tipo_oportunidade, fase, tipo_cliente, valor_estimado, etapa_funnel, proxima_acao
        ]
        st.success("Alterações salvas com sucesso!")

    st.dataframe(df)
else:
    st.warning("Nenhuma oportunidade encontrada.")
