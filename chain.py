from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models import *
import os
from dotenv import load_dotenv, find_dotenv
from helpers import sample_lesson

load_dotenv(find_dotenv())
OpenAI_key = os.environ.get("OPENAI_API_KEY")
Anthropic_key = os.environ.get("ANTHROPIC_API_KEY")

default_provider = "openai"


def get_chat(provider: str):
    if provider == "openai":
        return ChatOpenAI(
            model="gpt-4-turbo",
            openai_api_key=OpenAI_key,
            temperature=0,
        )
    else:
        return ChatAnthropic(
            temperature=0, model_name="claude-3-opus-20240229", api_key=Anthropic_key
        )


def generate_lesson(
    lesson_params: LessonParams,
    test: bool = False,
    provider: str = default_provider,
) -> Lesson:
    if test:
        return sample_lesson
    chat = get_chat(provider).with_structured_output(Lesson)

    system = """You are the best teacher at the language transfer project. Remember that the language transfer project emphasises the thinking based approach and understanding the grammar and structure of a language rather than memorizing vocab lists. You will be asked to create a lesson for a student. The parameters are.  Difficulty: - Complete Beginner - Basics - Intermediate - Expert  - Advanced  Topic: text written by the user of this web app that the language should be structured around.   Target language: the language the user wants to learn  Native language: the language the user already understands  Here are some examples of how you should generate the output.   
    
    [Example 1]  
    [Inputs]  
    Difficulty: Complete Beginner 
    Topic: anything 
    Target Language: Swahili 
    Native Language: English  
    
    [Output] 

    {{"thinking": {{
        "thinking": "In this lesson, we will explore how Swahili uses different word types, focusing on verbs. We'll look at the infinitive form of verbs using 'ku' and how to conjugate verbs in the present tense first person singular form using 'nina'. The verbs 'kulala' (to sleep), 'kula' (to eat), 'kusoma' (to read), and 'kuandika' (to write) will be used as examples."
    }},
    "lesson_introduction": {{
        "lesson_introduction": "Today we're going to learn about verbs in Swahili. We'll see how verbs are structured and how to say 'to do' something as well as how to conjugate verbs to say 'I am doing' something. Let's dive in and explore some examples!"
    }},
    "interactions": [
        {{
            "explanation": "In Swahili, the infinitive form of verbs, equivalent to 'to do' in English, starts with 'ku'. For example, 'to sleep' is 'kulala' and 'to eat' is 'kula'.",
            "question": "How do you say 'to sleep' in Swahili?",
            "expected": "kulala"
        }},
        {{
            "explanation": "To conjugate a verb in the present tense for 'I', we remove the 'ku' and add 'nina' to the beginning. 'Nina' combines 'ni' meaning 'I' and 'na' indicating present tense.",
            "question": "If 'lala' is the verb meaning sleep, how would you say 'I sleep' or 'I am sleeping'?",
            "expected": "ninalala"
        }},
        {{
            "explanation": "Let's look at a couple more examples. 'To read' in Swahili is 'kusoma' and 'to write' is 'kuandika'. Remember, to conjugate these in first person present tense, we drop the 'ku' and add 'nina'.",
            "question": "How would you say 'I am reading' in Swahili?",
            "expected": "ninasoma"
        }},
        {{
            "explanation": "Great! Now let's practice with 'kuandika', which means 'to write'.",
            "question": "Using 'kuandika', how would you translate 'I am writing' into Swahili?",
            "expected": "ninaandika"
        }},
        {{
            "explanation": "Great! Now let's practice with 'kuandika', which means 'to write'.",
            "question": "Using 'kuandika', how would you translate 'I am writing' into Swahili?",
            "expected": "ninaandika"
        }}
    ],
    "lesson_closing": {{
        "closing_message": "Excellent work today! You've gotten the hang of forming infinitive verbs with 'ku' and conjugating them in first person present tense using 'nina'. Keep practicing with even more verbs to expand your Swahili vocabulary and expression. I look forward to seeing you in the next lesson!"
    }},
    "continuation" : "learnt kulala, kusoma, kuandika and kula and introduced how to transform the infinitive to the first person present tense"
}}}}  
    Don't ask any questions in the explanation part. Make sure to introduce all vocab necessary to answer the question. in the explanation don't use overly grammatical langauge. use intuitive language.
    Your job is to create a lesson similar to the output of the example for the input that you will receive.

    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "please generate a lesson with native language: {native_language}, target_language: {target_language}, level: {level}, topic: {topic}",
            ),
        ],
    )
    chain = prompt | chat
    result = chain.invoke(
        {
            "native_language": lesson_params.native_language,
            "target_language": lesson_params.target_language,
            "level": lesson_params.level,
            "topic": lesson_params.topic,
        }
    )
    return result


def generate_continuation_lesson(
    lesson_params: LessonParams,
    continuation: str,
    student_feedback: str,
    test: bool = False,
    provider: str = default_provider,
) -> Lesson:
    if test:
        return sample_lesson
    chat = get_chat(provider).with_structured_output(Lesson)

    system = """You are the best teacher at the language transfer project. Remember that the language transfer project emphasises the thinking based approach and understanding the grammar and structure of a language rather than memorizing vocab lists. You will be asked to create a lesson for a student. The parameters are.  Difficulty: - Complete Beginner - Basics - Intermediate - Expert  - Advanced  Topic: text written by the user of this web app that the language should be structured around.   Target language: the language the user wants to learn  Native language: the language the user already understands  Here are some examples of how you should generate the output.   
    
    [Example 1]  
    [Inputs]  
    Difficulty: Complete Beginner 
    Topic: anything 
    Target Language: Swahili 
    Native Language: English  
    
    [Output] 

    {{"thinking": {{
        "thinking": "In this lesson, we will explore how Swahili uses different word types, focusing on verbs. We'll look at the infinitive form of verbs using 'ku' and how to conjugate verbs in the present tense first person singular form using 'nina'. The verbs 'kulala' (to sleep), 'kula' (to eat), 'kusoma' (to read), and 'kuandika' (to write) will be used as examples."
    }},
    "lesson_introduction": {{
        "lesson_introduction": "Today we're going to learn about verbs in Swahili. We'll see how verbs are structured and how to say 'to do' something as well as how to conjugate verbs to say 'I am doing' something. Let's dive in and explore some examples!"
    }},
    "interactions": [
        {{
            "explanation": "In Swahili, the infinitive form of verbs, equivalent to 'to do' in English, starts with 'ku'. For example, 'to sleep' is 'kulala' and 'to eat' is 'kula'.",
            "question": "How do you say 'to sleep' in Swahili?",
            "expected": "kulala"
        }},
        {{
            "explanation": "To conjugate a verb in the present tense for 'I', we remove the 'ku' and add 'nina' to the beginning. 'Nina' combines 'ni' meaning 'I' and 'na' indicating present tense.",
            "question": "If 'lala' is the verb meaning sleep, how would you say 'I sleep' or 'I am sleeping'?",
            "expected": "ninalala"
        }},
        {{
            "explanation": "Let's look at a couple more examples. 'To read' in Swahili is 'kusoma' and 'to write' is 'kuandika'. Remember, to conjugate these in first person present tense, we drop the 'ku' and add 'nina'.",
            "question": "How would you say 'I am reading' in Swahili?",
            "expected": "ninasoma"
        }},
        {{
            "explanation": "Great! Now let's practice with 'kuandika', which means 'to write'.",
            "question": "Using 'kuandika', how would you translate 'I am writing' into Swahili?",
            "expected": "ninaandika"
        }}
    ],
    "lesson_closing": {{
        "closing_message": "Excellent work today! You've gotten the hang of forming infinitive verbs with 'ku' and conjugating them in first person present tense using 'nina'. Keep practicing with even more verbs to expand your Swahili vocabulary and expression. I look forward to seeing you in the next lesson!"
    }},
    "continuation" : "learnt kulala and kula and introduced how to transform kulala to ninalala"
}}}}  
        
    You have already created a lesson like the one shown above. The student enjoyed the lesson and would like another one. You will be provided with their feedback and a summary of the previous lesson so that you can carry on a new one. 

    """

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "please generate a lesson with native language: {native_language}, target_language: {target_language}, level: {level}, topic: {topic}. The previous lesson was about the following: {continuation}. The student feedback is the following: {student_feedback}. Please generate a new lesson.",
            ),
        ],
    )
    chain = prompt | chat
    result = chain.invoke(
        {
            "native_language": lesson_params.native_language,
            "target_language": lesson_params.target_language,
            "level": lesson_params.level,
            "topic": lesson_params.topic,
            "continuation": continuation,
            "student_feedback": student_feedback,
        }
    )
    return result


def get_follow_on(
    interaction: Interaction,
    answer: str,
    lesson_params: LessonParams,
    provider: str = default_provider,
):
    chat = get_chat(provider).with_structured_output(FollowUp)
    system = """You are the best teacher at the language transfer project. Remember that the language transfer project emphasises the thinking based approach and understanding the grammar and structure of a language rather than memorizing vocab lists. You have created a lesson for a user. 
    You first said an explanation of a new concept, then you asked a question to the student, then you received a response.
    Your job is to check whether the response to the explanation and question was correct. If it was no follow up is needed and null can be generated. 
    The response may be wrong however, or the student may have simply asked for clarification. In this case please generate a follow up, which is another interaction with an explanation, question and expected answer.
    When assessing if an answer is correct, you can be lenient on punctuation and usage of synonyms. 
    Please bear in mind the student has native language: {native_language}, they want to learn: {target_language} at level: {level} and requested a lesson about the topic: {topic}."""

    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", system),
            (
                "human",
                "the student was given this explanation '{explanation}'. the student was asked the question: '{question}'. the student gave this answer: {answer}. ",
            ),
        ],
    )

    chain = prompt | chat
    result = chain.invoke(
        {
            "native_language": lesson_params.native_language,
            "target_language": lesson_params.target_language,
            "level": lesson_params.level,
            "topic": lesson_params.topic,
            "explanation": interaction.explanation,
            "question": interaction.question,
            "expected": interaction.expected,
            "answer": answer,
        }
    )
    return result
