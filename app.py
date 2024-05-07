import streamlit as st
from helpers import *
from chain import generate_lesson, generate_continuation_lesson, get_follow_on
from models import *

TESTING = False

lesson_started_key = "lesson_started"
chat_history_key = "chat_history"
end_of_lesson_key = "end_of_lesson"
if lesson_started_key not in st.session_state:
    st.session_state[lesson_started_key] = False
if chat_history_key not in st.session_state:
    st.session_state[chat_history_key] = [("assistant", introduction_message)]
if end_of_lesson_key not in st.session_state:
    st.session_state[end_of_lesson_key] = False

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
        lesson_params=get_lesson_params(),
        continuation=st.session_state.continuation_prompt,
        student_feedback=difficulty_to_string(difficulty),
        test=TESTING,
    )
    start_lesson(lesson)
    st.rerun()


def start_initial_lesson():
    lesson = generate_lesson(
        lesson_params=get_lesson_params(),
        test=TESTING,
    )
    print(lesson)
    start_lesson(lesson)


def check_non_expected_response(user_input: str):
    # check if a follow on is needed if the response is wrong
    current_interaction: Interaction = st.session_state.interactions[
        st.session_state.curr_msg_idx
    ]
    follow_on: Optional[Interaction] = get_follow_on(
        interaction=current_interaction,
        answer=user_input,
        lesson_params=get_lesson_params(),
    ).interaction
    if follow_on:
        print("adding follow on")
        print(follow_on)
        st.session_state.interactions.insert(
            st.session_state.curr_msg_idx + 1, follow_on
        )
        update_max_len_interactions()
    else:
        print("skipping follow on")


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
    st.session_state[end_of_lesson_key] = False
    st.session_state[lesson_started_key] = True


with st.form("my_form"):
    # Define the available languages and levels
    with st.sidebar:
        st.write("What do you want to learn?")
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
                check_non_expected_response(user_input=prompt)

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
        st.session_state[end_of_lesson_key] = True
        with st.chat_message("assistant", avatar=get_avatar("assistant")):
            st.markdown(new_lesson_nudge, unsafe_allow_html=True)

if st.session_state[end_of_lesson_key]:
    continue_easier = st.button(
        "New lesson, but easier 😭",
        key="new-easier",
        help="if this lesson was too hard!",
    )
    continue_same = st.button(
        "New lesson, same difficulty 🤓",
        key="new-same",
        help="if this lesson was just right!",
    )
    continue_harder = st.button(
        "New lesson, but harder 💪",
        key="new-harder",
        help="if this lesson was too easy!",
    )

    if continue_easier:
        start_continuation_lesson(ContinuationDifficulty.EASIER)
    elif continue_same:
        start_continuation_lesson(ContinuationDifficulty.SAME)
    elif continue_harder:
        start_continuation_lesson(ContinuationDifficulty.HARDER)
