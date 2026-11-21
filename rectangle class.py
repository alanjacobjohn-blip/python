class Rectangle:
    def __init__(self, length, breadth):
        self.__length = length
        self.__breadth = breadth

    # Method to calculate area
    def area(self):
        return self.__length * self.__breadth

    # Overloading < operator
    def __lt__(self, other):
        return self.area() < other.area()


# Getting input from user
l1 = float(input("Enter length of first rectangle: "))
b1 = float(input("Enter breadth of first rectangle: "))

l2 = float(input("Enter length of second rectangle: "))
b2 = float(input("Enter breadth of second rectangle: "))

# Creating objects
r1 = Rectangle(l1, b1)
r2 = Rectangle(l2, b2)

# Display areas
print("Area of first rectangle:", r1.area())
print("Area of second rectangle:", r2.area())

# Comparing areas
if r1 < r2:
    print("First rectangle has smaller area")
else:
    print("First rectangle does not have smaller area")
