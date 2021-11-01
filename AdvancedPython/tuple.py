# they can't be changed after creation
mytuple = ("Max", 28, "Boston") # also without parentesis
print(mytuple)

mytuple = ("Max") # it is NOT recognise as a tuple
print(type(mytuple))
mytuple = ("Max",) # it is recognise as a tuple
print(type(mytuple))

mytuple = tuple(["Max", 28, "Boston"]) # create tuple from a list
print(mytuple)

item = mytuple[0]
print(item)

for i in mytuple:
    print(i)

if "Max" in mytuple:
    print("yes")
else: 
    print("no")

mytuple=("a","p","p","l","e")
print(len(mytuple))

print(mytuple.count("p"))

print(mytuple.index("p"))# return the position of the first p

mylist = list(mytuple)
print(mylist)
mytuple2 = tuple(mylist)
print(mytuple2)

a= (1,2,3,4,5,6,7,8,9,10)
b = a[2:5]
print(b)
b = a[::2]
print(b)
b= a[::-1]
print(b)

mytuple = ("Max", 28, "Boston")
name, age, city = mytuple
print(name)
print(age)
print(city)

a= (1,2,3,4)
i1, *i2, i3 = a
print(i1) # first element
print(i3) # last element
print(i2) #elements between i1 and i3 in a list

# compare a tuple with a list -> working with tuples can be more eficent
## the list use more space than the tuple
import sys
mytuple = ("Max", 28, "Boston")
mylist = ["Max", 28, "Boston"]
print(sys.getsizeof(mytuple),"bytes")
print(sys.getsizeof(mylist),"bytes")
## it take much longer to create a list than a tuple
import timeit
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))
print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))

