import streamlit as st
import pandas as pd
from datetime import datetime

# Carregar dados
@st.cache_data
def load_data():
    return pd.read_csv("CRM_Clientes_Allcap_Trust.csv")

df = load_data()

# Título do app
st.title("📊 CRM de Oportunidades - Allcap")
st.subheader("Gerencie suas oportunidades de forma eficiente")

# Formulário para adicionar nova oportunidade
st.sidebar.header("➕ Adicionar Nova Oportunidade")
with st.sidebar.form("nova_oportunidade"):
    nome = st.text_input("Nome do Cliente")
    contato = st.text_input("Contato")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    tipo_oportunidade = st.selectbox("Tipo de Oportunidade", ["Venda", "Parceria Comercial", "Ambos"])
    fase = st.selectbox("Fase", ["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado Perdido"])
    tipo_cliente = st.selectbox("Tipo de Cliente", ["PF", "PJ"])
    segmento_mercado = st.text_input("Segmento do Cliente")
    produto = st.text_input("Produto/Solução Específica")
    valor_estimado = st.number_input("Valor Estimado (R$)", min_value=0.0, step=1000.0)
    prazo_desejado = st.number_input("Prazo Desejado (meses)", min_value=0, step=1)
    taxa_juros = st.text_input("Taxa de Juros (Estimativa)")
    etapa_funil = st.text_input("Etapa no Funil de Vendas")
    ultima_interacao = st.date_input("Data da Última Interação", datetime.today())
    proxima_acao = st.text_input("Próxima Ação")
    responsavel = st.text_input("Responsável pela Oportunidade")
    probabilidade = st.slider("Probabilidade de Fechamento (%)", 0, 100, 50)
    valor_total = st.number_input("Valor Total (R$)", min_value=0.0, step=1000.0)
    data_fechamento = st.date_input("Data de Fechamento", datetime.today())
    historico_interacoes = st.text_area("Histórico de Interações")
    
    submit = st.form_submit_button("Adicionar Oportunidade")
    if submit:
        novo_id = f"OP{len(df)+1:03d}"
        nova_oportunidade = pd.DataFrame([[
            datetime.today().strftime('%d/%m/%Y'), novo_id, nome, contato, email, telefone, cidade, estado, 
            tipo_oportunidade, fase, tipo_cliente, segmento_mercado, produto, valor_estimado, prazo_desejado, 
            taxa_juros, etapa_funil, ultima_interacao, proxima_acao, responsavel, probabilidade, valor_total, 
            data_fechamento, historico_interacoes
        ]], columns=df.columns)
        df = pd.concat([df, nova_oportunidade], ignore_index=True)
        st.success("✅ Oportunidade adicionada com sucesso!")

# Seleção de oportunidade para edição
st.subheader("📋 Oportunidades Registradas")
selecao = st.selectbox("Selecione uma Oportunidade para Editar", df["ID"].tolist())

if selecao:
    oportunidade = df[df["ID"] == selecao].iloc[0]
    with st.form("editar_oportunidade"):
        nome = st.text_input("Nome do Cliente", oportunidade["Nome"])
        fase = st.selectbox("Fase", ["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado Perdido"], index=["Lead Em Potencial", "Em Negociação", "Proposta Aprovada", "Fechado", "Descartado Perdido"].index(oportunidade["Fase"]))
        valor_estimado = st.number_input("Valor Estimado (R$)", min_value=0.0, step=1000.0, value=oportunidade["Valor Estimado (R$)"])
        probabilidade = st.slider("Probabilidade de Fechamento (%)", 0, 100, int(oportunidade["Probabilidade de Fechamento (%)"]))
        data_fechamento = st.date_input("Data de Fechamento", datetime.today())
        submit_editar = st.form_submit_button("Salvar Alterações")
        
        if submit_editar:
            df.loc[df["ID"] == selecao, ["Nome", "Fase", "Valor Estimado (R$)", "Probabilidade de Fechamento (%)", "Data de Fechamento"]] = [nome, fase, valor_estimado, probabilidade, data_fechamento]
            st.success("✅ Oportunidade atualizada com sucesso!")

# Exibir DataFrame atualizado
st.write(df)
