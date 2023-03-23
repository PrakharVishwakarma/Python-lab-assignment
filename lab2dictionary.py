# Create a new dictionary
dictionary = {'character': 'ram', 'durration': 50, 'city': 'Delhi'}

# Printing the dictionary:
print(dictionary)

# Get a list of all keys in the dictionary
print("Get a list of all keys : ",list(dictionary.keys()))

# Get a list of all values in the dictionary
print("Get a list of all values : ",list(dictionary.values()))

# Get a list of all key-value pairs in the dictionary
print("Get a list of all key-value pairs ",list(dictionary.items()))

# Check if a key is in the dictionary
print('durration' in dictionary)

# Add a new key-value pair to the dictionary
dictionary['occupation'] = 'Engineer'
print("Adding a new key-value pair ",(dictionary))

# Update the value of an existing key in the dictionary
dictionary['durration'] = 35
print("Updating the value ",dictionary)

# Remove a key-value pair from the dictionary
del dictionary['city']
print("Remove a key-value pair ",dictionary)

# Remove all key-value pairs from the dictionary
dictionary.clear()
print("Removing all key-value pairs ",dictionary)

# Get the length of the dictionary:
print("The length of the dictionary ",len(dictionary))

# Check the data type of the dictionary:
print("The data type of the dictionary ",type(dictionary))
