from tkinter import *
l=Tk()
l.title('factorial')
#to calculate factorial
def fact(a):
    x=1
    while a>0:
        x*=a
        a-=1
    return x
#to get number
number=Entry(l,fg='#3ca5bf',bg='#4e0d03',width=100,borderwidth=7)
number.grid(row=0,column=0)
number.insert(0,'enter the number=')


#function to do the calculation
def num(x):
    a=int(number.get())
    global text
    global button
    button=Button(l,text='click for calculating factorial!',padx=10,pady=10,fg='#1735ae',bg='#75aa24',command= lambda:num(x+1))
    button.grid(row=1,column=0)
    
    
    b=str(fact(a))
    if x==1:
        text=Label(l,text=b)
        text.grid(row=2,column=0)
    else:
        text.grid_forget()
        text=Label(l,text=b)
        text.grid(row=2,column=0)
        




#to enter button
button=Button(l,text='click for calculating factorial!',padx=10,pady=10,fg='#1735ae',bg='#75aa24',command= lambda:num(1))
button.grid(row=1,column=0)
l.mainloop()
