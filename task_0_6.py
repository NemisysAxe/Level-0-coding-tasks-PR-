from tkinter import Y


def maximum_value(*numbers):
    largest_number = numbers[0]
    
    for number in numbers:
        if number > largest_number:
            largest_number = number
    
    return largest_number 

maxi_value = maximum_value(1,5,27,50)
print(maxi_value)



