


# import random 

# out_of_guesses = 9
# words = ["kids", "food", "house", "car",]


# secret_word = random.choice(words)
# guess = ""



# while guess != secret_word and not (out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess:")
#         guess_count += 1
#     else:
#         out_of_lives = True

# if out_of_guesses:
#     print("Out of Lives, You Lose!")

# else:
#     print("You Win")
    

# print(secret_word)




import random

lives = 9

words = ["kids", "food", "house", "car",]

secret_word = random.choice(words)

clue = []

for x in secret_word:
    clue.append("_ ")  # - - - - - pizza

# clue = "_ "*len(secret_word)

print(secret_word)

def update_clue(guessed_letter): # p

    index = 0

    while index < len(secret_word):  #secret_word[index]

        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter 

        index += 1


while lives > 0:

    print(clue)
    print(f"You have {lives} remaining")
    # show the number char need to guess
    # input a char
    guess = input("guess a letter or the whole word: ")

    if guess in secret_word :
        #function
        # take guess, secret, clue
        update_clue(guess)
        pass
    else:
        print("Incorrect. You lose a life")
        lives -= 1

# check to see if that char is a letter in the word

## true: need to see the word with their guess
## f the word has been guessed, then exit out of the while loop



for index in secret_word:
    clue.append("?")


print(secrtet_word)


# while lives > 0:
#     pass 




# def game(setting, time):
#     return f'Guess the word {x} for {x} minutes.'

# numberOfMinutes = input('how long should this blend')
# desiredSetting = input('what setting should we use')

# print(blend(desiredSetting, numberOfMinutes))




