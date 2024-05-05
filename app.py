import streamlit as st
from helpers import *
from chain import generate_lesson

TESTING = True

lesson_started_key = "lesson_started"
chat_history_key = "chat_history"
if lesson_started_key not in st.session_state:
    st.session_state[lesson_started_key] = False
if chat_history_key not in st.session_state:
    st.session_state[chat_history_key] = [("assistant", introduction_message)]

st.markdown(
    """
    <style>
    .e1nzilvr3 {display: none}
    </style>
    """,
    unsafe_allow_html=True,
)

st.title(landing_page_title)

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
    st.session_state[chat_history_key] = []
    st.session_state[chat_history_key].append(("assistant", "I am generating a lesson"))
    st.session_state[lesson_started_key] = True

    lesson = generate_lesson(
        st.session_state.native_language,
        st.session_state.target_language,
        st.session_state.level,
        st.session_state.topic,
        TESTING,
    )

    st.session_state.interactions = lesson.interactions
    st.session_state.closing_message = lesson.lesson_closing_message

    st.session_state.curr_msg_idx = 0
    st.session_state.max_msg_idx = len(lesson.interactions)

    assistant_output = get_assistant_output(st.session_state.interactions[0])

    st.session_state[chat_history_key] = [
        ("assistant", lesson.lesson_introduction_message.text),
        ("assistant", assistant_output),
    ]


def get_avatar(user):
    if user == "assistant":
        return "👴"
    else:
        return "🙋🏻‍♀️"


for user, text in st.session_state[chat_history_key]:
    with st.chat_message(user, avatar=get_avatar(user)):
        st.markdown(text, unsafe_allow_html=True)

if st.session_state[lesson_started_key]:
    if prompt := st.chat_input("enter what you want to say!"):

        st.session_state[chat_history_key].append(("user", prompt))
        with st.chat_message("user", avatar=get_avatar("user")):
            st.markdown(prompt)

        expected = st.session_state.interactions[st.session_state.curr_msg_idx].expected
        if prompt.lower() != expected.lower():
            response = f"That's not quite what I was expecting. I was expecting you to say: {expected}"
            with st.chat_message("assistant", avatar=get_avatar("assistant")):
                st.markdown(response)

        st.session_state.curr_msg_idx += 1
        if st.session_state.curr_msg_idx < st.session_state.max_msg_idx:
            new_teacher_stmt = get_assistant_output(
                st.session_state.interactions[st.session_state.curr_msg_idx]
            )
            st.session_state[chat_history_key].append(("assistant", new_teacher_stmt))
            with st.chat_message("assistant", avatar=get_avatar("assistant")):
                st.markdown(new_teacher_stmt, unsafe_allow_html=True)
        else:
            with st.chat_message("assistant", avatar=get_avatar("assistant")):
                st.markdown(
                    st.session_state.closing_message.text, unsafe_allow_html=True
                )
