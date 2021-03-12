name = input("What is your name: ")
#print("GoodMorning " + name)
print(f"GoodMorning, {name}")
n = int(input("Type any Number: " + name))
if n > 0:
    print("n is Positive")
elif n < 0:
    print("n is Negative")
else:
    print("n is zero")
name = "Harry"
#list
names = ["COllins","Otieno","Odhiambo"]
print(names)
print(names[2])
names.append("Jatelo")
names.sort()
print(f"There are {len(names)}")
print(names)
#set
s = set()
s.add(10)
s.add(569)
s.add(1000)
print(s)
print(f"There are {len(s)} elements")
#looping
for i in [0,1,2,3,4,5]:
    print(i)
# range
for i in range(6):
    print(i)
#dictionary
rooms = {"Collins":"Karungu", "Otieno":"Migori","James":"Aendo"}
print(rooms["Collins"])
#functions
def square(x):
    return x*x
for i in range (10):
    print(f"The square of {i} is {square(i)}")
#class
class point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
p = point(2, 5)
print(p.x)
print(p.y)
def __init__(self, capacity):
    self.capacity = capacity
    self.passengers = []
def add_passenger(self, name):
    if not self.open_seats():
        return False
    self.passengers.append(name)
    return True
def open_seats(self):
    return self.capacity - len(self.passengers)
flight = Flight(3)
people = ["Collins", "Velma", "Kyeen", "Naila", "Christian"]
for person in people:
    success = flight.add_passenger(person)
    if success:
        print(f"Added {person} to flight successfully.")
    else :
        print(f"No available seats for {person}")
# decorators
def announce(f):
    def wrapper():
        print("About to run a funcion")
        f()
        print("done with the function")
    return wrapper
@announce
def hello():
    print("Hello World")
#exceptions
import sys
try:
x = int(input("xs: "))
y = int(input("y: "))
except ValueError
print("Error: invalid input")
try :
    result = x / y
except ZeroDivisionError:
    print("Error: can not divide by Zero")
exit.sys(1)
