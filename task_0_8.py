def time(time_in_mins):
    hours = (time_in_mins // 60) 
    minutes = (time_in_mins % 60)
   
    if hours == 0 or hours > 1:
        hours_print = "hours" 
    else:
        hours_print = "hour"
        
    if minutes == 0 or minutes > 1:
        minutes_print = "minutes"
    else:
        minutes_print = "minute"
            
    print(f"{hours} {hours_print}, {minutes} {minutes_print}")
    
time(60)
