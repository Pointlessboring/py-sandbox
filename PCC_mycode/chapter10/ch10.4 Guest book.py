filename = 'guest_book.txt'

while True:
    name = input ("Enter your name (type 'quit' to exit). ")
    if name == 'quit':
        break
    
    print(f"Welcome, {name}!")
    with open(filename, 'a') as file_object:
        file_object.write(name+"\n")