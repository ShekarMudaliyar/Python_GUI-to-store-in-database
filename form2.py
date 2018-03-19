from tkinter import *
from mysql.connector import *
from tkinter import messagebox as msg

con=Connect(user='root',password='123456',host='127.0.0.1')
cur=con.cursor()
cur.execute('use data')  #data is the database name
def sub():
    cur.execute("insert into stud values('"+name.get()+"',"+str(rollno.get())+",'"+add.get()+"',"+str(pno.get())+");")
    cur.close()
    con.commit()
    con.close()
    msg.showinfo('rows','Rows Inserted')
    
root=Tk()
l1=Label(root,text='Name')
l1.grid(row=0,column=0)
name=StringVar()
e1=Entry(root,textvariable=name)
e1.grid(row=0,column=1)

l2=Label(root,text='Roll no')
l2.grid(row=1,column=0)
rollno=IntVar()
e2=Entry(root,textvariable=rollno)
e2.grid(row=1,column=1)

l3=Label(root,text='address')
l3.grid(row=2,column=0)
add=StringVar()
e3=Entry(root,textvariable=add)
e3.grid(row=2,column=1)

l4=Label(root,text='phone no')
l4.grid(row=3,column=0)
pno=IntVar()
e4=Entry(root,textvariable=pno)
e4.grid(row=3,column=1)

b1=Button(root,text='Submit',command=sub)
b1.grid(row=5,column=0)
root.mainloop()

