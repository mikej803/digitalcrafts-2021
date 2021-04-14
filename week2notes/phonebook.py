
import pickle


# electronic_phonebook = {
#     'Igor': '857-485-2935',
#     'Jazz': '334-584-2345',
#     'John': '803-793-0866',
#     'Mark': '757-685-3300',
#     'Jason': '609-502-1229'
# }



with open('phonebook.pickle', 'rb') as fh:
    electronic_phonebook = pickle.load(fh)
# with open('phonebook.pickle', 'wb') as fh:
#     pickle.dump(electronic_phonebook, fh)
users_input = input('''
Electonic Phone Book
===========================
1. Look up an entry
2. Set an entry
3. Delete an entry
4. List all entries
5. Quit
What do you want to do (1-5)?''' )



#lookingup
def lookup(name):
    print(f"\nlook up entry for {name}: {electronic_phonebook[name]}")
# set a entry
def set_entry():
    entry_name = input('\nName? ')
    entry_number = input('Number? ')
    electronic_phonebook[entry_name] = entry_number
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(electronic_phonebook, fh)
    print(f'Entry stored for: {entry_name}')  #{electronic_phonebook[entry_name]}
    
# deleting
def delete(name):
    del electronic_phonebook[name]
    with open('phonebook.pickle', 'wb') as fh:
        pickle.dump(electronic_phonebook, fh)
    print(f"You have deleted the entry for {name}")
# list
def list():
    print('Listed entries in phonebook: ')
    for x in electronic_phonebook:
        with open('phonebook.pickle', 'rb') as fh:
            electric_phonebook = pickle.load(fh)
        print(f'{x}: {electronic_phonebook[x]}')



while users_input != '5':
    users_input = input('Whats next? ')

    if users_input == '1':
        name = input('What name are you looking for? ')
        lookup(name)
    elif users_input == '2':
        set_entry()
    elif users_input == '3':
        name = input('Who would you like to delete? ')
        delete(name)
    elif users_input == '4':
        list()
    elif users_input == '5':
        print('Bye')
        break
























