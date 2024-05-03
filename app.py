import streamlit as st

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

st.title("Poppa")
st.header("Language lessons on demand!")

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
            "Select the language you want to learn:", languages, key="target_language"
        )
        current_language = st.selectbox(
            "Select your current language:", languages, key="native_language"
        )
        level = st.selectbox(
            "Select your level in the language you're learning:", levels, key="level"
        )
        topic = st.text_input("Enter the topic you want to learn about:", key="topic")

        submit = (
            st.form_submit_button("Start learning!")
            if st.session_state[lesson_started_key]
            else st.form_submit_button("Start new lesson!")
        )
user_input = None
if submit:
    system_message = f"You are a language tutor helping a {level} learner of {target_language} whose current language is {current_language}. The topic for the lesson is: {topic}. Provide an engaging and interactive lesson on this topic."
    st.session_state.chat_history.append(("assistant", "I am generating a lesson"))
    st.session_state[lesson_started_key] = True

for user, text in st.session_state.chat_history:
    with st.chat_message(user):
        st.markdown(text)

if st.session_state[lesson_started_key]:
    if prompt := st.chat_input("enter what you want to say!"):

        st.session_state.chat_history.append(("user", prompt))
        with st.chat_message("user"):
            st.markdown(prompt)

        response = f"You want a lesson in {st.session_state.native_language} for {st.session_state.target_language} at {st.session_state.level} level on {st.session_state.topic} and you said {prompt}"

        st.session_state.chat_history.append(("assistant", response))
        with st.chat_message("assistant"):
            st.markdown(response)
