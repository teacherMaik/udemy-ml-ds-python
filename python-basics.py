import numpy as np

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums:
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")

# generate a range of 10 numbers with mean of 25 and std of 5
A = np.random.normal(25, 5, 10)

print(A)


# Lists
# length of lists
print(len(nums))

# Gets first 4 elements of list
print(nums[:4])

# Gets all elements after 4th
print(nums[4:])

# extracts second to last element from list
print(nums[-2])

# Extracts all elements up to second to last element from list
print(nums[:-2])

# Extracts last 2 elements fo list
print(nums[-2:])

# Extend to append one list to another (horizontally) and append to append one element
nums.extend([10, 11])
nums.append(12)
print(nums)

# Lists of lists
y = [13, 14, 15]
list_of_lists = [nums, y]

print(list_of_lists)

z = [3, 1, 5, 7, 2, 9, 3, 8]

# We can sort in ascending or descending
z.sort()
print(z)
z.sort(reverse=True)

# Reverses given order of elements in list
z.reverse()
print(z)

# Tuples (Values cannot be modified, inmutable)
x_tuple = (1, 2, 3)

print(len(x_tuple))

# Referencing and structing same as with lists. Destructuring example for both:

(user_age, user_income) = '42,84000'.split(',')

user_data = (int(user_age), int(user_income))
print(user_data)

# Dictionaries (Hash or lookup table in other languages)
captains = {}
captains['Enterprise'] = 'Kirk'
captains['Black Pearl'] = 'Sparrow'
captains['Education'] = 'Brugess'

print(captains)
print(captains.get('Black Pearl'))

for ship in captains:
    print(f"{ship}: {captains[ship]}")


# Functions
def square_int(x):
    return x*x

print(square_int(4))

# Pass functions as paramenters (Functional programming)
def do_something(f, x):
    return f(x)

print(do_something(square_int, 3))

# Lambdas (Simple inline functions)

# lambda indicates nameless function, taking in parameter x
# function has implicit return statement, which in this case is x*x*x
# 3 is the second parameter of our do_something function, so in this case 3^3
print(do_something(lambda x: x*x*x, 3))

# Bollean Expressions
if 1 is 3:
    print("Huh?")
elif 1 > 3:
    print("Yikes!")
else:
    print("Yes, 1 is not 3")

# Activity
n = list(range(1, 43))
print(n)

for val in n:
    if val % 2 == 0:
        print(val, "is even")
    elif val % 2 != 0:
        print(val, "is odd")