import numbers
import random

numbers = [0,1,2,3,4,5,6,7,8,9]

password_list = []
for num in range (0,4):
    password_list.append(random.choice(numbers))

password = ""
for num in password_list:
    password += str(num)

print(f"Your code OTP is {password}")

