# *args collects positional arguments into a tuple
def add_numbers(*args):
    print(f"This is args: {args}")
    total = 0
    for n in args:
        total += n
    return total


# **kwargs collects keyword arguments into a dictionary
def print_user(**kwargs):
    print(f"This is kwargs: {kwargs}")
    for key, value in kwargs.items():
        print(key, value)


if __name__ == "__main__":
    print(add_numbers(1, 2, 3, 4, 5))
    print_user(name="Alice", age=30, city="Warsaw")
