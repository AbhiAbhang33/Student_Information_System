import tkinter as tk

root=tk.Tk()
root.title("Student Information System")
root.geometry("750x650+395+105")
root.resizable(True,True)
font = "Helvetica 35 bold italic underline"
title = tk.Label(root, text =f"Student Result",font = font, fg = 'red')
title.pack()


font = "Helvetica 20 bold"
#Creations of Lables
lab1 = tk.Label(root, text="     Name :- ", font = font, fg = "black")
lab1.place(x=35, y=80)

lab2 = tk.Label(root, text="     Java :-", font = font, fg = "black")
lab2.place(x=35, y=170)

lab3 = tk.Label(root, text="     Python :-", font = font, fg = "black")
lab3.place(x=35, y=225)

lab4 = tk.Label(root, text="     C++ :- ", font = font, fg = "black")
lab4.place(x=35, y=280)

lab5 = tk.Label(root, text="     ASP.NET :- ", font = font, fg = "black")
lab5.place(x=35, y=335)

lab5 = tk.Label(root, text="    Total :- ", font = font, fg = "black")
lab5.place(x=35, y=435)

lab6 = tk.Label(root, text=" Persentage :- ", font = font, fg = "black")
lab6.place(x=35, y=490)


#Creations of Entry
lb1 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb1.place(x=235, y=80, width=400)

lb2 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb2.place(x=235,y=170, width=300)

lb3 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb3.place(x=235, y=225, width=300)

lb4 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb4.place(x=235, y=280, width=300)

lb5 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb5.place(x=235, y=335, width=300)

lb6 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb6.place(x=235, y=435, width=300)

lb7 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb7.place(x=235, y=490, width=300)


#Creations of Buttons
but1 = tk.Button(root, text="Back",bg="white", font="Helvetica 20 bold")
but1.place(x=55, y=560)

but2 = tk.Button(root, text="Update",bg="white", font="Helvetica 20 bold")
but2.place(x=157, y=560)

but3 = tk.Button(root, text="Reset",bg="white", font="Helvetica 20 bold")
but3.place(x=285, y=560)

but4 = tk.Button(root, text="Save",bg="white", font="Helvetica 20 bold")
but4.place(x=395, y=560)

but5 = tk.Button(root, text="Exit",bg="white", font="Helvetica 20 bold",
               command = root.destroy)
but5.place(x=495, y=560)

root.mainloop()