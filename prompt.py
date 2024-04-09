import anthropic

client = anthropic.Anthropic(
    api_key="my_api_key",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "You are the best teacher at the language transfer project. Remember that the language transfer project emphasises the thinking based approach and understanding the grammar and structure of a language rather than memorizing vocab lists. You will be asked to create a lesson for a student. The parameters are.\n\nDifficulty:\n- Complete Beginner\n- Basics\n- Intermediate\n- Expert \n- Advanced\n\nTopic: text written by the user of this web app that the language should be structured around. \n\nTarget language: the language the user wants to learn\n\nNative language: the language the user already understands\n\nHere are some examples of how you should generate the output. \n\n[Example 1]\n\n[Inputs]\n\nDifficulty: Complete Beginner\nTopic: anything\nTarget Language: Swahili\nNative Language: English\n\n[Output]\n<teacher>We're going to break down Swahili and language generally to see how we use it to express ideas. How we convert ideas into language. So, the first thing we can say about languages generally is that they have words and also that they have different types of words. And these\ndifferent types of words behave in different ways. For example, we have verbs. In English, these are two words; so: to come, to want, to be in the standard form. You know? Whether we can put to in front of to eat, to sleep… In Swahili verbs don't have to in front of them but ku.\nKu, which is k-u. So, where in English, we have to sleep and that's two words, in Swahili, we have one word and that's kulala. So, kulala is to sleep.</teacher>\n<student>Kulala</student>\n<teacher>and the word is probably echoic which just means it's like an echo of the action of the verb. So, kulala maybe it comes from singing somebody to sleep, like lullaby, which is also an echoic, no? Lalala or too low. There we have kulala, to sleep.</teacher>\n<student>Kulala</student>\n<teacher>And if we get rid of one of those las how is this going to sound?</teacher>\n<student>Kula</student>\n<teacher>Kula, good, you put the accent again on the second last syllable, kula; and that means to eat by coincidence. So, already we have two verbs in Swahili. What is to sleep?</teacher>\n<student>Kulala</student>\n<teacher>And to eat?</teacher>\n<student>Kula</student>\n<teacher>very good. So, these are verbs once we put to in front of. But of course, verbs aren't just the to forms, no? We don't just say to sleep but I sleep, he sleeps, I slept and all of this we get from to\nsleep. In Swahili to get these different meanings out of a true form the first thing we do is the same as what we do in English is to lose the to, no? Before we say I sleep we get rid of the to of to sleep. So, if kulala is to sleep, what is the bit that represents to?</teacher>\n<student>Ku</student>\n<teacher>Good. So, if you get rid of it, what do we left with?</teacher>\n<student>Lala</student>\n<teacher>Lala. So, we left with lala. Now to show I sleep or I'm sleeping we will add on to the beginning of lala to give that information. And to say I sleep or I'm sleeping we need to add on two pieces of information. We need to add on the information of I and we need to add on the information of the present; that we are in the present tense. That is I am sleeping rather than I slept or will sleep. The sound for I in Swahili is ni. And the sound for the present is na. Now put those two sounds together. What will it sound like?</teacher>\n<student>nina</student>\n<teacher>Nina. So, to say I in the present we have nina and we add that on to our verb without the ku. So tell me: I sleep or I'm sleeping</teacher>\n<teacher>Ninalala</teacher>\n\nYour job is to create a lesson similar to the output of the example for the following input. \n\nDifficulty: Complete Beginner\nNative Language: English\nTarget Language: French\nTopic: food\n\n"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "<teacher>\nLet's explore the French language and how it expresses ideas, focusing on the topic of food. One fundamental aspect of language is that it consists of different types of words that behave in various ways. In French, as in English, we have nouns, which are words that represent people, places, things, or ideas. For example, in English, we say \"food,\" and in French, the equivalent word is \"nourriture.\"\n</teacher>\n\n<student>\nNourriture\n</student>\n\n<teacher>\nVery good. Now, let's look at a more specific type of food: bread. In French, the word for bread is \"pain.\" Can you repeat that?\n</teacher>\n\n<student>\nPain\n</student>\n\n<teacher>\nExcellent. Now, if we want to say \"the bread,\" we need to add an article before the noun. In French, the definite article for masculine nouns is \"le.\" So, how would you say \"the bread\" in French?\n</teacher>\n\n<student>\nLe pain\n</student>\n\n<teacher>\nPerfect! You're getting the hang of it. Now, let's try something a little different. In English, we say \"I eat,\" using the verb \"to eat.\" In French, the verb \"to eat\" is \"manger.\" Can you say \"manger\"?\n</teacher>\n\n<student>\nManger\n</student>\n\n<teacher>\nGreat job. Now, to say \"I eat\" in French, we need to conjugate the verb \"manger\" according to the subject pronoun \"I,\" which is \"je\" in French. The conjugated form of \"manger\" for \"je\" is \"mange.\" So, how would you say \"I eat\" in French?\n</teacher>\n\n<student>\nJe mange\n</student>\n\n<teacher>\nFantastic! You've just learned how to say \"I eat\" in French. Let's put it all together now. How would you say \"I eat the bread\" in French?\n</teacher>\n\n<student>\nJe mange le pain\n</student>\n\n<teacher>\nBravo! You've successfully constructed a simple sentence in French using a subject pronoun, a conjugated verb, and a noun with its appropriate article. Keep practicing, and soon you'll be expressing more complex ideas about food and other topics in French!\n</teacher>"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Continue the conversation with a next lesson, keep the difficulty for a complete beginner. the student has provided the following comments:\n\n[Comments]\nNo comments, that was clear to me!"
                }
            ]
        },
        {
            "role": "assistant",
            "content": [
                {
                    "type": "text",
                    "text": "<teacher>\nGreat! Since you're comfortable with the previous lesson, let's continue exploring French with a focus on food. In the last lesson, we learned how to say \"I eat the bread\" in French, which was \"Je mange le pain.\" Now, let's learn how to express our likes and dislikes in French.\n</teacher>\n\n<student>\nOkay, I'm ready to learn more!\n</student>\n\n<teacher>\nTo say that you like something in French, you can use the verb \"aimer,\" which means \"to like.\" For example, to say \"I like,\" you would say \"j'aime.\" The apostrophe is used because \"je\" ends with a vowel, and \"aime\" starts with one. Can you repeat \"j'aime\"?\n</teacher>\n\n<student>\nJ'aime\n</student>\n\n<teacher>\nExcellent! Now, let's combine that with what we learned in the previous lesson. How would you say \"I like bread\" in French?\n</teacher>\n\n<student>\nJ'aime le pain\n</student>\n\n<teacher>\nPerfect! You're making great progress. Now, let's learn how to say \"I don't like.\" In French, to make a sentence negative, you add \"ne\" before the verb and \"pas\" after it. So, \"I don't like\" would be \"je n'aime pas.\" Can you repeat that?\n</teacher>\n\n<student>\nJe n'aime pas\n</student>\n\n<teacher>\nWell done! Let's practice with another food item. In French, \"chocolate\" is \"chocolat.\" How would you say \"I like chocolate\" in French?\n</teacher>\n\n<student>\nJ'aime le chocolat\n</student>\n\n<teacher>\nFantastic! Now, let's try saying \"I don't like chocolate\" in French.\n</teacher>\n\n<student>\nJe n'aime pas le chocolat\n</student>\n\n<teacher>\nBravo! You've just learned how to express your likes and dislikes in French using the verb \"aimer\" and the negative form \"ne ... pas.\" Keep practicing these phrases with different food items, and you'll soon be able to express your preferences confidently in French!\n</teacher>"
                }
            ]
        }
    ]
)
print(message.content)