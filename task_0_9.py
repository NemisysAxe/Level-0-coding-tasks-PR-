def search_vowels(string):

    lowercase_string = string.lower()
    vowel = ['a','e','i','o','u']
    vowelist = " "

    for char in lowercase_string:
        if char in vowel and char not in vowelist:
                vowelist += char
                vowelist += ","

        remove_trailing_comma = vowelist[:-1]

    print(f"Vowels:{remove_trailing_comma}" , end = " ")

search_vowels("August")
#search_vowels("Umuzi")


