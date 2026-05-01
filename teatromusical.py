import streamlit as st

st.title('Teatro Musical 101 - Guia para iniciantes!')
st.write("Tudo que você precisa saber para explorar esse universo!")

st.image("https://i.pinimg.com/1200x/1f/49/d4/1f49d4e8ecacf1f139bba0c73453bcf5.jpg", caption="Elenco original da produção de Hamilton da Broadway", width=300)

st.write("-----------------------------------------")
st.markdown('**Afinal, o que é teatro musical?**')
st.markdown("""
O teatro musical combina música, dança e representação em uma única performance,
contando histórias por meio desses elementos.
""")


st.markdown('**E no Brasil:**')
st.write("""
O teatro musical chegou ao Brasil no final do século XIX, inicialmente com o **Teatro** **de** **Revista**, 
um tipo de espetáculo leve e satírico que misturava música, dança e esquetes para comentar 
acontecimentos e costumes da época. A primeira adaptação de uma peça da Broadway foi 
Minha Querida Lady (My Fair Lady), com Bibi Ferreira e Paulo Autran e, no fim dos anos 60, o teatro nacional 
era divido entre adaptações de grandes espetáculos como Jesus Cristo Superstar e Rocky Horror Show, mas também contou 
com produções nacionais, como Roda Viva e Ópera do Malandro.
""")


st.markdown('**Como funciona uma peça de teatro?**')
st.write("""Quando chega o horário de começar a peça são tocados três sinais, em que o último representa o início da peça. 
Elas são divididas em três partes, o primeiro ato, intervalo e o segundo ato.""")

with st.expander("O que acontece no Ato 1?"):
    st.write("""
O Ato 1 é responsável por apresentar a história.

Aqui você vai ver:
- Introdução dos personagens principais  
- Explicação do contexto da história  
- Surgimento do conflito principal  

Geralmente termina com um momento marcante que deixa o público curioso para o que vem depois.
""")
with st.expander("O que você encontra no Ato 2?"):
    st.write("""
O Ato 2 desenvolve e resolve a história.

Aqui você vai ver:
- Evolução do conflito  
- Momentos emocionais mais intensos  
- Clímax (ponto mais importante da história)  
- Desfecho final  

É onde tudo se resolve.
""")

import streamlit as st

st.sidebar.title("Camarim")

pagina = st.sidebar.radio(
    "Escolha:",
    ["Tipos de músicas", "Elementos de cena", "Personagens e Elenco"]
)


if pagina == "Tipos de músicas":
    st.title("🎶 Tipos de músicas")

    with st.expander("Ver termos", expanded=True):
        st.markdown("""
- **Solo** → a música é cantada por uma pessoa só  
- **Dueto** → dois personagens cantam  
- **Ensemble vocal** → coral  
- **Opening Number** → primeira música do show  
- **I Want Song** → música onde o personagem revela seu objetivo  
- **11 o’clock number** → música forte perto do final  
- **Reprise** → repetição de uma música com novo significado  
""")


elif pagina == "Elementos de cena":
    st.title("🎭 Elementos de cena")

    with st.expander("Ver termos", expanded=True):
        st.markdown("""
- **Cenário (Set)** → ambiente físico  
- **Figurino** → roupas dos personagens  
- **Props** → objetos usados em cena  
- **Iluminação** → luzes do espetáculo  
- **Sound design** → efeitos sonoros  
""")


elif pagina == "Personagens e Elenco":
    st.title("🎬 Personagens e elenco")

    with st.expander("Ver termos", expanded=True):
        st.markdown("""
- **Protagonista** → personagem principal  
- **Antagonista** → quem gera conflito  
- **Coadjuvante** → personagens de apoio  
- **Ensemble** → grupo que canta/dança/atua sem foco principal  
- **Cover** → substituto que assume o papel quando necessário  
""")

import streamlit as st
import pandas as pd

st.title("Onde o teatro musical acontece")

st.write("Compare os principais centros de teatro musical:")

dados = {
    "Aspecto": [
        "Localização",
        "Importância",
        "Idioma",
        "Tipo de produção",
        "Fama mundial",
        "Exemplos"
    ],
    "Broadway": [
        "Nova York, EUA",
        "Maior centro do mundo",
        "Inglês",
        "Grandes produções profissionais",
        "Muito alta",
        "Hamilton, Wicked"
    ],
    "West End": [
        "Londres, Reino Unido",
        "Principal da Europa",
        "Inglês",
        "Produções de alto nível",
        "Muito alta",
        "Les Misérables, Phantom of the Opera"
    ],
    "Outros países": [
        "Brasil, França, Alemanha...",
        "Crescendo no cenário mundial",
        "Idioma local",
        "Adaptações e produções originais",
        "Média",
        "Wicked (Brasil), Sherek (Brasil) *EM CARTAZ*, produções nacionais"
    ]
}

