"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

import sys

f, max_number = sys.argv
max_number = int(max_number)
# Create a dictonary of numbers to words

#Create a function that creates a list
#   of number words from the dictionary

d = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14 : 'fourteen',
    15 : 'fifteen',
    16 : 'sixteen',
    17 : 'seventeen',
    18 : 'eighteen',
    19 : 'nineteen',
    20 : 'twenty',
    30 : 'thirty',
    40 : 'forty',
    50 : 'fifty',
    60 : 'sixty',
    70 : 'seventy',
    80 : 'eighty',
    90 : 'ninety',
    100: 'hundred',
    1000: 'onethousand'
}


def solveit(max_number):
    #create words list
    words = create_words(max_number)

    # Count Letters
    return count_letters(words)

# Create a function that counts the letters in a list
def count_letters(words):
    letters_used = 0
    for word in words:
        letters_used += len(word)
    return letters_used

def create_words(max_number):
    words = []
    for i in range(1, max_number+1):
    # <21
        if i < 21:
            s = d[i]
    # <100
        elif i < 100:
            s = d[(i-i%10)] + d[i%10]
    # <1000
        elif i < 1000:
            s = d[(i/100)] + d[100] + "and" + d[(i%100)] + d[i%10]
    # 1000
        # elif i == 1000:
        #     s = d[i]
        words.append(s)
    print words
    return words

print solveit(max_number)

        