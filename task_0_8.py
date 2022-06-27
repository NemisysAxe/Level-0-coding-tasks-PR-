def time(time_in_mins):
    hours = (time_in_mins // 60) 
    minutes = (time_in_mins % 60)
   
    if hours <= 0 or hours == 1:
        hours_print = "hour" 
    else:
        hours_print = "hours"
        
    if minutes <= 0 or minutes == 1:
        minutes_print = "minute"
    else:
        minutes_print = "minutes"
            
    print(f"{hours} {hours_print}, {minutes} {minutes_print}")
    
time(64)
