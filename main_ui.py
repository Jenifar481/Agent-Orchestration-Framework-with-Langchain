import streamlit as st
import requests
from datetime import datetime
import time

API_URL = "http://localhost:8000/run"

st.set_page_config(
    page_title="Multi-Agent AI",
    page_icon="🤖",
    layout="wide"
)

col1, col2, col3 = st.columns([1, 1, 1])
with col2: 
     st.title("(■ _ ■) Multi Agent AI")
     st.markdown("---")

now = datetime.now()
st.markdown(
    f"<p style='text-align:center; color:gray;'>🗒 ⤷{now.strftime('%A, %d %B %Y')}✦</p>",
    unsafe_allow_html=True
)

time.sleep(1)

st.caption(" Research • Summarize • Email Automation")

if "result" not in st.session_state:
    st.session_state.result = None

query = st.text_area("🔍︎ Enter your research topic:", placeholder="E.g., AI in Healthcare", height=100,
    help="Enter a topic and the agents will research, summarize, and draft an email", max_chars=2000)


col1, col2 = st.columns([1,1])
with col1:
    run = st.button(" Run ")

if run and query:
    with st.spinner("Agents are working... Please wait"):
        response = requests.post(API_URL, json={"query": query})
        st.session_state.result = response.json()

# ✅ Tabs are ALWAYS visible
tab1, tab2, tab3 = st.tabs(
    ["📚 Research Agent", "🕮 Summary Agent", "✉︎⌯⌲ Email Agent"]
)

with tab1:
    st.subheader("Research Output ⫘")
    if st.session_state.result:
        st.write(st.session_state.result["research"])
    else:
        st.info("Run the agents to view research output.")

with tab2:
    st.subheader("Summary Output 𓂃✍︎ ")
    if st.session_state.result:
        st.write(st.session_state.result["summary"])
    else:
        st.info("Summary will appear here after execution.")

with tab3:
    st.subheader("Email Draft જ⁀✎✉ ")
    if st.session_state.result:
        st.text(st.session_state.result["email"])
    else:
        st.info("Generated email will be shown here.")

with st.sidebar:
    st.title("֎ Multi-Agent AI")
    st.caption("LangChain powered")
    st.markdown("---")
    st.write("• Research Agent")
    st.write("• Summary Agent")
    st.write("• Email Agent")


st.caption("Developed by Jenifar")

st.markdown(
    "<hr><center>Built with Streamlit • LangChain</center>",
    unsafe_allow_html=True
)



