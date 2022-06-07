from pydoc import describe
from this import d
def describe_city(city, country="USA"):
    print(f"{city.title()} is in {country}")


describe_city('Reykjavik', 'Iceland')
describe_city('New York')