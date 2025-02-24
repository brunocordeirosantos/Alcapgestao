import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="CRM de Oportunidades - Allcap", layout="wide")

# Inicializar o dataframe no cache do Streamlit (evita perda de dados ao interagir com a interface)
if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(columns=[
        "ID", "Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado", 
        "Tipo de Oportunidade", "Fase", "Tipo de Cliente"
    ])

df = st.session_state.df  # Atribuir ao dataframe local para facilitar a manipulação

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

# Opções pré-definidas para os campos
tipos_oportunidade = ["Venda", "Parceria Comercial", "Outros"]
fases = ["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado"]
tipos_cliente = ["PF", "PJ"]

novo_tipo_oportunidade = st.sidebar.selectbox("Tipo de Oportunidade", tipos_oportunidade)
novo_fase = st.sidebar.selectbox("Fase", fases)
novo_tipo_cliente = st.sidebar.selectbox("Tipo de Cliente", tipos_cliente)

# Botão para adicionar a nova oportunidade
if st.sidebar.button("Adicionar Oportunidade"):
    novo_id = f"OP{len(df) + 1:03d}"  # Gera um novo ID automático
    nova_linha = pd.DataFrame([[novo_id, novo_nome, novo_contato, novo_email, novo_telefone, 
                                 novo_cidade, novo_estado, novo_tipo_oportunidade, novo_fase, novo_tipo_cliente]], 
                               columns=df.columns)
    st.session_state.df = pd.concat([df, nova_linha], ignore_index=True)
    st.success(f"Oportunidade {novo_id} adicionada com sucesso!")
    st.rerun()  # Atualiza a página para refletir as mudanças

# Layout para edição de oportunidades
st.markdown("### 📑 Oportunidades Registradas")

# Selecionar oportunidade para editar
if len(df) > 0:
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

        txt_tipo_oportunidade = st.selectbox("Tipo de Oportunidade", tipos_oportunidade, index=tipos_oportunidade.index(oportunidade["Tipo de Oportunidade"]))
        txt_fase = st.selectbox("Fase", fases, index=fases.index(oportunidade["Fase"]))
        txt_tipo_cliente = st.selectbox("Tipo de Cliente", tipos_cliente, index=tipos_cliente.index(oportunidade["Tipo de Cliente"]))

        if st.button("Salvar Alterações"):
            df.loc[df["ID"] == oportunidade_id, ["Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado", "Tipo de Oportunidade", "Fase", "Tipo de Cliente"]] = \
                [txt_nome, txt_contato, txt_email, txt_telefone, txt_cidade, txt_estado, txt_tipo_oportunidade, txt_fase, txt_tipo_cliente]
            st.session_state.df = df
            st.success("Alterações salvas com sucesso!")
            st.rerun()  # Atualiza a página para refletir as mudanças

else:
    st.info("Nenhuma oportunidade cadastrada. Adicione uma nova para começar!")
