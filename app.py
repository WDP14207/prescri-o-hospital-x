import streamlit as st
import pandas as pd

# Dicionário de redirecionamento
classificacao = {
    "meropenem": "Antibiótico",
    "omeprazol": "Profilaxia de Úlcera",
    "enoxaparina": "Profilaxia para TVP",
    "dieta branda": "Dieta",
    "dipirona acm": "Medicamentos ACM"
}

# Lista de categorias
categorias = ["Prescrição", "Dieta", "Antibiótico", "Profilaxia de Úlcera", "Profilaxia para TVP", "Medicamentos ACM"]
dados = {categoria: [] for categoria in categorias}

st.title("Organizador de Prescrição Médica")

entrada = st.text_area("Digite os itens da prescrição (um por linha):")

if st.button("Organizar Prescrição"):
    linhas = entrada.lower().splitlines()

    for item in linhas:
        categoria = classificacao.get(item.strip(), "Prescrição")
        dados[categoria].append(item)

    # Garantir que todas as colunas tenham o mesmo número de linhas
    max_len = max(len(v) for v in dados.values())
    for key in dados:
        while len(dados[key]) < max_len:
            dados[key].append("")

    df = pd.DataFrame(dados)
    st.success("Prescrição organizada com sucesso:")
    st.dataframe(df)