def search_vowels(string):

    lowercase_string = string.lower()
    vowel = ['a','e','i','o','u']
    vowel_capturer = " "

    for char in lowercase_string:
        if char in vowel and char not in vowel_capturer:
                vowel_capturer += char
                vowel_capturer += ", "

        remove_trailing_comma = vowel_capturer[:-2]

    print(f"Vowels:{remove_trailing_comma}" , end = " ")


search_vowels("Umuzi")


