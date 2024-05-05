from langchain_anthropic import ChatAnthropic
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from models import Lesson
import os
from dotenv import load_dotenv, find_dotenv
from helpers import sample_lesson

load_dotenv(find_dotenv())
OpenAI_key = os.environ.get("OPENAI_API_KEY")
Anthropic_key = os.environ.get("ANTHROPIC_API_KEY")


def get_chat(provider: str):
    if provider == "openai":
        return ChatOpenAI(
            model="gpt-3.5-turbo",
            openai_api_key=OpenAI_key,
            temperature=0,
        )
    else:
        return ChatAnthropic(
            temperature=0, model_name="claude-3-opus-20240229", api_key=Anthropic_key
        )


def generate_lesson(
    native_language: str,
    target_language: str,
    level: str,
    topic: str,
    test: bool = False,
    provider: str = "openai",
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
            "native_language": native_language,
            "target_language": target_language,
            "level": level,
            "topic": topic,
        }
    )
    return result


def generate_continuation_lesson(
    native_language: str,
    target_language: str,
    level: str,
    topic: str,
    continuation: str,
    student_feedback: str,
    test: bool = False,
    provider: str = "openai",
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
            "native_language": native_language,
            "target_language": target_language,
            "level": level,
            "topic": topic,
            "continuation": continuation,
            "student_feedback": student_feedback,
        }
    )
    return result
