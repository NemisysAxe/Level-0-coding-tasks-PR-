def temp_c(x):
    multiplier = 1.8
    constant = 32
    temp_f = (x * multiplier) + constant
    
    x = print(str(x) + " C" + " is" + " " + str(temp_f) + " F")
    return x
    
temp_c(11)


def temp_f(y):
    multiplier = 1.8
    constant = 32
    temp_c= (y - constant)/multiplier
        
    z = print(str(y) + " F" + " is" + " " + str(temp_c) + " C")
    return z

temp_f(50)
    

