input = input("Bir dize girin: ")

longest_substring = "" #en uzun tekrarsız alt dizeyi tutacak değişken
current_substring = "" #mevcut alt dizeyi geçici olarak tutacak değişken 

for character in input: #dizeyi karakter karakter gezecek döngü 
    if character in current_substring:
        index = current_substring.index(character)
        current_substring = current_substring[index + 1:]
    current_substring += character

    if len(current_substring) > len(longest_substring):
        longest_substring = current_substring

print("En uzun yinelemesiz alt dize:", longest_substring)
print("Uzunluk:", len(longest_substring))