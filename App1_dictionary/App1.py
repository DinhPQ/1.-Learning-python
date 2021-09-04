import json
import difflib
from difflib import get_close_matches

data = json.load(open("App1_dictionary\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        check = input("Did you mean %s instead? \nEnter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])
        if check == "Y" or check == "y":
            return data[get_close_matches(w, data.keys())[0]]
        else:
            return "The word does not exist!"
    else:
        return "The word does not exist!"

word = input("Enter the word: ")

print(translate(word))