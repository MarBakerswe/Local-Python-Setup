# Takes in any number of arguments and prints them on at a time

def print_args(*args):
    for arg in args:
        print(f"arg = {arg}")

# Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. 
# The result of both nested functions should then be added together and printed

def do_math(num1, num2):
    def add():
        return num1 + num2
    def subtract():
        return num1 - num2
    print(add() + subtract())

# Takes in two strings: a student's name and their lunch preference. 
# The function should print both strings. If a lunch preference is not given, 
# "Mystery Meat" should be printed instead.

def lunch_order(name, food = "Mystery Meat"):
    print(f"{name} ordered {food} for lunch.")

# sum_n_product - Accepts two integers and returns both the sum and the product.

def sum_n_product(num1, num2):
    return num1 + num2, num1 * num2

# alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can 
# hold functions in Python just like they can in JS. Alternatively, you can call a 
# function from inside another function.

def arb_args(*args):
    for arg in args:
        print(f"arg = {arg}")

alias_arb_args = arb_args

# arb_mean - Accepts any number of integers and prints their average.

def arb_mean(*args):
    print(sum(args) / len(args))

# arb_longest_string - Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
    longest = ""
    for arg in args:
        if len(arg) > len(longest):
            longest = arg
    return longest