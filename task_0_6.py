def maximum_value(*x):
    largest_number = x[0]
    
    for numbers in x:
         if numbers > largest_number:
            largest_number = numbers
    
    return largest_number 

maxi_value = maximum_value(1,5,27,50)
print(maxi_value)



