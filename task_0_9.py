
def print_vowels (string):

    vowels_uppercase = "AEIOU"
    vowels_lowercase = "aeiou"
    vowels = vowels_lowercase + vowels_uppercase
    
    for vowel in string:
        if vowel in vowels:
            if vowel > vowels_uppercase:  
                if vowel in vowels_lowercase:
                    print(vowel,sep = "," ,end =" ")
                  
print_vowels('Umuzi')




