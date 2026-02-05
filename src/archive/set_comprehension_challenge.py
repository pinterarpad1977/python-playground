'''
Create a set of all unique first letters of these words.
'''

words = ["apple", "banana", "apple", "cherry", "banana", "date"]

unique_starts = { w[0] for w in words }
#print(unique_starts)

'''
Create a set containing the squares of all even numbers, 
with duplicates removed automatically.
'''

nums = [1, 2, 2, 3, 4, 4, 5, 6]

square_set = { num **2 for num in nums if num % 2 == 0 }
#print(square_set)

'''
Create a set of the words in lowercase
'''

raw_words = ["Apple", "banana", "APPLE", "Banana", "Cherry", "cherry", "CHERRY"]

lower_set = { word.lower() for word in raw_words }
#print(lower_set)

'''
Create a set of all unique vowels that appear in these words, 
ignoring case.
'''
words2 = ["Apple", "banana", "Cherry", "date", "Elderberry", "fig", "Grape"]
wovels = [ "a", "e", "i", "o", "u"]
unique_wovels = { 
    letter.lower() 
    for word in words2 
    for letter in word 
    if letter.lower() in wovels }

print(unique_wovels)

