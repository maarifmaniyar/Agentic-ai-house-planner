import streamlit as st
import time

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI House Planner Pro",
    page_icon="🏠",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS (Premium Look)
# -----------------------------
st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.hero {
    text-align:center;
    padding:20px;
    border-radius:20px;
    background: linear-gradient(90deg,#eef2ff,#f8fafc);
    margin-bottom:20px;
}

.hero h1{
 font-size:48px;
}

.card {
 background:white;
 padding:20px;
 border-radius:18px;
 box-shadow:0 4px 20px rgba(0,0,0,0.08);
}

.small-box{
 background:#f8fafc;
 padding:15px;
 border-radius:14px;
}
</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('''
<div class='hero'>
<h1>🏠 AI House Planner Pro</h1>
<p>Multi-Agent Home Design using CrewAI</p>
</div>
''', unsafe_allow_html=True)

# -----------------------------
# SIDEBAR INPUTS
# -----------------------------
st.sidebar.title("⚙ Project Inputs")
st.caption("Built with CrewAI + Streamlit + Agentic AI")