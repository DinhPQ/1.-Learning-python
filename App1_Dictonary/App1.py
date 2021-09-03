import json

data = json.load(open("data.json"))

def dictionary(w):
    return data(w)

word = input("Enter the word: ")

print(dictionary(word))