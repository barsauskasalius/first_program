"""
Sentence manipulation Class.
Class has to do following tasks:
* add sentence to the list
* remove sentence from the list
* find and return all sentences which contains certain word
* return first word from the sentence
* make all sentences camel case
* make all sentences lower case
* print all sentences
"""
import re


class SentenceManipulation:
    def __init__(self):
        self.sentence_list = []

    def add_sentence(self, sentence: str):
        self.sentence_list.append(sentence)

    def remove_sentence_by_index(self, index: int):
        del self.sentence_list[index]

    # "I like python !"
    def find_word(self, word):
        found = []
        for sentence in self.sentence_list:  # type: str
            search = sentence.find(word)
            if search != -1:
                found.append(sentence)
        return found

    def first_letter_upper(self):
        new = []
        for sentence in self.sentence_list:  # type: str
            new.append(sentence.title())
        self.sentence_list = new

    def print_all(self):
        print(" ".join(self.sentence_list))


mp = SentenceManipulation()

mp.add_sentence("I  like python !")
mp.add_sentence("coding is fun")
mp.add_sentence("I am 30 years old")

mp.first_letter_upper()
mp.print_all()

mp.remove_sentence_by_index(0)
