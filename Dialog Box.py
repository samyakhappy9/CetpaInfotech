from tkinter import *
from tkinter import filedialog
import sqlite3 as s
scr=Tk()
fm=Frame(scr,width=650,height=450,bg='light blue',bd=20,relief='ridge')
fm.pack()
fm.place(x=0,y=50)
l1=Listbox(fm,font=('times',20,'bold'),height=10,width=40)
l1.pack()
l1.place(x=7,y=10)
def create_fun1():
    txt1=StringVar()
    create_fun=Toplevel(scr)
    create_frame=Frame(create_fun,width=700,height=400,bd=20,relief='ridge')
    create_frame.pack()

def opens():
    name=filedialog.askopenfilename()
    global c
    global client
    ls=[]
    if name.endswith('.db'):
        client=s.connect(name)
        c=client.cursor()
        c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'")
        for i in c.fetchall():
            ls.append(i)
            l1.insert(0,i)

b=Button(scr,text='Open',font=('times',15,'bold'),command=opens)
b.grid(row=0,column=1)
b1=Button(scr,text='Create',font=('times',15,'bold'),command=create_fun1)
b1.grid(row=0,column=2)
b2=Button(scr,text='Delete',font=('times',15,'bold'))
b2.grid(row=0,column=3)

txt2=StringVar()
fm1=Frame(scr,width=650,height=650,relief='ridge',bd=20)
fm1.place(x=650,y=50)
n1=Entry(fm1,font=('arial',15,'bold'),textvariable=txt2,width=40,bd=5)
txt2.set('Enter a Query:')
n1.place(x=60,y=500)
button_query=Button(fm1,text="Execute",font=('times',15,'italic'),bd=3)
button_query.place(x=250,y=250)

scr.mainloop()