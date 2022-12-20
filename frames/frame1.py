import tkinter as tk
from PIL import ImageTk
import random
import csv

bg_colour = "#00A76D"

class Page1:

    def __init__(self, root=None):
        self.root = root
        root.title("Undecided? Choose yur recipe here!")
        self.frame = tk.Frame(root, width=100, height=100, bg=bg_colour)
        # create logo widget
        logo_img = ImageTk.PhotoImage(file="images/Page_2_logo.png")
        logo_widget = tk.Label(self.frame, image=logo_img, bg=bg_colour)
        logo_widget.image = logo_img
        logo_widget.pack()

        self.frame.grid(row=0, column=0, sticky="nesw")
        self.frame.pack()
        tk.Label(self.frame, text='What are we going to cook today?', bg=bg_colour, fg="white", font=("Shanti", 30)).pack(pady=30)

        tk.Button(self.frame, text="Let's begin!", font=("Ubuntu", 20), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2", activeforeground="black", command=self.make_page_2).pack(pady=30)
        self.page_2 = Page2(master=self.root, app=self)

    def main_page(self):
        self.frame.pack()

    def make_page_2(self):
        self.frame.pack_forget()
        self.page_2.start_page()

class Page2:
    def __init__(self, master=None, app=None):
        self.master = master
        self.app = app
        self.frame = tk.Frame(self.master, width=1000, height=1000, bg=bg_colour)


        tk.Label(self.frame, text='Here it is, enjoy!', bg=bg_colour, fg="white", font=("Shanti", 50)).pack(pady=30)

        tk.Button(self.frame, text='Go back', font=("Ubuntu", 20), bg="#28393a", fg="white", cursor="hand2", activebackground="#badee2", activeforeground="black", command=self.go_back).pack(pady=30)

        # create logo widget
        logo_img = ImageTk.PhotoImage(file="images/Recipe_logo.png")
        logo_widget = tk.Label(self.frame, image=logo_img, bg=bg_colour)
        logo_widget.image = logo_img
        logo_widget.pack()



    def start_page(self):
        self.frame.pack()

    def go_back(self):
        self.frame.pack_forget()
        self.app.main_page()

