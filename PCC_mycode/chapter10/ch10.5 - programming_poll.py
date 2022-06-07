filename = 'motivation.txt'

while True:
    why = input("Why you you like programming? (type 'quit' to exit) ")

    if why == 'quit':
        break

    with open(filename, 'a') as file_object:
        file_object.write(why+"\n")
    
