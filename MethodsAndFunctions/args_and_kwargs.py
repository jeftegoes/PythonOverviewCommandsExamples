# *args = Tuple
def my_func_with_args(*args):
    print(args)
    for item in args:
        print(item)

# **kwargs = Dictionary
def my_func_with_kwargs(**kwargs):
    print(kwargs)
    if ("fruit" in kwargs):
        print("My fruit of choice is {}.".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here.")

def my_func_with_args_kwargs(*args, **kwargs):
    print("I would like {} {}.".format(args[0], kwargs["food"]))

my_func_with_args(40, 60, 100, 100, 20)
my_func_with_kwargs(fruit="apple", veggie="lettuce")
my_func_with_args_kwargs(10, 20, 30, fruit="orange", food="eggs", animal="dog")
