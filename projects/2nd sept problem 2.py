total_sec = int(input("Enter total seconds: "))
hours = total_sec // 3600
mins = (total_sec - (hours*3600)) // 60
seconds = total_sec - (hours*3600 + mins *60)
print(f"{total_sec} seconds = {hours} hours + {mins} minutes + {seconds} seconds")