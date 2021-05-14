# print of odd number from 500 to 1000


num = 500
while num <= 1000:
    if num % 2 == 1:
        print(num)
    num += 1




# print numbers 1 to 200 which are even numbers
num = 1
while num <= 200:
    if num % 2 == 0:
        print(num)
    num += 1



# print numbers 100 to 200 which are divisible by 3,5,7


num = 100
while num <= 200:
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        print(num)
    num += 1
