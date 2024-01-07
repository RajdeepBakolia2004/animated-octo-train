from tkinter import *
file=Tk()
file.title('test')

#to resize the screen
file.geometry('600x790')


#to make frame
q1=LabelFrame(file,padx=58,pady=5,bd=5)
q1.grid(row=0,column=0,pady=1)
q2=LabelFrame(file,padx=62,pady=5,bd=5)
q2.grid(row=1,column=0,pady=1)
q3=LabelFrame(file,padx=15,pady=5,bd=5)
q3.grid(row=2,column=0,pady=1)
q4=LabelFrame(file,padx=65,pady=5,bd=5)
q4.grid(row=3,column=0,pady=1)
q5=LabelFrame(file,padx=5,pady=5,bd=5)
q5.grid(row=4,column=0,pady=1)
q6=LabelFrame(file,padx=5,pady=5,bd=5)
q6.grid(row=5,column=0,pady=1)
q7=LabelFrame(file,padx=97,pady=5,bd=5)
q7.grid(row=6,column=0,pady=1)
q8=LabelFrame(file,padx=79,pady=5,bd=5)
q8.grid(row=7,column=0,pady=1)
q9=LabelFrame(file,padx=34,pady=5,bd=5)
q9.grid(row=8,column=0,pady=1)
q0=LabelFrame(file,padx=60,pady=5,bd=5)
q0.grid(row=9,column=0,pady=1)



#values
val1=0
val2=0
val3=0
val4=0
val5=0
val6=0
val7=0
val8=0
val9=0
val10=0


#q1
R1=Entry(q1,width=50,bg='#e2ed2c',fg='#0d0504')
R1.insert(0,'what is the speed of light in m/s?')
R1.grid(row=0,column=0,columnspan=4)

