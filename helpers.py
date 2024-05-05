from models import *

supported_languages = [
    "English",
    "French",
    "Chinese",
    "Spanish",
    "Hindi",
    "Portuguese",
    "German",
    "Japanese",
    "Arabic",
    "Russian",
    "Korean",
    "Indonesian",
    "Italian",
    "Dutch",
    "Turkish",
    "Polish",
    "Swedish",
    "Filipino",
    "Malay",
    "Romanian",
    "Ukrainian",
    "Greek",
    "Czech",
    "Danish",
    "Finnish",
    "Bulgarian",
    "Croatian",
    "Slovak",
    "Tamil",
]

introduction_message = """Please fill out the form on the left and we can jump into a lesson on anything you want :) <br>
By the way, I can teach you any language, from any language, at any level! Let's go!"""

landing_page_title = "👴 poppa - infinite language lessons"

sample_lesson = Lesson(
    thinking=Thinking(
        text="In this lesson, we will explore how Swahili uses different word types, focusing on verbs. We'll look at the infinitive form of verbs using 'ku' and how to conjugate verbs in the present tense first person singular form using 'nina'. The verbs 'kulala' (to sleep) and 'kula' (to eat) will be used as examples."
    ),
    lesson_introduction_message=Introduction(
        text="Today we're going to learn about verbs in Swahili. We'll see how verbs are structured and how to say 'to do' something as well as how to conjugate verbs to say 'I am doing' something. Let's dive in and explore some examples!"
    ),
    interactions=[
        Interaction(
            explanation="In Swahili, the infinitive form of verbs, equivalent to 'to do' in English, starts with 'ku'. For example, 'to sleep' is 'kulala' and 'to eat' is 'kula'.",
            question="How do you say 'to sleep' in Swahili?",
            expected="kulala",
        ),
        Interaction(
            explanation="To conjugate a verb in the present tense for 'I', we remove the 'ku' and add 'nina' to the beginning. 'Nina' combines 'ni' meaning 'I' and 'na' indicating present tense.",
            question="If 'lala' is the verb meaning sleep, how would you say 'I sleep' or 'I am sleeping'?",
            expected="ninalala",
        ),
    ],
    lesson_closing_message=Closing(
        text="Great job today! You learned how to form infinitive verbs with 'ku' and conjugate them in first person present tense using 'nina'. Keep practicing with other verbs and soon you'll be expressing yourself more fully in Swahili. Come back for the next lesson!"
    ),
)


def get_assistant_output(interaction: Interaction) -> str:
    return f"{interaction.explanation} {interaction.question}"
