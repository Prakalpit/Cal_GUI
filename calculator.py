# this project will deal with making a calculator using tkinter
# we need to import tkinter for it
from tkinter import *

root = Tk()
root.title("Calculator")  # giving title
root.iconbitmap(r'C:\Users\Dell\Desktop\logo.ico')  # adding icon
root.geometry("500x390")
# text to say this program only adds

'''
Below from this line will include all the functions 
'''
#difining a function to add the numbers
def Button_add():
    f_num = num1.get()
    s_num = num2.get()
    global frist_num
    global second_num
    frist_num = float(f_num)
    second_num = float(s_num)
    ans.insert(0, frist_num + second_num)

#defining another function to subract
def button_sub():
    f_num = num1.get()
    s_num = num2.get()
    global frist_num
    global second_num
    frist_num = float(f_num)
    second_num = float(s_num)
    ans.insert(0, frist_num - second_num)


#defining another function to divide
def division():
    f_num = num1.get()
    s_num = num2.get()
    global frist_num
    global second_num
    frist_num = float(f_num)
    second_num = float(s_num)
    ans.insert(0, frist_num / second_num)

#defining another function to multiply
def btn_multiply():
    f_num = num1.get()
    s_num = num2.get()
    global frist_num
    global second_num
    frist_num = float(f_num)
    second_num = float(s_num)
    ans.insert(0, frist_num * second_num)

#defining a function to clear all
def All_clear():
    ans.delete(0, END)
    num1.delete(0, END)
    num2.delete(0, END)


Wel_come = Label(root, text="""
Please make sure you go according to the options we provide 
""")
Wel_come.grid(row=0, column=0)
# creating text to ask the user to input the number
lbl1 = Label(root, text="Enter first number: ")
lbl1.grid(row=1, column=0)
# creating entry for entering first number
num1 = Entry(root)
num1.grid(row=1, column=1)
# text to enter second number
lbl2 = Label(root, text="Enter second number: ")
lbl2.grid(row=2, column=0)
# entry for second number
num2 = Entry(root)
num2.grid(row=2, column=1)
# answer box
ans = Entry(root)
ans.grid(row=7, column=1)
# space adding
sp = Label(root, text="""

""")
sp.grid(row=4, column=0)

# make button to add the numbers
btn_add = Button(root, text="Add(+)", command=Button_add)
btn_add.grid(row=3, column=0)

#button to add this command to
subtr_btn=Button(root, text="subtract(-)", command=button_sub)
subtr_btn.grid(row=4, column=0)

#button for division
div_btn=Button(root, text="divide(/)", command=division)
div_btn.grid(row=5, column=0)
#button for product
prd_btn=Button(root, text="Multiply(x)", command=btn_multiply)
prd_btn.grid(row=6, column=0)
# clear button
clear_button = Button(root, text="Clear All", command=All_clear)
clear_button.grid(row=7, column=0)

# final
root.mainloop()
# program ends here
