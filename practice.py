# c=[1,3,5,6]
# newnum=[a**2 for a in c ]
# print(newnum)


# Create a list of strings
lannister = ['cersei', 'jaime', 'tywin', 'tyrion', 'joffrey']

# Define generator function get_lengths
def get_lengths(input_list):
    """Generator function that yields the
    length of the strings in input_list."""

    # Yield the length of a string
    for person in input_list:
        yield len(person)

for value in get_lengths(lannister):
    print(value)
