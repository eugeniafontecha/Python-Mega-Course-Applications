from tkinter import *

window=Tk()

def convert_kg():
    g = float(e1_value.get())*1000
    p = float(e1_value.get())*2.20462
    o = float(e1_value.get())*35.274
    
    t_g.delete(1.0, END)
    t_p.delete(1.0, END)
    t_o.delete(1.0, END)

    t_g.insert(END,g)
    t_p.insert(END,p)
    t_o.insert(END,o)

#label Kg en 0,0
l1=Label(window, text="Kg")
l1.grid(row=0,column=0)

#entry en 0,1
e1_value=StringVar()
e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

#botón Covnert en 0,2
b1 = Button(window, text="Convert",command=convert_kg)
b1.grid(row=0,column=2)

#text g en 1,0
t_g=Text(window,height=1,width=20)
t_g.grid(row=1,column=0)

#text pounds en 1,1
t_p=Text(window,height=1,width=20)
t_p.grid(row=1,column=1)

#text ounces en 1,2
t_o=Text(window,height=1,width=20)
t_o.grid(row=1,column=2)

window.mainloop()