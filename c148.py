from tkinter import *
import random

root = Tk()
root.title("list")
root.geometry("400x400")

random_number_list = Label(root)
random_number_sorted_list = Label(root)

def randomlist():
    random_list = random.sample(range(1,50),7)
    random_number_list["text"] = "number list : " + str(random_list)
    random_list.sort()
    random_number_sorted_list["text"] = "sorted number list : " + str(random_list)
    
btn=Button(root,text="generate random list",command=randomlist)
btn.place(relx=0.5,rely=0.4,anchor=CENTER)

random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)


root.mainloop()