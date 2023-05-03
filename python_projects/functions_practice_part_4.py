# Define the max_num() function
def max_num(a, b, c):
    return max(a, b, c) # or return max([a, b, c])

print(max_num(1, 5, 3))   # 5

# Define the mult_list() function
lst = [1, 2, 3, 4] # global variable

def mult_list(lst):
    result = 1
    for num in lst:
        result *= num # or result = result * num
    return result

print(mult_list(lst)) 

# Define the rev_string() function
s = "hello world"

def rev_string(s):
    return s[::-1]

print(rev_string(s))   # "dlrow olleh"

print(num_within(3, 2, 4))   # True
print(num_within(3, 1, 3))   # True
print(num_within(10, 2, 5))  # False

# Define the num_within() function
def num_within(num, start, end):
    return start <= num <= end


# Define the pascal() function
def pascal(n): # n is the number of rows
    triangle = [] # initialize the triangle
    for i in range(n):
        row = [1] 
        for j in range(1, i+1): 
            row.append(row[j-1]*(i+1-j)//j) # calculate the next value
        triangle.append(row) # append the row to the triangle
    for row in triangle:
        print(row)

pascal(5) # print the first 5 rows of Pascal's triangle