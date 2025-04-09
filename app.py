import streamlit as st

st.set_page_config(page_title="Precificadora Veggie", layout="centered")

st.title("🌱 Precificadora Veggie")
st.markdown("Ferramenta do Hub Encontro D’Água ✨")

st.markdown("Essa calculadora foi feita para ajudar mães e empreendedoras a reconhecer o valor do seu trabalho e precificar com mais consciência e sustentabilidade.")

# ========== INGREDIENTES ==========
st.header("🥬 Ingredientes")
ingredientes = []
for i in range(1, 11):
    nome = st.text_input(f"Ingrediente {i} - Nome", key=f"nome_{i}")
    preco_total = st.number_input(f"Valor pago por {nome} (R$)", min_value=0.0, key=f"preco_{i}")
    porcentagem = st.slider(f"Porcentagem usada por sanduíche (%)", 0, 100, 0, key=f"porcentagem_{i}")

    if nome and preco_total > 0 and porcentagem > 0:
        custo = (porcentagem / 100) * preco_total
        ingredientes.append((nome, custo))

# ========== GÁS ==========
st.header("🔥 Gás")
preco_botija = st.number_input("Preço da botija (R$)", min_value=0.0)
dias = st.number_input("Duração média da botija (dias)", min_value=1)
uso_dia = st.number_input("Tempo de uso por dia (minutos)", min_value=1)
tempo_total = st.number_input("Tempo total para produzir todos os sanduíches (min)", min_value=1)
qtd_produzida = st.number_input("Quantidade produzida nesse tempo", min_value=1)

valor_minuto = preco_botija / (dias * uso_dia)
tempo_unitario = tempo_total / qtd_produzida
gasto_gas_unit = valor_minuto * tempo_unitario

# ========== CUSTOS EXTRAS ==========
st.header("📦 Outros Custos")
embalagem = st.number_input("Custo da embalagem (R$)", min_value=0.0)
transporte = st.number_input("Transporte por unidade (R$)", min_value=0.0)
tempo_valor = st.number_input("Quanto vale seu tempo por unidade? (R$)", min_value=0.0)

# ========== LUCRO ==========
st.header("📈 Margem de Lucro")
lucro = st.slider("Margem de lucro desejada (%)", 0, 200, 30)

# ========== CÁLCULO FINAL ==========
if st.button("📊 Calcular"):
    custo_ingredientes = sum([c for _, c in ingredientes])
    custo_total = custo_ingredientes + embalagem + transporte + tempo_valor + gasto_gas_unit
    preco_sugerido = custo_total * (1 + lucro / 100)

    st.success(f"💰 Custo por unidade: R$ {custo_total:.2f}")
    st.success(f"💸 Preço sugerido com lucro: R$ {preco_sugerido:.2f}")

    preco_final = st.number_input("Preço que você pretende cobrar (R$)", min_value=0.0)
    if preco_final:
        lucro_real = preco_final - custo_total
        st.info(f"💡 Lucro real por unidade: R$ {lucro_real:.2f}")

# ========== MENSAGENS FINAIS ==========

st.markdown("---")
st.subheader("📌 Lembrete importante:")
st.markdown("""
Valor não é só o preço que se cobra.  
É o cuidado com o tempo, os ingredientes, a criatividade, o esforço e a experiência que você entrega.  
Essa calculadora foi criada para **te ajudar a reconhecer e honrar seu trabalho com justiça e sustentabilidade**.

Tudo que é feito com amor, merece ser valorizado com dignidade. 💛
""")

st.markdown("---")
st.subheader("🌊 Sobre o Hub Encontro D’Água")
st.markdown("""
Somos um espaço digital que une **tecnologia, ética e propósito**.  
Criamos agentes de IA e automações com alma para ajudar mães, artistas e pequenos negócios a crescerem com leveza e autonomia.  
Aqui, tecnologia é cuidado. É tempo devolvido. É sistema circular.  
👉 Siga a gente: **@encontrodagua.hub** 💧
""")

st.markdown("---")
st.subheader("♻️ Nosso compromisso com a sustentabilidade")
st.markdown("""
Essa ferramenta faz parte do nosso compromisso com a **sustentabilidade, impacto social e regeneração**.

Acreditamos numa tecnologia feita para apoiar — e não excluir. Por isso, oferecemos esta ferramenta de forma **acessível e inclusiva**, como parte do nosso movimento por uma **economia circular e solidária**.

Se você quiser e puder apoiar o Hub, existem duas formas:
- 💬 Indique para outra mãe, artesã ou empreendedora!
- 💛 Faça uma contribuição simbólica via Pix: **encontrodaguahub@gmail.com**

Sua ajuda nos permite continuar criando ferramentas que cuidam. 🌱
""")

st.markdown("---")
st.subheader("✨ Avaliação e Feedback")
st.markdown("[⭐ Avalie ou envie sugestões clicando aqui](https://tally.so/r/wbGRAy)")
