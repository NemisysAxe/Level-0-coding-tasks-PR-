def temperture_in_celsius(value_in_c):
    multiplier = 1.8
    constant = 32
    temperture_in_fahrenheit = (value_in_c * multiplier) + constant
    
    x = f"{value_in_c} C is {temperture_in_fahrenheit} F"
    return x
    
print(temperture_in_celsius(11))


def temperture_in_fahrenheit(value_in_f):
    multiplier = 1.8
    constant = 32
    temperture_in_celsius= (value_in_f - constant)/multiplier
        
    z = f"{value_in_f} F is {temperture_in_celsius} C"
    return z

print(temperture_in_fahrenheit(50))
    

