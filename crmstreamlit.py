import streamlit as st
import pandas as pd

# Nome do arquivo CSV
CSV_FILE = "CRM_Clientes_Allcap_Trust - CRM (1).csv"

# Função para carregar os dados do CSV
def load_data():
    df = pd.read_csv(CSV_FILE)
    df.columns = df.columns.str.strip()  # Remove espaços extras dos nomes das colunas
    return df

# Função para salvar as alterações no CSV
def save_data(df):
    df.to_csv(CSV_FILE, index=False)

# Carregar os dados
df = load_data()

# Sidebar para adicionar nova oportunidade
st.sidebar.markdown("## ➕ Adicionar Nova Oportunidade")
novo_nome = st.sidebar.text_input("Nome do Cliente")
novo_contato = st.sidebar.text_input("Contato")
novo_email = st.sidebar.text_input("E-mail")
novo_telefone = st.sidebar.text_input("Telefone")
novo_cidade = st.sidebar.text_input("Cidade")
novo_estado = st.sidebar.text_input("Estado")

novo_tipo_oportunidade = st.sidebar.selectbox(
    "Tipo de Oportunidade", df["Tipo de Oportunidade"].unique()
)
novo_fase = st.sidebar.selectbox("Fase", df["Fase"].unique())
novo_tipo_cliente = st.sidebar.selectbox("Tipo de Cliente", df["Tipo de Cliente"].unique())

if st.sidebar.button("Adicionar Oportunidade"):
    # Criar um novo ID automaticamente
    novo_id = f"OP{str(len(df) + 1).zfill(3)}"

    # Criar nova linha com os dados inseridos
    nova_oportunidade = {
        "ID": novo_id,
        "Nome": novo_nome,
        "Contato": novo_contato,
        "E-mail": novo_email,
        "Telefone": novo_telefone,
        "Cidade": novo_cidade,
        "Estado": novo_estado,
        "Tipo de Oportunidade": novo_tipo_oportunidade,
        "Fase": novo_fase,
        "Tipo de Cliente": novo_tipo_cliente,
    }

    df = df.append(nova_oportunidade, ignore_index=True)  # Adicionar nova linha ao DataFrame
    save_data(df)  # Salvar no CSV
    st.sidebar.success("Oportunidade adicionada com sucesso!")
    st.experimental_rerun()  # Atualiza a página

# Interface principal
st.title("📊 CRM de Oportunidades - Allcap")
st.subheader("Gerencie suas oportunidades de forma eficiente")

st.markdown("### 📝 Oportunidades Registradas")
selecionado = st.selectbox("Selecione uma Oportunidade para Editar", df["ID"].unique())

# Verificar se a oportunidade existe antes de acessar
if selecionado in df["ID"].values:
    oportunidade = df[df["ID"] == selecionado].iloc[0]

    txt_nome = st.text_input("Nome do Cliente", oportunidade.get("Nome", ""))
    txt_contato = st.text_input("Contato", oportunidade.get("Contato", ""))
    txt_email = st.text_input("E-mail", oportunidade.get("E-mail", ""))
    txt_telefone = st.text_input("Telefone", oportunidade.get("Telefone", ""))
    txt_cidade = st.text_input("Cidade", oportunidade.get("Cidade", ""))
    txt_estado = st.text_input("Estado", oportunidade.get("Estado", ""))

    txt_tipo_oportunidade = st.selectbox(
        "Tipo de Oportunidade", df["Tipo de Oportunidade"].unique(), 
        index=list(df["Tipo de Oportunidade"].unique()).index(oportunidade.get("Tipo de Oportunidade", ""))
    )

    txt_fase = st.selectbox("Fase", df["Fase"].unique(), 
        index=list(df["Fase"].unique()).index(oportunidade.get("Fase", ""))
    )

    txt_tipo_cliente = st.selectbox("Tipo de Cliente", df["Tipo de Cliente"].unique(), 
        index=list(df["Tipo de Cliente"].unique()).index(oportunidade.get("Tipo de Cliente", ""))
    )

    if st.button("Salvar Alterações"):
        df.loc[df["ID"] == selecionado, "Nome"] = txt_nome
        df.loc[df["ID"] == selecionado, "Contato"] = txt_contato
        df.loc[df["ID"] == selecionado, "E-mail"] = txt_email
        df.loc[df["ID"] == selecionado, "Telefone"] = txt_telefone
        df.loc[df["ID"] == selecionado, "Cidade"] = txt_cidade
        df.loc[df["ID"] == selecionado, "Estado"] = txt_estado
        df.loc[df["ID"] == selecionado, "Tipo de Oportunidade"] = txt_tipo_oportunidade
        df.loc[df["ID"] == selecionado, "Fase"] = txt_fase
        df.loc[df["ID"] == selecionado, "Tipo de Cliente"] = txt_tipo_cliente

        save_data(df)
        st.success("Oportunidade atualizada com sucesso!")
        st.experimental_rerun()
else:
    st.warning("Oportunidade não encontrada. Verifique se o ID está correto.")

