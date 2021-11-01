
mylist= ["banana","cherry", "apple"]
print(mylist)

mylist2 = list()
print(mylist2)

mylist3 = [5, True, "apple", "pp"]

item = mylist[-1]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("No")

print(len(mylist))

mylist.append("lemon")
print(mylist)

mylist.insert(1,"blueberry")
print(mylist)

item2 = mylist3.pop()
print(item2)
print(mylist)

item3 = mylist.remove("cherry")

item4=mylist2.clear()

reversList = mylist.reverse()

mylist.sort()

new_list_sorted = sorted(mylist) # if i don't want to sort my original list

new_list = [0, 1] * 5
print(new_list)

mylist5 = [1,2,3,4,5]
mylist6 = new_list + mylist5
print(mylist6)

a= mylist6[1:4]
print(a)

b= mylist6[::2] # with -1 -> reverse the list
print(b)

print("Original and copy")
mylist_org= ["banana","cherry", "apple"]
mylist_cpy = mylist_org # both refere to the same list inside memory
mylist_cpy.append("copy mod")
print(mylist_org)
print(mylist_cpy)
print("with .copy()" )
mylist_org= ["banana","cherry", "apple"]
mylist_cpy = mylist_org.copy() # do not refere to the same list inside memory
mylist_cpy.append("copy mod")
print(mylist_org)
print(mylist_cpy)
mylist_org= ["banana","cherry", "apple","cherry", "apple"]
print("---------------")
mylist_cpy = mylist_org[1:3] # do not refere to the same list inside memory
mylist_cpy.append("copy mod")
print(mylist_org)
print(mylist_cpy)

# to created a squared list:
print("squared list")
mylist = [1,2,3,4,5]
a=[i*i for i in mylist]
print(mylist)
print(a)