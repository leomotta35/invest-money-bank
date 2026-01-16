import streamlit as st
from PIL import Image

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Invest Money Bank | Banco Digital",
    page_icon="🏦",
    layout="wide"
)

# ===============================
# LOGO JPEG
# ===============================
logo = Image.open("logo.jpeg")

# ===============================
# LINK WHATSAPP COM TEXTO
# ===============================
WHATS_LINK = "https://wa.me/5521967184404?text=Tenho%20interesse%20na%20solu%C3%A7%C3%A3o%20financeira."

# ===============================
# CSS PREMIUM
# ===============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.main {
    background-color: #f4f6f9;
}

.hero {
    background: linear-gradient(135deg, #052e1c, #0f5132);
    padding: 60px;
    border-radius: 24px;
    color: white;
    margin-bottom: 50px;
}

.card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.08);
    margin-bottom: 30px;
}

.section-title {
    font-size: 28px;
    font-weight: 700;
    margin-bottom: 18px;
    color: #052e1c;
}

.badge {
    background: #16a34a;
    color: white;
    padding: 6px 16px;
    border-radius: 30px;
    font-size: 13px;
    font-weight: 600;
    display: inline-block;
    margin-bottom: 12px;
}

.cta {
    background: linear-gradient(135deg, #16a34a, #22c55e);
    padding: 18px 36px;
    border-radius: 18px;
    color: white;
    font-weight: 700;
    text-decoration: none;
    font-size: 18px;
}

.whats {
    position: fixed;
    bottom: 28px;
    right: 28px;
    background: #25d366;
    width: 64px;
    height: 64px;
    border-radius: 50%;
    font-size: 30px;
    color: white;
    text-align: center;
    line-height: 64px;
    text-decoration: none;
    box-shadow: 0 12px 30px rgba(0,0,0,0.3);
    z-index: 9999;
}

.footer {
    text-align: center;
    color: #6b7280;
    font-size: 14px;
    margin-top: 60px;
    padding-bottom: 30px;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# HERO
# ===============================
col1, col2 = st.columns([1, 2])

with col1:
    st.image(logo, width=180)

with col2:
    st.markdown(f"""
    <div class="hero">
        <h1>Invest Money Bank</h1>
        <h3>Banco Digital de Soluções Financeiras Empresariais</h3>
        <p>
        Crédito estruturado, capital de giro, consórcios e soluções patrimoniais
        com inteligência financeira e segurança institucional.
        </p>
        <br>
        <a href="{WHATS_LINK}" target="_blank" class="cta">
            Falar com um Especialista
        </a>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# SOLUÇÕES
# ===============================
st.markdown('<div class="section-title">Soluções Financeiras</div>', unsafe_allow_html=True)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="card">
    <span class="badge">Crédito</span>
    <ul>
        <li>Capital de Giro</li>
        <li>Empréstimos Empresariais</li>
        <li>Home Equity</li>
        <li>CGI e CGA</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="card">
    <span class="badge">Estruturado</span>
    <ul>
        <li>CCB Tokenizada</li>
        <li>CRI / CRA</li>
        <li>FIDC</li>
        <li>Debêntures</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="card">
    <span class="badge">Planejamento</span>
    <ul>
        <li>Consórcios Estratégicos</li>
        <li>Financiamento Imobiliário</li>
        <li>Crédito Patrimonial</li>
    </ul>
    </div>
    """, unsafe_allow_html=True)

# ===============================
# WHATSAPP FLUTUANTE
# ===============================
st.markdown(f"""
<a href="{WHATS_LINK}" target="_blank" class="whats">☎</a>
""", unsafe_allow_html=True)

# ===============================
# FOOTER
# ===============================
st.markdown("""
<div class="footer">
© 2026 Invest Money Bank • Banco Digital de Soluções Financeiras
</div>
""", unsafe_allow_html=True)




