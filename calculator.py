# module imports

import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()

class Start:
    def __init__(self, master):

        # root
        print("Welcome to Calculator!")
        master.title("Calculator") # title of the program
        master.configure(bg="#e0e0e0") # background color of the "master" frame
        master.resizable(False, False) # makes the program not resizable (horizontally, vertically)
        master.iconbitmap("icon.ico")
        self.master = master

        self.window_size = "1310x360"#"310x412"
        self.window_scale_value = 2
        self.master.geometry(self.window_size) # the height, and width of the program
            
        self.operator = "" # this is the actual numbers that are being operated
        self.str_var = tk.StringVar() # creates a new so-called "string Variable" which is basically a string that acts like a variable
        self.str_var.set(self.operator) # this is the value that will be shown as a string in the upper label

        self.scale_button_str_value = "+"
        self.scale_button_str_var = tk.StringVar()
        self.scale_button_str_var.set(self.scale_button_str_value)

        self.default_text_size = 40
        self.variable_size = self.default_text_size # this size will change depending on the length of the value displayed in the calculator

        self.display_style = tkFont.Font(family="Roboto", size=self.variable_size) # set text fontstyle and size for the display text
        self.text_style = tkFont.Font(family="Roboto", size=28) # set text fontstyle and size for the buttons

        # user interface (UI)
        frame1 = tk.Frame(highlightcolor="#ffffff")
        frame1.place(rely=0.28, relx=0.01, relwidth=1, relheight=1)
        label2 = tk.Label(bg="#C4C4C4", anchor="e", textvariable=self.str_var, font=self.display_style)  
        label2.place(relwidth=0.9625, relheight=0.18, relx=0.015, rely=0.02)

        frame2 = tk.Frame(highlightcolor="#ff0000")
        frame2.place(relx=0.015, rely=0.21, relwidth=0.9625, relheight=0.06)

        scale_window_button = tk.Button(master, bg="#ccffcc", activebackground="#bbffbb", relief="sunken", bd=0, textvariable=self.scale_button_str_var, command=lambda: self.scale_window())
        scale_window_button.place(relwidth=0.07, relheight=0.05, relx=0.902, rely=0.215)

        self.b1 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="1", font=self.text_style, command=lambda: self.button_click(1))
        self.b1.grid(row=0, column=0)
        master.bind("1", lambda e: self.button_click(1))

        self.b2 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="2", font=self.text_style, command=lambda: self.button_click(2))
        self.b2.grid(row=0, column=1)
        master.bind("2", lambda e: self.button_click(2))

        self.b3 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="3", font=self.text_style, command=lambda: self.button_click(3))
        self.b3.grid(row=0, column=2)
        master.bind("3", lambda e: self.button_click(3))

        self.b4 = tk.Button(frame1, bg="#94b5FF", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="÷", font=self.text_style, command=lambda: self.button_click("/"))
        self.b4.grid(row=1, column=6)
        master.bind("d", lambda e: self.button_click("/"))

        self.b5 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="4", font=self.text_style, command=lambda: self.button_click(4))
        self.b5.grid(row=0, column=3)
        master.bind("4", lambda e: self.button_click(4))

        self.b6 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="5", font=self.text_style, command=lambda: self.button_click(5))
        self.b6.grid(row=0, column=4)
        master.bind("5", lambda e: self.button_click(5))

        self.b7 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken",  text="6", font=self.text_style, command=lambda: self.button_click(6))
        self.b7.grid(row=1, column=0)
        master.bind("6", lambda e: self.button_click(6))

        self.b8 = tk.Button(frame1, bg="#94b5FF", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="x", font=self.text_style, command=lambda: self.button_click("*"))
        self.b8.grid(row=0, column=6)
        master.bind("m", lambda e: self.button_click("*"))

        self.b9 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="7", font=self.text_style, command=lambda: self.button_click(7))
        self.b9.grid(row=1, column=1)
        master.bind("7", lambda e: self.button_click(7))

        self.b10 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="8", font=self.text_style, command=lambda: self.button_click(8))
        self.b10.grid(row=1, column=2)
        master.bind("8", lambda e: self.button_click(8))

        self.b11 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="9", font=self.text_style, command=lambda: self.button_click(9))
        self.b11.grid(row=1, column=3)
        master.bind("9", lambda e: self.button_click(9))

        self.b12 = tk.Button(frame1, bg="#94b5FF", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="-", font=self.text_style, command=lambda: self.button_click("-"))
        self.b12.grid(row=1, column=5)
        master.bind("-", lambda e: self.button_click("-"))

        self.b13 = tk.Button(frame1, bg="#CBCBCB", activebackground="#FBFBFB", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="C", font=self.text_style, command=lambda: self.clear_display())
        self.b13.grid(row=0, column=8)
        master.bind("c", lambda e: self.clear_display())

        self.b14 = tk.Button(frame1, bg="#C79595", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="e", font=self.text_style, command=lambda: self.clear_digit())
        self.b14.grid(row=0, column=7)
        master.bind("<BackSpace>", lambda e: self.clear_digit())

        self.b15 = tk.Button(frame1, bg="#EFEFEF", activebackground="#FFE9A4", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="0", font=self.text_style, command=lambda: self.button_click(0))
        self.b15.grid(row=1, column=4)
        master.bind("0", lambda e: self.button_click(0))

        self.b16 = tk.Button(frame1, bg="#CBCBCB", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="=", font=self.text_style, command=lambda: self.equals())
        self.b16.grid(row=1, column=7)
        master.bind("<Return>", lambda e: self.equals())

        self.b17 = tk.Button(frame1, bg="#969696", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="≈", font=self.text_style, command=lambda: self.round_to_int())
        self.b17.grid(row=1, column=8)
        master.bind("r", lambda e: self.round_to_int())

        self.b18 = tk.Button(frame1, bg="#94b5FF", activebackground="#EFEFEF", width=3*self.window_scale_value, height=1*self.window_scale_value, relief="sunken", text="+", font=self.text_style, command=lambda: self.button_click("+"))
        self.b18.grid(row=0, column=5)
        master.bind("+", lambda e: self.button_click("+"))

    # logic
    def button_click(self, x): # checks what button is pressed and performs actions according to that
        
        if len(self.operator) > 19:
            return print("you have reached maximum limit of digits!")

        if len(self.operator) > 0:
            if self.operator[-1] == "+" or self.operator[-1] == "-" or self.operator[-1] == "*" or self.operator[-1] == "/":
                if x == 0:
                    return print("you can't have 0 as the first number after operand!")
                elif x == "+" or x == "-" or x == "*" or x == "/":
                    return print("operand has already been chosen!")    

        if x == 0:
            if self.operator[0] == "0":
                return print("you can't have 0 as the first number!")
        
        if x == str(x): # <--- targetting "+", "-", "*" and "/"
            if self.operator[0] == x:
                return print("please type a number first...")
            else:
                self.operator += str(x)
                self.str_var.set(self.operator)
                print(self.operator)

        else:
            self.operator += str(x)
            self.str_var.set(self.operator)
            print(self.operator)

        self.adaptive_text_display()

    def clear_display(self):
        
        self.operator = ""
        print(self.operator)
        self.str_var.set("")
        self.adaptive_text_display()

    def clear_digit(self):
        
        self.operator = self.operator[:-1]
        self.str_var.set(self.operator)
        print(self.operator)
        self.adaptive_text_display()

    def equals(self):
        
        
        sumup = eval(self.operator) # <--- calculations happen here
        sumup = str(sumup)
        self.str_var.set(sumup)
        self.operator = sumup
        print(self.operator)

        self.adaptive_text_display()

    def round_to_int(self): # rounds the displaying number to nearest int
        print(f"converting {self.operator} to type float so round() can be used...") 
        self.operator = float(self.operator)
        print(f"rounding {self.operator} to nearest integer...")
        self.operator = round(self.operator)
        print(f"{self.operator} is now an integer after rounding...")
        self.str_var.set(self.operator)
        print(f"converting {self.operator} back to string...")
        self.operator = str(self.operator)
            
        self.adaptive_text_display()

    # extra
    def adaptive_text_display(self): # small extra that makes font smaller when working with big numbers
        if len(self.operator) > 10:
            self.display_style.config(size=30*self.window_scale_value)
            if len(self.operator) > 13:
                self.display_style.config(size=19*self.window_scale_value)
            else:
                pass
        else:
            self.display_style.config(size=self.default_text_size)

    def scale_window(self): # scale window size to be bigger / smaller
        if self.window_size == "310x412":
            self.window_size = "585x660"
            self.window_scale_value = 2
            self.default_text_size = 80

            self.scale_button_str_value = "-"
            self.scale_button_str_var.set(self.scale_button_str_value)

        elif self.window_size == "1300x660":
            self.window_scale_value = 3
            self.default_text_size = 80
        else:
            self.window_size = "310x412"
            self.window_scale_value = 1
            self.default_text_size = 40

            self.scale_button_str_value = "+"
            self.scale_button_str_var.set(self.scale_button_str_value)

        self.adaptive_text_display()


        # update window size with the new values
        self.master.geometry(self.window_size)

        # update size of all buttons
        self.b1.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b2.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b3.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b4.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b5.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b6.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b7.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b8.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b9.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b10.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b11.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b12.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b13.config(width=2*self.window_scale_value, height=1*self.window_scale_value)
        self.b14.config(width=1*self.window_scale_value, height=1*self.window_scale_value)
        self.b15.config(width=3*self.window_scale_value, height=1*self.window_scale_value)
        self.b16.config(width=2*self.window_scale_value, height=1*self.window_scale_value)
        self.b17.config(width=1*self.window_scale_value, height=1*self.window_scale_value)
        self.b18.config(width=3*self.window_scale_value, height=1*self.window_scale_value)

                
# start the program
start = Start(root)

root.mainloop()

# - help -
# https://www.youtube.com/watch?v=9WPmxH4RRZ0