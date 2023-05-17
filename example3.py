#!python3
# Example using place to create your GUI

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
label1.place(x=50,y=50)
entry1.place(x=150,y=50)

entry2 = tk.Entry(window, width=40)
label2 = tk.Label(window,text="email", bg="#FFFFFF")
label2.place(x=50,y=70)
entry2.place(x=150,y=70)

entry3 = tk.Entry(window, width=40)
label3 = tk.Label(window,text="password", bg="#FFFFFF")
label3.place(x=50,y=90)
entry3.place(x=150,y=90)

entry4 = tk.Entry(window,width=60)
b1 = tk.Button(window,text="Go")
entry4.place(x=50,y=110)
b1.place(x=100,y=130)

b1.bind("<Button-1>",run)



window.mainloop()