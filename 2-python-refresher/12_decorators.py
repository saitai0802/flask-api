# A decorator is just a function that gets called before another function

import functools  # function tools

# ----------------- Example 1: Easiest function -----------------
def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_f():
        print("Hello!")
        func() # <=========== Actually this my_function()
        print("After!")
    return function_that_runs_f

@my_decorator
def my_function():
    print("I'm in the function.")

my_function()
print("\n")


# ----------------- Example 2: send arguments to the actual function that we run -----------------
def my_decorator(f):
    @functools.wraps(f)
    def function_that_runs_f(*args, **kwargs): # If my_function got parameters, that part will be so useful.
        print("Hello!")
        f(*args, **kwargs) # <=========== Actually this my_function()
        print("After!")
    return function_that_runs_f

@my_decorator
def my_function(arg1, arg2):
    print(arg1 + arg2)

my_function(56, 89)
print("\n")

# ----------------- Example 3: send arguments to decorator -----------------
def decorator_arguments(number):
    def my_decorator(f):
        @functools.wraps(f)
        def function_that_runs_f(*args, **kwargs): # If my_function got parameters, that part will be so useful.
            print("Hello!")
            if number == 56:
                print("Not running!")
            else:
                f(*args, **kwargs) # <=========== Actually this my_function()
            print("After")
        return function_that_runs_f
    return my_decorator

@decorator_arguments(56)
def my_function():
    print("Hello!")

my_function()
