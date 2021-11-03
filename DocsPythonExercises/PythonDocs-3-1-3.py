# 3.1.3. Lists
# https://docs.python.org/3/tutorial/introduction.html#using-python-as-a-calculator

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
squares = [1, 4, 9, 16, 25]
print(squares  + [36, 49, 64, 81, 100])

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print(cubes)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters)
letters[2:5] = ['C', 'D', 'E']
print(letters)
letters[2:5] = []
print(letters)