import json
import difflib
from difflib import get_close_matches

data = json.load(open("App1_dictionary\data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data: #since the database has definition of cities that capitalised. however, our code is lower case all the input and will eliminate the search for this such.
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        check = input("Did you mean %s instead? \nEnter Y if yes, or N if no: " %get_close_matches(w, data.keys())[0])
        if check == "Y" or check == "y":
            return data[get_close_matches(w, data.keys())[0]]
        elif check == "N" or check == "n":
            return "Does not find any match for your choice!"
        else:
            return "The word does not exist!"
    else:
        return "The word does not exist!"

word = input("Enter the word: ")

output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)