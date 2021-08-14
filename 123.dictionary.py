import json
from difflib import get_close_matches #this library is used to give close match of word like if the key is rock and we mistakenly give input as rack,roocck,then it should consider it as a rock
data = json.load(open("data.json")) #data.json file is converted or loaded into the python dictionary 

# in dictionary there is only key like rock paper etc but if i want to insert a key without affecting cases like rock as Rock ROCK etc then also it should also give me the output.
# it should not show me the error like Rock is not key,it should consider Rock ROCK rock and rock as rock. 
def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :#get_close_matches()will give the similar word from the all the keys of dictionary even if we give wrong input as ROOCK rocck etc.
      #if the length of the word that have entered wrong(rocckk)>0 
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])#it will show the correct word (key)from dictionary like rock. 
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys ")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("pugger your paw steps on wrong keys")



word = input("Enter the word you want to search")
output = translate(word)

# if one word has more than one meaning then it should show in a different line so human can read it easily for eg. give input as paper
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
