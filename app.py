from typing import Dict, Any
from dotenv import load_dotenv
import warnings
warnings.filterwarnings("ignore", category=UserWarning)
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import DuckDuckGoSearchRun, WikipediaQueryRun, ArxivQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_classic.agents import create_react_agent, AgentExecutor
from langchain_classic import hub
load_dotenv()

# ------------------ LLM ------------------
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# ------------------ TOOLS ------------------
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
web = DuckDuckGoSearchRun()
arxiv = ArxivQueryRun()

tools = [wiki, web, arxiv]

# ------------------ PROMPT ------------------
prompt = hub.pull("hwchase17/react")

# ------------------ RESEARCH AGENT ------------------
research_agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt
)

research_executor = AgentExecutor(
    agent=research_agent,
    tools=tools,
    verbose=False,
    handle_parsing_errors=True
)

# ------------------ SUMMARIZER AGENT ------------------
def summarizer_agent(content: str) -> str:
    prompt = f"""
Summarize the following content from research agent into 100-150 words.
Make it professional, structured, and accurate.

Content:
{content}
"""
    return llm.invoke(prompt).content

# ------------------ EMAIL AGENT ------------------
def email_agent(content: str) -> str:
    return f"""
Subject: Research Summary Overview

Dear Sir/Madam,

{content}

Regards,
AI Research Assistant
"""

# ------------------ ORCHESTRATOR ------------------
def run_pipeline(query: str) -> Dict[str, Any]:
    research_result = research_executor.invoke({"input": query})
    research_text = research_result.get("output", query)

    summary = summarizer_agent(research_text)
    email = email_agent(summary)

    return {
        "research": research_text,
        "summary": summary,
        "email": email
    }

