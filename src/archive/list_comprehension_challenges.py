'''
Create a list where:
• even numbers become their square
• odd numbers become their cube
'''

nums = [1, 2, 3, 4, 5, 6]

magic_list = [ x ** 2 if x % 2 == 0 else x ** 3 for x in nums]
#print(magic_list)


'''
Use a list comprehension
Extract only the digits
Convert them to integers
'''

s = "a1b2c3d4e5"

numbers_extracted = [ int(c) for c in s if c.isdigit() ]
#print(numbers_extracted)

'''
Flatten the list
Keep only the positive numbers
Do it all in one list comprehension
'''

nested = [
    [1, -2, 3],
    [4, -5],
    [-6, 7, 8, -9]
]

flat_positive = [ item for n in nested for item in n if item > 0]
#print(flat_positive)


'''
Create a dictionary where:
keys → the animal names
values → the length of each name
'''

animals = ["cat", "dog", "parrot", "snake", "cow"]

dct_len = { animal: len(animal) for animal in animals }
#print(dct_len)


'''
Create a dictionary where:
keys → the animal names
values → the length of the name
BUT include only animals with names longer than 3 letters
'''

dct_len_filtered = { animal: len(animal) for animal in animals if len(animal) > 3}
print(dct_len_filtered)
