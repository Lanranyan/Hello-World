
import math

def fibon_sequence(n):  # everything under and indented under def is part of the function
    x = 1
    y = 1

    count = 1   ### "cont" is 'continue' # Quotes don't work around the 1
    n = int(input('Enter how many Fibonacci numbers you want:'))
    while count <= n:
        print('A new Fibon number is:',x+y)
        temp = x
        x = y
        y = y + temp
        count = count + 1

def swap(a,b):
    temp = a
    a = b
    b = temp
    return print(a,b)

def distance2d(x1, y1, x2, y2):
    d = math.sqrt((x1 -x2)**2+(y1 - y2)**2)
    return d

def distance3d(x1, y1, z1, x2, y2, z2):
    d = math.sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)

#### Gets rid of the same letters
def eliminate_repeats(oldlist):
    newlist = []          #empty
    for letter in oldlist:
        if letter not in newlist:  # Checks if letter from the old is in new <- empty so ideal
            newlist.append(letter)   # take away the repeating letter
    return newlist

def convert_list_2word(alist):
    n = len(alist)
    new_word = ''
    for i in range(n):
        new_word = new_word + alist[i]
    return new_word

def translate(text1, dict1):
    list_text = text1.split()
    new_list = []
    for word in list_text:
        translation = dict1.get(word)
        new_list.append(translation if translation else word)
    return' '.join(new_list)

print(translate(text, mydictionary))
