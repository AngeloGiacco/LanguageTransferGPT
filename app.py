import streamlit as st
from helpers import *

lesson_started_key = "lesson_started"

if lesson_started_key not in st.session_state:
    st.session_state[lesson_started_key] = False
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.markdown(
    """
    <style>
    .e1nzilvr3 {display: none}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("👴 poppa - infinite language lessons")

with st.form("my_form"):
    # Define the available languages and levels
    with st.sidebar:
        st.write("What do you want to learn?")
        languages = ["English", "Spanish", "French", "German", "Italian"]
        levels = [
            "Complete Beginner",
            "Basic",
            "Intermediate",
            "Advanced",
            "Expert",
        ]
        target_language = st.selectbox(
            "Select the language you want to learn:",
            supported_languages,
            key="target_language",
            index=1,
        )
        current_language = st.selectbox(
            "Select your current language:",
            supported_languages,
            key="native_language",
            index=0,
        )
        level = st.selectbox(
            "Select your level in the language you're learning:",
            levels,
            key="level",
            index=1,
        )
        topic = st.text_input("Want to learn something in particular?", key="topic")

        submit = (
            st.form_submit_button("Start learning!")
            if not st.session_state[lesson_started_key]
            else st.form_submit_button("Start new lesson!")
        )
if submit:
    st.session_state.chat_history = []
    st.session_state.chat_history.append(("assistant", "I am generating a lesson"))
    st.session_state[lesson_started_key] = True


def get_avatar(user):
    if user == "assistant":
        return "👴"
    else:
        return "🙋🏻‍♀️"


for user, text in st.session_state.chat_history:
    with st.chat_message(user, avatar=get_avatar(user)):
        st.markdown(text, unsafe_allow_html=True)

if st.session_state[lesson_started_key]:
    if prompt := st.chat_input("enter what you want to say!"):

        st.session_state.chat_history.append(("user", prompt))
        with st.chat_message("user", avatar=get_avatar("user")):
            st.markdown(prompt)

        response = f"<p>You want a lesson in {st.session_state.native_language} for {st.session_state.target_language} at {st.session_state.level} level on {st.session_state.topic} and you said {prompt}</p>"

        st.session_state.chat_history.append(("assistant", response))
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            st.markdown(response, unsafe_allow_html=True)
