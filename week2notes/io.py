

# file_handler = open('preamble.txt', 'r') #read only

# contents = file_handler.read()

# file_handler.close() #always use this to close file

# print(contents)


# file_handler = open('newFile.txt', 'w') #Write to a file

# contents = file_handler.write("hello world")

# file_handler.close() #always use this to close file
# #Type code and the new file name to open

# file_handler = open('newFile.txt', 'a') #amend to a file

# contents = file_handler.write("\n\nhere is some new text on a new line")

# file_handler.close() #always use this to close file
#Type code and the new file name to open


# with open('KLeonard.txt', 'w') as file_handler:  #doesnt need to close
#     contents = file_handler.write("Kawhi Leornard is my favorite player in the current NBA.")


import pickle

students = {
    'Giselle': 'Las Vegas',
    'Layne': 'Atlanta',
    'Victoria': 'Humble'
}

# with open('data.pickle', 'wb') as fh:
#     pickle.dump(students, fh)


with open('data.pickle', 'rb') as fh:
    student = pickle.load(fh)
print(students)