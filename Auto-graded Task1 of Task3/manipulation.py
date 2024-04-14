"""Pseudocode:

1. Prompt the user to enter a sentence and store it in a variable str_manip.
2. Calculate the length of str_manip using len() and store it in a variable length_str.
3. Get the last letter of str_manip and store it in a variable last_letter.
4. Replace all occurrences of last_letter in str_manip with '@' using the replace() method.
5. Get the last three characters of str_manip using slicing and reverse it.
6. Create a five-letter word using the first three characters and the last two characters of str_manip.
7. Print the length of str_manip, the modified str_manip, the reversed last three characters,
and the created five-letter word."""

# Step 1: Ask the user to enter a sentence
str_manip = input("Enter a sentence: ")

# Step 2: Calculate the length of str_manip
length_of_str = len(str_manip)

# Step 3: Find the last letter in the sentence
last_letter = str_manip[-1]

# Step 4: Replace every occurrence of last_letter with '@'
modified_str = str_manip.replace(last_letter, '@')

# Step 5: Print the length of str_manip
print("Length of the sentence:", length_of_str)

# Step 6: Print modified_str
print("Modified sentence:", modified_str)

# Step 7: Print the last three characters of str_manip in reverse order
print("Last three characters backwards:", str_manip[-3:][::-1])

# Step 8: Create a five-letter word using the first three characters and the last two characters in str_manip
five_letter_word = str_manip[:3] + str_manip[-2:]

# Step 9: Print five_letter_word
print("Five-letter word:", five_letter_word)
