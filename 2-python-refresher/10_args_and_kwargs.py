print("----------Problem----------")
def my_method(arg1, arg2):
    return arg1 + arg2

def my_really_long_addition(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5
print(my_really_long_addition(13, 45, 66, 3, 4))

def adding_simplified(arg_list):
    return sum(arg_list)
print(adding_simplified([13, 45, 66, 3, 4]))

print("\n----------Example args----------")
# But you need a list :(
def what_are_args(*args):
    print(args)
print(what_are_args(12, 35, 64, 'hello'))

def adding_more_simplified(*args):
    return sum(args)  # args = a tuple of arguments passed
print(adding_more_simplified(13, 45, 66, 3, 4))

print("\n----------Example kwargs----------")
# As well as a tuple of args, we can pass kwargs
# kwargs = dictionary - whose keys become separate keyword arguments and the values become values of these arguments.
def what_are_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)
    print("~~~~~~~~")

# non-positional arguments
def does_order_matter(location, name):
    print(location)
    print(name)
    print("-----------")

what_are_kwargs(name='Jose', location='UK') # No args
what_are_kwargs(12, 35, 66, name='Jose', location='UK')
does_order_matter(name='Jose', location='UK')
print("\n")

# =============Conclusion==============
# args(arguments) are a tuple
# kwargs(keyword arguments) is a dictionary
# This will come in handy!
