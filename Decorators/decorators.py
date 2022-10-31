def new_decorator(original_func):
    def wrap_func():
        print("Some extra code, before the original function.")

        original_func()

        print("Some extra code, after the original function!")

    return wrap_func


def func_needs_decorator():
    print("I want to be decorated!!")


decorated_func = new_decorator(func_needs_decorator)
decorated_func()


@new_decorator
def func_needs_decorator_2():
    print("I want to be decorated!!")

func_needs_decorator_2()
