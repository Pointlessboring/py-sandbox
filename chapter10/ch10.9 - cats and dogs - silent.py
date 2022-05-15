
def get_from_file(filename):

    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        for line in contents:
            print(line.strip())

get_from_file('cats.txt')
get_from_file('dogs.txt')