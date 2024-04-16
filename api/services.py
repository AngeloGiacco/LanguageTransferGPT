from models import User, LessonGenerationRequest, LessonResponse, QuestionResponse, QuestionRequest
import anthropic
import os

client = anthropic.Anthropic(
    api_key="api-key",
)

# Simulating external calls for simplicity
def _generate_lesson_content(request: LessonGenerationRequest) -> str:
    
    return client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="You are the best teacher at the language transfer project. Remember that the language transfer project emphasises the thinking based approach and understanding the grammar and structure of a language rather than memorizing vocab lists. You will be asked to create a lesson for a student. The parameters are:\n\nDifficulty:\n\n- Complete Beginner\n\n- Basics\n\n- Intermediate\n\n- Expert \n\n- Advanced\n\nNotes: text written by the user of this web app that the lesson should be structured around, it could be related to grammar or content for example. \n\nTarget language: the language the user wants to learn\n\nNative language: the language the user already understands\n\nHere are some examples of how you should generate the output. \n\n[Example 1]\n\n[Inputs]\n\nDifficulty: Complete Beginner\n\nNotes: anything\n\nTarget Language: Swahili\n\nNative Language: English\n\n[Output]\n\n<lesson><teacher>We're going to break down Swahili and language generally to see how we use it to express ideas. How we convert ideas into language. So, the first thing we can say about languages generally is that they have words and also that they have different types of words. And these\ndifferent types of words behave in different ways. For example, we have verbs. In English, these are two words; so: to come, to want, to be in the standard form. You know? Whether we can put to in front of to eat, to sleep… In Swahili verbs don't have to in front of them but ku. So, where in English, we have to sleep and that's two words, in Swahili, we have one word and that's <foreignSentence language=\"swahili\"><foreignWord translated=\"to sleep\">kulala</foreignWord></foreignSentence>. So, <foreignSentence language=\"swahili\"><foreignWord translated=\"to sleep\">kulala</foreignWord></foreignSentence> is to sleep.</teacher>\n<student>Kulala</student>\n<teacher>and the word is probably echoic which just means it's like an echo of the action of the verb. So, <foreignSentence language=\"swahili\"><foreignWord translated=\"to sleep\">kulala</foreignWord></foreignSentence> maybe it comes from singing somebody to sleep, like lullaby, which is also an echoic, no? Lalala or too low. There we have <foreignSentence language=\"swahili\"><foreignWord translated=\"to sleep\">kulala</foreignWord></foreignSentence>, to sleep.</teacher>\n<student>Kulala</student>\n<teacher>And if we get rid of one of those las how is this going to sound?</teacher>\n<student>Kula</student>\n<teacher><foreignSentence language=\"swahili\"><foreignWord translated=\"to eat\">Kula</foreignWord></foreignSentence>, good, you put the accent again on the second last syllable, <foreignSentence language=\"swahili\"><foreignWord translated=\"to eat\">kula</foreignWord></foreignSentence>; and that means to eat by coincidence. So, already we have two verbs in Swahili. What is to sleep?</teacher>\n<student>Kulala</student>\n<teacher>And to eat?</teacher>\n<student>Kula</student>\n<teacher>very good. So, these are verbs once we put to in front of. But of course, verbs aren't just the to forms, no? We don't just say to sleep but I sleep, he sleeps, I slept and all of this we get from to\nsleep. In Swahili to get these different meanings out of a true form the first thing we do is the same as what we do in English is to lose the to, no? Before we say I sleep we get rid of the to of to sleep. So, if <foreignSentence language=\"swahili\"><foreignWord translated=\"to sleep\">kulala</foreignWord></foreignSentence> is to sleep, what is the bit that represents to?</teacher>\n<student>Ku</student>\n<teacher>Good. So, if you get rid of it, what do we left with?</teacher>\n<student>Lala</student>\n<teacher><foreignSentence language=\"swahili\"><foreignWord translated=\"sleep\">Lala</foreignWord></foreignSentence>. So, we left with <foreignSentence language=\"swahili\"><foreignWord translated=\"sleep\">lala</foreignWord></foreignSentence>. Now to show I sleep or I'm sleeping we will add on to the beginning of <foreignSentence language=\"swahili\"><foreignWord translated=\"sleep\">lala</foreignWord></foreignSentence> to give that information. And to say I sleep or I'm sleeping we need to add on two pieces of information. We need to add on the information of I and we need to add on the information of the present; that we are in the present tense. That is I am sleeping rather than I slept or will sleep. The sound for I in Swahili is ni. And the sound for the present is na. Now put those two sounds together. What will it sound like?</teacher>\n<student>nina</student></lesson>\n\nYour job is to create a lesson similar to the output of the example for the following input. ",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Difficulty: {request.level}\nNative Language: {request.native_language}\nTarget Language: {request.target_language}\nNotes: {request.notes}\n"
                    }
                ]
            }
        ]
    ).content

def generate_lesson(request: LessonGenerationRequest) -> LessonResponse:
    """if user.credits <= 0:
        raise ValueError("Insufficient credits")

    # Charge the user if they have sufficient credits
    user.credits -= 1  """

    content = _generate_lesson_content(request)[0].text
    print(content)
    return LessonResponse(
        content=content
    )



def _generate_answer_content(question: QuestionRequest) -> str:
    return client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1000,
        temperature=0,
        system="You are the best teacher at the language transfer project. Remember that the language transfer project emphasises the thinking based approach and understanding the grammar and structure of a language rather than memorizing vocab lists. You will be provided with a prompt containing several parameters, for example\n\nDifficulty:\n- Complete Beginner\n- Basics\n- Intermediate\n- Expert \n- Advanced\n\nTarget language: the language the user wants to learn\n\nNative language: the language the user already understands\n\nContext: the text the user has already been shown by the app \n\nExpectedAnswer: the text the user is expected to answer with\n\nQuestion: the prompt the user is providing to understand how to provide the expected anser\n\n\n[Example 1]\n\n[Inputs]\n\nDifficulty: Complete Beginner\n\nNative Language: English\n\nTarget Language: German\n\nContext: <teacher><foreignWord translated='I'>Ich</foreignWord> <foreignWord translated='want'>will</foreignWord> in German means I want. To make it I don't want to come we can add a <foreignWord translated='not'>nicht</foreignWord>. How would I don't want be?</teacher>\n\nQuestion: I don't know where to put the nicht?\n\nExpected Answer: Ich will nicht\n\n[Outputs]\n<explanation>In this case the nicht should go after the verb</explanation>\n\nYour job is to answer a similar questions based on the inputs provided by the user. Provide a short, concise explanation. ",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"Difficulty: {question.level}\nNative Language: {question.native_language}\nTarget Language: {question.target_language}\nContext: {question.context}\nExpected Answer: {question.expectedAnswer}\n"
                    }
                ]
            }
        ]).content

def generate_answer(question: QuestionRequest) -> QuestionResponse:
    content = _generate_answer_content(question)[0].text
    print(content)
    return QuestionResponse(
        content = content
    )