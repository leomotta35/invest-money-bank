import streamlit as st
from PIL import Image

# ===============================
# CONFIGURAÇÃO DA PÁGINA
# ===============================
st.set_page_config(
    page_title="Invest Money Bank",
    page_icon="💰",
    layout="centered"
)

# ===============================
# CARREGAR LOGO
# ===============================
logo = Image.open("logo.jpeg")

# ===============================
# CSS PERSONALIZADO
# ===============================
st.markdown("""
<style>
.main {
    background-color: #f5f6fa;
}

.header {
    background: linear-gradient(135deg, #064e3b, #16a34a);
    padding: 25px;
    border-radius: 14px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
}

.header img {
    margin-bottom: 10px;
}

.card {
    background-color: white;
    padding: 22px;
    border-radius: 14px;
    box-shadow: 0 8px 20px rgba(0,0,0,0.08);
    margin-bottom: 22px;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 40px;
    padding-bottom: 20px;
}

.btn-whats {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25d366;
    color: white;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    font-size: 28px;
    text-align: center;
    line-height: 60px;
    text-decoration: none;
    box-shadow: 0 8px 20px rgba(0,0,0,0.3);
    z-index: 9999;
}

.btn-whats:hover {
    background-color: #1ebe5d;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# CABEÇALHO
# ===============================
st.markdown('<div class="header">', unsafe_allow_html=True)
st.image(logo, width=140)
st.markdown("""
<h1>Invest Money Bank</h1>
<p>Soluções Financeiras Empresariais</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# SERVIÇOS
# ===============================
st.markdown("""
<div class="card">
<h2>Serviços</h2>
<ul>
    <li>Capital de Giro</li>
    <li>Empréstimo</li>
    <li>Crédito</li>
    <li>Home Equity</li>
    <li>CGI e CGA</li>
    <li>Consórcio</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# CONTEÚDO PRINCIPAL
# ===============================
st.markdown("""
<div class="card">
<h2>Capital de Giro – Melhores Taxas do Mercado</h2>

<p>
O Invest Money Bank atua há 18 anos no mercado financeiro, sendo parceiro master
dos principais bancos do Brasil, oferecendo linhas de capital de giro com
condições diferenciadas e taxas altamente competitivas.
</p>

<p>
Nossas soluções são estruturadas para fortalecer o fluxo de caixa, ampliar
investimentos e apoiar o crescimento sustentável do seu negócio.
</p>

<p>
Colocamo-nos à disposição para agendar uma reunião e avaliar, de forma totalmente
personalizada, a melhor proposta de crédito para sua empresa.
</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# BOTÃO PRINCIPAL
# ===============================
st.markdown("""
<div style="text-align:center; margin-bottom: 30px;">
    <a href="https://wa.me/5521967184404" target="_blank"
       style="
       background:#16a34a;
       color:white;
       padding:14px 22px;
       border-radius:12px;
       font-weight:bold;
       text-decoration:none;
       ">
       Fale com um Especialista
    </a>
</div>
""", unsafe_allow_html=True)

# ===============================
# BOTÃO FLUTUANTE WHATSAPP
# ===============================
st.markdown("""
<a href="https://wa.me/5521967184404" target="_blank" class="btn-whats">
    ☎
</a>
""", unsafe_allow_html=True)

# ===============================
# RODAPÉ
# ===============================
st.markdown("""
<div class="footer">
© 2026 Invest Money Bank<br>
Soluções Financeiras Empresariais
</div>
""", unsafe_allow_html=True)
