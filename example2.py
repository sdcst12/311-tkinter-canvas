#!python3
# Example using grid to create your GUI

import tkinter as tk

def run(event):
    name = entry1.get()
    email = entry2.get()
    pw = entry3.get()
    output = f"Your name is {name} and your email is {email}"
    entry4.delete(0,tk.END)
    entry4.insert(0,output)

window = tk.Tk()
window.title('Sample')
window.geometry('400x200')



entry1 = tk.Entry(window, width=40)
label1 = tk.Label(window,text="Name", bg="#FFFFFF")
label1.grid(row=1,column=0)
entry1.grid(row=1,column=1)

entry2 = tk.Entry(window, width=40)
label2 = tk.Label(window,text="email", bg="#FFFFFF")
label2.grid(row=2,column=0)
entry2.grid(row=2,column=1)

entry3 = tk.Entry(window, width=40)
label3 = tk.Label(window,text="password", bg="#FFFFFF")
label3.grid(row=3,column=0)
entry3.grid(row=3,column=1)

entry4 = tk.Entry(window,width=60)
entry4.grid(row=4,columnspan=2)
b1 = tk.Button(window,text="Go")
b1.grid(row=5,columnspan=2)

b1.bind("<Button-1>",run)



window.mainloop()