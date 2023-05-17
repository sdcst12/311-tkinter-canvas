#!python3
# Example using pack to create your GUI

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
f1 = tk.Frame()
f2 = tk.Frame()
f3 = tk.Frame()

entry1 = tk.Entry(f1, width=40)
label1 = tk.Label(f1,text="Name", bg="#FFFFFF")
f1.pack()
label1.pack(side=tk.LEFT)
entry1.pack(side=tk.LEFT)

entry2 = tk.Entry(f2, width=40)
label2 = tk.Label(f2,text="email", bg="#FFFFFF")
f2.pack()
label2.pack(side=tk.LEFT)
entry2.pack(side=tk.LEFT)

entry3 = tk.Entry(f3, width=40)
label3 = tk.Label(f3,text="password", bg="#FFFFFF")
f3.pack()
label3.pack(side=tk.LEFT)
entry3.pack(side=tk.LEFT)

entry4 = tk.Entry(window,width=60)
entry4.pack()
b1 = tk.Button(window,text="Go")
b1.pack()

b1.bind("<Button-1>",run)



window.mainloop()