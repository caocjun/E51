import time

minutes = int(input("enter the number of minutes to focus:"))
seconds = minutes * 60

while seconds:
    minutes, secs = divmod(minutes, seconds)
    timer = '{:02d}:{:02d}'.format(minutes, seconds)
    print(time, end="\r")
    time.sleep(5)

    print("time，up！")
    
