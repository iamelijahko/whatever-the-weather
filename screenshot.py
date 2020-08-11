import pyautogui   # import PyAutoGUI library
import tkinter as tk  # import tkinter library

# create main window
window = tk.Tk()

# define a method that will call whenever button will be clicked
def take():
    image = pyautogui.screenshot("tkscreen.png")

# create a button
shot_btn = tk.Button(window,text = "Take Screenshot", command=take())

# place the button on the window
shot_btn.place(x=50, y=50)
window.mainloop()