import tkinter as tk
import math
import time

def update_clock():
    current_time = time.localtime()
    hours = current_time.tm_hour
    minutes = current_time.tm_min
    seconds = current_time.tm_sec

    # Calculate the angles for the clock hands
    hour_angle = (hours % 12 + minutes / 60) * 30
    minute_angle = (minutes + seconds / 60) * 6
    second_angle = seconds * 6

    # Update the clock hands' positions
    canvas.delete("all")
    draw_clock_face()
    draw_hand(hour_angle, 80, "blue")
    draw_hand(minute_angle, 100, "green")
    draw_hand(second_angle, 120, "red")

    root.after(1000, update_clock)

def draw_hand(angle, length, color):
    x = center_x + length * math.cos(math.radians(270 - angle))
    y = center_y - length * math.sin(math.radians(270 - angle))
    canvas.create_line(center_x, center_y, x, y, fill=color, width=3)

def draw_clock_face():
    canvas.create_oval(center_x - 130, center_y - 130, center_x + 130, center_y + 130, outline="black", width=4)
    for i in range(1, 13):
        angle = math.radians(270 - i * 30)
        x = center_x + 110 * math.cos(angle)
        y = center_y - 110 * math.sin(angle)
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 12, "bold"))

# Create the main window
root = tk.Tk()
root.title("Analog Clock")

# Set the size of the window and calculate the center coordinates
window_width = 400
window_height = 400
center_x = window_width // 2
center_y = window_height // 2

# Create the canvas to draw the clock
canvas = tk.Canvas(root, width=window_width, height=window_height)
canvas.pack()

# Start the clock
update_clock()

root.mainloop()
