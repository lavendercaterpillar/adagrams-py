from random import randint

LETTER_POOL = {
    'A': 9, 
    'B': 2, 
    'C': 2, 
    'D': 4, 
    'E': 12, 
    'F': 2, 
    'G': 3, 
    'H': 2, 
    'I': 9, 
    'J': 1, 
    'K': 1, 
    'L': 4, 
    'M': 2, 
    'N': 6, 
    'O': 8, 
    'P': 2, 
    'Q': 1, 
    'R': 6, 
    'S': 4, 
    'T': 6, 
    'U': 4, 
    'V': 2, 
    'W': 2, 
    'X': 1, 
    'Y': 2, 
    'Z': 1
}


def draw_letters():
    # Convert letter pool dict to a list with letters repeated the same number as in the pool
    # the list above has 98 letters.
    # make a random selection out of 98 letters of pool list.
    # add the selected letter to the hand and add a counter that shows frequency of the letter in the hand
    # draw hand should be a dict array with k/v as letters / freq
    # check if freq of the selected letter is less than the freq of the pool
    # repeat this for 10 times!
    # return is a list of hand letters!
    
    letter_pool_list = []
    hand_dict = {}
    hand_list = []

    for letter, frequency in LETTER_POOL.items():
        for i in range(frequency):
            letter_pool_list.append(letter)

    # for i in range(10):
    hand_counter = 1
    while hand_counter <= 10:
        draw = randint(0, 97)
        letter = letter_pool_list[draw]

        if letter not in hand_dict:
            hand_dict[letter] = 1
        else:
            if hand_dict[letter] < LETTER_POOL[letter]:
                hand_dict[letter] += 1
            else:
                continue
        
        hand_counter += 1

    for letter, frequency in hand_dict.items():
        for i in range(frequency):
            hand_list.append(letter)

    return hand_list


def uses_available_letters(word, letter_bank):
    # first need to understand what are letters in word and how many of the letter do we have.
    # then I need to compare each letter with my draw bank:
    # if the letter in the word doesn't exist in the draw return false
    # if the letter is in the draw bank then check if the frequency in the word 
    # is more than the frequency of same letter in the draw bank
    
    word = word.upper()
    word_dict = {}
    letter_bank_dict = {}


    for character in word:
        if character not in word_dict:
            word_dict[character] = 1
        else:
            word_dict[character] += 1

    for character in letter_bank:
        if character not in letter_bank_dict:
            letter_bank_dict[character] = 1
        else:
            letter_bank_dict[character] += 1

    for character, frequency in word_dict.items():
        if  character not in letter_bank_dict:
            return False
        else:
            if frequency > letter_bank_dict[character]:
                return False
    return True
    

def make_dict(array):
    '''
    input: a sting or a list of characters
    output: a dictionary of letters as keys, and frequency as values
    '''
    make_dict = {}
    for character in array:
        if character not in make_dict:
            make_dict[character] = 1
        else:
            make_dict[character] += 1
    return make_dict


def score_word(word):
    # build a score chart
    # then start to calc the score.
    # compare the letters in the word with the letters in score chart. 
    # add corresponding value to the total score
    # Chech if the length of word is more than 7 
    # (should we check if it is more than 10?)
    # return the total score

    score_chart = {'A':1,
                   'B':3,
                   'C':3,
                   'D':2,
                   'E':1,
                   'F':4,
                   'G':2,
                   'H':4,
                   'I':1,
                   'J':8,
                   'K':5,
                   'L':1,
                   'M':3,
                   'N':1,
                   'O':1,
                   'P':3,
                   'Q':10,
                   'R':1,
                   'S':1,
                   'T':1,
                   'U':1,
                   'V':4,
                   'W':4,
                   'X':8,
                   'Y':4,
                   'Z':10}
    # letter_bank = draw_letters()
    word = word.upper()
    word_dict = make_dict(word)

    # if uses_available_letters(word, letter_bank):
    total_score = 0

    for letter, frequency in word_dict.items():
        total_score += score_chart[letter] * frequency

    if len(word) >= 7:
        total_score += 8

    return total_score
    

def get_highest_word_score(word_list):
    pass

