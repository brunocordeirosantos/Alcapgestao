import streamlit as st
import pandas as pd

# URL do arquivo CSV no GitHub
CSV_URL = "https://raw.githubusercontent.com/brunocordeirosantos/Alcapgestao/main/CRM_Clientes_Allcap_Trust%20-%20CRM%20(1).csv"

@st.cache_data
def load_data():
    try:
        df = pd.read_csv(CSV_URL, sep=",", encoding="utf-8", dtype=str)
        return df.fillna("")  # Preenchendo valores nulos com string vazia para evitar erros
    except Exception as e:
        st.error(f"Erro ao carregar os dados: {e}")
        return pd.DataFrame()

def save_data(df):
    df.to_csv("CRM_Clientes_Allcap_Trust - CRM (1).csv", index=False)

st.title("📊 CRM de Oportunidades - Allcap")
st.subheader("Gerencie suas oportunidades de forma eficiente")

df = load_data()

# Barra lateral para adicionar nova oportunidade
st.sidebar.header("➕ Adicionar Nova Oportunidade")
novo_nome = st.sidebar.text_input("Nome do Cliente")
novo_contato = st.sidebar.text_input("Contato")
novo_email = st.sidebar.text_input("E-mail")
novo_telefone = st.sidebar.text_input("Telefone")
novo_cidade = st.sidebar.text_input("Cidade")
novo_estado = st.sidebar.text_input("Estado")
novo_tipo_op = st.sidebar.selectbox("Tipo de Oportunidade", ["Venda", "Parceria Comercial", "Venda, Parceria Comercial"])
novo_fase = st.sidebar.selectbox("Fase", ["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado Perdido"])
novo_tipo_cliente = st.sidebar.selectbox("Tipo de Cliente", ["PF", "PJ"])
novo_valor = st.sidebar.text_input("Valor Estimado (R$)")

if st.sidebar.button("Adicionar Oportunidade"):
    novo_id = f"OP{len(df) + 1:03}"  # Gera um ID único
    nova_oportunidade = {
        "ID": novo_id,
        "Nome": novo_nome,
        "Contato": novo_contato,
        "E-mail": novo_email,
        "Telefone": novo_telefone,
        "Cidade": novo_cidade,
        "Estado": novo_estado,
        "Tipo de Oportunidade": novo_tipo_op,
        "Fase": novo_fase,
        "Tipo de Cliente": novo_tipo_cliente,
        "Valor Estimado (R$)": novo_valor,
    }
    df = df.append(nova_oportunidade, ignore_index=True)
    save_data(df)
    st.sidebar.success("Oportunidade adicionada com sucesso!")

# Selecionar oportunidade para edição
st.subheader("📋 Oportunidades Registradas")
selecao = st.selectbox("Selecione uma Oportunidade para Editar", df["ID"].tolist())

if selecao:
    oportunidade = df[df["ID"] == selecao].iloc[0]
    txt_nome = st.text_input("Nome do Cliente", oportunidade["Nome"])
    txt_contato = st.text_input("Contato", oportunidade["Contato"])
    txt_email = st.text_input("E-mail", oportunidade["E-mail"])
    txt_telefone = st.text_input("Telefone", oportunidade["Telefone"])
    txt_cidade = st.text_input("Cidade", oportunidade["Cidade"])
    txt_estado = st.text_input("Estado", oportunidade["Estado"])
    txt_tipo_op = st.selectbox("Tipo de Oportunidade", ["Venda", "Parceria Comercial", "Venda, Parceria Comercial"], index=["Venda", "Parceria Comercial", "Venda, Parceria Comercial"].index(oportunidade["Tipo de Oportunidade"]))
    txt_fase = st.selectbox("Fase", ["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado Perdido"], index=["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado Perdido"].index(oportunidade["Fase"]))
    txt_tipo_cliente = st.selectbox("Tipo de Cliente", ["PF", "PJ"], index=["PF", "PJ"].index(oportunidade["Tipo de Cliente"]))
    txt_valor = st.text_input("Valor Estimado (R$)", oportunidade["Valor Estimado (R$)"])

    if st.button("Salvar Alterações"):
        df.loc[df["ID"] == selecao, ["Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado", "Tipo de Oportunidade", "Fase", "Tipo de Cliente", "Valor Estimado (R$)"]] = [txt_nome, txt_contato, txt_email, txt_telefone, txt_cidade, txt_estado, txt_tipo_op, txt_fase, txt_tipo_cliente, txt_valor]
        save_data(df)
        st.success("Alterações salvas com sucesso!")
