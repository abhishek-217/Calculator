# Import the tkinter Library of Python
from tkinter import *
root=Tk()

# Title of Interface
root.title("Calculator")
root.geometry("600x500")
e=Entry(root,width=20,font="lucida 20 bold")

e.grid(row=0,column=0,columnspan=10)

# Function for Click button
def Click(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, current + str(number))

# Function for Clear button
def Clear():
    e.delete(0, END)


# Function for Equal button
def Equal():
    try:
        result = str(eval(e.get()))
        e.delete(0, END)
        e.insert(0, result)
    except:
        e.delete(0, END)
        e.insert(0, "Error")

# Create_Buttons
button1=Button(root,text="1",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(1),font="lucida 15 bold")
button2=Button(root,text="2",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(2),font="lucida 15 bold")
button3=Button(root,text="3",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(3),font="lucida 15 bold")
button4=Button(root,text="4",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(4),font="lucida 15 bold")
button5=Button(root,text="5",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(5),font="lucida 15 bold")
button6=Button(root,text="6",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(6),font="lucida 15 bold")
button7=Button(root,text="7",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(7),font="lucida 15 bold")
button8=Button(root,text="8",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(8),font="lucida 15 bold")
button9=Button(root,text="9",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(9),font="lucida 15 bold")
button0=Button(root,text="0",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click(0),font="lucida 15 bold")
buttonadd=Button(root,text="+",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click("+"),font="lucida 15 bold")
buttonsub=Button(root,text="-",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click("-"),font="lucida 15 bold")
buttonmul=Button(root,text="*",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click("*"),font="lucida 15 bold")
buttondiv=Button(root,text="/",padx=20,pady=22,fg="blue", bg="grey", command=lambda: Click("/"),font="lucida 15 bold")
buttoneq=Button(root,text="=",padx=20,pady=22,fg="black", bg="grey", command=Equal,font="lucida 15 bold")
buttondot=Button(root,text=".",padx=20,pady=22,fg="black", bg="grey", command=lambda: Click("."),font="lucida 15 bold")
buttonclear=Button(root,text="Clear",padx=20,pady=22,fg="black", bg="grey", command=Clear,font="lucida 15 bold")

# Placed the buttons
button3.grid(row=3,column=0)
button2.grid(row=3,column=1)
button1.grid(row=3,column=2)
buttonadd.grid(row=3,column=3)

button6.grid(row=2,column=0)
button5.grid(row=2,column=1)
button4.grid(row=2,column=2)
buttonsub.grid(row=2,column=3)

button9.grid(row=1,column=0)
button8.grid(row=1,column=1)
button7.grid(row=1,column=2)
buttonmul.grid(row=1,column=3,padx=10)

button0.grid(row=4,column=0)
buttoneq.grid(row=4,column=1)
buttondot.grid(row=4,column=2)
buttonclear.grid(row=4,column=3)

root.mainloop()