df = pd.DataFrame(dados)
df.set_index("Aspecto", inplace=True)
st.dataframe(df, use_container_width=True)

st.write('**Premiações importantes:**')
st.markdown("""
🏆 Tony Awards: principal prêmio da Broadway
🏆 Olivier Awards: principal do West End
""")
st.info("EGOT: Alguém que é vencedor de um Emmy, Grammy, Oscar e um TONY")
import streamlit as st

st.set_page_config(page_title="Alguns do smúsicais mais famosos da Broadway")


if "musical" not in st.session_state:
    st.session_state.musical = None


if st.session_state.musical:
    if st.button("⬅️ Voltar"):
        st.session_state.musical = None

if st.session_state.musical is None:
    st.title("Produções mais famosas")

    st.write("Clique em um musical para ver mais:")

    if st.button("Hamilton"):
        st.session_state.musical = "Hamilton"

    if st.button("Wicked"):
        st.session_state.musical = "Wicked"

    if st.button("Beetlejuice"):
        st.session_state.musical = "Beetlejuice"

    if st.button("Hadestown"):
        st.session_state.musical = "Hadestown"

    if st.button("Little Shop of Horrors"):
        st.session_state.musical = "LittleShop"


elif st.session_state.musical == "Hamilton":
    st.title("Hamilton")
    st.video("https://youtu.be/H7Dl0uZhPvs?si=oBAtt3bayfm0XG8R", caption = Satisfied, Hamilton an American Musical)
    st.image("https://i.pinimg.com/1200x/d7/74/c5/d774c594a84ed120ef0a6e0878eb9f75.jpg")
    st.write('Hamilton foi criado pelo compositor e liricista Lin-Manuel Miranda. Teve sua estreia como um musical Off-Broadway, ou seja num teatro que comporta entre 99 até 499
    pessoas em 17 de fevereiro de 2015 no Public Theater em Nova York antes de estreiar na Broadway no dia 6 de agosto. Baseado na vida de Alexander Hamilton, esse
    musical impressionante junta hip-hop e Broadway de maneiras jamais vistas antes e elevou o status de Hamilton 
    no conjunto dos Founding Fathers, enquanto o humaniza de uma forma tocante e inspiradora. Sendo considerado o musical americano mais importante dessa geração, ele levou para casa a maiorida dos Tony na premiação de 2016.')
    st.write('Em 2016 Hamilton ganhou o prêmio Pulitzer na categoria de Drama, e recebeu um número inédito de 
    16 indicações, as quais foram ganhas várias, incluindo o prêmio de Melhor Ator. No total foram conquistados 11 Tonys, quase quebrando o record por um. Hamilton ganhou Melhor Musical 
    e Lin Manuel Miranda ganhou Melhor Roteiro e Melhor Trilha Sonora. Em Julho daquele ano, ele fez sua última aparição no musical.')

# 🧙‍♀️ WICKED
elif st.session_state.musical == "Wicked":
    st.title("Wicked")
    st.image("https://upload.wikimedia.org/wikipedia/en/3/3c/Wicked_poster.jpg")

    st.write("""
Mostra a história das bruxas de Oz antes da chegada de Dorothy,
explorando amizade, identidade e preconceito.
""")

# 🪲 BEETLEJUICE
elif st.session_state.musical == "Beetlejuice":
    st.title("Beetlejuice")
    st.image("https://upload.wikimedia.org/wikipedia/en/3/3a/Beetlejuice_musical.jpg")

    st.write("""
Uma comédia sombria sobre uma garota que faz amizade com um espírito caótico,
misturando humor, morte e muito caos.
""")

# 🌿 HADESTOWN
elif st.session_state.musical == "Hadestown":
    st.title("Hadestown")
    st.image("https://upload.wikimedia.org/wikipedia/en/6/6e/Hadestown_poster.jpg")

    st.write("""
Reconta o mito de Orfeu e Eurídice em um mundo inspirado na Grande Depressão,
com uma trilha sonora folk e jazz.
""")

# 🌱 LITTLE SHOP OF HORRORS
elif st.session_state.musical == "LittleShop":
    st.title("Little Shop of Horrors")
    st.image("https://upload.wikimedia.org/wikipedia/en/6/6c/Little_shop_of_horrors_poster.jpg")

    st.write("""
Conta a história de um jovem que cultiva uma planta carnívora misteriosa
que traz sucesso… mas exige sacrifícios assustadores.
""")
