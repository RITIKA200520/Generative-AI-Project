import streamlit as st
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage


# ---------------------------------------
# LOAD API KEY
# ---------------------------------------
load_dotenv()


# ---------------------------------------
# GEMINI MODEL
# ---------------------------------------
model = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    temperature=0,
)


# ---------------------------------------
# AI MODES
# ---------------------------------------
modes = {
    "😡 Angry": "You are an angry AI agent. You respond aggressively, impatiently and in a frustrated way.",

    "😂 Funny": "You are a funny AI agent. You respond with jokes, humor and playful comments.",

    "😢 Sad": "You are a sad AI agent. You respond in a sad, emotional and slightly gloomy way."
}


# ---------------------------------------
# PAGE SETTINGS
# ---------------------------------------
st.set_page_config(
    page_title="AI Mood Chatbot",
    page_icon="🤖",
    layout="centered"
)


# ---------------------------------------
# CUSTOM CSS
# ---------------------------------------
st.markdown("""
<style>

.main {
    background-color: #0e1117;
}

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


# ---------------------------------------
# TITLE
# ---------------------------------------
st.markdown(
    '<div class="title">🤖 AI Mood Chatbot</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Choose your AI personality and start chatting</div>',
    unsafe_allow_html=True
)


# ---------------------------------------
# INITIAL SESSION STATE
# ---------------------------------------
if "mode" not in st.session_state:
    st.session_state.mode = "😂 Funny"

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(
            content=modes[st.session_state.mode]
        )
    ]


# ---------------------------------------
# MODE SELECTION
# ---------------------------------------
st.markdown(
    '<div class="mode-title">🎭 Choose AI Mode</div>',
    unsafe_allow_html=True
)


col1, col2, col3 = st.columns(3)


with col1:
    if st.button("😡 Angry", use_container_width=True):
        st.session_state.mode = "😡 Angry"

        st.session_state.messages = [
            SystemMessage(
                content=modes["😡 Angry"]
            )
        ]

        st.rerun()


with col2:
    if st.button("😂 Funny", use_container_width=True):
        st.session_state.mode = "😂 Funny"

        st.session_state.messages = [
            SystemMessage(
                content=modes["😂 Funny"]
            )
        ]

        st.rerun()


with col3:
    if st.button("😢 Sad", use_container_width=True):
        st.session_state.mode = "😢 Sad"

        st.session_state.messages = [
            SystemMessage(
                content=modes["😢 Sad"]
            )
        ]

        st.rerun()


# ---------------------------------------
# CURRENT MODE
# ---------------------------------------
st.info(
    f"Current AI mode: **{st.session_state.mode}**"
)


# ---------------------------------------
# SHOW CHAT HISTORY
# ---------------------------------------
for message in st.session_state.messages:

    if isinstance(message, HumanMessage):

        with st.chat_message("user"):
            st.write(message.content)

    elif isinstance(message, AIMessage):

        with st.chat_message("assistant"):
            st.write(message.content)


# ---------------------------------------
# CHAT INPUT
# ---------------------------------------
prompt = st.chat_input(
    "Type your message here..."
)


# ---------------------------------------
# WHEN USER SENDS MESSAGE
# ---------------------------------------
if prompt:

    # Show user message
    with st.chat_message("user"):
        st.write(prompt)

    # Add user message to memory
    st.session_state.messages.append(
        HumanMessage(content=prompt)
    )

    try:

        # Ask Gemini
        response = model.invoke(
            st.session_state.messages
        )

        answer = response.text

        # Add AI response
        st.session_state.messages.append(
            AIMessage(content=answer)
        )

        # Display AI response
        with st.chat_message("assistant"):
            st.write(answer)

    except Exception as e:

        st.error(
            f"Something went wrong:\n\n{e}"
        )


# ---------------------------------------
# CLEAR CHAT
# ---------------------------------------
if st.button("🧹 Clear Chat"):

    st.session_state.messages = [
        SystemMessage(
            content=modes[st.session_state.mode]
        )
    ]

    st.rerun()