
def get_from_file(filename):

    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f"The file {filename} appears to be missing.")
    else:
        for line in contents:
            print(line.strip())

get_from_file('cats.txt')
get_from_file('dogs.txt')