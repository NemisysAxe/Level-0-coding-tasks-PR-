def temperture_in_fahrenheit(value_in_celsius):
    multiplier = 1.8
    constant = 32
    temperture_in_fahrenheit = (value_in_celsius * multiplier) + constant
    
    temperture_in_fahrenheit_output = f"{temperture_in_fahrenheit} F"
    
    return temperture_in_fahrenheit_output
    
print(temperture_in_fahrenheit(11))


def temperture_in_celsius(value_in_fahrenheit):
    multiplier = 1.8
    constant = 32
    temperture_in_celsius= (value_in_fahrenheit - constant)/multiplier
        
    temperture_in_celsius_output = f"{temperture_in_celsius} C"
   
    return temperture_in_celsius_output

print(temperture_in_celsius(50))
    

