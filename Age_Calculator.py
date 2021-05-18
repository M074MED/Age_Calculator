from tkinter import *
from tkinter import messagebox
age_calc = Tk(className=" Age Calculator By M074MED")  # or age_calc.title("Age Calculator")

age_calc.geometry("400x200")

the_age = Label(age_calc, text="Enter Your Age", height=2, font=("Arial", 20), bg="black", fg="white")
the_age.pack()

age = StringVar()
age.set("000")
age_input = Entry(age_calc, width=3, font=("Arial", 20), textvariable=age)
age_input.pack()


def calc():
    the_age_value = age.get()
    months = int(the_age_value)*12
    weeks = months*4
    days = int(the_age_value)*365
    line1 = "Your Age In Months Is: " + str(months)  # or line1 = f"Your Age In Months Is: {Months}"
    line2 = "\nYour Age In Weeks Is: " + str(weeks)
    line3 = "\nYour Age In Days Is: " + str(days)
    all_lines = [line1, line2, line3]
    messagebox.showinfo("Your Age In Some Time Units", "\n".join(all_lines))


btn = Button(age_calc, text="Calculate", width=20, height=2, font=("Arial", 12), activebackground="#4436FC", bg="blue",
             activeforeground="black", fg="white", borderwidth=0, command=calc)
btn.pack()


age_calc.mainloop()
