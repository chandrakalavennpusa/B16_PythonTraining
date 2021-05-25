stu_ids = [101, 102, 103, 105, 106]
stu_ids.append(101)
print("stuids after append:", stu_ids)
stu_ids.append((120,122))
print("After append:", stu_ids)
stu_ids.append([130,132,133])
print("After append:", stu_ids)
stu_ids.append("hello")
print("After append:", stu_ids)
stu_ids.append({150, 155},)
print("After append:", stu_ids)
stu_ids.append(True)
print(("After append:", stu_ids))
for ind, val in enumerate(stu_ids):
    print("ind, " ", val")
print("After append:", stu_ids)
emp_ids = [10, 20, 30, 40, 50, 60]
print("Before extend:", emp_ids)
emp_ids.extend([80, 90, 100])
print("After expand:", emp_ids)
emp_ids.extend("python")
print("After expand:", emp_ids)
emp_ids.extend((110,120,130,140))
print("After expand:", emp_ids)
####### append vs extend................


emp_ids = [1, 2, 3, 4, 5, 6]
emp_ids.append([7, 8, 9])
print("After append:", emp_ids)
emp_ids.extend([10, 11, 12, 13, 14])
print("After expand:", emp_ids)


########pop function list


cust_ids = [120, 121, 145, 150, 170, 180, 201, 304,]
print("Before pop elements:", cust_ids)
cust_ids.pop(0)
print("After pop:", cust_ids)   #pop allows only index for removal of elements from list
cust_ids.pop()
print("After pop:", cust_ids)
cust_ids.pop(5)
print("After pop:", cust_ids)


#  Remove function#########

bank_ids = [150, 151, 152, 153, 155, 170, 175,177, 178, 201, 202 ]
print("Before removal:", bank_ids)
bank_ids.remove(155)
print("Before removal:", bank_ids)
bank_ids.remove(202)
print("Before removal:", bank_ids)


#### pop vs remove #########

bank_ids = [21, 22, 23, 35,36, 37, 45, 47, 49, 55, 67, 89, 97 ]
print("Before pop elements:", cust_ids)
bank_ids.pop(7)
print("After pop:", bank_ids)
bank_ids.remove(97)
print("After removal:", bank_ids)



######insert fun ction######


cust_ids = [ 26, 17, 29, 75, 89, 65, 57, 45, 38, 76, 54]
cust_ids[0] = 34
print ("inserting value:", cust_ids) #in the place of 26 ,34 has inserted.
cust_ids.insert(2,198)
cust_ids.insert(7, 46)
print("inserted value:", cust_ids)
cust_ids[-1] = 23
print("inserted value:", cust_ids)
cust_ids.insert(6, 66)
print("inserted value:", cust_ids)


######count function########


worker_ids = [ 1, 5, 7, 4, 4, 7, 2, 9, 9, 11, 33, 45, 24, 45, 1, 1]
print("Before count:", worker_ids)
worker_ids.count(1)
print(("After count:", worker_ids.count(1)))


#######index function#################

employee_ids = [11, 34, 56, 78, 89, 45, 67, 23, 65, 70, 80]
employee_ids.index(45)
print("After indexing:", employee_ids.index(45))
print("After indexing:",employee_ids.index(11))
print("After indexing:", employee_ids.index(80))


####### sort function#############

cust_ids = [1, 5, 6, 7, 9, 10, 45, 56, 67, 89, 24, 47]
cust_ids.sort()
print("After sorting:", cust_ids)


stu_ids = [20, 25, 11, 45, 67, 101, 345, 103, 145]
stu_ids.sort()
print("After sorting:", stu_ids)


########reverse function############


emp_ids = [14, 11, 2, 4, 10, 56, 76, 32, 35, 65, 21, 24, 60]
emp_ids.reverse()
print("After reversing:", emp_ids)

stu_ids = [10, 45, 57, 32, 47, 2, 1, 3, 5, 7, 80, 70 ]
stu_ids.reverse()
print("After reversing:", stu_ids)


######sort function###################


cust_ids = [40, 45, 34, 23, 11, 22, 40, 45, 56, 27, 65, 56, 90]
cust_ids.sort()
print("After sorting:", cust_ids)


cust_ids.sort(reverse=True)
print("After sorting:", cust_ids)


############   copy function #############

stu_ids = [1, 3, 5, 7, 3,6, 1, 4, 7,]
print("Before copying:", stu_ids)
stu_ids2 = stu_ids.copy()
print("After copying to stu_ids2:", stu_ids2)
print("Normal copy function:", id(stu_ids), id(stu_ids2))
stu_ids.append(100)
print("After append:", stu_ids)
print("After append:", stu_ids2)
stu_ids2.append(24)
print("After append stu_ids2:", stu_ids2)
print("After append:",stu_ids)



######Another way of copying#####

cust_ids = [34, 23, 56, 45, 87, 89, 34, 57, 11, 1, 2, 5, 8]
cust_ids2 = cust_ids
print("After copying:", cust_ids2)
cust_ids.append(13)
print("After appending a var:", cust_ids, cust_ids2)
cust_ids.extend([1, 3])
print("After extend:", cust_ids, cust_ids2)
cust_ids.extend([300])
print(("After extend:", cust_ids, cust_ids2))










