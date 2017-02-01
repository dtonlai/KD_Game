import tkinter as tk
import time
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("250x250")

#message = tk.Message(window, text="this is a message", width=50)
#message.pack

def count_down():
	timer = 10
	text_display = tk.Text(master=window, height=5, width=10)
	text_display.grid(row=2)
	text_display.insert(tk.END, timer)
	while timer >= 0:
		text_display.configure(text=timer)
		time.sleep(1)
		timer -= 1
	time.sleep(1)
	timer = "Ka-Boom!"
#def configure_label():
	#label.configure(text="Button clicked!")


label = tk.Label(window, text="Don't click that button!", width=200)
label.pack()

button = tk.Button(window, text="Start" , command=count_down)
button.pack()

window.mainloop()