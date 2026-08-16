# Bugged na verison
class Car:
    action =[]

    def add_action(self, action):
        self.action.append(action)

car1 = Car()
car2 = Car()

car1.add_action("Drive to the store")
print()
print(car1.action) 
print(car2.action)  

#Correk version
class Car:
    def __init__(self):
        self.action = []

    def add_action(self, action):
        self.action.append(action)

car1 = Car()
car2 = Car()

car1.add_action("Turn on windshield wipers")
print()
print(car1.action)
print(car2.action)
print()