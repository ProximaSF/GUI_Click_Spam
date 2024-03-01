import tkinter as tk
import threading
from time import *

root = tk.Tk()
root.title("Title Meh")
root.geometry("200x200")

def countdown(): #Countdown from 3 to 0
    global timer
    timer  = 4
    for i in range(4):
        timer  = timer - 1
        sleep(1)
        print(timer)
timer_threading = threading.Thread(target=countdown)
timer_threading.start() # Start the funciton automatically, run in the background

clicks_storage = []
size_list = 0

count = tk.IntVar(value=0) # Set count variable to object 0
speed = tk.IntVar(value=0) # Set speed variable to object 0 
speed_set = False

def on_button_command():
    global speed_set
    # if speed_set = False here, it will turn to False after it has turned to True
    if timer > 0: # Check if timer is 0, if not, allow clicks.
        count.set(count.get() + 1)
        clicks_storage.append(".")
    else: # Else disable and display speed/sec and the message
        print("Time out")
        size_list = len(clicks_storage)
        if speed_set == False: # To avoid changing the speed txt more than once.
            speed.set(speed.get() + size_list)
            speed_set = True # set global variable speed_set (line 24) to True

label = tk.Label(root, textvariable=0)
label.pack()

button = tk.Button(root, text = "click me", command = on_button_command)
button.pack()

Speed_label_title = tk.Label(root, text="Clicks Per Second", height=1)
Speed_label_title.pack()

label2 = tk.Label(root, textvariable=speed)
label2.pack()

root.mainloop()
