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
# LOGO
# ===============================
logo = Image.open("logo.jpeg")

# ===============================
# CSS PERSONALIZADO
# ===============================
st.markdown("""
<style>
.main { background-color: #f5f6fa; }

.header {
    background: linear-gradient(135deg, #064e3b, #16a34a);
    padding: 30px;
    border-radius: 16px;
    text-align: center;
    color: white;
    margin-bottom: 35px;
}

.card {
    background: white;
    padding: 26px;
    border-radius: 16px;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    margin-bottom: 26px;
}

.badge {
    background: #16a34a;
    color: white;
    padding: 6px 14px;
    border-radius: 30px;
    font-size: 14px;
    display: inline-block;
    margin-bottom: 12px;
}

.footer {
    text-align: center;
    color: gray;
    font-size: 14px;
    margin-top: 50px;
    padding-bottom: 20px;
}

.btn-whats {
    position: fixed;
    bottom: 25px;
    right: 25px;
    background-color: #25d366;
    color: white;
    width: 62px;
    height: 62px;
    border-radius: 50%;
    font-size: 28px;
    text-align: center;
    line-height: 62px;
    text-decoration: none;
    box-shadow: 0 8px 22px rgba(0,0,0,0.3);
    z-index: 9999;
}
</style>
""", unsafe_allow_html=True)

# ===============================
# CABEÇALHO
# ===============================
st.markdown('<div class="header">', unsafe_allow_html=True)
st.image(logo, width=150)
st.markdown("""
<h1>Invest Money Bank</h1>
<p><strong>Soluções Financeiras Empresariais e Patrimoniais</strong></p>
</div>
""", unsafe_allow_html=True)

# ===============================
# SERVIÇOS (ORIGINAL)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Nossos Serviços</span>
<ul>
<li>Capital de Giro</li>
<li>Empréstimos Empresariais</li>
<li>Crédito Personalizado</li>
<li>Home Equity</li>
<li>CGI e CGA</li>
<li>Consórcio</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# CAPITAL DE GIRO (ORIGINAL)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Capital de Giro – Melhores Taxas do Mercado</span>

<p>
O <strong>Invest Money Bank</strong> atua há <strong>18 anos</strong> no mercado financeiro,
sendo parceiro master dos principais bancos do Brasil, o que nos permite oferecer
linhas de capital de giro com condições diferenciadas e taxas altamente competitivas
para empresas de todos os portes.
</p>

<p>
Nossas soluções são estruturadas para fortalecer o fluxo de caixa,
ampliar investimentos e apoiar o crescimento do seu negócio.
</p>

<p>
Colocamo-nos à disposição para agendar uma reunião e avaliar,
de forma totalmente personalizada, a melhor proposta de crédito para sua empresa.
</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# SOBRE NÓS (PDF)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Sobre Nós</span>
<p>
Somos um <strong>hub completo de crédito e soluções financeiras</strong>.
Atuamos junto aos maiores bancos, fundos e estruturas do mercado,
oferecendo acesso a <strong>mais de 20 linhas de crédito</strong>.
</p>

<p>
Nosso compromisso é entregar soluções financeiras
<strong>seguras, eficientes e personalizadas</strong>,
sempre com transparência, estratégia e atendimento humano.
</p>

<p><strong>Seu parceiro financeiro estratégico.</strong></p>
</div>
""", unsafe_allow_html=True)

# ===============================
# DIFERENCIAIS (PDF)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Nossos Diferenciais</span>
<ul>
<li>Acesso facilitado aos principais bancos e fundos do país</li>
<li>Atendimento consultivo e personalizado</li>
<li>Especialistas dedicados do início à liberação</li>
<li>Processos seguros, compliance e LGPD</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# SOLUÇÕES FINANCEIRAS (PDF + ORIGINAL)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Soluções Financeiras</span>
<ul>
<li><strong>Capital de Giro:</strong> com e sem garantia</li>
<li><strong>Crédito com Garantia:</strong> Imóvel (CGI) e Veículo (CGA)</li>
<li><strong>Home Equity:</strong> crédito com taxas reduzidas</li>
<li><strong>Consórcios Estratégicos:</strong> imóveis, veículos e ativos</li>
<li><strong>Financiamento Imobiliário</strong></li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# CRÉDITOS ESTRUTURADOS (PDF)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Créditos Estruturados</span>
<ul>
<li>CCB Tokenizada</li>
<li>CRI – Certificados de Recebíveis Imobiliários</li>
<li>CRA – Certificados de Recebíveis do Agronegócio</li>
<li>FIDC – Fundos de Investimento em Direitos Creditórios</li>
<li>Debêntures (inclusive incentivadas)</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# PERFORMANCE (PDF)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Nossos Resultados</span>
<ul>
<li>+120.000 clientes atendidos (PF e PJ)</li>
<li>R$ 10,8 bilhões em crédito concedido</li>
<li>R$ 240 milhões faturados nos últimos 90 dias</li>
<li>78% de assertividade nas operações</li>
<li>Liberação média entre 30 e 90 dias</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ===============================
# JORNADA DO CLIENTE (PDF)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Como Trabalhamos</span>
<ol>
<li>Análise e diagnóstico financeiro</li>
<li>Estruturação e busca das melhores propostas</li>
<li>Apresentação clara e objetiva</li>
<li>Formalização e liberação do crédito</li>
</ol>
</div>
""", unsafe_allow_html=True)

# ===============================
# CONTATO (PDF)
# ===============================
st.markdown("""
<div class="card">
<span class="badge">Contato</span>
<p><strong>E-mail:</strong> contato@investbankcompany.com.br</p>
<p><strong>Telefone:</strong> (11) 3120-3001</p>
<p><strong>Website:</strong> voce.investbankcompany.com.br</p>
<p><strong>CNPJ:</strong> 11.465.461/0001-56</p>
</div>
""", unsafe_allow_html=True)

# ===============================
# CTA FINAL
# ===============================
st.markdown("""
<div style="text-align:center; margin-bottom: 40px;">
<a href="https://wa.me/5521967184404" target="_blank"
style="background:#16a34a;color:white;padding:14px 26px;
border-radius:14px;font-weight:bold;text-decoration:none;">
Falar com um Especialista
</a>
</div>
""", unsafe_allow_html=True)

# ===============================
# WHATSAPP FLUTUANTE
# ===============================
st.markdown("""
<a href="https://wa.me/5521967184404" target="_blank" class="btn-whats">☎</a>
""", unsafe_allow_html=True)

# ===============================
# RODAPÉ
# ===============================
st.markdown("""
<div class="footer">
© 2026 Invest Money Bank • Soluções Financeiras Empresariais
</div>
""", unsafe_allow_html=True)

