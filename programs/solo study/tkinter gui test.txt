from tkinter import *

def create_canvas_window():
    canvas_window = Toplevel ()
    canvas_window.title("Interactive Canvas")
    canvas_window.geometry("500x300")
    canvas = Canvas(canvas_window, width=500, height=300)
    canvas.pack(fill=BOTH, expand=1)

    def on_canvas_click(event):
        canvas.create_oval(event.x-5, event.y-5, event.x+5, event.y+5, fill='black')
    
    #bind the function to the canvas widget, so it gets called when the canvas is clicked
    canvas.bind('<Button-1>', on_canvas_click)
    

tk = Tk()
tk.title("tkinter GUI demonstration")
tk.geometry("800x300") #x/y, window size

#button opens the canvas window when clicked
frame = Frame(tk, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
button = Button(frame, text="Open Canvas", command=create_canvas_window)
button.pack(side=TOP, fill=BOTH, pady=5, padx=5)

tk.mainloop()