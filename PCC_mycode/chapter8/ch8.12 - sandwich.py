def make_sandwich(*items):
    """ Print list of items to be included in the sandwich"""

    print(f"\nPreparing a sandwich with the following ingredients")
    for item in items: 
        print(f"- {item}")

make_sandwich('salami', 'butter', 'garlic')
make_sandwich('brie', 'salad')
make_sandwich('chicken', 'avocado', 'mango')
