import streamlit as st

st.set_page_config(
    page_title="PHANTOM v3.0 SPECTRE",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ PHANTOM v3.0 SPECTRE")
st.subheader("Cybersecurity & OSINT Framework")

st.success("Dashboard is running!")

st.sidebar.title("Navigation")

module = st.sidebar.selectbox(
    "Select Module",
    [
        "Home",
        "IP Intelligence",
        "DNS Recon",
        "Port Scanner",
        "SSL/TLS Inspector",
        "HTTP Header Audit",
        "WHOIS Lookup"
    ]
)

st.header(module)
st.write("Welcome to PHANTOM Web Dashboard.")