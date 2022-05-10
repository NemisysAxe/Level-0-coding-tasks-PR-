def temp_c(x):
    multiplier = 1.8
    constant = 32
    temp_f = (x * multiplier) + constant
    
    x = (str(x) + " C" + " is" + " " + str(temp_f) + " F")
    return x
    
print(temp_c(11))


def temp_f(y):
    multiplier = 1.8
    constant = 32
    temp_c= (y - constant)/multiplier
        
    z = (str(y) + " F" + " is" + " " + str(temp_c) + " C")
    return z

print(temp_f(50))
    

