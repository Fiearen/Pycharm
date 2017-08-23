# 1. Numbers
numbers = []
for i in range(5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is ", numbers[0])
print("The last number is ", numbers[-1])
print("The smallest number is ", min(numbers))
print("The largest number is ", max(numbers))
print("The average of the numbers is ", sum(numbers) / len(numbers))


# 2. Woefully inadequate security checker
user_names = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
              'swei45''BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState',
              'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
user_name = input("What is your username: ")
if user_name in user_names:
    print("Access granted")
else:
    print("Access denied")
