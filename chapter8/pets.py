def describe_pet(pet_name, animal_type='dog'):
    """displays information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
describe_pet(pet_name='willy', animal_type='dog')
describe_pet(pet_name='fido')