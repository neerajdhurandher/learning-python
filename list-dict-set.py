### List
# - **Ordered**: Elements have a defined order.
# - **Mutable**: Elements can be changed.
# - **Allows Duplicates**: Can contain duplicate elements.

# Example of a list
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]

# Accessing elements
print(my_list[0])  # Output: 1

# Modifying elements
my_list[0] = 10
print(my_list)  # Output: [10, 2, 3, 4, 5]

### Dictionary
# - **Unordered**: Elements do not have a defined order (insertion order is preserved in Python 3.7+).
# - **Mutable**: Elements can be changed.
# - **Key-Value Pairs**: Stores data in key-value pairs.
# - **Unique Keys**: Keys must be unique.

# Example of a dictionary
my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# Accessing elements
print(my_dict['name'])  # Output: Alice

# Modifying elements
my_dict['age'] = 26
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

### Set
# - **Unordered**: Elements do not have a defined order.
# - **Mutable**: Elements can be changed.
# - **No Duplicates**: Cannot contain duplicate elements.

# Example of a set
my_set = {1, 2, 3, 4, 5}
my_set_2 = set([1, 2, 7, 8, 9])  # Another way to create a set
print(my_set)  # Output: {1, 2, 3, 4, 5}

print(my_set | my_set_2)  # Output: {1, 2, 3, 4, 5, 7, 8, 9}
print(my_set.union(my_set_2))  # Output: {1, 2, 3, 4, 5, 7, 8, 9}

print(my_set & my_set_2)  # Output: {1, 2}
print(my_set.intersection(my_set_2))  # Output: {1, 2}

print(my_set - my_set_2)  # Output: {3, 4, 5}
print(my_set.difference(my_set_2))  # Output: {3, 4, 5}
print(my_set_2 - my_set)  # Output: {8, 9, 7}

print(my_set ^ my_set_2)  # Output: {3, 4, 5, 7, 8, 9}
print(my_set.symmetric_difference(my_set_2))  # Output: {3, 4, 5, 7, 8, 9}

# Adding elements
my_set.add(6)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# Sets automatically remove duplicates
my_set.add(3)
print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

print(1 in my_set)  # Output: True

my_set.remove(3)
# '3' should be member of the set else Raises an error if element is not present

my_set.discard(3)
# removes '3' if present in set else does nothing if element is not present
