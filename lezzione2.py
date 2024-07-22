class Student:
	studentGrades = []

	def __init__(self, studentName, grade):
		self.name = studentName
		self.studentGrades.append(grade)

	@classmethod
	def getGroupAverage(cls):
		avg = sum(cls.studentGrades) / len(cls.studentGrades)
		return avg

# Example usage
student1 = Student("Alice", 90)
student2 = Student("Bob", 80)
student3 = Student("Charlie", 85)

average_grade = Student.getGroupAverage()
print(f"The average grade of all students is: {average_grade}")

class Animal:
	def __init__(self, name, legs):
		self.name = name
		self.legs = legs

	def setLegs(self, legs):
		self.legs = legs

	def getLegs(self):
		return self.legs

	def printInfo(self):
		print(f"Name: {self.name}, Legs: {self.legs}")

# 1. Create two realistic instances of Animals
dog = Animal("Dog", 4)
bird = Animal("Bird", 2)

# 2. Print the name of each object
print(dog.name)
print(bird.name)

# 3. Change the amount of legs of one object using the dot notation
bird.setLegs(3)
print(f"{bird.name} now has {bird.legs} legs.")

# 4. Add a method setLegs() to set the legs of an object and repeat task 3 but this time using the method.
dog.setLegs(3)
print(f"{dog.name} now has {dog.getLegs()} legs using setLegs method.")

# 5. Add a method getLegs() to return the amount of legs
# Already implemented above.

# 6. Add a method named printInfo that prints all attributes of the Animal
dog.printInfo()
bird.printInfo()


class Food:
    def __init__(self, name:str, price:float, description:str):
        self.name = name
        self.price = price
        self.description = description

food = Food("Pizza", 10.99, "A delicious pizza with pepperoni and cheese.")
food1 = Food("Burger", 5.99, "A juicy burger with lettuce, tomato, and cheese.")
food2 = Food("Salad", 7.99, "A fresh salad with lettuce, tomatoes, and cucumbers.")

class Menu:
    def __init__(self):
        self.menu = []

    def addFood(self, food):
        self.menu.append(food)

    def removeFood(self, food):
        self.menu.remove(food)

    def printPrices(self):
        for food in self.menu:
            print(f"{food.name} - ${food.price}")

    def getAveragePrice(self):
        prices = [food.price for food in self.menu]
        avg = sum(prices) / len(prices)
        return avg

menu = Menu()
menu.addFood(food)
menu.addFood(food1)
menu.addFood(food2)

food3 = Food("Fries", 2.99, "Crispy fries with ketchup.")
food4 = Food("Soda", 1.99, "A refreshing soda with ice.")
menu.addFood(food3)
menu.addFood(food4)

menu.printPrices()
average_price = menu.getAveragePrice()
print(f"The average price of all foods is: ${average_price}")
