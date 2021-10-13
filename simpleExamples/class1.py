# this python code creates 8 lines of output when calling this python module. 
# understand and explain each of the 8 lines 

# Function defined outside the class
print("python example 1 classes ")

def f1(self, x, y):
    return min(x, x+y)

print(f1(0,1,2))


# python class
class C:
    """simple class"""
    def __init__(self):
       self.data = []
       print("init")
    i = 59
    f = f1
    def g(self):
        return 'hello world'
    h = g

#outputs
c = C()
print(c.i) 
print(c.f(4,8)) 
print(c.g())
print(c.h())
print(c.__doc__)    