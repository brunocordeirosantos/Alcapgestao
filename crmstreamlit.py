import streamlit as st
import pandas as pd

# Configuração da página
st.set_page_config(page_title="CRM de Oportunidades - Allcap", layout="wide")

# Inicializa a estrutura de dados no session state
if "oportunidades" not in st.session_state:
    st.session_state.oportunidades = pd.DataFrame(columns=[
        "ID", "Nome", "Contato", "E-mail", "Telefone", "Cidade", "Estado",
        "Tipo de Oportunidade", "Fase", "Tipo de Cliente", "Valor Estimado (R$)",
        "Etapa no Funil de Vendas", "Próxima Ação"
    ])

# Geração de um novo ID para cada nova oportunidade
def gerar_novo_id():
    if not st.session_state.oportunidades.empty:
        ultimo_id = st.session_state.oportunidades["ID"].str.extract(r'(\d+)').dropna().astype(int).max()[0]
        return f"OP{ultimo_id + 1:03d}"
    else:
        return "OP001"

# Formulário para adicionar novas oportunidades
with st.sidebar:
    st.markdown("### ➕ Adicionar Nova Oportunidade")
    
    novo_id = gerar_novo_id()
    nome = st.text_input("Nome do Cliente")
    contato = st.text_input("Contato")
    email = st.text_input("E-mail")
    telefone = st.text_input("Telefone")
    cidade = st.text_input("Cidade")
    estado = st.text_input("Estado")
    tipos_oportunidade = ["Venda", "Parceria Comercial"]
    tipo_oportunidade = st.selectbox("Tipo de Oportunidade", tipos_oportunidade)
    fases = ["Lead Em Potencial", "Em Negociação", "Fechado", "Descartado Perdido"]
    fase = st.selectbox("Fase", fases)
    tipos_cliente = ["PF", "PJ"]
    tipo_cliente = st.selectbox("Tipo de Cliente", tipos_cliente)
    valor_estimado = st.text_input("Valor Estimado (R$)")
    etapa_funil = st.text_input("Etapa no Funil de Vendas")
    proxima_acao = st.text_input("Próxima Ação")

    if st.button("Adicionar Oportunidade"):
        nova_oportunidade = pd.DataFrame([{
            "ID": novo_id, "Nome": nome, "Contato": contato, "E-mail": email, "Telefone": telefone,
            "Cidade": cidade, "Estado": estado, "Tipo de Oportunidade": tipo_oportunidade,
            "Fase": fase, "Tipo de Cliente": tipo_cliente, "Valor Estimado (R$)": valor_estimado,
            "Etapa no Funil de Vendas": etapa_funil, "Próxima Ação": proxima_acao
        }])

        st.session_state.oportunidades = pd.concat([st.session_state.oportunidades, nova_oportunidade], ignore_index=True)
        st.success(f"Oportunidade {novo_id} adicionada com sucesso!")
        st.rerun()  # Substituído o experimental_rerun()

# Seção principal - Edição de oportunidades
st.markdown("## 📋 Oportunidades Registradas")
if not st.session_state.oportunidades.empty:
    id_selecionado = st.selectbox("Selecione uma Oportunidade para Editar", st.session_state.oportunidades["ID"])

    oportunidade = st.session_state.oportunidades[st.session_state.oportunidades["ID"] == id_selecionado].iloc[0]

    txt_nome = st.text_input("Nome do Cliente", oportunidade["Nome"], key="nome_cliente")
    txt_contato = st.text_input("Contato", oportunidade["Contato"], key="contato")
    txt_email = st.text_input("E-mail", oportunidade["E-mail"], key="email")
    txt_telefone = st.text_input("Telefone", oportunidade["Telefone"], key="telefone")
    txt_cidade = st.text_input("Cidade", oportunidade["Cidade"], key="cidade")
    txt_estado = st.text_input("Estado", oportunidade["Estado"], key="estado")

    txt_tipo_oportunidade = st.selectbox(
        "Tipo de Oportunidade", tipos_oportunidade,
        index=tipos_oportunidade.index(oportunidade["Tipo de Oportunidade"]) if oportunidade["Tipo de Oportunidade"] in tipos_oportunidade else 0,
        key="tipo_oportunidade"
    )

    txt_fase = st.selectbox(
        "Fase", fases,
        index=fases.index(oportunidade["Fase"]) if oportunidade["Fase"] in fases else 0,
        key="fase"
    )

    txt_tipo_cliente = st.selectbox(
        "Tipo de Cliente", tipos_cliente,
        index=tipos_cliente.index(oportunidade["Tipo de Cliente"]) if oportunidade["Tipo de Cliente"] in tipos_cliente else 0,
        key="tipo_cliente"
    )

    txt_valor_estimado = st.text_input("Valor Estimado (R$)", oportunidade["Valor Estimado (R$)"], key="valor_estimado")
    txt_etapa_funil = st.text_input("Etapa no Funil de Vendas", oportunidade["Etapa no Funil de Vendas"], key="etapa_funil")
    txt_proxima_acao = st.text_input("Próxima Ação", oportunidade["Próxima Ação"], key="proxima_acao")

    if st.button("Salvar Alterações"):
        st.session_state.oportunidades.loc[st.session_state.oportunidades["ID"] == id_selecionado, :] = [
            id_selecionado, txt_nome, txt_contato, txt_email, txt_telefone, txt_cidade, txt_estado,
            txt_tipo_oportunidade, txt_fase, txt_tipo_cliente, txt_valor_estimado, txt_etapa_funil, txt_proxima_acao
        ]
        st.success(f"Oportunidade {id_selecionado} atualizada com sucesso!")
        st.rerun()

else:
    st.info("Nenhuma oportunidade cadastrada ainda. Use o menu lateral para adicionar.")
