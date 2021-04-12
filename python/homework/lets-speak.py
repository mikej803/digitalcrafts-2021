


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

















