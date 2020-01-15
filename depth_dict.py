# The nested dictionary that will be passed as parameter
a = {
    'key1': 1,
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 4
        }
    }
}


# The function to print all keys with their depth . . .
def print_depth(dictionary, depth = 1):
    for key, value in dictionary.items():

        # Check if value is a dictionary
        if type(value) is dict:
            yield (key, depth)
            # Recursion for next data and increase depth
            yield from print_depth(value, depth + 1)

        else:
            yield (key, depth)


# Let's print all keys with their depth . . .
for key, depth in list(print_depth(a)):
    print(key, depth)


print('_______________________________')
