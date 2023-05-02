import time

minutes = int(input("enter the number of minutes to focus:"))
seconds = minutes * 10

while seconds:
    mins, secs = divmod(minutes, seconds)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    print(time, end="\r")
    time.sleep(1)

    print("time，up！")
    
