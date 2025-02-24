import streamlit as st
import pandas as pd

# Carregar os dados do CSV no GitHub
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/brunocordeirosantos/Alcapgestao/main/CRM_Clientes_Allcap_Trust%20-%20CRM%20(1).csv"
    df = pd.read_csv(url, delimiter=",", encoding="utf-8")
    return df

df = load_data()

st.set_page_config(page_title="CRM de Oportunidades - Allcap", layout="wide")

# Layout Principal
st.title("📊 CRM de Oportunidades - Allcap")
st.subheader("Gerencie suas oportunidades de forma eficiente")

# Sidebar - Adicionar nova oportunidade
st.sidebar.markdown("## ➕ Adicionar Nova Oportunidade")

novo_nome = st.sidebar.text_input("Nome do Cliente")
novo_contato = st.sidebar.text_input("Contato")
novo_email = st.sidebar.text_input("E-mail")
novo_telefone = st.sidebar.text_input("Telefone")
novo_cidade = st.sidebar.text_input("Cidade")
novo_estado = st.sidebar.text_input("Estado")

# Evita duplicidade de elementos
tipos_oportunidade = df["Tipo de Oportunidade"].dropna().unique().tolist() if "Tipo de Oportunidade" in df.columns else []
fases = df["Fase"].dropna().unique().tolist() if "Fase" in df.columns else []
tipos_cliente = df["Tipo de Cliente"].dropna().unique().tolist() if "Tipo de Cliente" in df.columns else []

novo_tipo_oportunidade = st.sidebar.selectbox("Tipo de Oportunidade", tipos_oportunidade, index=0 if tipos_oportunidade else None)
novo_fase = st.sidebar.selectbox("Fase", fases, index=0 if fases else None)
novo_tipo_cliente = st.sidebar.selectbox("Tipo de Cliente", tipos_cliente, index=0 if tipos_cliente else None)

# Botão para adicionar a nova oportunidade
if st.sidebar.button("Adicionar Oportunidade"):
    novo_id = f"OP{len(df) + 1:03d}"
    nova_linha = pd.DataFrame(
        [[novo_id, novo_nome, novo_contato, novo_email, novo_telefone, novo_cidade, novo_estado, novo_tipo_oportunidade, novo_fase, novo_tipo_cliente]],
        columns=["ID", "Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado", "Tipo de Oportunidade", "Fase", "Tipo de Cliente"]
    )
    df = pd.concat([df, nova_linha], ignore_index=True)
    st.success(f"Oportunidade {novo_id} adicionada com sucesso!")

# Layout para edição de oportunidades
st.markdown("### 📑 Oportunidades Registradas")

# Selecionar oportunidade para editar
oportunidade_id = st.selectbox("Selecione uma Oportunidade para Editar", df["ID"].unique())

# Exibir os dados da oportunidade selecionada
if oportunidade_id:
    oportunidade = df[df["ID"] == oportunidade_id].iloc[0]

    txt_nome = st.text_input("Nome do Cliente", oportunidade["Nome"])
    txt_contato = st.text_input("Contato", oportunidade["Contato"])
    txt_email = st.text_input("E-mail", oportunidade["E-mail"])
    txt_telefone = st.text_input("Telefone", oportunidade["Telefone"])
    txt_cidade = st.text_input("Cidade", oportunidade["Cidade"])
    txt_estado = st.text_input("Estado", oportunidade["Estado"])

    txt_tipo_oportunidade = st.selectbox("Tipo de Oportunidade", tipos_oportunidade, index=tipos_oportunidade.index(oportunidade["Tipo de Oportunidade"]) if oportunidade["Tipo de Oportunidade"] in tipos_oportunidade else 0)
    txt_fase = st.selectbox("Fase", fases, index=fases.index(oportunidade["Fase"]) if oportunidade["Fase"] in fases else 0)
    txt_tipo_cliente = st.selectbox("Tipo de Cliente", tipos_cliente, index=tipos_cliente.index(oportunidade["Tipo de Cliente"]) if oportunidade["Tipo de Cliente"] in tipos_cliente else 0)

    if st.button("Salvar Alterações"):
        df.loc[df["ID"] == oportunidade_id, ["Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado", "Tipo de Oportunidade", "Fase", "Tipo de Cliente"]] = \
            [txt_nome, txt_contato, txt_email, txt_telefone, txt_cidade, txt_estado, txt_tipo_oportunidade, txt_fase, txt_tipo_cliente]
        st.success("Alterações salvas com sucesso!")
