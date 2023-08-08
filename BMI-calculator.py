from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Create the main application window
root = Tk()
root.title("BMI Calculator")
root.geometry("470x580+300+200")
root.resizable(False, False)
root.configure(bg="#f0f1f5")


# Define the BMI calculation function
def BMI():
    h = float(Height.get())
    w = float(Weight.get())

    # convert height to meter
    m = h / 100
    bmi = round(float(w / m ** 2))
    label1.config(text=bmi)

    if bmi < -18.5:
        label2.config(text="Underweight!!!")
        label3.config(text="Your weight falls below the normal range")
    elif 18.5 <= bmi <= 25:
        label2.config(text="Normal")
        label3.config(text="You have ideal body weight ")
    elif 25 <= bmi <= 30:
        label2.config(text="Overweight!!!")
        label3.config(text="Your weight exceeds the normal range")
    else:
        label2.config(text="Obese !!!!!!!!")
        label3.config(text="Your health could be at risk ")


# Application Icon
image_icon = PhotoImage(file="icon.png")
root.iconphoto(False, image_icon)

# TOP Image
top = PhotoImage(file="Top.png")
top_image = Label(root, image=top, background="#f0f1f5")
top_image.place(x=-10, y=10)

# Bottom Box
Label(root, width=72, height=18, bg="lightblue").pack(side=BOTTOM)

# Two Boxes
box = PhotoImage(file="Box.png")
Label(root, image=box).place(x=20, y=100)
Label(root, image=box).place(x=240, y=100)

# Scale Image
scale = PhotoImage(file="scale.png")
Label(root, image=scale, bg="lightblue").place(x=20, y=310)

# Slider 1
current_value = tk.DoubleVar()


def get_current_value():
    return "{: 2f}".format((current_value.get()))


def slider_changed(event):
    Height.set(get_current_value())

    size = int(float(get_current_value()))
    img = (Image.open("man.png"))
    resized_image = img.resize((50, 10 + size))
    photo2 = ImageTk.PhotoImage(resized_image)
    man_image.configure(image=photo2)
    man_image.place(x=70, y=550 - size)
    man_image.image = photo2


# Command to change background color od scale
style = ttk.Style()
style.configure("TScale", background="white")
slider = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale",
                   command=slider_changed, variable=current_value)
slider.place(x=80, y=250)

# Slider 2
current_value2 = tk.DoubleVar()


def get_current_value2():
    return "{: 2f}".format((current_value2.get()))


def slider_changed2(event):
    Weight.set(get_current_value2())


style2 = ttk.Style()
style2.configure("TScale", background="white")
slider2 = ttk.Scale(root, from_=0, to=220, orient="horizontal", style="TScale",
                    command=slider_changed2, variable=current_value2)
slider2.place(x=300, y=250)

# Entry Box

Height = StringVar()
Weight = StringVar()
height = Entry(root, textvariable=Height, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
height.place(x=35, y=160)
Height.set(get_current_value())

weight = Entry(root, textvariable=Weight, width=5, font="arial 50", bg="#fff", fg="#000", bd=0, justify=CENTER)
weight.place(x=255, y=160)
Weight.set(get_current_value2())

# Man Image
man_image = Label(root, bg="lightblue")
man_image.place(x=50, y=530)

# view Report Button

Button(root, text="View Report", width=15, height=2, font="aerial 10 bold",
       bg="#1f6e68", fg="white", command=BMI).place(x=280, y=340)

# Labels

label1 = Label(root, font="aerial 60 bold", bg="lightblue", fg="#fff")
label1.place(x=125, y=305)

label2 = Label(root, font="aerial 20 bold", bg="lightblue", fg="#3b3a3a")
label2.place(x=280, y=430)

label3 = Label(root, font="aerial 10 bold", bg="lightblue")
label3.place(x=190, y=500)

# Start the main event loop

root.mainloop()
