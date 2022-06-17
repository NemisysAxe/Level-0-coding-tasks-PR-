
def print_common_letters (char1, char2):
         
    vowels = "AEIOU".lower()
    for word1 in char1 and char2:
        if word1 in vowels and char1 and char2:
            print(word1, end= ",")

    for word1 in char1 and char2:
        if word1 in char1 and char2:
            if word1 not in vowels:
                print(word1, sep=",", end="'")
         
print_common_letters('house','computers')
