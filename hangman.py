import random

level = {1: "easy", 2: "medium", 3: "hard"}

easy = ["One", "Two",]
medium = ["tricky", "More Tricky",]
hard = ["very hard indeed", "even harder",]



def get_level(l):
    words = level[l]
    word_list = eval(words)
    print(word_list[random.randint(0, len(word_list)-1 )])

get_level(1)


def get_word():
    pass

def keep_score():
    pass







