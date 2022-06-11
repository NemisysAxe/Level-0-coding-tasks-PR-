def temperture_in_celsius(x):
    multiplier = 1.8
    constant = 32
    temperture_in_fahrenheit = (x * multiplier) + constant
    
    x = f"{x} C is {temperture_in_fahrenheit} F"
    return x
    
print(temperture_in_celsius(11))


def temperture_in_fahrenheit(y):
    multiplier = 1.8
    constant = 32
    temperture_in_celsius= (y - constant)/multiplier
        
    z = f"{y} F is {temperture_in_celsius} C"
    return z

print(temperture_in_fahrenheit(50))
    

