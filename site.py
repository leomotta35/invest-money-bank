import streamlit as st
from PIL import Image

# =====================================================
# CONFIGURAÇÃO DA PÁGINA
# =====================================================
st.set_page_config(
    page_title="Invest Money Bank | Banco Digital",
    page_icon="🏦",
    layout="wide"
)

logo = Image.open("logo.jpeg")

WHATS_LINK = "https://wa.me/5521967184404?text=Tenho%20interesse%20na%20solu%C3%A7%C3%A3o%20financeira."

# =====================================================
# CSS PREMIUM
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #f4f6f9;
}

/* HEADER */
.header {
    background: white;
    padding: 16px 40px;
    border-radius: 0 0 24px 24px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.08);
    position: sticky;
    top: 0;
    z-index: 1000;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #052e1c, #0f5132);
    padding: 60px;
    border-radius: 28px;
    color: white;
    margin: 40px 0;
}

/* CARDS */
.card {
    background: white;
    padding: 32px;
    border-radius: 24px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    margin-bottom: 35px;
}

/* TITLES */
.title {
    font-size: 34px;
    font-weight: 700;
    color: #052e1c;
    margin-bottom: 18px;
}

.subtitle {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 12px;
}

/* BADGE */
.badge {
    background: #16a34a;
    color: white;
    padding: 6px 18px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 16px;
}

/* CTA */
.cta {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    padding: 18px 40px;
    border-radius: 20px;
    color: white;
    font-weight: 700;
    text-decoration: none;
    font-size: 18px;
}

/* WHATS */
.whats {
    position: fixed;
    bottom: 28px;
    right: 28px;
    background: #25d366;
    width: 66px;
    height: 66px;
    border-radius: 50%;
    font-size: 30px;
    color: white;
    text-align: center;
    line-height: 66px;
    text-decoration: none;
    box-shadow: 0 14px 35px rgba(0,0,0,0.35);
    z-index: 9999;
}

/* FOOTER */
.footer {
    background: #052e1c;
    color: #d1fae5;
    padding: 40px;
    border-radius: 28px 28px 0 0;
    margin-top: 80px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# HEADER + NAVEGAÇÃO
# =====================================================
st.markdown('<div class="header">', unsafe_allow_html=True)

col_logo, col_menu = st.columns([1, 3])

with col_logo:
    st.image(logo, width=140)

with col_menu:
    st.markdown("""
    <div style="text-align:right; padding-top:30px;">
        <a href="#inicio">Início</a>&nbsp;&nbsp;&nbsp;
        <a href="#solucoes">Soluções</a>&nbsp;&nbsp;&nbsp;
        <a href="#institucional">Institucional</a>&nbsp;&nbsp;&nbsp;
        <a href="#contato">Contato</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# HERO
# =====================================================
st.markdown(f"""
<div class="hero" id="inicio">
<h1>Invest Money Bank</h1>
<h3>Banco Digital de Soluções Financeiras Empresariais e Patrimoniais</h3>

<p>
Somos especialistas em estruturar crédito inteligente para empresas e pessoas físicas
que buscam crescimento, liquidez, reorganização financeira ou alavancagem patrimonial.
</p>

<p>
Atuamos com capital próprio, bancos parceiros e fundos estruturados, oferecendo
<strong>segurança, estratégia e condições diferenciadas</strong>.
</p>

<br>
<a href="{WHATS_LINK}" class="cta" target="_blank">
Falar com um Especialista
</a>
</div>
""", unsafe_allow_html=True)

# =====================================================
# SOLUÇÕES
# =====================================================
st.markdown('<div id="solucoes" class="title">Soluções Financeiras</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <span class="badge">Crédito Empresarial</span>
    <p>
    Linhas de capital de giro, empréstimos empresariais e crédito estruturado
    com foco em fluxo de caixa, expansão e reorganização financeira.
    </p>
    <ul>
        <li>Capital de Giro</li>
        <li>Crédito PJ</li>
        <li>Home Equity</li>
        <li>CGI e CGA</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <span class="badge">Crédito Estruturado</span>
    <p>
    Estruturas financeiras avançadas para operações de médio e grande porte,
    com soluções personalizadas.
    </p>
    <ul>
        <li>CCB Tokenizada</li>
        <li>CRI / CRA</li>
        <li>FIDC</li>
        <li>Debêntures</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <span class="badge">Planejamento</span>
    <p>
    Soluções patrimoniais e estratégicas para aquisição de ativos e organização
    financeira de longo prazo.
    </p>
    <ul>
        <li>Consórcios Estratégicos</li>
        <li>Financiamento Imobiliário</li>
        <li>Crédito Patrimonial</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# =====================================================
# INSTITUCIONAL
# =====================================================
st.markdown("""
<div class="card" id="institucional">
<span class="badge">Institucional</span>
<h2>18 anos de credibilidade no mercado financeiro</h2>

<p>
O Invest Money Bank atua como um hub financeiro independente, conectando clientes
aos principais bancos, fundos e estruturas do mercado.
</p>

<p>
Já estruturamos mais de <strong>R$ 10,8 bilhões em crédito</strong>, atendendo mais de
<strong>120 mil clientes</strong>, com processos seguros, compliance rigoroso e total transparência.
</p>

<p>
Nossa atuação é baseada em análise técnica, estratégia financeira e
relacionamento de longo prazo.
</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# CONTATO
# =====================================================
st.markdown("""
<div class="card" id="contato">
<span class="badge">Contato</span>
<p><strong>E-mail:</strong> contato@investbankcompany.com.br</p>
<p><strong>Telefone:</strong> (11) 3120-3001</p>
<p><strong>CNPJ:</strong> 11.465.461/0001-56</p>
</div>
""", unsafe_allow_html=True)

# =====================================================
# WHATSAPP FLUTUANTE
# =====================================================
st.markdown(f"""
<a href="{WHATS_LINK}" class="whats" target="_blank">☎</a>
""", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================
st.markdown("""
<div class="footer">
<p><strong>Invest Money Bank</strong></p>
<p>Banco Digital de Soluções Financeiras Empresariais</p>
<p>© 2026 • Todos os direitos reservados</p>
</div>
""", unsafe_allow_html=True)






