# 4. More Control Flow Tools
# Besides the while statement just introduced, Python uses the usual flow control statements known from other languages, with some twists.
# https://docs.python.org/3/tutorial/controlflow.html

# 4.1. if Statements

x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')