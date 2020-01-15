class Person(object):
    def __init__(self, first_name, last_name, father):
        self.first_name = first_name
        self.last_name = last_name
        self.father = father

person_a = Person('User', '1', None)
person_b = Person('User', '2', person_a)

# The nested dictionary that will be passed as parameter
a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4,
            'user': person_b,
        }
    }
}

# Convert Person Object into a Dictionary
def objectToDict(x):
    return dict((key + ': ', getattr(x, key)) for key in dir(x) if key not in dir(x.__class__))

def print_depth(dictionary, depth = 1):
    for key, value in dictionary.items():

        # Check if value is a dictionary
        if type(value) is dict:
            yield (key, depth)
            # Recursion for next data and increase depth
            yield from print_depth(value, depth + 1)

        # Check if value is a Person Object
        elif type(value) is Person:
            if type(objectToDict(value)) is dict:
                # Add a collon when key is 'user' as expected by given sample output
                if key == 'user':
                    yield (key + ': ', depth)

                # Normal scenario
                else:
                    yield (key, depth)

                # Recursion for next data and increase depth
                yield from print_depth(objectToDict(value), depth + 1)

        # Check if value is not a Person Object or a Dictionary
        else:
            yield (key, depth)


# Let's print all keys with their depth . . .
for key, depth in list(print_depth(a)):
    print(key, depth)


print('_______________________________')