def ans1(x):
    global val1
    if x==0:
        val1=1
        R1=Entry(q1,width=50,bg='#09f430',fg='#0d0504')
        R1.insert(0,'what is the speed of light in m/s?')
        R1.grid(row=0,column=0,columnspan=4)
        oR1=Radiobutton(q1,text='299792458',variable=ov1,value=0,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR1.grid(row=1,column=0)
        oR2=Radiobutton(q1,text='375745777',variable=ov1,value=1,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR2.grid(row=1,column=1)
        oR3=Radiobutton(q1,text='12356789 ',variable=ov1,value=2,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR3.grid(row=1,column=2)
        oR4=Radiobutton(q1,text='30000000',variable=ov1,value=3,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR4.grid(row=1,column=3)
    else:
        R1=Entry(q1,width=50,bg='#e10326',fg='#0d0504')
        R1.insert(0,'what is the speed of light in m/s?')
        R1.grid(row=0,column=0,columnspan=4)
        oR1=Radiobutton(q1,text='299792458',variable=ov1,value=0,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR1.grid(row=1,column=0)
        oR2=Radiobutton(q1,text='375745777',variable=ov1,value=1,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR2.grid(row=1,column=1)
        oR3=Radiobutton(q1,text='12356789 ',variable=ov1,value=2,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR3.grid(row=1,column=2)
        oR4=Radiobutton(q1,text='30000000',variable=ov1,value=3,command=lambda:ans1(ov1.get()),state=DISABLED)
        oR4.grid(row=1,column=3)

ov1=IntVar()
ov1.set(9)
oR1=Radiobutton(q1,text='299792458',variable=ov1,value=0,command=lambda:ans1(ov1.get()))
oR1.grid(row=1,column=0)
oR2=Radiobutton(q1,text='375745777',variable=ov1,value=1,command=lambda:ans1(ov1.get()))
oR2.grid(row=1,column=1)
oR3=Radiobutton(q1,text='12356789 ',variable=ov1,value=2,command=lambda:ans1(ov1.get()))
oR3.grid(row=1,column=2)
oR4=Radiobutton(q1,text='30000000',variable=ov1,value=3,command=lambda:ans1(ov1.get()))
oR4.grid(row=1,column=3)


#q2
R2=Entry(q2,width=50,bg='#e2ed2c',fg='#0d0504')
R2.insert(0,'What is nucleus made of?')
R2.grid(row=0,column=0,columnspan=4)

def ans2(x):
    if x==0:
        global val2
        val2=1
        R2=Entry(q2,width=50,bg='#09f430',fg='#0d0504')
        R2.insert(0,'What is nucleus made of?')
        R2.grid(row=0,column=0,columnspan=4)
        oR5=Radiobutton(q2,text='Electron',variable=ov2,value=3,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR5.grid(row=1,column=0)
        oR6=Radiobutton(q2,text='Protons ',variable=ov2,value=1,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR6.grid(row=1,column=1)
        oR7=Radiobutton(q2,text='Neutrons',variable=ov2,value=2,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR7.grid(row=1,column=2)
        oR8=Radiobutton(q2,text='Both b and c',variable=ov2,value=0,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR8.grid(row=1,column=3)
    else:
        R2=Entry(q2,width=50,bg='#e10326',fg='#0d0504')
        R2.insert(0,'What is nucleus made of?')
        R2.grid(row=0,column=0,columnspan=4)
        oR5=Radiobutton(q2,text='Electron',variable=ov2,value=3,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR5.grid(row=1,column=0)
        oR6=Radiobutton(q2,text='Protons ',variable=ov2,value=1,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR6.grid(row=1,column=1)
        oR7=Radiobutton(q2,text='Neutrons',variable=ov2,value=2,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR7.grid(row=1,column=2)
        oR8=Radiobutton(q2,text='Both b and c',variable=ov2,value=0,command=lambda:ans2(ov2.get()),state=DISABLED)
        oR8.grid(row=1,column=3)

ov2=IntVar()
ov2.set(9)
oR5=Radiobutton(q2,text='Electron',variable=ov2,value=3,command=lambda:ans2(ov2.get()))
oR5.grid(row=1,column=0)
oR6=Radiobutton(q2,text='Protons ',variable=ov2,value=1,command=lambda:ans2(ov2.get()))
oR6.grid(row=1,column=1)
oR7=Radiobutton(q2,text='Neutron',variable=ov2,value=2,command=lambda:ans2(ov2.get()))
oR7.grid(row=1,column=2)
oR8=Radiobutton(q2,text='Both b and c',variable=ov2,value=0,command=lambda:ans2(ov2.get()))
oR8.grid(row=1,column=3)


#q3
R3=Entry(q3,width=50,bg='#e2ed2c',fg='#0d0504')
R3.insert(0,'Who created python?')
R3.grid(row=0,column=0,columnspan=4)

def ans3(x):
    if x==0:
        global val3
        val3=1
        R3=Entry(q3,width=50,bg='#09f430',fg='#0d0504')
        R3.insert(0,'Who created python?')
        R3.grid(row=0,column=0,columnspan=4)
        oR9=Radiobutton(q3,text='Charles Babage',variable=ov3,value=1,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR9.grid(row=1,column=0)
        oR10=Radiobutton(q3,text='Guido van roussum',variable=ov3,value=0,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR10.grid(row=1,column=1)
        oR11=Radiobutton(q3,text='Alan turing',variable=ov3,value=2,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR11.grid(row=1,column=2)
        oR11=Radiobutton(q3,text='jack finey',variable=ov3,value=3,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR11.grid(row=1,column=3)
    else:
        R3=Entry(q3,width=50,bg='#e10326',fg='#0d0504')
        R3.insert(0,'Who created python?')
        R3.grid(row=0,column=0,columnspan=4)
        oR9=Radiobutton(q3,text='Charles Babage',variable=ov3,value=1,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR9.grid(row=1,column=0)
        oR10=Radiobutton(q3,text='Guido van roussum',variable=ov3,value=0,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR10.grid(row=1,column=1)
        oR11=Radiobutton(q3,text='Alan turing',variable=ov3,value=2,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR11.grid(row=1,column=2)
        oR12=Radiobutton(q3,text='jack finey',variable=ov3,value=3,command=lambda:ans3(ov3.get()),state=DISABLED)
        oR12.grid(row=1,column=3)

ov3=IntVar()
ov3.set(9)
oR9=Radiobutton(q3,text='Charles Babage',variable=ov3,value=1,command=lambda:ans3(ov3.get()))
oR9.grid(row=1,column=0)
oR10=Radiobutton(q3,text='Guido van roussum',variable=ov3,value=0,command=lambda:ans3(ov3.get()))
oR10.grid(row=1,column=1)
oR11=Radiobutton(q3,text='Alan turing',variable=ov3,value=2,command=lambda:ans3(ov3.get()))
oR11.grid(row=1,column=2)
oR12=Radiobutton(q3,text='jack finey',variable=ov3,value=3,command=lambda:ans3(ov3.get()))
oR12.grid(row=1,column=3)


#q4
R4=Entry(q4,width=50,bg='#e2ed2c',fg='#0d0504')
R4.insert(0,'The sum of unit digit of -1!,2!,3!...100! is-')
R4.grid(row=0,column=0,columnspan=4)

def ans4(x):
    if x==0:
        global val4
        val4=1
        R4=Entry(q4,width=50,bg='#09f430',fg='#0d0504')
        R4.insert(0,'The sum of unit digit of -1!,2!,3!...100! is-')
        R4.grid(row=0,column=0,columnspan=4)
        oR12=Radiobutton(q4,text='not defined',variable=ov4,value=1,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR12.grid(row=1,column=0)
        oR13=Radiobutton(q4,text='13',variable=ov4,value=0,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR13.grid(row=1,column=1)
        oR15=Radiobutton(q4,text='10',variable=ov4,value=2,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR15.grid(row=1,column=2)
        oR16=Radiobutton(q4,text='10008',variable=ov4,value=3,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR16.grid(row=1,column=3)
    else:
        R4=Entry(q4,width=50,bg='#e10326',fg='#0d0504')
        R4.insert(0,'The sum of unit digit of -1!,2!,3!...100! is-')
        R4.grid(row=0,column=0,columnspan=4)
        oR12=Radiobutton(q4,text='not defined',variable=ov4,value=1,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR12.grid(row=1,column=0)
        oR13=Radiobutton(q4,text='13',variable=ov4,value=0,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR13.grid(row=1,column=1)
        oR15=Radiobutton(q4,text='10',variable=ov4,value=2,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR15.grid(row=1,column=2)
        oR16=Radiobutton(q4,text='10008',variable=ov4,value=3,command=lambda:ans4(ov4.get()),state=DISABLED)
        oR16.grid(row=1,column=3)

ov4=IntVar()
ov4.set(9)
oR12=Radiobutton(q4,text='not defined',variable=ov4,value=1,command=lambda:ans4(ov4.get()))
oR12.grid(row=1,column=0)
oR13=Radiobutton(q4,text='13',variable=ov4,value=0,command=lambda:ans4(ov4.get()))
oR13.grid(row=1,column=1)
oR15=Radiobutton(q4,text='10',variable=ov4,value=2,command=lambda:ans4(ov4.get()))
oR15.grid(row=1,column=2)
oR16=Radiobutton(q4,text='10008',variable=ov4,value=3,command=lambda:ans4(ov4.get()))
oR16.grid(row=1,column=3)


#q5
R5=Entry(q5,width=70,bg='#e2ed2c',fg='#0d0504')
R5.insert(0,'Which one of the following is more elastic steel or rubber?')
R5.grid(row=0,column=0,columnspan=4)

def ans5(x):
    if x==0:
        global val5
        val5=1
        R5=Entry(q5,width=70,bg='#09f430',fg='#0d0504')
        R5.insert(0,'Which one of the following is more elastic steel or rubber?')
        R5.grid(row=0,column=0,columnspan=4)
        oR17=Radiobutton(q5,text='Rubber',variable=ov5,value=1,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR17.grid(row=1,column=0)
        oR18=Radiobutton(q5,text='Both are equally elastic ',variable=ov5,value=2,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR18.grid(row=1,column=1)
        oR19=Radiobutton(q5,text='Steel',variable=ov5,value=0,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR19.grid(row=1,column=2)
        oR20=Radiobutton(q5,text='Can’t be measured',variable=ov5,value=3,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR20.grid(row=1,column=3)
    else:
        R5=Entry(q5,width=70,bg='#e10326',fg='#0d0504')
        R5.insert(0,'Which one of the following is more elastic steel or rubber?')
        R5.grid(row=0,column=0,columnspan=4)
        oR17=Radiobutton(q5,text='Rubber',variable=ov5,value=1,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR17.grid(row=1,column=0)
        oR18=Radiobutton(q5,text='Both are equally elastic ',variable=ov5,value=2,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR18.grid(row=1,column=1)
        oR19=Radiobutton(q5,text='Steel',variable=ov5,value=0,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR19.grid(row=1,column=2)
        oR20=Radiobutton(q5,text='Can’t be measured',variable=ov5,value=3,command=lambda:ans5(ov5.get()),state=DISABLED)
        oR20.grid(row=1,column=3)

ov5=IntVar()
ov5.set(9)
oR17=Radiobutton(q5,text='Rubber',variable=ov5,value=1,command=lambda:ans5(ov5.get()))
oR17.grid(row=1,column=0)
oR18=Radiobutton(q5,text='Both are equally elastic ',variable=ov5,value=2,command=lambda:ans5(ov5.get()))
oR18.grid(row=1,column=1)
oR19=Radiobutton(q5,text='Steel',variable=ov5,value=0,command=lambda:ans5(ov5.get()))
oR19.grid(row=1,column=2)
oR20=Radiobutton(q5,text='Can’t be measured',variable=ov5,value=3,command=lambda:ans5(ov5.get()))
oR20.grid(row=1,column=3)
        

#Q1
l1=Label(q6,text='Function for printing some text on screen in python programming language is-')
l1.grid(row=0,column=0,columnspan=2)

def wer1():
    global a1
    x=a1.get()
    if x=='print()':
        global val6
        val6=1
        b1=Button(q6,text='press to record',bg='#0a0da8',bd=5,command=wer1,state=DISABLED)
        b1.grid(row=1,column=1)
        a1=Entry(q6,bg='#09f430',fg='#0d0504')
        a1.insert(0,x)
        a1.grid(row=1,column=0)
    else:
        b1=Button(q6,text='press to record',bg='#0a0da8',bd=5,command=wer1,state=DISABLED)
        b1.grid(row=1,column=1)
        a1=Entry(q6,bg='#e10326',fg='#0d0504')
        a1.insert(0,x)
        a1.grid(row=1,column=0)

a1=Entry(q6,bg='#e2ed2c',fg='#0d0504')
a1.grid(row=1,column=0)

b1=Button(q6,text='press to record',bg='#0a0da8',bd=5,command=wer1)
b1.grid(row=1,column=1)


#Q2
l2=Label(q7,text='Sodium belongs to which group and period-')
l2.grid(row=0,column=0,columnspan=2)

def wer2():
    global a2
    x=a2.get()
    if x=='Group=1 Period=3':
        global val7
        val7=1
        b2=Button(q7,text='press to record',bg='#0a0da8',bd=5,command=wer2,state=DISABLED)
        b2.grid(row=1,column=1)
        a2=Entry(q7,bg='#09f430',fg='#0d0504')
        a2.insert(0,x)
        a2.grid(row=1,column=0)
    else:
        b2=Button(q7,text='press to record',bg='#0a0da8',bd=5,command=wer2,state=DISABLED)
        b2.grid(row=1,column=1)
        a2=Entry(q7,bg='#e10326',fg='#0d0504')
        a2.insert(0,x)
        a2.grid(row=1,column=0)

a2=Entry(q7,bg='#e2ed2c',fg='#0d0504')
a2.insert(0,'Group= Period=')
a2.grid(row=1,column=0)

b2=Button(q7,text='press to record',bg='#0a0da8',bd=5,command=wer2)
b2.grid(row=1,column=1)


#Q3
l3=Label(q8,text='What is the derivative of 6x+6x^2 with respect to x-')
l3.grid(row=0,column=0,columnspan=2)

def wer3():
    global a3
    x=a3.get()
    temp=x
    x=x.split('+')
    if '6' in x and '12x' in x and len(x)==2:
        global val8
        val8=1
        b3=Button(q8,text='press to record',bg='#0a0da8',bd=5,command=wer3,state=DISABLED)
        b3.grid(row=1,column=1)
        a3=Entry(q8,bg='#09f430',fg='#0d0504')
        a3.insert(0,temp)
        a3.grid(row=1,column=0)
    else:
        b3=Button(q8,text='press to record',bg='#0a0da8',bd=5,command=wer3,state=DISABLED)
        b3.grid(row=1,column=1)
        a3=Entry(q8,bg='#e10326',fg='#0d0504')
        a3.insert(0,temp)
        a3.grid(row=1,column=0)

a3=Entry(q8,bg='#e2ed2c',fg='#0d0504')
a3.grid(row=1,column=0)

b3=Button(q8,text='press to record',bg='#0a0da8',bd=5,command=wer3)
b3.grid(row=1,column=1)


#Q4
l4=Label(q9,text='What is the weight of an object of mass m at the centre of the earth-')
l4.grid(row=0,column=0,columnspan=2)

def wer4():
    global a4
    x=a4.get()
    if x=='0':
        global val9
        val9=1
        b4=Button(q9,text='press to record',bg='#0a0da8',bd=5,command=wer4,state=DISABLED)
        b4.grid(row=1,column=1)
        a4=Entry(q9,bg='#09f430',fg='#0d0504')
        a4.insert(0,x)
        a4.grid(row=1,column=0)
    else:
        b4=Button(q9,text='press to record',bg='#0a0da8',bd=5,command=wer4,state=DISABLED)
        b4.grid(row=1,column=1)
        a4=Entry(q9,bg='#e10326',fg='#0d0504')
        a4.insert(0,x)
        a4.grid(row=1,column=0)

a4=Entry(q9,bg='#e2ed2c',fg='#0d0504')
a4.grid(row=1,column=0)

b4=Button(q9,text='press to record',bg='#0a0da8',bd=5,command=wer4)
b4.grid(row=1,column=1)


#Q5
l5=Label(q0,text='Is total mechanical energy of an system always conserved-')
l5.grid(row=0,column=0,columnspan=2)

def answer(x):
    if x==1:
        global val10
        val10=1
        opt1=Button(q0,text='True',bg='#09f430',fg='#0d0504',command=lambda:answer(1),state=DISABLED)
        opt1.grid(row=1,column=0)
        opt2=Button(q0,text='False',bg='#09f430',fg='#0d0504',command=lambda:answer(0),state=DISABLED)
        opt2.grid(row=1,column=1)
    else:
        opt1=Button(q0,text='True',bg='#e10326',fg='#0d0504',command=lambda:answer(1),state=DISABLED)
        opt1.grid(row=1,column=0)
        opt2=Button(q0,text='False',bg='#e10326',fg='#0d0504',command=lambda:answer(0),state=DISABLED)
        opt2.grid(row=1,column=1)

opt1=Button(q0,text='True',bg='#e2ed2c',fg='#0d0504',command=lambda:answer(0))
opt1.grid(row=1,column=0)
opt2=Button(q0,text='False',bg='#e2ed2c',fg='#0d0504',command=lambda:answer(1))
opt2.grid(row=1,column=1)


#scorecard
score=0
def scor():
    global score
    if val1==1:
        score+=1
    if val2==1:
        score+=1
    if val3==1:
        score+=1
    if val4==1:
        score+=1
    if val5==1:
        score+=1
    if val6==1:
        score+=1
    if val7==1:
        score+=1
    if val8==1:
        score+=1
    if val9==1:
        score+=1
    if val10==1:
        score+=1
    but.grid_forget()
    label=Label(file,text='you scored '+str(score)+' out of 10.',anchor=W)
    label.grid(row=10,column=0,pady=4)
    
but=Button(file,text="click to calculate score",command=scor)
but.grid(row=10,column=0,pady=4)


#reset button
def ref():
    global q1
    global q2
    global q3
    global q4
    global q5
    global q6
    global q7
    global q8
    global q9
    global q0
    global file
    for wid in q1.winfo_children():
        wid.destroy()
    for wid in q2.winfo_children():
        wid.destroy()
    for wid in q3.winfo_children():
        wid.destroy()
    for wid in q4.winfo_children():
        wid.destroy()
    for wid in q5.winfo_children():
        wid.destroy()
    for wid in q6.winfo_children():
        wid.destroy()
    for wid in q7.winfo_children():
        wid.destroy()
    for wid in q8.winfo_children():
        wid.destroy()
    for wid in q9.winfo_children():
        wid.destroy()
    for wid in q0.winfo_children():
        wid.destroy()
    for wid in file.winfo_children():
        wid.destroy()
    q1=LabelFrame(file,padx=58,pady=5,bd=5)
    q1.grid(row=0,column=0,pady=1)
    q2=LabelFrame(file,padx=62,pady=5,bd=5)
    q2.grid(row=1,column=0,pady=1)
    q3=LabelFrame(file,padx=15,pady=5,bd=5)
    q3.grid(row=2,column=0,pady=1)
    q4=LabelFrame(file,padx=65,pady=5,bd=5)
    q4.grid(row=3,column=0,pady=1)
    q5=LabelFrame(file,padx=5,pady=5,bd=5)
    q5.grid(row=4,column=0,pady=1)
    q6=LabelFrame(file,padx=5,pady=5,bd=5)
    q6.grid(row=5,column=0,pady=1)
    q7=LabelFrame(file,padx=97,pady=5,bd=5)
    q7.grid(row=6,column=0,pady=1)
    q8=LabelFrame(file,padx=79,pady=5,bd=5)
    q8.grid(row=7,column=0,pady=1)
    q9=LabelFrame(file,padx=34,pady=5,bd=5)
    q9.grid(row=8,column=0,pady=1)
    q0=LabelFrame(file,padx=60,pady=5,bd=5)
    q0.grid(row=9,column=0,pady=1)
    global val1
    global val2
    global val3
    global val4
    global val5
    global val6
    global val7
    global val8
    global val9
    global val10
    val1=0
    val2=0
    val3=0
    val4=0
    val5=0
    val6=0
    val7=0
    val8=0
    val9=0
    val10=0
    global R1
    R1=Entry(q1,width=50,bg='#e2ed2c',fg='#0d0504')
    R1.insert(0,'what is the speed of light in m/s?')
    R1.grid(row=0,column=0,columnspan=4)
    def ans1(x):
        global val1
        if x==0:
            val1=1
            R1=Entry(q1,width=50,bg='#09f430',fg='#0d0504')
            R1.insert(0,'what is the speed of light in m/s?')
            R1.grid(row=0,column=0,columnspan=4)
            oR1=Radiobutton(q1,text='299792458',variable=ov1,value=0,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR1.grid(row=1,column=0)
            oR2=Radiobutton(q1,text='375745777',variable=ov1,value=1,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR2.grid(row=1,column=1)
            oR3=Radiobutton(q1,text='12356789 ',variable=ov1,value=2,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR3.grid(row=1,column=2)
            oR4=Radiobutton(q1,text='30000000',variable=ov1,value=3,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR4.grid(row=1,column=3)
        else:
            R1=Entry(q1,width=50,bg='#e10326',fg='#0d0504')
            R1.insert(0,'what is the speed of light in m/s?')
            R1.grid(row=0,column=0,columnspan=4)
            oR1=Radiobutton(q1,text='299792458',variable=ov1,value=0,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR1.grid(row=1,column=0)
            oR2=Radiobutton(q1,text='375745777',variable=ov1,value=1,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR2.grid(row=1,column=1)
            oR3=Radiobutton(q1,text='12356789 ',variable=ov1,value=2,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR3.grid(row=1,column=2)
            oR4=Radiobutton(q1,text='30000000',variable=ov1,value=3,command=lambda:ans1(ov1.get()),state=DISABLED)
            oR4.grid(row=1,column=3)
    ov1=IntVar()
    ov1.set(9)
    oR1=Radiobutton(q1,text='299792458',variable=ov1,value=0,command=lambda:ans1(ov1.get()))
    oR1.grid(row=1,column=0)
    oR2=Radiobutton(q1,text='375745777',variable=ov1,value=1,command=lambda:ans1(ov1.get()))
    oR2.grid(row=1,column=1)
    oR3=Radiobutton(q1,text='12356789 ',variable=ov1,value=2,command=lambda:ans1(ov1.get()))
    oR3.grid(row=1,column=2)
    oR4=Radiobutton(q1,text='30000000',variable=ov1,value=3,command=lambda:ans1(ov1.get()))
    oR4.grid(row=1,column=3)
    R2=Entry(q2,width=50,bg='#e2ed2c',fg='#0d0504')
    R2.insert(0,'What is nucleus made of?')
    R2.grid(row=0,column=0,columnspan=4)
    def ans2(x):
        if x==0:
            global val2
            val2=1
            R2=Entry(q2,width=50,bg='#09f430',fg='#0d0504')
            R2.insert(0,'What is nucleus made of?')
            R2.grid(row=0,column=0,columnspan=4)
            oR5=Radiobutton(q2,text='Electron',variable=ov2,value=3,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR5.grid(row=1,column=0)
            oR6=Radiobutton(q2,text='Protons ',variable=ov2,value=1,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR6.grid(row=1,column=1)
            oR7=Radiobutton(q2,text='Neutrons',variable=ov2,value=2,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR7.grid(row=1,column=2)
            oR8=Radiobutton(q2,text='Both b and c',variable=ov2,value=0,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR8.grid(row=1,column=3)
        else:
            R2=Entry(q2,width=50,bg='#e10326',fg='#0d0504')
            R2.insert(0,'What is nucleus made of?')
            R2.grid(row=0,column=0,columnspan=4)
            oR5=Radiobutton(q2,text='Electron',variable=ov2,value=3,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR5.grid(row=1,column=0)
            oR6=Radiobutton(q2,text='Protons ',variable=ov2,value=1,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR6.grid(row=1,column=1)
            oR7=Radiobutton(q2,text='Neutrons',variable=ov2,value=2,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR7.grid(row=1,column=2)
            oR8=Radiobutton(q2,text='Both b and c',variable=ov2,value=0,command=lambda:ans2(ov2.get()),state=DISABLED)
            oR8.grid(row=1,column=3)
    ov2=IntVar()
    ov2.set(9)
    oR5=Radiobutton(q2,text='Electron',variable=ov2,value=3,command=lambda:ans2(ov2.get()))
    oR5.grid(row=1,column=0)
    oR6=Radiobutton(q2,text='Protons ',variable=ov2,value=1,command=lambda:ans2(ov2.get()))
    oR6.grid(row=1,column=1)
    oR7=Radiobutton(q2,text='Neutron',variable=ov2,value=2,command=lambda:ans2(ov2.get()))
    oR7.grid(row=1,column=2)
    oR8=Radiobutton(q2,text='Both b and c',variable=ov2,value=0,command=lambda:ans2(ov2.get()))
    oR8.grid(row=1,column=3)
    R3=Entry(q3,width=50,bg='#e2ed2c',fg='#0d0504')
    R3.insert(0,'Who created python?')
    R3.grid(row=0,column=0,columnspan=4)
    def ans3(x):
        if x==0:
            global val3
            val3=1
            R3=Entry(q3,width=50,bg='#09f430',fg='#0d0504')
            R3.insert(0,'Who created python?')
            R3.grid(row=0,column=0,columnspan=4)
            oR9=Radiobutton(q3,text='Charles Babage',variable=ov3,value=1,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR9.grid(row=1,column=0)
            oR10=Radiobutton(q3,text='Guido van roussum',variable=ov3,value=0,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR10.grid(row=1,column=1)
            oR11=Radiobutton(q3,text='Alan turing',variable=ov3,value=2,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR11.grid(row=1,column=2)
            oR11=Radiobutton(q3,text='jack finey',variable=ov3,value=3,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR11.grid(row=1,column=3)
        else:
            R3=Entry(q3,width=50,bg='#e10326',fg='#0d0504')
            R3.insert(0,'Who created python?')
            R3.grid(row=0,column=0,columnspan=4)
            oR9=Radiobutton(q3,text='Charles Babage',variable=ov3,value=1,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR9.grid(row=1,column=0)
            oR10=Radiobutton(q3,text='Guido van roussum',variable=ov3,value=0,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR10.grid(row=1,column=1)
            oR11=Radiobutton(q3,text='Alan turing',variable=ov3,value=2,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR11.grid(row=1,column=2)
            oR12=Radiobutton(q3,text='jack finey',variable=ov3,value=3,command=lambda:ans3(ov3.get()),state=DISABLED)
            oR12.grid(row=1,column=3)
    ov3=IntVar()
    ov3.set(9)
    oR9=Radiobutton(q3,text='Charles Babage',variable=ov3,value=1,command=lambda:ans3(ov3.get()))
    oR9.grid(row=1,column=0)
    oR10=Radiobutton(q3,text='Guido van roussum',variable=ov3,value=0,command=lambda:ans3(ov3.get()))
    oR10.grid(row=1,column=1)
    oR11=Radiobutton(q3,text='Alan turing',variable=ov3,value=2,command=lambda:ans3(ov3.get()))
    oR11.grid(row=1,column=2)
    oR12=Radiobutton(q3,text='jack finey',variable=ov3,value=3,command=lambda:ans3(ov3.get()))
    oR12.grid(row=1,column=3)
    R4=Entry(q4,width=50,bg='#e2ed2c',fg='#0d0504')
    R4.insert(0,'The sum of unit digit of -1!,2!,3!...100! is-')
    R4.grid(row=0,column=0,columnspan=4)
    def ans4(x):
        if x==0:
            global val4
            val4=1
            R4=Entry(q4,width=50,bg='#09f430',fg='#0d0504')
            R4.insert(0,'The sum of unit digit of -1!,2!,3!...100! is-')
            R4.grid(row=0,column=0,columnspan=4)
            oR12=Radiobutton(q4,text='not defined',variable=ov4,value=1,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR12.grid(row=1,column=0)
            oR13=Radiobutton(q4,text='13',variable=ov4,value=0,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR13.grid(row=1,column=1)
            oR15=Radiobutton(q4,text='10',variable=ov4,value=2,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR15.grid(row=1,column=2)
            oR16=Radiobutton(q4,text='10008',variable=ov4,value=3,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR16.grid(row=1,column=3)
        else:
            R4=Entry(q4,width=50,bg='#e10326',fg='#0d0504')
            R4.insert(0,'The sum of unit digit of -1!,2!,3!...100! is-')
            R4.grid(row=0,column=0,columnspan=4)
            oR12=Radiobutton(q4,text='not defined',variable=ov4,value=1,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR12.grid(row=1,column=0)
            oR13=Radiobutton(q4,text='13',variable=ov4,value=0,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR13.grid(row=1,column=1)
            oR15=Radiobutton(q4,text='10',variable=ov4,value=2,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR15.grid(row=1,column=2)
            oR16=Radiobutton(q4,text='10008',variable=ov4,value=3,command=lambda:ans4(ov4.get()),state=DISABLED)
            oR16.grid(row=1,column=3)
    ov4=IntVar()
    ov4.set(9)
    oR12=Radiobutton(q4,text='not defined',variable=ov4,value=1,command=lambda:ans4(ov4.get()))
    oR12.grid(row=1,column=0)
    oR13=Radiobutton(q4,text='13',variable=ov4,value=0,command=lambda:ans4(ov4.get()))
    oR13.grid(row=1,column=1)
    oR15=Radiobutton(q4,text='10',variable=ov4,value=2,command=lambda:ans4(ov4.get()))
    oR15.grid(row=1,column=2)
    oR16=Radiobutton(q4,text='10008',variable=ov4,value=3,command=lambda:ans4(ov4.get()))
    oR16.grid(row=1,column=3)
    R5=Entry(q5,width=70,bg='#e2ed2c',fg='#0d0504')
    R5.insert(0,'Which one of the following is more elastic steel or rubber?')
    R5.grid(row=0,column=0,columnspan=4)
    def ans5(x):
        if x==0:
            global val5
            val5=1
            R5=Entry(q5,width=70,bg='#09f430',fg='#0d0504')
            R5.insert(0,'Which one of the following is more elastic steel or rubber?')
            R5.grid(row=0,column=0,columnspan=4)
            oR17=Radiobutton(q5,text='Rubber',variable=ov5,value=1,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR17.grid(row=1,column=0)
            oR18=Radiobutton(q5,text='Both are equally elastic ',variable=ov5,value=2,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR18.grid(row=1,column=1)
            oR19=Radiobutton(q5,text='Steel',variable=ov5,value=0,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR19.grid(row=1,column=2)
            oR20=Radiobutton(q5,text='Can’t be measured',variable=ov5,value=3,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR20.grid(row=1,column=3)
        else:
            R5=Entry(q5,width=70,bg='#e10326',fg='#0d0504')
            R5.insert(0,'Which one of the following is more elastic steel or rubber?')
            R5.grid(row=0,column=0,columnspan=4)
            oR17=Radiobutton(q5,text='Rubber',variable=ov5,value=1,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR17.grid(row=1,column=0)
            oR18=Radiobutton(q5,text='Both are equally elastic ',variable=ov5,value=2,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR18.grid(row=1,column=1)
            oR19=Radiobutton(q5,text='Steel',variable=ov5,value=0,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR19.grid(row=1,column=2)
            oR20=Radiobutton(q5,text='Can’t be measured',variable=ov5,value=3,command=lambda:ans5(ov5.get()),state=DISABLED)
            oR20.grid(row=1,column=3)
    ov5=IntVar()
    ov5.set(9)
    oR17=Radiobutton(q5,text='Rubber',variable=ov5,value=1,command=lambda:ans5(ov5.get()))
    oR17.grid(row=1,column=0)
    oR18=Radiobutton(q5,text='Both are equally elastic ',variable=ov5,value=2,command=lambda:ans5(ov5.get()))
    oR18.grid(row=1,column=1)
    oR19=Radiobutton(q5,text='Steel',variable=ov5,value=0,command=lambda:ans5(ov5.get()))
    oR19.grid(row=1,column=2)
    oR20=Radiobutton(q5,text='Can’t be measured',variable=ov5,value=3,command=lambda:ans5(ov5.get()))
    oR20.grid(row=1,column=3)
    l1=Label(q6,text='Function for printing some text on screen in python programming language is-')
    l1.grid(row=0,column=0,columnspan=2)
    def wer1():
        global a1
        x=a1.get()
        if x=='print()':
            global val6
            val6=1
            b1=Button(q6,text='press to record',bg='#0a0da8',bd=5,command=wer1,state=DISABLED)
            b1.grid(row=1,column=1)
            a1=Entry(q6,bg='#09f430',fg='#0d0504')
            a1.insert(0,x)
            a1.grid(row=1,column=0)
        else:
            b1=Button(q6,text='press to record',bg='#0a0da8',bd=5,command=wer1,state=DISABLED)
            b1.grid(row=1,column=1)
            a1=Entry(q6,bg='#e10326',fg='#0d0504')
            a1.insert(0,x)
            a1.grid(row=1,column=0)
    global a1
    a1=Entry(q6,bg='#e2ed2c',fg='#0d0504')
    a1.grid(row=1,column=0)
    b1=Button(q6,text='press to record',bg='#0a0da8',bd=5,command=wer1)
    b1.grid(row=1,column=1)
    l2=Label(q7,text='Sodium belongs to which group and period-')
    l2.grid(row=0,column=0,columnspan=2)
    def wer2():
        global a2
        x=a2.get()
        if x=='Group=1 Period=3':
            global val7
            val7=1
            b2=Button(q7,text='press to record',bg='#0a0da8',bd=5,command=wer2,state=DISABLED)
            b2.grid(row=1,column=1)
            a2=Entry(q7,bg='#09f430',fg='#0d0504')
            a2.insert(0,x)
            a2.grid(row=1,column=0)
        else:
            b2=Button(q7,text='press to record',bg='#0a0da8',bd=5,command=wer2,state=DISABLED)
            b2.grid(row=1,column=1)
            a2=Entry(q7,bg='#e10326',fg='#0d0504')
            a2.insert(0,x)
            a2.grid(row=1,column=0)
    global a2
    a2=Entry(q7,bg='#e2ed2c',fg='#0d0504')
    a2.insert(0,'Group= Period=')
    a2.grid(row=1,column=0)
    b2=Button(q7,text='press to record',bg='#0a0da8',bd=5,command=wer2)
    b2.grid(row=1,column=1)
    l3=Label(q8,text='What is the derivative of 6x+6x^2 with respect to x-')
    l3.grid(row=0,column=0,columnspan=2)
    def wer3():
        global a3
        x=a3.get()
        temp=x
        x=x.split('+')
        if '6' in x and '12x' in x and len(x)==2:
            global val8
            val8=1
            b3=Button(q8,text='press to record',bg='#0a0da8',bd=5,command=wer3,state=DISABLED)
            b3.grid(row=1,column=1)
            a3=Entry(q8,bg='#09f430',fg='#0d0504')
            a3.insert(0,temp)
            a3.grid(row=1,column=0)
        else:
            b3=Button(q8,text='press to record',bg='#0a0da8',bd=5,command=wer3,state=DISABLED)
            b3.grid(row=1,column=1)
            a3=Entry(q8,bg='#e10326',fg='#0d0504')
            a3.insert(0,temp)
            a3.grid(row=1,column=0)
    global a3
    a3=Entry(q8,bg='#e2ed2c',fg='#0d0504')
    a3.grid(row=1,column=0)
    b3=Button(q8,text='press to record',bg='#0a0da8',bd=5,command=wer3)
    b3.grid(row=1,column=1)
    l4=Label(q9,text='What is the weight of an object of mass m at the centre of the earth-')
    l4.grid(row=0,column=0,columnspan=2)
    def wer4():
        global a4
        x=a4.get()
        if x=='0':
            global val9
            val9=1
            b4=Button(q9,text='press to record',bg='#0a0da8',bd=5,command=wer4,state=DISABLED)
            b4.grid(row=1,column=1)
            a4=Entry(q9,bg='#09f430',fg='#0d0504')
            a4.insert(0,x)
            a4.grid(row=1,column=0)
        else:
            b4=Button(q9,text='press to record',bg='#0a0da8',bd=5,command=wer4,state=DISABLED)
            b4.grid(row=1,column=1)
            a4=Entry(q9,bg='#e10326',fg='#0d0504')
            a4.insert(0,x)
            a4.grid(row=1,column=0)
    global a4
    a4=Entry(q9,bg='#e2ed2c',fg='#0d0504')
    a4.grid(row=1,column=0)
    b4=Button(q9,text='press to record',bg='#0a0da8',bd=5,command=wer4)
    b4.grid(row=1,column=1)
    l5=Label(q0,text='Is total mechanical energy of an system always conserved-')
    l5.grid(row=0,column=0,columnspan=2)
    def answer(x):
        if x==1:
            global val10
            val10=1
            opt1=Button(q0,text='True',bg='#09f430',fg='#0d0504',command=lambda:answer(1),state=DISABLED)
            opt1.grid(row=1,column=0)
            opt2=Button(q0,text='False',bg='#09f430',fg='#0d0504',command=lambda:answer(0),state=DISABLED)
            opt2.grid(row=1,column=1)
        else:
            opt1=Button(q0,text='True',bg='#e10326',fg='#0d0504',command=lambda:answer(1),state=DISABLED)
            opt1.grid(row=1,column=0)
            opt2=Button(q0,text='False',bg='#e10326',fg='#0d0504',command=lambda:answer(0),state=DISABLED)
            opt2.grid(row=1,column=1)
    opt1=Button(q0,text='True',bg='#e2ed2c',fg='#0d0504',command=lambda:answer(0))
    opt1.grid(row=1,column=0)
    opt2=Button(q0,text='False',bg='#e2ed2c',fg='#0d0504',command=lambda:answer(1))
    opt2.grid(row=1,column=1)
    global score
    score=0
    def scor1():
        global score
        if val1==1:
            score+=1
        if val2==1:
            score+=1
        if val3==1:
            score+=1
        if val4==1:
            score+=1
        if val5==1:
            score+=1
        if val6==1:
            score+=1
        if val7==1:
            score+=1
        if val8==1:
            score+=1
        if val9==1:
            score+=1
        if val10==1:
            score+=1
        but.grid_forget()
        label=Label(file,text='you scored '+str(score)+' out of 10.',anchor=W)
        label.grid(row=10,column=0,pady=4)
        
    but=Button(file,text="click to calculate score",command=scor1)
    but.grid(row=10,column=0,pady=4)
    reset=Button(file,text="reset",bg='grey',padx=7,pady=7,bd=10,command=ref)
    reset.grid(row=11,column=0)

reset=Button(file,text="reset",bg='grey',padx=7,pady=7,bd=10,command=ref)
reset.grid(row=11,column=0)


file.mainloop()
