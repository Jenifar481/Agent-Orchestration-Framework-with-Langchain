import streamlit as st
import requests
from app import run_pipeline
from datetime import datetime
import time

API_URL = "http://localhost:8000/run"

import base64

def load_logo_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

st.set_page_config(
    page_title="Multi-Agent AI",
    page_icon="logo.png",
    layout="wide"
)

top_logo_base64 = load_logo_base64("im.png")

st.markdown(
    """
    <style>
    /* TextArea container */
    textarea {
    background-color: #EBF9FA !important;
    color: #1f2a44 !important;
    border: 1px solid #c7d2fe !important;
    border-radius: 12px !important;
}

textarea:focus {
    border-color: #4f46e5 !important;
    box-shadow: 0 0 8px rgba(79,70,229,0.4) !important;
}
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.markdown(
        f"""
        <div style="
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 14px;
        ">
            <img src="data:image/png;base64,{top_logo_base64}"
                 style="height:42px;" />
            <h1 style="
                margin: 0;
                color: var(--text-color);
                font-weight: 700;
            ">
                Multi-Agent AI
            </h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown("---")

now = datetime.now()
st.markdown(
    f"<p style='text-align:center; color:gray;'>🗒 ⤷{now.strftime('%A, %d %B %Y | %I:%M %p')}✦</p>",
    unsafe_allow_html=True
)

time.sleep(1)

#-----------------------
# Background Styling
#-----------------------

st.markdown(
    """
    <style>
        .stApp {
            background:
                radial-gradient(
                    circle at top left,
                    rgba(0, 128, 244, 0.22),
                    transparent 42%
                ),
                radial-gradient(
                    circle at bottom right,
                    rgba(132, 88, 131, 0.20),
                    transparent 46%
                ),
                linear-gradient(
                    135deg,
                    #f5f7fb,
                    #eef1f8
                );
        }
    </style>
    """,
    unsafe_allow_html=True
)



st.caption(" Research • Summarize • Email Automation")

if "result" not in st.session_state:
    st.session_state.result = None

query = st.text_area("🔍︎ Enter your research topic:", placeholder="E.g., AI in Healthcare", height=100,
    help="Enter a topic and the agents will research, summarize, and draft an email")


col1, col2 = st.columns([1,1])
with col1:
    run = st.button(" Run ")

if run and query:
    with st.spinner("Agents are working... Please wait"):
      st.session_state.result = run_pipeline(query)

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
    st.subheader("Email Draft ⁀✎✉ ")
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
