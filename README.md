# Poppa

poppa teaches you any language, in whatever language you need, on any topic you need, whenever you want

powered by anthropic + eleven labs. 

## goal
our goal is to make this version of Poppa publicly available, with a set number of free lessons per month

at any point during a lesson, the student can ask for help, talking to the model to understand the problem better

we will also auto-generate an entire course from beginner -> hero for the most popular languages (should cost less, but can't be interacted with)

## architecture

end goal for the backend is something like this

vocab spaced repetition store helps provide words that either haven't be practiced recently or should be introuced to the lesson generation prompt

the grammar memory is a description of the user's understanding of the language's grammar (updated to fit into a max token count )

Along with the user prompt, which helps us understand if the next lesson should be harder/easier or should be on a specific topic, 
we can generate the perfect next lesson

-------------------------------
|vocab spaced repetition store|--------------
-------------------------------             |
                                            |
                                            ⌄ 
---------------                       --------------------
| user prompt |---------------------->| generated lesson |
---------------                       --------------------
                                            ^
----------------                            |
|grammar memory|----------------------------| 
----------------