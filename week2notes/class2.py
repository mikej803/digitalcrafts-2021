




# # # class GoogleMapsAPI:

# # #     def __init__(self, address1, address2):

# # #         self.address1 = address1
# # #         self.address2 = address2

# # #     def map(self):
# # #         pass

# # #     def _determineLat(self):
# # #         pass
# # #     def _determineLong(self):
# # #         pass
# # # map = GoogleMapsAPI("123 sesame st.", "678 sesame st.")
# # # map._determineLat()

# # # class CrazyString(str):
# # #     def __init__(self, word):
# # #         self.word = word


# # # kanye = CrazyString('west')

# # # print(kanye.capitalize())


# # class CrazyString(str):
# #     def __init__(self, word):
# #         self.word = word

# #     def reverse(self):
# #         revString = ''

# #         for char in self.word:
# #             revString = char + revString

# #         return revString

# # kanye = CrazyString('west')

# # print(kanye.capitalize())

# # print(kanye.reverse())

# # Implicit Inheritance

# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color


#     def carDetails(self):
#         print(f"{self.make} {self.model} {self.color}")


# class Hybrid(Car):

#     def carType(self):
#         print("I'm a hybrid car")



    




# class Electric(Car):

#     def carType(self):
#         print("I'm an electric car")



# car = Car("ford", "mustang", "green")
# car.carDetails()
# hybrid = Hybrid("toyota", "prius", "marble")
# hybrid.carDetails()






# #override explicity
# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color


#     def carDetails(self):
#         print(f"{self.make} {self.model} {self.color}")


# class Hybrid(Car):

#     def carType(self):
#         print("I'm a hybrid car")

#     def carDetails(self):
#         print("I'm in the hybrid class")

    




# class Electric(Car):

#     def carType(self):
#         print("I'm an electric car")



# car = Car("ford", "mustang", "green")
# car.carDetails()
# hybrid = Hybrid("toyota", "prius", "marble")
# hybrid.carDetails()



# #using super()
# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color


#     def carDetails(self):
#         print(f"{self.make} {self.model} {self.color}")


# class Hybrid(Car):

#     def carType(self):
#         print("I'm a hybrid car")

#     def carDetails(self):
#         print("I'm in the hybrid class")
#         super(Hybrid, self). carDetails()
#         print("after the hybrid car")

    




# class Electric(Car):

#     def carType(self):
#         print("I'm an electric car")



# car = Car("ford", "mustang", "green")
# car.carDetails()
# hybrid = Hybrid("toyota", "prius", "marble")
# hybrid.carDetails()





# class Car:
#     def __init__(self, make, model, color):
#         self.make = make
#         self.model = model
#         self.color = color


#     def carDetails(self):
#         print(f"{self.make} {self.model} {self.color}")


# class Hybrid(Car):

#     def __init__(self, typeOfCar, make, model, color):
#         self.typeOfCar = typeOfCar
#         super(Hybrid, self).__init__(make, model, color)
    

#     def carType(self):
#         print("I'm a hybrid car")

#     def carDetails(self):
#         print("I'm in the hybrid class")
#         super(Hybrid, self). carDetails()
#         print("after the hybrid car")

    




# class Electric(Car):

#     def carType(self):
#         print("I'm an electric car")



# car = Car("ford", "mustang", "green")
# car.carDetails()
# hybrid = Hybrid("Hybrid", "toyota", "prius", "marble")
# hybrid.carDetails()




#composition

class Student:
    def __init__(self, firstName, campus):
        self.firstName = firstName
        self.campus = campus

    def addStudent(self, firstName, campus):
        student = Student(firstName, campus)
        self.student.append(student)

    def print(self):
        print(f"{self.firstName} is located in {self.campus}")

class Campus:
    def __init__(self)
        self.students = []

    def addStudent(self, firstName, campus):
        student = Student(firstName, campus)
        self.students.append(student)

    def showCurrentStudents(self):
        for studentsObJ in self.student:
            print(f"{studentObJ.firstName} {studentObJ.campus}")

campus = Campus()

campus.addStudent('Giselle', 'Las Vegas')
campus.addStudent('Carol', 'Atlanta')
campus.addStudent('Jacob', 'Tampa')
campus.addStudent('Victoria', 'Houston')
campus.addStudent('Brandon', 'Dallas')
campus.addStudent('Dot', 'Auburn')

campus.showCurrentStudents()


student1 = Student('Carol', "Atlanta")
student1 = Student('Giselle', "Las Vegas")
student1 = Student('Jacob', "Tampa")
student1 = Student('Victoria', "Houston")
student1 = Student('Brandon', "Dallas")
student1 = Student('Dot', "Auburn")


class AccountHolder:
    def __init__(self, fName, acountType, stats, balance):
        pass

    def deposit(self):
        pass


class Bank:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.accounts = []

    def open_new_account(self, fName, accountType, stats, balance):
        #create new Account Holder
        #store new account inside of self.accounts
        pass

    def show_account_holder(self):
        # show detailed account information for specific account holder
        pass

    def show_account(self):
        #print all account holders
        pass

    def show_bank_balance(self):
        #show bank balance of entire bank
        pass



















