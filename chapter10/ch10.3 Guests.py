filename = 'users.txt'

while True:
    name = input ("Enter your name (type 'quit' to exit). ")
    if name == 'quit':
        break
    
    with open(filename, 'a') as file_object:
        file_object.write(name+"\n")