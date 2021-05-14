# print of numbers 50 to 100 which are dividible by 8 or 5



num = 50
while num <= 100:
    if num % 8 == 0 or num % 5 == 0:
        print(num)
    num+= 1






#  .......print numbers 1 to 100 which are divisible  by 3 ..........
num = 1
while num <= 100:
 if num % 3 == 0:
     print(num)
num += 1



# for the first prime numbers  from 1 to 100


for Number in range (1,101):
    count = 0
    for i in range(2,(Number//2 + 1)):
        if (Number % i == 0):
            count = count + 1
            break
    if(count == 0 and Number != 1):
        print("%d"%Number,end='')
