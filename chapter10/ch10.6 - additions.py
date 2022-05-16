

print("\nGive me 2 numbers to add.")
print("Type 'quit' to exit.")

num1 = input("First number: ")
if num1 == 'quit':
    exit()

num2 = input("Secondß number: ")
if num2 == 'quit':
    exit()

try: 
    total = int(num1) + int(num2)
except ValueError:
    print(f"I cannot add {num1} and {num2}")
else:
    print(total)

