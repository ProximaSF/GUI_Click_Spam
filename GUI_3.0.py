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
            speed_calculation()
        else:
            timer = timer - 1
            sleep(1)
            print(timer)
timer_threading = threading.Thread(target = countdown)
timer_threading.start()

count = tk.IntVar(value=0)
speed = tk.IntVar(value=0)

def speed_calculation():
    global speed
    global count
    global click_list_size
    global click_list
    size = len(click_list)
    speed_cal = size/4
    speed.set(speed.get() + speed_cal)
    click_list.clear()
    root.after(2000, lambda: speed.set(0))
    root.after(0, lambda: count.set(0)) # Look at notes to see what it does

def spam_click():
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