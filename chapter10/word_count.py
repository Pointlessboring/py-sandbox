def count_words(filename):
    """Count the approximate number of words in a file."""

    path = "../../pcc_2e/chapter_10/"
    try:
        with open(path+filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
    else:
        words = contents.split()
        print(f"The file {filename} has about {len(words)} words.")

filenames = ['alice.txt', 'missing.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for filename in filenames: 
    count_words(filename)

