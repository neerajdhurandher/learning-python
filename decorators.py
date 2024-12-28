# what is decorator? give me definition with example.
# A decorator is a design pattern in Python that allows a user to add new functionality to an existing object without
# modifying its structure. Decorators are usually called before the definition of a function you want to decorate.
def ex1():
    # Define a decorator function
    def my_decorator(func):
        def wrapper():
            print("Something is happening before the function is called.")
            result = func()
            print("Something is happening after the function is called.")
            return result
        return wrapper

    # Use the decorator
    @my_decorator
    def say_hello():
        print("Hello!")
        return "ok"

    # Call the decorated function
    result = say_hello()
    print(result)

def ex2():
    # Define a decorator function
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            print("Something is happening before the function is called.")
            result = func(*args, **kwargs)
            print("Something is happening after the function is called.")
            return result
        return wrapper

    # Use the decorator
    @my_decorator
    def say_hello(name):
        print(f"Hello, {name}!")

    # Call the decorated function
    say_hello("Alice")


def ex3():
    # Define the first decorator
    def decorator_one(func):
        def wrapper(*args, **kwargs):
            print("Decorator One: Before the function call")
            result = func(*args, **kwargs)
            print("Decorator One: After the function call")
            return result
        return wrapper

    # Define the second decorator
    def decorator_two(func):
        def wrapper(*args, **kwargs):
            print("Decorator Two: Before the function call")
            result = func(*args, **kwargs)
            print("Decorator Two: After the function call")
            return result
        return wrapper

    # Use multiple decorators
    @decorator_one
    @decorator_two
    def say_hello(name):
        print(f"Hello, {name}!")

    # Call the decorated function
    say_hello("Alice")

ex3()