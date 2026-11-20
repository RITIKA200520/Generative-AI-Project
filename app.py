import os
import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)

st.markdown("""
<style>
.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    margin-bottom: 5px;
}
.subtitle {
    text-align: center;
    color: #aaaaaa;
    font-size: 17px;
    margin-bottom: 25px;
}
.mode-title {
    text-align: center;
    font-size: 20px;
    font-weight: bold;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

MODES = {
    "😡 Angry": "You are an angry AI agent. You respond aggressively, impatiently and in a frustrated way.",
    "😂 Funny": "You are a funny AI agent. You respond with jokes, humor and playful comments.",
    "😢 Sad":   "You are a sad AI agent. You respond in a sad, emotional and slightly gloomy way.",
    "😊 Normal": "You are a helpful, friendly AI assistant. You respond clearly and politely.",
}

MODEL_NAME = "gemini-2.0-flash-lite"


def get_api_key() -> str | None:
    """Return Google API key from Streamlit secrets, env, or sidebar input."""
    if hasattr(st, "secrets") and "GOOGLE_API_KEY" in st.secrets:
        return st.secrets["GOOGLE_API_KEY"]
    return os.getenv("GOOGLE_API_KEY")


# --- Sidebar ---
with st.sidebar:
    st.header("⚙️ Configuration")
    api_key = get_api_key()
    if not api_key:
        api_key = st.text_input(
            "Google API Key",
            type="password",
            placeholder="AIza...",
            help="Get your free key at https://aistudio.google.com",
        )
        if api_key:
            os.environ["GOOGLE_API_KEY"] = api_key
    else:
        st.success("API key loaded ✓")

    st.markdown("---")
    st.caption("Powered by Google Gemini")


# --- Title ---
st.markdown('<div class="title">🤖 AI Mood Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Choose your AI personality and start chatting</div>', unsafe_allow_html=True)

# --- Gate: require API key before proceeding ---
if not api_key:
    st.warning("Please enter your Google API Key in the sidebar to get started.")
    st.stop()

# --- Lazy model init (recreate only when key changes) ---
if "api_key_used" not in st.session_state or st.session_state.api_key_used != api_key:
    os.environ["GOOGLE_API_KEY"] = api_key
    st.session_state.api_key_used = api_key
    st.session_state.model = ChatGoogleGenerativeAI(model=MODEL_NAME, temperature=0.7)

model: ChatGoogleGenerativeAI = st.session_state.model

# --- Session defaults ---
if "mode" not in st.session_state:
    st.session_state.mode = "😂 Funny"

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=MODES[st.session_state.mode])]


def switch_mode(new_mode: str) -> None:
    st.session_state.mode = new_mode
    st.session_state.messages = [SystemMessage(content=MODES[new_mode])]


# --- Mode selection ---
st.markdown('<div class="mode-title">🎭 Choose AI Mode</div>', unsafe_allow_html=True)
cols = st.columns(len(MODES))
for col, mode_name in zip(cols, MODES):
    with col:
        if st.button(mode_name, use_container_width=True):
            switch_mode(mode_name)
            st.rerun()

st.info(f"Current AI mode: **{st.session_state.mode}**")

# --- Chat history ---
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

# --- Chat input ---
prompt = st.chat_input("Type your message here...")

if prompt:
    with st.chat_message("user"):
        st.write(prompt)

    st.session_state.messages.append(HumanMessage(content=prompt))

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.invoke(st.session_state.messages)
                answer = response.content
                st.session_state.messages.append(AIMessage(content=answer))
                st.write(answer)
            except Exception as e:
                err = str(e)
                if "API_KEY" in err.upper() or "401" in err or "403" in err:
                    st.error("Invalid or missing API key. Please check your Google API Key in the sidebar.")
                else:
                    st.error(f"Something went wrong: {err}")

# --- Clear chat ---
if st.button("🧹 Clear Chat"):
    switch_mode(st.session_state.mode)
    st.rerun()
