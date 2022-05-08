favorite_fruits = ['strawberries', 'bananas', 'apples', 'raspberries', 'melons']

test_cases = ['citrus', 'melons', 'bananas', 'peaches']

for test in test_cases:
    if test in favorite_fruits:
        print(f"You really like {test}")
    else:
        print(f"Not a fan of {test}?")
