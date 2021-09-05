#First is to define the function that transform the input sentence into the readable-friendly sentence
from typing import ChainMap


def sentence_maker(sentence):
    interrogative = ("how", "what", "why", "is", "are", "could", "would", "when", "where", "does", "did", "do")
    capitalized = sentence.capitalize()
    if sentence.startswith(interrogative):
        return "{}?".format(capitalized)
    else:
        return "{}.".format(capitalized)

results = []    
while True:
    user_input = input("Type something: ")
    if user_input == "\end":
        break
    else:
        results.append(sentence_maker(user_input))

print(" ".join(results))