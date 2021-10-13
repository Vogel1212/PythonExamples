#interactive console
for letra in 'Python':
    cod = ord(letra)
    print (cod, letra)
    
#interact over a list
print("List Interation")
l = ["geeks","for","geeks"]
for i in l:
    print(i)

#intercat over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks","for","geeks")
for i in t:
    print(i)

#interact over a string
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)

#interact over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" %(i, d[i]))