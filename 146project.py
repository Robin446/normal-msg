from tkinter import *
root = Tk()

root.title("fibonacci")
root.geometry("3000x400")

enter_number = Entry(root)
enter_number.place(relx=0.5,rely=0.4,anchor=CENTER)

label_series = Label(root,text="fibonacci series")
label_flower = Label(root)
label_spiral = Label(root)

def fibonacci():
    num = int(enter_number.get())
    first_no = 0
    second_no = 1
    sum1 = 0
    counter = 1
    while(counter <= num):
        label_series["text"] += str(sum1) +" "
        counter = counter + 1
        first_no = second_no
        second_no = sum1
        sum1 = first_no + second_no
    label_flower["text"] = "Flower is fully bloomed"
    label_spiral["text"] = "Spirals in Right direction are : " + str(first_no) + "\n Spirals in left direction are : " + str(second_no) + "\n Total spiral are : "+ str(sum1)

btn = Button(root , text = "Show fibonacci series", command=fibonacci)

btn.pack()
label_series.pack()
label_flower.pack()
label_spiral.pack()

root.mainloop()