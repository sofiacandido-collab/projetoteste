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
        st.rerun()

    if st.button("Wicked"):
        st.session_state.musical = "Wicked"
        st.rerun()

    if st.button("Beetlejuice"):
        st.session_state.musical = "Beetlejuice"
        st.rerun()

    if st.button("Hadestown"):
        st.session_state.musical = "Hadestown"
        st.rerun()

    if st.button("Little Shop of Horrors"):
        st.session_state.musical = "LittleShop"
        st.rerun()

elif st.session_state.musical == "Hamilton":
    st.title("Hamilton")
    st.video("https://youtu.be/H7Dl0uZhPvs?si=oBAtt3bayfm0XG8R")
    st.write("""Hamilton foi criado pelo compositor e liricista Lin-Manuel Miranda. Teve sua estreia como um musical Off-Broadway, ou seja num teatro que comporta entre 99 até 499
    pessoas em 17 de fevereiro de 2015 no Public Theater em Nova York antes de estrear na Broadway no dia 6 de agosto. 
    Baseado na vida de Alexander Hamilton, esse musical impressionante junta hip-hop e Broadway de maneiras jamais vistas antes 
    e levou o status de Hamilton no conjunto dos Founding Fathers, enquanto o humaniza de uma forma tocante e inspiradora. 
    Sendo considerado o musical americano mais importante dessa geração, ele levou para casa a maioria dos Tony na premiação de 2016.""")
    st.image("https://i.pinimg.com/1200x/d7/74/c5/d774c594a84ed120ef0a6e0878eb9f75.jpg")
    st.write("""Em 2016 Hamilton ganhou o prêmio Pulitzer na categoria de Drama, e recebeu um número
    inédito de 16 indicações, as quais foram ganhas várias, incluindo o prêmio de Melhor Ator. No total foram 
    conquistados 11 Tonys, quase quebrando o record por um. Hamilton ganhou Melhor Musical e Lin Manuel Miranda
    ganhou Melhor Roteiro e Melhor Trilha Sonora. Em Julho daquele ano, ele fez sua última aparição no musical.""")


elif st.session_state.musical == "Wicked":
    st.title("Wicked")
    st.video("https://youtu.be/2fR4JotwwWo?si=9GIXvzJ3T1D5Gxs7")
    st.video("https://youtu.be/68wWliAYP7o?si=QW4sgfAf9EzEQOcy")
    st.write("""Wicked foi criado pelo compositor e letrista Stephen Schwartz e teve sua 
    estreia na Broadway no dia 30 de outubro de 2003, no Gershwin Theatre em Nova York. Baseado no 
    livro *Wicked: The Life and Times of the Wicked Witch of the West*, de Gregory Maguire, o musical 
    apresenta uma releitura do universo de Oz antes da chegada de Dorothy.
    
    A história acompanha a relação entre Elphaba, a futura Bruxa Má do Oeste, e Glinda, mostrando amizade, 
    conflitos e questões como preconceito e identidade. Com músicas marcantes e uma narrativa emocional, 
    Wicked se tornou um dos musicais mais populares da Broadway, sendo um enorme sucesso de público e 
    crítica. Ao longo dos anos, recebeu diversas indicações e prêmios, incluindo o Tony Awards, 
    consolidando seu lugar como um dos musicais mais importantes do século XXI.""")

    st.image('https://i.pinimg.com/1200x/17/ff/9a/17ff9a65fb7e05aa4c822b288d4e44b9.jpg')
    st.write("""Wicked já conquistou mais de 100 prêmios ao longo de sua trajetória, 
    incluindo 3 Tony Awards e 1 Grammy Award, consolidando-se como um dos maiores sucessos da 
    Broadway; além disso, o musical já teve mais de 15 produções oficiais ao redor do mundo, passando 
    por países como Estados Unidos, Reino Unido, Austrália, Alemanha, Japão, Brasil e Coreia do Sul.""")



elif st.session_state.musical == "Beetlejuice":
    st.title("Beetlejuice")
    st.video('https://youtu.be/QMrt9demNeA?si=-n4HREKEtmOrnLPj')
    st.write(""" Beetlejuice é um musical baseado no filme de Beetlejuice, com música e letras de Eddie Perfect. 
    A produção estreou na Broadway em 2019, no Winter Garden Theatre, trazendo uma adaptação irreverente, 
    sombria e extremamente humorada da história original. O espetáculo acompanha Lydia Deetz, uma adolescente 
    fascinada pela morte, que acaba cruzando o caminho do excêntrico e caótico  Beetlejuice, resultando
    em uma narrativa cheia de sarcasmo, energia e números musicais marcantes.

    Apesar de sua temporada inicial na Broadway ter sido relativamente curta, Beetlejuice rapidamente
    conquistou uma base de fãs muito dedicada, especialmente entre o público mais jovem. Após ser 
    encerrado em 2020, o musical ganhou uma nova chance e retornou aos palcos em 2022, desta vez 
    no Marquis Theatre, demonstrando a força de sua popularidade. Sua estética única, humor ácido e 
    abordagem moderna ajudaram a diferenciar a produção dentro do cenário tradicional do teatro musical.""")
    st.image("https://i.pinimg.com/736x/94/b2/3d/94b23d618a049222fbc5a8be96e40464.jpg")
    st.write("""Em termos de reconhecimento, Beetlejuice recebeu diversas indicações ao Tony Awards, 
    incluindo categorias importantes como Melhor Musical e Melhor Roteiro. Embora não tenha sido um grande 
    vencedor em número de prêmios, o espetáculo se destacou pelo impacto cultural e pelo engajamento do 
    público, além de expandir sua presença com turnês e produções internacionais, consolidando-se como 
    um musical contemporâneo de grande relevância.""")

    
