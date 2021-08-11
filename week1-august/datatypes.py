# first finding type of data
a=3
b="Hello"
print(type(a))
print(type(b))
# list
list=[1,3,5,4,6]
for i in list:
    print(i)
print(list)
# list comprehension
new_list=[i for i in list]
print(new_list)
print(new_list[0:3])
print(new_list[3:5])
print(new_list[2:])
# tuple
print("tuple")
tup=(1,3,5,7,2,4)
print(tup)
print(tup[-3])
print(tup[2:])
# dictonary
print("dictonary")
dict={}
print(dict)
# Creating a Dictionary
# with Integer Keys
dict={1:"hello",2:"CrossMl"}
print(dict)
# with mixed Keys
dict={1:"hello","company":"CrossMl"}
print(dict)