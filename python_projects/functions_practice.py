def hello():
    print('Hello')

def pack(arg1, argu2, arg3):
    return [arg1, argu2, arg3]


def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty!")
    else:
        print(f"First I eat {food_list[0]}")
        for i in range(1, len(food_list)):
            print(f"Next I eat {food_list[i]}")


hello()

packed_items = pack("sandwich", "apple", "chips")
print(packed_items)

eat_lunch(["sandwich", "apple", "chips"])