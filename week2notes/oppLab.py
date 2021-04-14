





# # # # DIRs

# # # chris = {
# # #     "firstName": "Chris",
# # #     "lastName": "Owens",
# # #     "greeting": greeting
# # # }

# # # matt = {
# # #     "firstName": "Matt",
# # #     "lastName": "Fisher",
# # #     "greeting": greeting
# # # }

# # # print(chris["firstName"], chris["lastName"])

# # # chris["greeting"]("Veronica")


# # # class Dir:
# # #     def greeting(self):
# # #         print('hello world')

# # # chris = DIR()
# # # matt = DIR()








# # # def greeting(name):
# # #     print(f"hello {name}")


# # # mike = {}



# # # class Student:
# # #     def __init__(self, fName, lName):
# # #         self.firstname = fName
# # #         self.lastName = lName
# # #         print(f'Hello {fName}{lName}')

        
# # #     def greeting(self, name):
# # #         print(f'hello {name}')


# # # mike = Student("Jake ", "Green ")
# # # jake = Student("Mike ", "Williams ")
# # # greeting = ("Hello ")







# # class Student:
# #     def __init__(self, fName, lName):
# #         self.firstname = fName
# #         self.lastName = lName
# #         print(f'{self.firstname} Say whats up to {self.firstname}')

        
# #     def greeting(self, name):
# #         print(f'{self.firstname} says hello, by the way {name}')

# # # class Campus:
# # #     def __init__(self)


# # jake = Student("Mike ", "Williams ")
# # mike = Student("Jake ", "Green ")
# # # greeting = ("Hello ")


# # mike.greeting("Jake")
# # jake.greeting("Mike")
# # # mike.firstname("Jake")
# # # jake.firstname("Mike")





# # # carol = Student()
# # # john = Student()
# # # jake = Student()

# # # mike.greeting('john')
# # # victoria.greeting('jake')
# # # carol.greeting('mike')
# # # john.greeting('victoria')
# # # jake.greeting('carol')


# # # Students


# # # mike = {
# # #     "firstName": "Mike",
# # #     "lastName": "Williams",
# # #     "greeting": greeting
# # # }

# # # victoria = {
# # #     "firstName": "Jake",
# # #     "lastName": "Green",
# # #     "greeting": greeting
# # # }

# #  notes

# def incrementCount():
#     global count = 0
#     count += 1
#     return count

# result = incrementCount()

# print(result)

# result = incrementCount()

# r2 = increment()
# print(result)




# class Counter():
#     def __init__(self):
#         self.count = 0

#     def increment(self):
#         self.count += 1
#         return self.count

# a = 5


# count1 = Counter()

# print(count1.increment())
# print(count1.increment())
# print(count1.increment())
# print(count1.increment())
# print(count1.increment())

# print("instance variable for count 1: ", count1.count)


# count2 = Counter()
# print("count2: ", count2.increment())



# class Button():

#     def __init__(self, color, height, width):
#         self.count = 0
#         self.color = color
#         self.height = height
#         self.width = width

#     def click(self):
#         self.count += 1

# navButton = Button('green', '100px', '200px')
# helpButton = Button('yellow', '50px', '25px')

# navButton.click()
# navButton.click()
# navButton.click()
# navButton.click()

# print(f'nav: {navButton.count} help: {helpButton.count}')

# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()
# helpButton.click()

# print(f'nav: {navButton.count} help: {helpButton.count}')




class Button():

    FontWeight = 'bold'
    FontColor = 'red'


    def __init__(self, color, height, width):
        self.count = 0
        self.color = color
        self.height = height
        self.width = width
        

    def click(self):
        self.count: += 1

    @classmethod
    def popUp(cls):
        print('popups are so annoying')

navButton = Button('green', '100px', '200px')
helpButton = Button('yellow', '50px', '25px')

Button.FontWeight = "33"
print(Button.FontWeight)

















