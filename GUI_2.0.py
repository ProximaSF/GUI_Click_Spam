import tkinter as tk
import threading
from time import *

root = tk.Tk()
root.title("Click speed")
root.geometry("200x200")

click_list = []

timer = 4
def countdown():
    global timer
    while True:
        if timer == 0:
            timer = 4
            speed_calculation() # Call speed_calculation() after every 4 sec to update interface
        else:
            timer = timer - 1
            sleep(1)
            print(timer)
# Start the funciton automatically, run in the background
timer_threading = threading.Thread(target = countdown)
timer_threading.start()

count = tk.IntVar(value=0)
speed = tk.IntVar(value=0)

def speed_calculation(): # Called to update interface
    global speed
    global click_list_size
    
    size = len(click_list)
    speed_cal = size/4
    speed.set(speed.get() + speed_cal)
    click_list.clear()
    sleep(1)
    speed.set(0)
# Make speed_calculation() run autmatically. Don't need this; check GUI_3.0
speed_calculation_threading = threading.Thread(target = speed_calculation)
speed_calculation_threading.start() 

def spam_click(): #C Continue asking for input
    count.set(count.get() + 1)
    click_list.append(".")

label = tk.Label(root, textvariable=count)
label.pack()

click_speed_title = tk.Label(root, text= "Clicks Per Second:", height=1)
click_speed_title.pack()

label2 = tk.Label(root, textvariable=speed)
label2.pack()

button = tk.Button(root, text = "click me", command = spam_click)
button.pack()

root.mainloop()