

def greeting(name):
    print(f"hello {name}")


# DIRs

chris = {
    "firstName": "Chris",
    "lastName": "Owens",
    "greeting": greeting
}

matt = {
    "firstName": "Matt",
    "lastName": "Fisher",
    "greeting": greeting
}

print(chris["firstName"], chris["lastName"])

chris["greeting"]("Veronica")


class Dir:
    def greeting(self):
        print('hello world')

chris = DIR()
matt = DIR()