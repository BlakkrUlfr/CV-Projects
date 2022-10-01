# *args: Positional Variable-Length Arguments

def add(*args):
    # print(args[1])
    # print(args[0])
    sum_all = 0
    for n in args:
        sum_all += n
    return sum_all


print(add(3, 5, 6, 2, 1, 7, 4, 3))


def fun(*args):
    print(type(args))


# **kwargs: Keyword Variable-Length Arguments

def calculate(n, **kwargs):
    print(kwargs)
    print(type(kwargs))
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


# How to use a **kwargs dictionary safely
class Car:
    def __init__(self, **kwargs):
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
print(my_car.colour)