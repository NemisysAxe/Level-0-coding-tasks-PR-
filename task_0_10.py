def print_common_letters (char1, char2):
    
    cha1 = char1.lower()
    cha2 = char2.lower()
    
    output = " "
    
    for word1 in cha1 and cha2:
        if word1 in cha1 and cha2 and word1 not in output:
             output += word1
             output += ","

    clean_list = output[:-1]     

    phrase = "Common letters"   
    print(f"{phrase}:{clean_list} ", end ='')

if __name__ == "__main__":
    print_common_letters('house','computers')
    
