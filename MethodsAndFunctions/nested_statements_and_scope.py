x = 25


def printer():
    x = 50
    return x


print(x)
print(printer())

# Global
name = "THIS IS A GLOBAL STRING"


def greet():
    # Enclosing
    name = "Sammy"

    def hello():
        # Local
        name = "IM A LOCAL"
        print(f"Hello {name}")

    hello()


greet()


y = 50


def func_y():
    global y
    print(f"Y is {y}")
    # Local reassignment on a global variable!
    y = 200
    print(f"I JUST LOCALLY CHANGED X TO {y}")


func_y()
print(y)


z = 50


# Best approach and safe!
def func_z(z):
    print(f"Z is {z}")
    # Local reassignment on a global variable!
    z = "NEW VALUE"
    print(f"I JUST LOCALLY CHANGED X TO {z}")
    return z


z = func_z(z)
print(z)
