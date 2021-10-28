# challenge SCCBrasil
# a program that by typing integers, will show all even numbers that are between 1 and between the typed number.

num=1
max = int(input("Enter an integer greater than 1: ") )

print("Even numbers between 1 and", max, ":")

while num <= max:
    if num%2==0:
        print(num,  end=" ")
    num+=1