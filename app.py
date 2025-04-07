import streamlit as st

st.set_page_config(page_title="Precificadora Veggie", layout="centered")

st.title("🥪 Calculadora de Preço de Sanduíche Vegano")
st.markdown("Calcule com facilidade o custo e preço final do seu produto! 💚")

# Entradas
st.subheader("🔢 Insira os dados do seu sanduíche:")

ingredientes = st.number_input("Custo total dos ingredientes por sanduíche (R$)", min_value=0.0, format="%.2f")
embalagem = st.number_input("Custo da embalagem (R$)", min_value=0.0, format="%.2f")
gás = st.number_input("Custo médio de gás por unidade (R$)", min_value=0.0, format="%.2f")
transporte = st.number_input("Custo de entrega ou transporte (por unidade) (R$)", min_value=0.0, format="%.2f")
tempo = st.number_input("Quanto você quer ganhar por unidade pelo seu tempo (R$)?", min_value=0.0, format="%.2f")
lucro = st.slider("Margem de lucro (%)", 0, 200, 30)

# Cálculo
if st.button("Calcular preço final"):
    custo_total = ingredientes + embalagem + gás + transporte + tempo
    preco_final = custo_total * (1 + lucro / 100)
    st.success(f"💰 Custo total: R$ {custo_total:.2f}")
    st.success(f"💸 Preço sugerido de venda: R$ {preco_final:.2f}")

st.markdown("---")
st.subheader("🌟 Avaliação")
avaliacao = st.radio("Como você avalia esta calculadora?", ["⭐", "⭐⭐", "⭐⭐⭐", "⭐⭐⭐⭐", "⭐⭐⭐⭐⭐"])
st.text_input("Deixe um elogio ou comentário positivo:")

st.markdown("---")
st.subheader("💬 Feedback / Sugestões de melhoria")
st.text_area("Tem alguma ideia pra deixar essa calculadora ainda melhor? Conta pra gente!")

st.caption("Desenvolvido com carinho por Encontro D'Água 🌱")
