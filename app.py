import streamlit as st
import pandas as pd

st.set_page_config(page_title="Prescrição Médica", layout="wide")

# Dicionário de classificação por palavra-chave
classificacao = {
    "meropenem": "Antibiótico",
    "omeprazol": "Profilaxia de Úlcera",
    "enoxaparina": "Profilaxia para TVP",
    "dieta branda": "Dieta",
    "dipirona acm": "Medicamentos ACM"
}

# Lista de categorias (com "Outros" incluído)
categorias = [
    "Dieta",
    "Antibiótico",
    "Profilaxia de Úlcera",
    "Profilaxia para TVP",
    "Medicamentos ACM",
    "Outros"
]

# Inicializa session_state para armazenar os dados cumulativos
if "dados" not in st.session_state:
    st.session_state.dados = {categoria: [] for categoria in categorias}

st.title("Organizador de Prescrição Médica")
st.markdown("Digite um item por vez e ele será classificado automaticamente.")

# Campo de entrada individual
entrada = st.text_input("Item da prescrição:")

# Botão para processar o item
if st.button("Organizar Prescrição"):
    if entrada.strip():
        item = entrada.strip().lower()
        categoria = classificacao.get(item, "Outros")
        st.session_state.dados[categoria].append(item)
        st.success(f'"{item}" adicionado à categoria *{categoria}*.')

# Exibir a tabela com os dados organizados
dados_ajustados = {}

# Igualar número de linhas entre colunas
max_linhas = max((len(itens) for itens in st.session_state.dados.values()), default=1)

for cat in categorias:
    col = st.session_state.dados.get(cat, [])
    while len(col) < max_linhas:
        col.append("")
    dados_ajustados[cat] = col

df = pd.DataFrame(dados_ajustados)
st.subheader("Prescrição Organizada")
st.dataframe(df, use_container_width=True)