num = 100
count = 0
while num <= 150:
    if count > 20:
        break
    if num % 2 == 0:
        print(num)
        count += 1
    num += 1
print("exited from the loop")
