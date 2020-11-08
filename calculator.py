# this project will deal with making a calculator using tkinter
# we need to import kinter for it
from tkinter import *

root = Tk()
root.title("Calculator")  # giving title
root.iconbitmap(r'C:\Users\Dell\Desktop\logo.ico')  # adding icon
root.geometry("500x390")
# text to say this program only adds
Only_adds = Label(root, text="""
This Programme only adds two numbers and prints out result 
""")
Only_adds.grid(row=0, column=0)
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
ans.grid(row=5, column=1)
# space adding
sp = Label(root, text="""

""")
sp.grid(row=4, column=0)


# defining a function to add
def Button_add():
    f_num = num1.get()
    s_num = num2.get()
    global frist_num
    global second_num
    frist_num = float(f_num)
    second_num = float(s_num)
    ans.insert(0, frist_num + second_num)


# make button to add the numbers
btn = Button(root, text="Add the numbers", command=Button_add)
btn.grid(row=3, column=0)


# another function to clear all
def All_clear():
    ans.delete(0, END)
    num1.delete(0, END)
    num2.delete(0, END)


# clear button
clear_button = Button(root, text="Clear All", command=All_clear)
clear_button.grid(row=6, column=0)
# final
root.mainloop()
# program ends here
