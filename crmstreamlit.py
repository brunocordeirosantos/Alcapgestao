import streamlit as st
import pandas as pd

# Caminho do arquivo CSV no GitHub
CSV_URL = "https://raw.githubusercontent.com/brunocordeirosantos/Alcapgestao/main/CRM_Clientes_Allcap_Trust%20-%20CRM%20(1).csv"

# Função para carregar os dados
def load_data():
    df = pd.read_csv(CSV_URL, encoding='utf-8', sep=',')
    return df

# Carrega os dados do CSV
df = load_data()

# Função para salvar nova oportunidade
def save_new_opportunity(new_opportunity):
    global df
    new_df = pd.DataFrame([new_opportunity])
    df = pd.concat([df, new_df], ignore_index=True)
    st.success("Oportunidade adicionada com sucesso!")

# Sidebar para adicionar nova oportunidade
st.sidebar.header("➕ Adicionar Nova Oportunidade")
with st.sidebar.form("nova_oportunidade_form"):
    novo_nome = st.text_input("Nome do Cliente")
    novo_contato = st.text_input("Contato")
    novo_email = st.text_input("E-mail")
    novo_telefone = st.text_input("Telefone")
    nova_cidade = st.text_input("Cidade")
    novo_estado = st.text_input("Estado")
    novo_tipo_op = st.selectbox("Tipo de Oportunidade", df["Tipo de Oportunidade"].unique())
    nova_fase = st.selectbox("Fase", df["Fase"].unique())
    novo_tipo_cliente = st.selectbox("Tipo de Cliente", df["Tipo de Cliente"].unique())
    novo_segmento = st.selectbox("Segmento de Mercado do Cliente", df["Segmento de Mercado do Cliente"].unique())
    novo_produto = st.text_input("Produto/Solução Específica")
    novo_valor = st.text_input("Valor Estimado (R$)")
    nova_etapa_f = st.text_input("Etapa no Funil de Vendas")
    nova_proxima_acao = st.text_input("Próxima Ação")
    novo_responsavel = st.text_input("Responsável pela Oportunidade")
    
    submit = st.form_submit_button("Adicionar Oportunidade")
    if submit:
        new_opportunity = {
            "ID": f"OP{len(df) + 1:03}",
            "Nome": novo_nome,
            "Contato": novo_contato,
            "E-mail": novo_email,
            "Telefone": novo_telefone,
            "Cidade": nova_cidade,
            "Estado": novo_estado,
            "Tipo de Oportunidade": novo_tipo_op,
            "Fase": nova_fase,
            "Tipo de Cliente": novo_tipo_cliente,
            "Segmento de Mercado do Cliente": novo_segmento,
            "Produto/Solução Específica": novo_produto,
            "Valor Estimado (R$)": novo_valor,
            "Etapa no Funil de Vendas": nova_etapa_f,
            "Próxima Ação": nova_proxima_acao,
            "Responsável pela Oportunidade": novo_responsavel,
        }
        save_new_opportunity(new_opportunity)

# Interface principal
st.title("📊 CRM de Oportunidades - Allcap")
st.subheader("Gerencie suas oportunidades de forma eficiente")

# Seleção de oportunidade para edição
st.markdown("### 📋 Oportunidades Registradas")
selected_id = st.selectbox("Selecione uma Oportunidade para Editar", df["ID"].unique())

# Filtra os dados com base no ID selecionado
oportunidade = df[df["ID"] == selected_id].iloc[0]

# Formulário para edição
txt_nome = st.text_input("Nome do Cliente", oportunidade["Nome"])
txt_tipo_op = st.selectbox("Tipo de Oportunidade", df["Tipo de Oportunidade"].unique(), index=list(df["Tipo de Oportunidade"].unique()).index(oportunidade["Tipo de Oportunidade"]))
txt_fase = st.selectbox("Fase", df["Fase"].unique(), index=list(df["Fase"].unique()).index(oportunidade["Fase"]))
txt_tipo_cliente = st.selectbox("Tipo de Cliente", df["Tipo de Cliente"].unique(), index=list(df["Tipo de Cliente"].unique()).index(oportunidade["Tipo de Cliente"]))
txt_valor = st.text_input("Valor Estimado (R$)", oportunidade["Valor Estimado (R$)"])
txt_cidade = st.text_input("Cidade", oportunidade["Cidade"])
txt_estado = st.text_input("Estado", oportunidade["Estado"])
txt_etapa = st.text_input("Etapa no Funil de Vendas", oportunidade["Etapa no Funil de Vendas"])
txt_prox_acao = st.text_input("Próxima Ação", oportunidade["Próxima Ação"])

if st.button("Salvar Alterações"):
    df.loc[df["ID"] == selected_id, "Nome"] = txt_nome
    df.loc[df["ID"] == selected_id, "Tipo de Oportunidade"] = txt_tipo_op
    df.loc[df["ID"] == selected_id, "Fase"] = txt_fase
    df.loc[df["ID"] == selected_id, "Tipo de Cliente"] = txt_tipo_cliente
    df.loc[df["ID"] == selected_id, "Valor Estimado (R$)"] = txt_valor
    df.loc[df["ID"] == selected_id, "Cidade"] = txt_cidade
    df.loc[df["ID"] == selected_id, "Estado"] = txt_estado
    df.loc[df["ID"] == selected_id, "Etapa no Funil de Vendas"] = txt_etapa
    df.loc[df["ID"] == selected_id, "Próxima Ação"] = txt_prox_acao
    st.success("Alterações salvas com sucesso!")