elif st.session_state.musical == "Hadestown":
    st.title("Hadestown")
    st.video('https://youtu.be/117ufXEhzRQ?si=j3sY7-sKcm823gee')
    st.write("""Hadestown é um musical criado pela cantora e compositora Anaïs Mitchell, 
    que reimagina dois mitos da Grécia Antiga: o de Orfeu e Eurídice e o de Hades e Perséfone. 
    A história se passa em um mundo com estética inspirada na Grande Depressão, misturando elementos 
    industriais com um clima quase mítico. A narrativa acompanha Orfeu, um jovem músico sonhador, 
    que se apaixona por Eurídice, uma garota marcada pela pobreza e pela instabilidade, criando um 
    contraste entre esperança e sobrevivência.

    Ao longo do musical, Eurídice acaba sendo levada para Hadestown, um submundo controlado por
    Hades, onde trabalhadores vivem em condições difíceis e repetitivas. Determinado a resgatá-la, 
    Orfeu embarca em uma jornada até esse mundo subterrâneo, usando sua música como principal força. 
    Paralelamente, o relacionamento entre Hades e Perséfone também é explorado, mostrando um casamento 
    em crise que influencia diretamente o equilíbrio entre os mundos. A história mistura romance,
    sacrifício e crítica social, criando uma atmosfera intensa e emocional.""")
    st.image("https://i.pinimg.com/736x/ba/73/93/ba7393c0be1a239c63ac6864e7ea4891.jpg")
    st.write("""O musical é conhecido por seu estilo único, que combina folk, jazz e blues, 
    além de uma narrativa cíclica — ou seja, uma história que se repete, mesmo quando já sabemos o final. 
    Diferente de muitos musicais tradicionais, Hadestown enfatiza mais a experiência emocional do que o 
    final feliz, reforçando a ideia de que algumas histórias precisam ser contadas repetidamente. 
    Essa abordagem torna o espetáculo profundamente marcante e reflexivo, destacando temas como amor, 
    escolha e consequência.""")
    
elif st.session_state.musical == "LittleShop":
    st.title("Little Shop of Horrors")
    st.video('https://youtu.be/80DqYSIQew8?si=7MpFUJOGADEyyz7n')
    st.write("""Little Shop of Horrors é um musical criado por Alan Menken (música) e Howard Ashman 
    (letras e roteiro), baseado no filme de 1960. A história acompanha Seymour, um jovem tímido que
    trabalha em uma floricultura decadente e descobre uma planta misteriosa que passa a atrair clientes 
    e trazer sucesso ao negócio. No entanto, essa planta — chamada Audrey II — revela rapidamente sua 
    natureza perigosa, exigindo sangue humano para crescer, o que leva a narrativa por um caminho cada 
    vez mais sombrio e moralmente complexo, misturando comédia, terror e crítica social.

    Ao longo do musical, Seymour se vê dividido entre o desejo de melhorar de vida, conquistar o amor
    de Audrey e lidar com as consequências das escolhas que faz para manter a planta viva. A obra se 
    destaca pelo tom irreverente, pelas influências de rock e doo-wop na trilha sonora e por seu humor
    ácido, que contrasta com a crescente tensão da história. Essa combinação faz com que o público se 
    envolva tanto com o lado cômico quanto com o suspense da trama, tornando o musical um clássico 
    cult do teatro musical.""")
    st.image("https://i.pinimg.com/1200x/a0/be/3b/a0be3bdf38a6b537f4ea7f0d931874b8.jpg")
    st.write("""Desde sua estreia Off-Broadway em 1982, Little Shop of Horrors recebeu diversos
    reconhecimentos, incluindo o prêmio de Melhor Musical no Drama Desk Awards e no Outer Critics 
    Circle Awards. Ao longo dos anos, ganhou múltiplos revivals e adaptações consolidando seu status 
    como um dos musicais mais influentes e duradouros do gênero, especialmente no circuito 
    alternativo e Off-Broadway.""")
