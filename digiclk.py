import tkinter as tk
import time

root = tk.Tk()
root.title("Digital Clock")

# Define the different colors to use for the clock
bg_color = "#FFA07A" # light salmon
fg_color = "#800000" # maroon

# Create a label for the clock with the defined colors
clock_label = tk.Label(root, font=('Bradley Hand ITC', 80, 'bold'), bg=bg_color, fg=fg_color)
clock_label.pack(pady=50)

# Define a function to update the clock every second
def update_clock():
    current_time = time.strftime("%I:%M:%S %p")
    clock_label.config(text=current_time)
    clock_label.after(1000, update_clock)

# Call the update_clock function to start the clock
update_clock()

root.mainloop()