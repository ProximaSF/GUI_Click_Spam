[Purpose]
The purpose of this project is to create a GUI (graphical user interface) pop-up window that will calculate the click speed when the user spam click the button on the pop-up window.

[GUI]
1. The `import threading` allow for function to run in the background rather than one functions at a time.

2. `import tkinter` allows users to create pop-up interface.
    • The `tk` in `import tkinter as tk` replaced the keyword `tkinter` for `tk` for faster typing. 
    
3. `cooldown()` is a threading function. Once the script start, this function runs automatically without need to be called.

    • The function will stop working once the `for-loop` ends. But if a infinite loop, the function will run indefititly. 

4. `count` and `speed` are not traditional variable for int because `tkinter` requires custome int for it to work in `tkinter` methods.

5. After creating a element (button, text, etc) in the interface, need to `pack()` the element. 

----------------------------------------------------------------

[GUI 2.0] Changes
1. Replaced the `for loop` in `cooldown()` for a `while loop` so the cooldown timer reset after it end.

    • After 4 seconds, call `speed_calcuaiton()` funciton in `cooldown()`. 

2. Added another background task `spam_click`. 
    • The purpose of this background funciton is to listen for user inputs forever once the code starts and append those into into a list.

----------------------------------------------------------------

[GUI 3.0] Changes
1. Removed two lines: `sleep(1)` and `speed.set(0)` for 
    `root.after(1000, lambda: speed.set(0))` and
    `roo.after(0, lambda: count.set(0))`

    • root.after(1000, lambda: speed.set(0))' will replaced the speed of the user back to 0 after 1 second. the `.after()` is a timer like `sleep()` or `time.sleep` but without blocking the rest of the code. This way, the user can see the speed for 2 second before reseting back to zero without affecting the `countdown()` funciton. 

    (NOTE): The time for the `after()` method is in **milliseconds**, so **1000 milliseconds** is equivalent to **1 second**. 

2. Removed:
    `speed_calculation_threading = threading.Thread(target = speed_calculation)` 
    and
    `speed_calculation_threading.start()`
    beacsue they are not needed since the function is being called from `countdown()`. Doesn't need to run automatically. 
----------------------------------------------------------------

[GUI 4.0] Changes
1. More organized. 

2. Added the variable `stop_thread` to handle ending the interface and the script without errors.

3. Removed `global speed` and `global count`
    • Because when you use speed and count inside the functions `spam_click()` and `speed_calculation()`, it is not modifying the variables themselves, but calling methods on the `IntVar` objects. Therefore, you don’t need to declare them as global.

4. Added a way to end the code after closing the interface. 
    • The `clase_interface()` function is exacuted by the line `root.protocol("WM_DELETE_WINDOW", close_interface)`.

    This will detect if the user closed the interface. If so, it runs the function which set the global variable `stop_thread` to `True` and that will stop the `countdown()` function from running automatically, allowing the stop the script entirely. 

----------------------------------------------------------------

[Application]

Use the `pyinstaller` package to convert a python script into an application.

1. If `pyinstaller` not installed, use `pip install pyinstaller` in terminal.
    • After installed, make sure the package is in the right PATH.
    • Issue I had was the `Script` directory with all the pip packages was not in the `System Environment Variable` `Path`
        ► `System Environment Variable` can be found by searching in your computer settings for Windows. 
2. Open the terminal for the directory that contain the script and type `pyinstall name_of_file.py`
3. If worked as expected, open that direction, 3 new item should be added, a `.spec`, `dist` folder and `build` folder
    • To run the application, go into `dist` folder, keep opening until you see the application with the name of your script. It should have a different image icon and the file type is `Application`