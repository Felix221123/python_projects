#this project gets the meaning od the word you type
from PyDictionary import PyDictionary
from pprint import pprint
dictionary=PyDictionary()



def gets_meanings():
    user_input = input('enter any word you would like to get the meaning of ...')
    dictionary = PyDictionary(user_input)
    pprint(dictionary.printMeanings())

def gets_synonyms():
    user_input = input('enter any word you would like to get the meaning of ...')
    dictionary = PyDictionary(user_input)
    pprint(dictionary.getSynonyms())

def gets_Meaning():
    user_input = input('enter any word you would like to get the meaning of ...')
    dictionary = PyDictionary(user_input)
    pprint(dictionary.getMeanings())


