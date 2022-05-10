prompt = "How old are you? "

while True:
    userinput = input(prompt)
    
    
    if userinput == '':
        break

    age = int(userinput)
    
    if age < 3:
        price = 0
    elif age >=3 and age < 12:
        price = 10
    else:
        price = 15
    
    print(f"Your ticket price is: ${price}")
    