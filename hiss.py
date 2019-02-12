'''
Create a file to save on memory
Read the file with Persistent memory
'''


import pickle   #

# Key = name of player, value is a tuple(# of games played, # victories
# history = {'Archy':(12, 4), 'Betty':(10,6)}    #### start off with a dictionary
# # print(history)
# # print(history['Archy'])    ## To print a specific key from the diction
# # print(history['Archy'][0])    ## To specifically print a certain key, refer to its number position 0, 1 , 2...
# #
# # print(history['Betty'][1])
#
# ###Print the rate of success for Betty, (6 out of 10)
# # print("Betty's victory rate is", history['Betty'][1]/history['Betty'][0])
# # print("Betty's victory rate is", (history['Betty'][1]/history['Betty'][0])*100,'%')
#
# # rate_a = history['Archy'][1]/history['Archy'][0]
# # print("Archy's win rate is ", rate_a)
#
# #How to add another player to the history dictionary
#
# # history['Klaudia'] = (84,36)
# # print(history)

def rate_of_winning(dict, player):
    rate = dict[player][1]/dict[player][0]
    return print("The rate of winnings for", player,'is', round(rate, 2))

# rate_of_winning(history, 'Archy')
# rate_of_winning(dict=history, player='Betty')

# file_p = open('historyfile,p','wb')   #
# pickle.dump(history, file_p)   #dump is the saving and downloading of
# file_p.close()

file_p = open('historyfile,p','rb')     #rb to read it
history = pickle.load(file_p)
file_p.close()
print(history)
# history["Clarissa"] = (100, 95)
# print(history)

# file_p = open('historyfile,p','wb')   #
# pickle.dump(history, file_p)   #dump is the saving
# file_p.close()

for key in history.keys():
    rate_of_winning(history, key)