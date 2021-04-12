


# A = "4", E = "3", "G" = "6", "I" = "1", "O" = "0", "S" = "5", "T" = "7"


# userinput = Whats up
# output = Wh475 up


userInput = input("Type your sentence? ")
output = ""


for char in userInput:
    if char == "a":
        output += "4"
    elif char == "e":
        output += "3"
    elif char == "g":
        output += "6"
    elif char == "i":
        output += "1"
    elif char == "o":
        output += "0"
    elif char == "s":
        output += "5"
    elif char == "t":
        output += "7"
    else:
        output += char

print(output)




# A => 4
# E => 3
# G => 6
# I => 1
# O => 0
# S => 5
# T => 7


# Michael = Michael.replace('A', '4')
# Michael = Michael.replace('E', '3')
# Michael = Michael.replace('G', '6')
# Michael = Michael.replace('I', '1')
# Michael = Michael.replace('O', '0')
# Michael = Michael.replace('S', '5')
# Michael = Michael.replace('T', '7')


# print(Michael)












# Translate a String to leetspeak
# Example : "I am a leet programmer"







# index = 0

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.upper in "AEGIOST":
#             translation = translation = "4"
#         else:
#             translation = translation + letter
#     return translation

# print(translate(input("Enter a phrase: ")))