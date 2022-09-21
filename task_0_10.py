def print_common_letters (string_a, string_b):

    string1 = string_a.lower()
    string2 = string_b.lower()
    common_chars = " "

    for char in string2:
        if char in string1 and string2 and char not in common_chars:
             common_chars += char
             common_chars += ","

    remove_trailing_comma = common_chars[:-1]

    required_phrase = "Common letters"
    print(f"{required_phrase}:{remove_trailing_comma} ", end ='')


#print_common_letters("house","computers")
print_common_letters("baseball","basketball")
#print_common_letters("corporate", "cooperate")
#print_common_letters("muse", "music")
