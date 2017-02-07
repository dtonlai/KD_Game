import tkinter as tk


root = tk.Tk()

###Variables
timer = [0, 10, 0]
pattern = '{0:02d}:{1:02d}:{2:02d}'
state = False


###Functions
def updateTime():
    if(state):
        global timer
        timer[2] -= 1
        if timer[2] <= 0:
            timer[1] -= 1
            timer[2] = 60
        if timer[1] <= 0 and timer[2] <= 1:
            timer[2] = 0
            pause()
            blowUp()

    timeString = pattern.format(timer[0], timer[1], timer[2])
    timeText.configure(text=timeString)
    root.after(10, updateTime)

def start():
    global state
    state = True

def pause():
    global state
    state = False

def blowUp():
    blowUpFrame = tk.Toplevel()
    blowUpLabel = tk.Label(blowUpFrame, text="KaBooOOoOoOoM!!!", font=("Comic Sans MS", 100))
    blowUpLabel.pack()
    blowUpButton = tk.Button(blowUpFrame, text="You're dead!", command=blowUpFrame.destroy)
    blowUpButton.pack()

###Widgets
timeText = tk.Label(root, text="00:10:00", font=("Helvetica", 150))
timeText.pack()

startButton = tk.Button(root, text="Start", command=start)
startButton.pack()

pauseButton = tk.Button(root, text="Pause", command=pause)
pauseButton.pack()

quitButton = tk.Button(root, text="Quit", command=root.destroy)
quitButton.pack()


updateTime()
root.mainloop()