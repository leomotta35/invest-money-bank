import streamlit as st
from PIL import Image

# ======================================================
# CONFIGURAÇÃO DA PÁGINA
# ======================================================
st.set_page_config(
    page_title="Invest Money Bank | Banco Digital",
    page_icon="🏦",
    layout="wide"
)

# ======================================================
# ASSETS
# ======================================================
logo = Image.open("logo.jpeg")

WHATS_CREDITO = "https://wa.me/5521967184404?text=Ol%C3%A1%2C%20tudo%20bem%3F%0ATenho%20interesse%20em%20uma%20solu%C3%A7%C3%A3o%20de%20cr%C3%A9dito%2Fcapital%20de%20giro%20pelo%20Invest%20Money%20Bank.%0A%0AGostaria%20de%20falar%20com%20um%20especialista%20para%20avaliar%20meu%20perfil%20e%20entender%20as%20melhores%20condi%C3%A7%C3%B5es%20dispon%C3%ADveis."

WHATS_CONSORCIO = "https://wa.me/5521967184404?text=Ol%C3%A1%21%0ATenho%20interesse%20em%20conhecer%20as%20op%C3%A7%C3%B5es%20de%20cons%C3%B3rcio%20estrat%C3%A9gico%20do%20Invest%20Money%20Bank.%0A%0AGostaria%20de%20receber%20uma%20an%C3%A1lise%20personalizada%20para%20meu%20perfil."

WHATS_HOME = "https://wa.me/5521967184404?text=Ol%C3%A1%2C%20tudo%20bem%3F%0ATenho%20interesse%20em%20estruturar%20uma%20opera%C3%A7%C3%A3o%20de%20Home%20Equity%20pelo%20Invest%20Money%20Bank.%0A%0ABusco%20uma%20solu%C3%A7%C3%A3o%20segura%2C%20com%20taxas%20competitivas%20e%20an%C3%A1lise%20especializada."

# ======================================================
# CSS PREMIUM
# ======================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main { background-color: #f4f6f9; }

/* HEADER */
.header {
    background: white;
    padding: 18px 40px;
    border-radius: 0 0 26px 26px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.08);
    margin-bottom: 35px;
}

.nav a {
    margin-left: 25px;
    font-weight: 600;
    text-decoration: none;
    color: #052e1c;
}

/* HERO */
.hero {
    background: linear-gradient(135deg, #052e1c, #0f5132);
    padding: 60px;
    border-radius: 32px;
    color: white;
    margin-bottom: 50px;
}

/* CARDS */
.card {
    background: white;
    padding: 36px;
    border-radius: 28px;
    box-shadow: 0 18px 42px rgba(0,0,0,0.08);
    margin-bottom: 35px;
}

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

.title {
    font-size: 34px;
    font-weight: 700;
    color: #052e1c;
    margin-bottom: 25px;
}

.cta {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    padding: 16px 34px;
    border-radius: 18px;
    color: white;
    font-weight: 700;
    text-decoration: none;
    font-size: 17px;
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
    font-size: 28px;
    color: white;
    text-align: center;
    line-height: 66px;
    text-decoration: none;
    box-shadow: 0 16px 40px rgba(0,0,0,0.35);
    z-index: 9999;
}

/* FOOTER */
.footer {
    background: #052e1c;
    color: #d1fae5;
    padding: 45px;
    border-radius: 32px 32px 0 0;
    margin-top: 80px;
}
</style>
""", unsafe_allow_html=True)

# ======================================================
# HEADER COM NAVEGAÇÃO
# ======================================================
st.markdown('<div class="header">', unsafe_allow_html=True)
col_logo, col_nav = st.columns([1, 3])

with col_logo:
    st.image(logo, width=150)

with col_nav:
    st.markdown("""
    <div class="nav" style="text-align:right; padding-top:40px;">
        <a href="#inicio">Início</a>
        <a href="#solucoes">Soluções</a>
        <a href="#institucional">Institucional</a>
        <a href="#contato">Contato</a>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ======================================================
# HERO
# ======================================================
st.markdown("""
<div class="hero" id="inicio">
<h1>Invest Money Bank</h1>
<h3>Banco Digital de Soluções Financeiras</h3>

<p>
Há mais de 18 anos estruturando crédito empresarial, patrimonial e
operações financeiras com segurança, estratégia e transparência.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# SOLUÇÕES
# ======================================================
st.markdown('<div class="title" id="solucoes">Nossas Soluções</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
    <span class="badge">Crédito</span>
    <p>Capital de giro, crédito empresarial, CGI e CGA para fortalecimento
    financeiro e expansão.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
    <span class="badge">Consórcio</span>
    <p>Consórcios estratégicos para aquisição de ativos com planejamento
    financeiro inteligente.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
    <span class="badge">Home Equity</span>
    <p>Crédito com garantia de imóvel, taxas reduzidas e prazos longos.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================================================
# BOTÕES WHATSAPP
# ======================================================
st.markdown("""
<div class="card">
<h2>Fale com um Especialista</h2>

<div style="display:flex; gap:20px; flex-wrap:wrap;">
<a href="{0}" target="_blank" class="cta">💼 Crédito / Capital de Giro</a>
<a href="{1}" target="_blank" class="cta">📑 Consórcio</a>
<a href="{2}" target="_blank" class="cta">🏠 Home Equity</a>
</div>
</div>
""".format(WHATS_CREDITO, WHATS_CONSORCIO, WHATS_HOME), unsafe_allow_html=True)

# ======================================================
# INSTITUCIONAL
# ======================================================
st.markdown("""
<div class="card" id="institucional">
<span class="badge">Institucional</span>
<p>
Mais de <strong>120 mil clientes atendidos</strong> e
<strong>R$ 10 bilhões estruturados</strong> em crédito.
</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# CONTATO
# ======================================================
st.markdown("""
<div class="card" id="contato">
<p><strong>Contato</strong></p>
<p>E-mail: contato@investbankcompany.com.br</p>
<p>Telefone: (11) 3120-3001</p>
</div>
""", unsafe_allow_html=True)

# ======================================================
# WHATS FLUTUANTE
# ======================================================
st.markdown(f'<a href="{WHATS_CREDITO}" class="whats" target="_blank">💬</a>', unsafe_allow_html=True)

# ======================================================
# FOOTER
# ======================================================
st.markdown("""
<div class="footer">
<p><strong>Invest Money Bank</strong></p>
<p>Banco Digital de Soluções Financeiras Empresariais</p>
<p>© 2026 • Todos os direitos reservados</p>
</div>
""", unsafe_allow_html=True)




