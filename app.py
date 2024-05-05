import streamlit as st
from helpers import *
from chain import generate_lesson, generate_continuation_lesson
from models import *

TESTING = False

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


def start_continuation_lesson(difficulty: ContinuationDifficulty):
    lesson = generate_continuation_lesson(
        st.session_state.native_language,
        st.session_state.target_language,
        st.session_state.level,
        st.session_state.topic,
        st.session_state.continuation_prompt,
        difficulty_to_string(difficulty),
        TESTING,
    )
    start_lesson(lesson)


def start_initial_lesson():
    lesson = generate_lesson(
        st.session_state.native_language,
        st.session_state.target_language,
        st.session_state.level,
        st.session_state.topic,
        TESTING,
    )
    start_lesson(lesson)


def start_lesson(lesson: Lesson):
    st.session_state.interactions = lesson.interactions
    st.session_state.closing_message = lesson.lesson_closing_message
    st.session_state.continuation_prompt = lesson.continuation_prompt
    st.session_state.curr_msg_idx = 0
    st.session_state.max_msg_idx = len(lesson.interactions)
    assistant_output = get_assistant_output(st.session_state.interactions[0])
    st.session_state[chat_history_key] = [
        ("assistant", lesson.lesson_introduction_message.text),
        ("assistant", assistant_output),
    ]
    st.session_state[lesson_started_key] = True


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

        submit = st.form_submit_button(
            "Start new lesson!", on_click=start_initial_lesson
        )


for user, text in st.session_state[chat_history_key]:
    with st.chat_message(user, avatar=get_avatar(user)):
        st.markdown(text, unsafe_allow_html=True)

if st.session_state[lesson_started_key]:
    if st.session_state.curr_msg_idx < st.session_state.max_msg_idx:
        if prompt := st.chat_input(
            "ask for clarification or answer, or just say anything !"
        ):

            st.session_state[chat_history_key].append(("user", prompt))
            with st.chat_message("user", avatar=get_avatar("user")):
                st.markdown(prompt)

            expected = st.session_state.interactions[
                st.session_state.curr_msg_idx
            ].expected
            if prompt.lower() != expected.lower():
                response = f"That's not quite what I was expecting. I was expecting you to say: {expected}"
                with st.chat_message("assistant", avatar=get_avatar("assistant")):
                    st.markdown(response)

            st.session_state.curr_msg_idx += 1
            if st.session_state.curr_msg_idx < st.session_state.max_msg_idx:
                new_teacher_stmt = get_assistant_output(
                    st.session_state.interactions[st.session_state.curr_msg_idx]
                )
                st.session_state[chat_history_key].append(
                    ("assistant", new_teacher_stmt)
                )
                with st.chat_message("assistant", avatar=get_avatar("assistant")):
                    st.markdown(new_teacher_stmt, unsafe_allow_html=True)
            else:
                st.session_state[chat_history_key].append(
                    ("assistant", st.session_state.closing_message.text)
                )
                with st.chat_message("assistant", avatar=get_avatar("assistant")):
                    st.markdown(
                        st.session_state.closing_message.text, unsafe_allow_html=True
                    )
                st.rerun()  # TODO: find a better way to ensure that input text box isnt shown
    else:
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            st.markdown(new_lesson_nudge, unsafe_allow_html=True)
        st.button(
            "New lesson, but easier 😭",
            key="new-easier",
            help="if this lesson was too hard!",
            on_click=start_continuation_lesson(ContinuationDifficulty.EASIER),
        )
        st.button(
            "New lesson, same difficulty 🤓",
            key="new-same",
            help="if this lesson was just right!",
            on_click=start_continuation_lesson(ContinuationDifficulty.SAME),
        )
        st.button(
            "New lesson, but harder 💪",
            key="new-harder",
            help="if this lesson was too easy!",
            on_click=start_continuation_lesson(ContinuationDifficulty.HARDER),
        )
