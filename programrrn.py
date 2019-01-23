'''
Illustration of tome
'''

text = "The ship crashed into ice and from the glacier spewed out greed, where they shall be cemented."
mydictionary = {'ice':'glacier', 'glacier':'an iceberg', 'greed':'seeds of spite', 'cemented':'tarred'}
list_text = text.split()
for i in range(len(list_text)):
    for key in mydictionary.keys():
        if list_text[i] == key:
            list_text.remove(list_text[i])
            list_text.insert(i, mydictionary[key])
print(list_text)

### Build a Dictionary
# mydictionary = {'apples':input("Some fruit"), 'bananas':input("Some other fruit or thing"),
#                 'great':input("An adjective"),'smart':input("Another adjective")}

# print(' '.join(list_text))
# print(mydictionary.get('ice'))
# print(mydictionary['greed'])
# print(mydictionary['cemented'])
#
# def translate(text1, dict1):
#     list_text = text1.split()
#     new_list = []
#     for word in list_text:
#         translation = dict1.get(word)
#         new_list.append(translation if translation else word)
#     return' '.join(new_list)
#
# print(translate(text, mydictionary))


# new_text =' '.join(list_text)
# print(new_text)


# text = "The cat ran away from home because the outside world was so tempting, unlike her boring home."

# list_text = text.split(" ")
# print(text)
# print()
# print(list_text)
# alist_text = text.split('a')
# print(alist_text)

### Put back the text
# new_text = ' '
# for word in list_text:
#     new_text = new_text +' '+word  ###Put space between the quotes

# print(new_text)

# from tomelib import eliminate_repeats
# from tomelib import convert_list_2word
# word = 'Hippopotomonstrosesquipedaliophobic'
# alist = list(word)
#
# print(alist)
#
# print(eliminate_repeats(alist))
# print(convert_list_2word(alist))

# def eliminate_repeats(oldlist):
#     newlist = []          #empty
#     for letter in oldlist:
#         if letter not in newlist:  # Checks if letter from the old is in new <- empty so ideal
#             newlist.append(letter)   # take away the repeating letter
#     return newlist
#
# print(eliminate_repeats(alist))
#
# for letter in eliminate_repeats(alist):
#     print(letter, end='')
# print()
# print(len(alist))
#
# # Second method to convert a list of characters into a word
#
# n = len(alist)
# new_word = ''
# for i in range(n):
#     new_word = new_word + alist[i]   # Brackets must be used
#
# print(new_word)






# from tomelib import distance2d
# from tomelib import distance3d
#
# word = 'whateveryouwant'
# alist = list(word)
# print(alist)
# print(list('whateveryouwant'))
