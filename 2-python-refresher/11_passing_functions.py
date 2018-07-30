def methodception(another):
    return another()

def add_two_numbers():
    return 35 + 77

# lambda is an anonymous function. It called ["declarative programming"]
# Extremly useful when we handle data
print(methodception(lambda: 35 + 77)) # return 112
print(methodception(add_two_numbers)) # return 112
print("\n")


# ----------------- Example 1 -----------------
# A lambda function is just a short, one-line function that has no name.
my_list = [13, 56, 77, 484]
print(list(filter(lambda x: x != 13, my_list))) # return [56, 77, 484]

# We could also do
def not_thirteen(x):
    return x != 13
print(list(filter(not_thirteen, my_list))) # return [56, 77, 484]
print("\n")


# ----------------- Example 2 -----------------
print((lambda x: x * 2)(5))  # return 10

def fname(x):
    return x*2
print(fname(5)) # return 10
print("\n")


# filter() passes each element of my_list as a parameter to the function.
# Pretty neat, eh?
