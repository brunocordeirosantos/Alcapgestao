import streamlit as st
import pandas as pd

# Função para carregar dados do CRM (pode ser substituído por um banco de dados)
def load_data():
    try:
        df = pd.read_csv("crm_data.csv")  # Nome do arquivo CSV que armazena os dados
    except FileNotFoundError:
        df = pd.DataFrame(columns=["ID", "Nome", "Tipo de Oportunidade", "Fase", "Produto/Solução", "Valor Estimado", "Responsável"])
    return df

# Função para salvar os dados no CSV
def save_data(df):
    df.to_csv("crm_data.csv", index=False)

# Carregar dados existentes
df = load_data()

# Criar o formulário para inserir novas oportunidades
st.sidebar.title("📌 Adicionar Nova Oportunidade")

with st.sidebar.form("nova_oportunidade"):
    id_op = st.text_input("ID da Oportunidade")
    nome = st.text_input("Nome do Cliente")
    tipo_op = st.selectbox("Tipo de Oportunidade", ["Venda", "Parceria Comercial"])
    fase = st.selectbox("Fase", ["Lead Em Potencial", "Em Negociação", "Fechado"])
    produto = st.selectbox("Produto/Solução", ["Home Equity", "Antecipação de Recebíveis", "FIDC"])
    valor_estimado = st.number_input("Valor Estimado (R$)", min_value=0, step=1000)
    responsavel = st.text_input("Responsável pela Oportunidade")
    
    submit = st.form_submit_button("Adicionar")

    if submit:
        novo_dado = pd.DataFrame([[id_op, nome, tipo_op, fase, produto, valor_estimado, responsavel]],
                                 columns=["ID", "Nome", "Tipo de Oportunidade", "Fase", "Produto/Solução", "Valor Estimado", "Responsável"])
        df = pd.concat([df, novo_dado], ignore_index=True)
        save_data(df)
        st.success(f"Oportunidade {id_op} adicionada com sucesso!")
        st.experimental_rerun()
        
# Exibir os dados atualizados
st.write("📊 **Oportunidades Cadastradas**")
st.dataframe(df)
