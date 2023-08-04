input = input("Enter a string: ")

longest_substring = "" #variable to hold the longest non-repeating substring
current_substring = "" #variable to temporarily store the current substring

#loop to iterate over the string character by character
for character in input: 
    if character in current_substring:
        index = current_substring.index(character)
        current_substring = current_substring[index + 1:]
    current_substring += character

   #if the length of the current substring is longer than the length of the longest non-repeating substring, the longest non-repeating substring is updated
    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

print("Longest substring without duplicates:", longest_substring)
print("Length", len(longest_substring))