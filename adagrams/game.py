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
    pass

def score_word(word):
    pass

def get_highest_word_score(word_list):
    pass

# print(draw_letters())