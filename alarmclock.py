import tkinter as tk
def setalarm():
    a = H_E.get()
    b = M_E.get()
    print(a,b)
window = tk.Tk()

window.title("alarm clock")
h = tk.Label(text = "Hour")
m = tk.Label(text = "Minute")
H_E = tk.Entry()
M_E = tk.Entry()
button = tk.Button(text = "set alarm", command = setalarm)



h.grid(row = 1, column = 1)
m.grid(row = 3, column = 1)
H_E.grid(row = 2, column = 1)
M_E.grid(row = 4, column = 1)
button.grid(row = 5 ,column = 1)

window.mainloop()


