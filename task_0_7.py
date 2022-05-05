#task_0_7

#The function will convert temperture from celsius to fahrenheit
def temp_c(x):
    multiplier = 1.8
    constant = 32
    temp_f = (x * multiplier) + constant
    
    print(str(x) + " C" + " is" + " " + str(temp_f) + " F")

    
temp_c(11)



#Converting F to C
def temp_f(y):
    multiplier = 1.8
    constant = 32
    temp_c= (y - constant)/multiplier
    
    
    print(str(y) + " F" + " is" + " " + str(temp_c) + " C")

temp_f(50)
    

