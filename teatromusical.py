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
O teatro musical chegou ao Brasil no final do século XIX, inicialmente com o *T*eatro** **de** **Revista**, 
um tipo de espetáculo leve e satírico que misturava música, dança e esquetes para comentar 
acontecimentos e costumes da época, A primeira adaptação de uma peça da Broadway foi 
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
