# Return a function a value

# Decorators
def smart_divide(func):
    def divide_check(a, b):
        # print(f"I am going to divide {a} and {b}...")
        if b == 0:
            print(f"Oops, {a} cannot be divide  by {b}.")
            return

        return func(a, b)

    return divide_check


@smart_divide
def divide(x, y):
    print(f"Your monthly bill per line is ${round(x / y, 2)}")


# Verizon: With iPhone
divide(140.92, 2)

# Verizon: With iPhone 15 Pro
divide(135.36, 2)

# Verizon: With iPhone 13 - Blue
divide(134.80, 2)
