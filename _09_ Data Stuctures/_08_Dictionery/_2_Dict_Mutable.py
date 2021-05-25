
# Dictionary is mutable

# CREATE
dict1 = {1: 'One', 2:'Two', 3:'Three'}

# RETRIEVE
print("Dictionary : ",dict1)
print("Dict item  :",dict1[2])

# UPDATE
dict1[2] = 'Twenty'
print("Dictionary update: ",dict1)

# DELETE
del dict1[3]
print("Dictionary delete: ",dict1)

dict1.clear()
print("Dictionary delete: ",dict1)

x = 10
print("X : ",x)
del x
print("X : ",x)

del dict1
print("Dictionary delete: ",dict1)


