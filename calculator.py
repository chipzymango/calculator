# - modules -

import tkinter as tk
import tkinter.font as tkFont

# - root - 

print("Welcome to Calculator!")
root = tk.Tk()
root.geometry("310x412") # the height, and width of the program
root.title("Calculator") # title of the program
root.configure(bg="#e0e0e0") # background color of the "root" frame
root.resizable(False, False) # makes the program not resizable (horizontally, vertically)
root.iconbitmap("icon.ico")
    
operator = "" # this is the actual numbers that are being operated
str_var = tk.StringVar() # creates a new so-called "string Variable" which is basically a string that acts like a variable
str_var.set(operator) # this is the value that will be shown as a string in the upper label

default_text_size = 40
variable_size = default_text_size # this size will change depending on the length of the value displayed in the calculator

display_style = tkFont.Font(family="Roboto", size=variable_size) # set text fontstyle and size for the display text
text_style = tkFont.Font(family="Roboto", size=28) # set text fontstyle and size for the buttons

# - GUI -

frame1 = tk.Frame(highlightcolor="#ffffff")
frame1.place(rely=0.28, relx=0.01, relwidth=1, relheight=1)
frame2 = tk.Label(bg="#C4C4C4", anchor="e", textvariable=str_var, font=display_style)  
frame2.place(relwidth=0.9625, relheight=0.225, relx=0.015, rely=0.02)

b1 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="1", font=text_style, command=lambda: button_click(1))
b1.grid(row=0, column=0)
root.bind("1", lambda e: button_click(1))
b2 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="2", font=text_style, command=lambda: button_click(2))
b2.grid(row=0, column=1)
root.bind("2", lambda e: button_click(2))
b3 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="3", font=text_style, command=lambda: button_click(3))
b3.grid(row=0, column=2)
root.bind("3", lambda e: button_click(3))
b4 = tk.Button(frame1, bg="#94B5FF", activebackground="#EFEFEF", width=3, height=1, relief="sunken", text="÷", font=text_style, command=lambda: button_click("/"))
b4.grid(row=0, column=3)
root.bind("d", lambda e: button_click("/"))
b5 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="4", font=text_style, command=lambda: button_click(4))
b5.grid(row=1, column=0)
root.bind("4", lambda e: button_click(4))
b6 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="5", font=text_style, command=lambda: button_click(5))
b6.grid(row=1, column=1)
root.bind("5", lambda e: button_click(5))
b7 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken",  text="6", font=text_style, command=lambda: button_click(6))
b7.grid(row=1, column=2)
root.bind("6", lambda e: button_click(6))
b8 = tk.Button(frame1, bg="#94B5FF", activebackground="#EFEFEF", width=3, height=1, relief="sunken", text="x", font=text_style, command=lambda: button_click("*"))
b8.grid(row=1, column=3)
root.bind("m", lambda e: button_click("*"))
b9 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="7", font=text_style, command=lambda: button_click(7))
b9.grid(row=2, column=0)
root.bind("7", lambda e: button_click(7))
b10 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="8", font=text_style, command=lambda: button_click(8))
b10.grid(row=2, column=1)
root.bind("8", lambda e: button_click(8))
b11 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="9", font=text_style, command=lambda: button_click(9))
b11.grid(row=2, column=2)
root.bind("9", lambda e: button_click(9))
b12 = tk.Button(frame1, bg="#94B5FF", activebackground="#EFEFEF", width=3, height=1, relief="sunken", text="-", font=text_style, command=lambda: button_click("-"))
b12.grid(row=2, column=3)
root.bind("-", lambda e: button_click("-"))
b13 = tk.Button(frame1, bg="#CBCBCB", activebackground="#FBFBFB", width=2, height=1, relief="sunken", text="C", font=text_style, command=lambda: clear_display())
b13.grid(row=3, column=0, sticky="w")
root.bind("c", lambda e: clear_display())
b14 = tk.Button(frame1, bg="#C79595", activebackground="#EFEFEF", width=1, height=1, relief="sunken", text="e", font=text_style, command=lambda: clear_digit())
b14.grid(row=3, column=0, sticky="e")
root.bind("<BackSpace>", lambda e: clear_digit())
b15 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3, height=1, relief="sunken", text="0", font=text_style, command=lambda: button_click(0))
b15.grid(row=3, column=1)
root.bind("0", lambda e: button_click(0))
b16 = tk.Button(frame1, bg="#CBCBCB", activebackground="#EFEFEF", width=2, height=1, relief="sunken", text="=", font=text_style, command=lambda: equals())
b16.grid(row=3, column=2, sticky="w")
root.bind("<Return>", lambda e: equals())
b17 = tk.Button(frame1, bg="#969696", activebackground="#EFEFEF", width=1, height=1, relief="sunken", text="≈", font=text_style, command=lambda: round_to_int())
b17.grid(row=3, column=2, sticky="e")
root.bind("r", lambda e: round_to_int())
b18 = tk.Button(frame1, bg="#94B5FF", activebackground="#EFEFEF", width=3, height=1, relief="sunken", text="+", font=text_style, command=lambda: button_click("+"))
b18.grid(row=3, column=3)
root.bind("+", lambda e: button_click("+"))

# - logic - 

def button_click(x): # checks what button is pressed and performs action according to that
    global operator
    if len(operator) > 20:
        return print("you have reached maximum limit of digits!")

    if len(operator) > 0:
        if operator[-1] == "+" or operator[-1] == "-" or operator[-1] == "*" or operator[-1] == "/":
            if x == 0:
                return print("you can't have 0 as the first number after operand!")
            elif x == "+" or x == "-" or x == "*" or x == "/":
                return print("operand has already been chosen!")    

    if x == 0:
        if operator[0] == "0":
            return print("you can't have 0 as the first number!")
    
    if x == str(x): # <--- targetting "+", "-", "*" and "/"
        if operator[0] == x:
            return print("please type a number first...")
        else:
            operator += str(x)
            str_var.set(operator)
            print(operator)

    else:
        operator += str(x)
        str_var.set(operator)
        print(operator)

    adaptive_text_display()

def clear_display():
    global operator
    operator = ""
    print(operator)
    str_var.set("")
    adaptive_text_display()

def clear_digit():
    global operator
    operator = operator[:-1]
    str_var.set(operator)
    print(operator)
    adaptive_text_display()

def equals():
    global operator
    global variable_size
    sumup = eval(operator) # <--- calculations happen here
    sumup = str(sumup)
    str_var.set(sumup)
    operator = sumup
    print(operator)

    adaptive_text_display()

def round_to_int(): # rounds the displaying number to nearest int
    global operator
    if float(operator):
        print(f"converting {operator} to type float so round() can be used...") 
        operator = float(operator)
        print(f"rounding {operator} to nearest integer...")
        operator = round(operator)
        print(f"{operator} is now an integer after rounding...")
        str_var.set(operator)
        print(f"converting {operator} back to string...")
        operator = str(operator)
        
    adaptive_text_display()

# - extra -

def adaptive_text_display(): # small extra that makes font smaller when working with big numbers
    if len(operator) > 10:
        display_style.config(size=30)
        if len(operator) > 13:
            display_style.config(size=19)
        else:
            pass
    else:
        display_style.config(size=default_text_size)
            
root.mainloop()

# - help -
# https://www.youtube.com/watch?v=9WPmxH4RRZ0