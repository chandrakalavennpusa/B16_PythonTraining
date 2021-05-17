 ######string####
msg = "HELLO WORLD"
for char in msg:
    print("char value : ", char)
word = "welcome"
for char in word:
    print("word : ", char)

 ####dictionery######
emp_data = {'emp_id':101,
            'emp_name':"chandra kala",
            'emp_sal':200000,
            'emp_status':'is_permanent'}
for key, val in emp_data.items():
   print(key,val)


######tuple####


stu_id = (20, 21, 22, 23, 24, 25)
for sid in stu_id:
    print("stu_id : ", sid)


emp_ids = (101, 102, 103, 104, 105)
for eid in emp_ids:
   print("emp_id : ", eid)