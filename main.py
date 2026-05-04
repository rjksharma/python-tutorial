# lis = [1,2,3,4,5,6,7]
# tup = ("1", "23", "24")
# lis.extend(tup)
# lis.pop(0)
# print(lis)
# print(type(lis))

# for i in lis:
#     print(i)

# lis = ["apple", "ball", "cat"]
# i = 0
# while i < len(lis):
#     print(lis[i])
#     i = i + 1

# fruit = ["apple", "ball", "cat", "dog"]
# newlist = []

# for x in fruit:
#     if "a" in x:
#         newlist.append(x)
# print(newlist)

# newlist1 = [x for x in fruit if "a" in x]
# print(newlist1)

# fruit = ["apple", "dxll", "qat", "dog"]
# fruit.sort(reverse=True)
# print(fruit)

# l = [1,2,3,4,5,6,7,8,9]
# copy_of_l = l.copy()
# print(type(l))
# print(copy_of_l)
# tup = tuple(l)
# # print(type(tup))

# name = str(input("Enter first word"))
# print(name)
# print(type(name))


# thislist = ["apple", "banana", "cherry"]
# mylist = thislist[:]
# print(mylist)

list1 = [1,2,3,4]
list2 = [2,3,4,2]
# for x in list2:
#     list1.append(x)
# print(list1)
# list1.sort()

# list1.extend(list2)
# print(list1)

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

# l = ["1",2,"4",5,2,5]
# for i in range(0,len(l),1):
#     print(l[i])

# l = [1,2,3,4,5,6,7,8,9]
# for i in range(len(l)-1, -1, -1):
#     print(l[i])

# l = [1,2,3,4,5,6,7,8,9]
# print(l[1:4])

# t = ("hen", "bat", "tcs")
# print(len(t))
# thistuple = ("apple",)
# print(type(thistuple))

# tup1 = (1,2,3,4,5)
# tup2 = (True, False, False)
# print(type(tup2))

# tup1 = (1,2,3,4)
# add = (5,)
# tup1 += add
# tup1 = list(tup1)
# tup1.remove(1)
# print(tup1)

# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)

# Method	Description
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found

# fruits = ("apple", "banana", "cherry")

# (green, yellow, red) = fruits

# print(green)
# print(yellow)
# print(red)

# x = frozenset({"apple", "banana", "cherry"})
# print(x)
# print(type(x))


# Set Methods
# Python has a set of built-in methods that you can use on sets.

# Method	Shortcut	Description
# add()	 	Adds an element to the set
# clear()	 	Removes all the elements from the set
# copy()	 	Returns a copy of the set
# difference()	-	Returns a set containing the difference between two or more sets
# difference_update()	-=	Removes the items in this set that are also included in another, specified set
# discard()	 	Remove the specified item
# intersection()	&	Returns a set, that is the intersection of two other sets
# intersection_update()	&=	Removes the items in this set that are not present in other, specified set(s)
# isdisjoint()	 	Returns whether two sets have a intersection or not
# issubset()	<=	Returns True if all items of this set is present in another set
#  	<	Returns True if all items of this set is present in another, larger set
# issuperset()	>=	Returns True if all items of another set is present in this set
#  	>	Returns True if all items of another, smaller set is present in this set
# pop()	 	Removes an element from the set
# remove()	 	Removes the specified element
# symmetric_difference()	^	Returns a set with the symmetric differences of two sets
# symmetric_difference_update()	^=	Inserts the symmetric differences from this set and another
# union()	|	Return a set containing the union of sets
# update()	|=	Update the set with the union of this set and others


# Dictionary Methods
# Python has a set of built-in methods that you can use on dictionaries.

# Method	Description
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary


# # Create variable day
# day = 3
# # Use match statement
# match day:
#  case 3:
#   print("Wednesday")
#  case _:
#   print("Other day")

# i = 0
# while i < 6:
#   i += 1
#   if i == 3:
#     continue
#   print(i)
    
# i = 0
# While loop: print 1-5, skip 3 with continue
# while i < 6:
#     i += 1  
#     if i == 3:
#         continue
#     print(i)

# def full(fname, lname):
#     return fname + lname

# result = full(fname = 1, lname= 2)
# print(result)

# class Person:
#     def __init__(self, name, age=12):
#         self.name = name
#         self.age = age
# p1 = Person("rajkumar")
# p2 = Person("Sharma", 34)
# print(p1.name, p1.age)
# print(p2.name, p2.age)


# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def bark(self):
#         return f"{self.name} say Woof!"
# d1 = Dog("Buddy", 3)
# print(d1.bark())

# Create the Rectangle class
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# r1 = Rectangle(5,3)
# print(r1.area())


# Create the Animal class
# class Animal:
#     def __init__(self, name):
#         self.name = name
#     def speak(self):
#         print(self.name)
# class Dog(Animal):
#     pass
# d1 = Dog("Rex")
# d1.speak()

# Create the Cat class
# class Cat:
#     def sound(self):
#         print("Meow")
# class Fox:
#     def sound(self):
#         print("Wa-pa-pa-pa-pa-pow!")
# # Create objects and loop
# c1 = Cat()
# f1 = Fox()
# c1.sound()
# f1.sound()


# num = int(input("Enter the calculate"))
# i = 0
# l = []
# while i < num:
#     user_input = input("Ente number")
#     l.append(user_input)
#     i += 1
# print(l)
# l.sort()
# print(l)

# n = int(input())
# arr = list(map(int, input().split()))
# for num in arr:
#     print(num, end ="")
# input_str = input()
# print(type(input_str))
# number = input_str.split(" ")
# print(type(number))
# print(number)

# user_input = str(input("Enter the string Here"))
# star = user_input.count("*")
# hash = user_input.count("#")
# if star > hash:
#     print("Negative Interger")
    
# elif star < hash:
#     print("Positver Interger")
# else:
#     print("0")

# user_input = str(input("Enter the string Here"))
# star = 0
# hash = 0
# for x in user_input:
#     if x == "*":
#         star += 1
#     elif x == "#":
#         hash += 1
# print(star)
# print(hash)
        
    
# arr = [8,4,9,2,1]
# first = arr[0]
# count = 1
# for x in arr:
#     if first < x:
#         count += 1
# print(count)
# b = list(input("Enter the your color"))
# print(b)
# # b = ["r","b","b","b","g","y","g","y","r"]
# un = []
# for i in b:
#     if i not in un:
#         un.append(i)
# for x in un:
#     if b.count(x) % 2 == 0:
#         # print(f"{x} colour ballon is present odd number of times in the bunch.")
#         pass
#     else:
#         print(f"{x} colour ballon is present even number of times in the bunch.")

# num = int(input("Enter no: "))
# risk = []
# i = 0
# allowed = [0,1,2]
# while i < num:
#     user_input = int(input("Enter risk number (1, 3, 5 only): "))
#     if user_input in allowed:
#         risk.append(user_input)
#         i += 1
#     else:
#         print("Invalid! Choose only 1, 3, or 5.")

# risk.sort()

# print(risk)



