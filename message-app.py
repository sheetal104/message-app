# -*- coding: utf-8 -*-
"""
Created on Sat Nov 23 2019

"""

from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox,scrolledtext

window=Tk()
window.title("Application")
window.geometry('1000x670')

users = []  #list of contacts

class AddCon:
    def __init__(self, win):
        self.lbl1=Label(win, text='Name')
        self.lbl2=Label(win, text='Phone number')
        self.lbl3=Label(win,text="Gender")
        self.lbl4=Label(win,text="Date of Birth")
        
        self.t1=Entry() #name
        self.t2=Entry() #phone number
        self.v0=StringVar() #gender
        self.v0.set("Male")
        self.g1=Radiobutton(win, text="Male", variable=self.v0,value="Male")
        self.g2=Radiobutton(win, text="Female", variable=self.v0,value="Female")
        self.s1 = Spinbox(win, from_=1, to=31, width=5)       #date
        self.s2 = Spinbox(win, from_=1980, to=2019, width=7)  #year
        self.s3 = StringVar()                                 #month
        self.s3.set("January")
        self.cb=Combobox(win,width=10,values=("January","February","March","April","May","June","July","August","September","October","November","December"))
        
        self.lbl3.place(x=75,y=150)
        self.lbl4.place(x=75,y=200)
        self.g1.place(x=175,y=150)
        self.g2.place(x=250, y=150)
        self.lbl1.place(x=75, y=50)
        self.t1.place(x=175, y=50)
        self.lbl2.place(x=75, y=100)
        self.t2.place(x=175, y=100)
        self.cb.place(x=175,y=200)
        self.s1.place(x=260,y=200)
        self.s2.place(x=310,y=200)
        
    def get_data(self):
        return {
                "name": self.t1.get(), "ph_no": self.t2.get(),
                "gender": self.v0.get(),
                "dob": (self.s1.get(),self.cb.get(),self.s2.get()),
                "msg": []
                }          #dictionary to store contact info
   
    def clear_text(self):
        self.t1.delete(0, 'end')
        self.t2.delete(0, 'end')
        self.v0.set(0)
        self.s1.delete(0,'end')
        self.s2.delete(0,'end')
        self.cb.set("")
        
    
class SearchCon:
    def __init__(self,win):
        self.l=Label(win,text="Search by Name: ")
        self.l.place(x=700,y=50)
        self.n=Entry()    #name
        self.n.place(x=800,y=50)
        self.r=Label(win,text="RESULTS ->")
        self.r.place(x=700,y=120)
        self.txt=scrolledtext.ScrolledText(win, width=45,height=8)  #search results
        self.txt.insert(INSERT,"")
        self.txt.place(x=700,y=150)
     
    def get_data(self):
        return self.n.get()
    
    def clear_text(self):
        self.n.delete(0,'end')
        self.txt.delete("1.0", 'end')
    
    def add_results(self,r):
        self.clear_text()
        self.txt.insert(INSERT,r)
        
class Inbox:
    def __init__(self,win):
        self.txt=scrolledtext.ScrolledText(win, width=40,height=9)
        self.txt.insert(INSERT," ")
        self.txt.place(x=75,y=450)
        
    def add_msg(self,m):
        self.txt.insert(INSERT,"\n" + m[0].upper() + " : " + m[1])  
        #display sent message
        
    def clear_text(self):
        self.txt.delete("1.0","end")

        
class Outbox:
    def __init__(self,win):
        self.l=Label(win,text="Name")
        self.l.place(x=700,y=450)
        self.n=Entry()   #name
        self.n.place(x=800,y=450)
        self.r=Label(win,text="Message")
        self.r.place(x=700,y=500)
        self.txt=Entry()  #message to be sent
        self.txt.place(x=800,y=500)
    
    def get_data(self):
        return (self.n.get(), self.txt.get())
    
    def clear_text(self):
        self.n.delete(0, 'end')
        self.txt.delete(0, 'end')
        
        
def addc():
    global contactBox
    users.append(contactBox.get_data()) #add entries to list
    print(users,"  in addc")
    contactBox.clear_text()
    messagebox.showinfo('Confirmation', 'Contact Saved!')
    
def search():
    global users
    md=""
    sname=usearch.get_data() #name to be searched 
    for i in users:
        if(sname==i["name"]): #check if sname is in the list of dictionaries
            r="\n Name: "+i["name"]+"\n Gender: "+i["gender"]+"\n DOB:"+str(i["dob"])+"\n"+" Phone Number: "+i["ph_no"]
            usearch.add_results(r)
            #show contact details
            print(i," in search")
            p=True
            break
        else:
            p=False
              
        
    if(p==True):
            mb="Contact Found!"
    else:
            print("User does not exist")        
            mb='Contact Not Found!'
            usearch.clear_text()
            
    messagebox.showinfo('Search Result',mb) 
    
def received():
   mywin.clear_text()
   messagebox.showinfo('Inbox', 'No messages to show!')
    
def send():
    global users
    mb=""
    m = send_msg.get_data()   #recepient and message
    for i in users:
        if(i['name']==m[0]):  #check if recepient belongs in contact list
            i['msg'].append(m)
            print(users,"in send")
            mywin.add_msg(m)
            p=True
            break
        else:
            p=False
            
    if(p==True):
            mb="Sent!"
            send_msg.clear_text()
    else:
            print("User does not exist")
            mb='Contact Not Found!'
            send_msg.clear_text()
            
    messagebox.showinfo('Outbox',mb)
    
    
lb1 = Label(window, text="\tADD CONTACTS\n\n",font=("Arial"))
lb1.grid(column=0, row=0)     
contactBox=AddCon(window)
b1=Button(text="SAVE",fg="blue",command=addc)
b1.place(x=200,y=250)

lb2= Label(window, text="SEARCH CONTACTS\n\n",font=("Arial"))
lb2.place(x=700,y=0) 
usearch=SearchCon(window)
b2=Button(text="SEARCH",fg="blue",command=search)
b2.place(x=800,y=75)

lb3= Label(window, text="\tMESSAGES RECEIVED\n\n",font=("Arial"))
lb3.place(x=0,y=400) 
mywin=Inbox(window)
b3=Button(text="CLEAR",fg="blue",command=received)
b3.place(x=230,y=620)

lb4= Label(window, text="SEND MESSAGE\n\n",font=("Arial"))
lb4.place(x=700,y=400) 
send_msg=Outbox(window)
b4=Button(text="SEND",fg="blue",command=send)
b4.place(x=800,y=610)

window.mainloop()

