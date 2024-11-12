"""
Author:- Abhi
Discription:- This code is used for save student information like personal details 
              and result of students.
Date:- Jan 16,2023
"""

import tkinter as tk
from dbconfig import con



# Function to connect to MySQL
def connect_to_mysql():
    global cursor
    cursor = con.cursor()
    print("Connected to MySQL")

# Function to close MySQL connection
def close_mysql_connection():
    cursor.close()
    con.close()
    print("MySQL connection closed")


# Function to insert data into MySQL
def insert_data():
    global roll_no, name, mob_no, email_id, address, aadhar_no, course
    roll_no = lb1.get()
    name = lb2.get()
    mob_no = lb3.get()
    email_id = lb4.get()
    address = lb5.get()
    aadhar_no = lb6.get()
    course = lb7.get()
    query = "INSERT INTO Students (roll_no, name, mob_no, email_id, address, aadhar_no, course) VALUES (%s, %s)"
    values = (roll_no, name, mob_no, email_id, address, aadhar_no, course)
    cursor.execute(query, values)
    con.commit()
    print("Data inserted successfully")

# Function to delete data from MySQL
def delete_data():
    name = roll_no.get()
    query = "DELETE FROM users WHERE name = %s"
    value = (name,)
    cursor.execute(query, value)
    con.commit()
    print("Data deleted successfully")

# Function to update data in MySQL
def update_data():
    roll_no = lb1.get()
    name = lb2.get()
    mob_no = lb3.get()
    email_id = lb4.get()
    address = lb5.get()
    aadhar_no = lb6.get()
    course = lb7.get()
    query = "UPDATE Student SET age = %s name = %s, mob_no = %s, email_id = %s, address = %s, aadhar_no = %s, course = %s WHERE roll_no = %s"
    values = (roll_no, name, mob_no, email_id, address, aadhar_no, course)
    cursor.execute(query, values)
    con.commit()
    print("Data updated successfully")

# Function to fetch and display data from MySQL
def view_data():
    query = "SELECT * FROM users"
    cursor.execute(query)
    result = cursor.fetchall()
    

root=tk.Tk()
root.title("Student Information System")
root.geometry("750x650+395+105")
root.resizable(True,True)
font = "Helvetica 35 bold italic underline"
title = tk.Label(root, text ="Student Information System",font = font, fg = 'red')
title.pack()


font = "Helvetica 25 bold"
#Creations of Lables
lab1 = tk.Label(root, text="Roll No :- ", font = font, fg = "black")
lab1.place(x=35, y=80)

lab2 = tk.Label(root, text="Name :- ", font = font, fg = "black")
lab2.place(x=35, y=135)

lab3 = tk.Label(root, text="Mobile No :- ", font = font, fg = "black")
lab3.place(x=35, y=190)

lab4 = tk.Label(root, text="Email ID :- ", font = font, fg = "black")
lab4.place(x=35, y=245)

lab5 = tk.Label(root, text="Address :- ", font = font, fg = "black")
lab5.place(x=35, y=300)

lab5 = tk.Label(root, text="Adhar No :- ", font = font, fg = "black")
lab5.place(x=35, y=435)

lab6 = tk.Label(root, text="Course :- ", font = font, fg = "black")
lab6.place(x=35, y=490)


#Creations of Entry
lb1 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb1.place(x=235, y=80, width=450)

lb2 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb2.place(x=235,y=135, width=450)

lb3 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb3.place(x=235, y=190, width=450)

lb4 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb4.place(x=235, y=245, width=450)

lb5 = tk.Text(root, bg="white", fg= "black", font= "arial 20 " )
lb5.place(x=235, y=300, width=450, height=125)

lb6 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb6.place(x=235, y=435, width=450)

lb7 = tk.Entry(root, bg="white", fg= "black", font= "arial 20 " )
lb7.place(x=235, y=490, width=450)


#Creations of Buttons
but1=tk.Button(root, text="Add",bg="white", font="Helvetica 20 bold", 
               command=insert_data)
but1.place(x=55, y=560)

but2=tk.Button(root, text="View",bg="white", font="Helvetica 20 bold",
               )
but2.place(x=140, y=560)

but2=tk.Button(root, text="Reset",bg="white", font="Helvetica 20 bold")
but2.place(x=235, y=560)

but3=tk.Button(root, text="Update",bg="white", font="Helvetica 20 bold")
but3.place(x=340, y=560)

but4=tk.Button(root, text="Delete",bg="white", font="Helvetica 20 bold")
but4.place(x=465, y=560)

but5=tk.Button(root, text="Next",bg="white", font="Helvetica 20 bold", 
               command=connect_to_mysql)
but5.place(x=580, y=560)

# Create a text area to display the result

root.mainloop()