import json
data = json.load(open("App1_dictionary\data.json"))

#The argument to process text type of data. "difflib"
import difflib

#The SequenceMatch from difflib: is to find out how match the string to the "list of string"
from difflib import SequenceMatcher
print(SequenceMatcher(None, "rainn", "rain").ratio())

#The get_close_matches from difflib: to return the close match of string from the "list of string".
#The argument is get_close_matches(word, possibilities, n=3, cutoff=0.6), in which:
#   The "word": is your variable that you looking for
#   The "possibilities" is the list of string that contain the results
#   The n=3 is the default number of results that you want to show.
#   The cutoff=0.6 is the matching ratio that you want to search for. The ratio can be calculated and visualised by SequenceMatcher(None, "input_string", "base_string").ratio()
from difflib import get_close_matches
results = get_close_matches("rainn", data.keys(), n = 10, cutoff = 0.5)
print(results)