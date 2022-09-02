from tkinter import *
import random

root = Tk()

root.title("lucky friend")
root.geometry("500x500")

listname = ["Bishal" , "Atharv" , "Varun" , "Sreyas v" , "Abhay"]
print(listname)

def random_number():
    random_no = random.randint(0 , 4)
    print(random_no)
    random_friend = listname[random_no]
    print("Your lucky friend is: " + random_friend)
    
    
btn1 = Button(root, text="lucky friend",command = random_number)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
