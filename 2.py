from  tkinter import*
from datetime import date
root =Tk()
root.title("getting started ")
root.geometry("400x300")
lb1=Label(text="Hey there", fg= "white",bg="black",height=1,width=300)
namelbl=Label(text="Full Name",bg ="#3895D3")
nameentry=Entry()
def display():
    name=nameentry.get()
    global Message
    Message="welcome to the application"
    greet= "hello""+name+""\n"
    textBox.insert(END,greet)
    textBox.insert(END,Message)
    textBox.insert(END,date.today())
textBox=Text(height=3)
btn =Button(text="Beign",command=display,height=1,bg="black",fg="white")
lb1.pack()
namelbl.pack()
nameentry.pack()
btn.pack()
textBox.pack()
root.mainloop()
