import time

minutee = int(input("enter the number of minutes to focus:"))
seconds = minutes * 60

while seconds:
    mins, secs = divmod(mins,secs)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(time,end="\r")
    time.sleep(1)
    seconds -= 1
    
    print("Time's up!")
    
