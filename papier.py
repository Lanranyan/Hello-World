
def gallows(penal):
    if penal == 0 :
        gal = "  _______| \n"\
              "         | \n"\
              "         | \n"\
              "         | \n"\
              "         | \n"\
              "         | \n"\
              "        / \ \n"\
              "       /   \ \n"
    if penal == 1:
        gal = "  _______|\n" \
              "  |      |\n" \
              "         |\n" \
              "         |\n" \
              "         |\n" \
              "         |\n" \
              "        / \ \n" \
              "       /   \ \n"
    if penal == 2:
        gal = "  -------|\n" \
              "  |      |\n" \
              "  O      |\n" \
              "         |\n" \
              "         |\n" \
              "         |\n" \
              "        / \ \n" \
              "       /   \ \n"
    if penal == 3:
        gal = "  -------|\n" \
              "  |      |\n" \
              "  O      |\n" \
              "  |      |\n" \
              "  |      |\n" \
              "         |\n" \
              "        / \ \n" \
              "       /   \ \n"
    if penal == 4:
        gal = "  -------|\n" \
              "  |      |\n" \
              "  O      |\n" \
              "  | /    |\n" \
              "  |      |\n" \
              "         |\n" \
              "        / \ \n" \
              "       /   \ \n"
    if penal == 5:
        gal = "  -------|\n" \


    return gal
"  -------|\n" \
"  |      |\n" \
"  O      |\n" \
"  | /    |\n" \
"  |      |\n" \
"         |\n" \
"        / \ \n" \
"       /   \ \n"

word = 'heist'
secret_word = list(word)   # list the letters of the word
print(secret_word)
new_word = ['*' for i in range(len(secret_word))]  # Replaces every letter with * asterick
print(new_word)

penalty = 0
letters_used = []
while '*' in new_word and penalty<7:     #For as long as there's astericks, the word hasn't been fully guessed
    guess = input("Enter a letter \n")   # part where a letter is inputted
    if guess not in secret_word or guess in letters_used:       # Checks with the list with the letters
        penalty += 1  ### Same as penalty + 1, no spaces should be between +=
    else:
        for i in range(len(secret_word)):   # assigns positions according to the letters
            if guess == secret_word[i]: #checks if the letter is right
                new_word[i] = secret_word[i]   #replaces the letters into the *
    letters_used.append(guess)  # adds the letter to what you've used
    print(letters_used)   # Shows what you've used
    print(new_word)  # prints word's current state
    print('penalty', penalty)  #shows penalty ## Here will be placed the gallow calls
    print(gallows(penalty))
print("End")





