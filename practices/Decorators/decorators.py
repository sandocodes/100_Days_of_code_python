# Return a function a value

# Decorators
def smart_divide(func):
    def divide_check(a, b):
        print(f"I am going to divide {a} and {b}...")
        if b == 0:
            print(f"Oops, {a} cannot be divide  by {b}.")
            return

        return func(a, b)

    return divide_check


@smart_divide
def divide(x, y):
    print(x / y)


divide(2, 5)
divide(2, 0)