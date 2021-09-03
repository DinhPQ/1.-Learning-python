import json

data = json.load(open("App1_dictionary\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "The word does not exist!"

word = input("Enter the word: ")

print(translate(word))