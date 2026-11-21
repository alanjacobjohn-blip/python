class Time:
    def __init__(self, hours, minutes):
        self.__hours = hours
        self.__minutes = minutes

    # Overloading + operator
    def __add__(self, other):
        total_minutes = self.__minutes + other.__minutes
        total_hours = self.__hours + other.__hours

        total_hours += total_minutes // 60
        total_minutes = total_minutes % 60

        return Time(total_hours, total_minutes)

    # Display time
    def display(self):
        print(self.__hours, "hours", self.__minutes, "minutes")


# Getting input from user
h1 = int(input("Enter hours of first time: "))
m1 = int(input("Enter minutes of first time: "))

h2 = int(input("Enter hours of second time: "))
m2 = int(input("Enter minutes of second time: "))

# Creating objects
t1 = Time(h1, m1)
t2 = Time(h2, m2)

# Adding two times
t3 = t1 + t2

# Display result
print("First time:")
t1.display()

print("Second time:")
t2.display()

print("Sum of two times:")
t3.display()
