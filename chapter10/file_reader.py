import os
print(f"\nCurrent directory is: {os.getcwd()}\n")

with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents)
print("\n")

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.strip())

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()
    
    pi_string = ''
    for line in lines:
        pi_string +=line.rstrip()

    print(pi_string)
    print(len(pi_string))