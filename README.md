# LanguageTransferGPT

## Todo:

 - [x] unsubscribe from scribd 

 - [x] clean corpus to unified standard 
 
 - [ ] reach out to Mihalis for all transcripts? 
 
 - [ ] fine tune LLM over corpus
 
 - [ ] usefine tuned LLM to batch create tracks for a course of specific new language
 
 - [ ] create new course by making lessons incrementally, one at a time and feeding already generated lessons into prompt. 
 
 - [ ] make it possible to create a lesson for a specific topic/word

## unified standard ideas for corpus:

- [x] Student: prefix not s: (same for teacher)

- [x] remove course style explanation (not needed to train on)

- [x] remove track numbers

- [x] add difficulty value to a chunk as a kind of positional element => might be helpful in future

- [ ] chunk into lessons?

## Languages to target

Courses to create from scratch:

- [ ] Swedish (personal interest)

- [ ] Russian

- [ ] Chinese

- [ ] Arabic

- [ ] Turkish

Courses to complete:

- [ ] German

- [ ] Italian 


Probably harder because there's not much material to train on:
- [ ] English for X-speaker

## finetuning ideas

I read the paper TaiwanLLM and think we could recreate their finetuning set up. 

It consists of:

1. Continued Pre-Training (CPT): fine tuning over a large corpus (in their case large scale scraping of Taiwanese content)

2. Supervised Fine-Tuning (SFT): "After continue-pretraining, we fine-tune the model on a dataset of
multi-turn dialogues". This is what we could use. 

3. Feedback Supervised Fine-Tuning (Feedback SFT): In the final stage, we refine the model based
on positive feedback from real users. Our MVP should allow users to provide binary feedback. 

Note for myself: just saw that gemma models have tokenization vocab of 256k which seems pretty high, 
would potentially make them a good choice for this project (i'm guessing there'd be better multilingual perf)