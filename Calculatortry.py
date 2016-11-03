from tkinter import *

window = Tk()
add0=0
class calculator:
    def __init__(self):
        self.x = 520
from tkinter import *

window = Tk()
add0=0
class calculator:
    def __init__(self):
        self.x = 500
        self.y = 150

        self.x1=600
        self.y1=150

        window.title('Calculator')
        l2=Label(window,text='Enter Price/Calculator',font=20)
        l2.place(x=20,y=30)
        self.string=StringVar()
        entry=Entry(window,textvariable=self.string,font=20)
        entry.place(x=160, y=30)
        l3=Label(window,text='Enter Item',font=20)
        l3.place(x=20, y=80)
        self.string12 = StringVar()
        entry12 = Entry(window, textvariable=self.string12, font=20)
        entry12.place(x=160, y=80)
       # add0=0
        #add1 = (self.string.get())
        #add11=int(add1)
        #add0 = add0+add11

        #entry.bind('<keyPress>',self.keyPress)
        entry.focus()


        btn=Button(window,height=2,width=4,padx=18,pady=18,text='7',command=lambda:self.addchar('7'))
        btn.place(x=20, y=140)
        btn1 = Button(window, height=2, width=4, padx=18, pady=18, text='8',command=lambda:self.addchar('8'))
        btn1.place(x=100, y=140)
        btn2 = Button(window, height=2, width=4, padx=18, pady=18, text='9',command=lambda:self.addchar('9'))
        btn2.place(x=180, y=140)
        btn3 = Button(window, height=2, width=4, padx=18, pady=18, text='/',command=lambda:self.addchar('/'))
        btn3.place(x=260, y=140)
        btn4 = Button(window, height=2, width=4, padx=18, pady=18, text='Clear',command=lambda: self.clear_txt())
        btn4.place(x=340, y=140)
        btn5 = Button(window, height=2, width=4, padx=18, pady=18, text='<-',command=lambda: self.delete(),)
        btn5.place(x=420, y=140)

        btn6 = Button(window, height=2, width=4, padx=18, pady=18, text='4',command=lambda:self.addchar('4'))
        btn6.place(x=20, y=220)
        btn7 = Button(window, height=2, width=4, padx=18, pady=18, text='5',command=lambda:self.addchar('5'))
        btn7.place(x=100, y=220)
        btn8 = Button(window, height=2, width=4, padx=18, pady=18, text='6',command=lambda:self.addchar('6'))
        btn8.place(x=180, y=220)
        btn9 = Button(window, height=2, width=4, padx=18, pady=18, text='*',command=lambda:self.addchar('*'))
        btn9.place(x=260, y=220)
        btn10 = Button(window, height=2, width=4, padx=18, pady=18, text='(',command=lambda:self.addchar('('))
        btn10.place(x=340, y=220)
        btn11 = Button(window, height=2, width=4, padx=18, pady=18, text=')',command=lambda:self.addchar(')'))
        btn11.place(x=420, y=220)


        btn12 = Button(window, height=2, width=4, padx=18, pady=18, text='1',command=lambda:self.addchar('1'))
        btn12.place(x=20, y=300)
        btn13 = Button(window, height=2, width=4, padx=18, pady=18, text='2',command=lambda:self.addchar('2'))
        btn13.place(x=100, y=300)
        btn14 = Button(window, height=2, width=4, padx=18, pady=18, text='3',command=lambda:self.addchar('3'))
        btn14.place(x=180, y=300)
        btn15 = Button(window, height=2, width=4, padx=18, pady=18, text='-',command=lambda:self.addchar('-'))
        btn15.place(x=260, y=300)

        btn16 = Button(window, height=2, width=4, padx=18, pady=18, text='0',command=lambda:self.addchar('0'))
        btn16.place(x=20, y=300)
        btn17 = Button(window, height=2, width=4, padx=18, pady=18, text='.',command=lambda:self.addchar('.'))
        btn17.place(x=100, y=380)
        btn18 = Button(window, height=2, width=4, padx=18, pady=18, text='%',command=lambda:self.addchar('%'))
        btn18.place(x=180, y=380)
        btn19 = Button(window, height=2, width=4, padx=18, pady=18, text='+',command=lambda:self.addchar('+'))
        btn19.place(x=260, y=380)

        btn20 = Button(window, height=2, width=4, padx=18, pady=18, text='=',command=lambda: self.equal())
        btn20.place(x=340, y=300)
        btn21 = Button(window, height=2, width=4, padx=18, pady=18, text='LIST', command=lambda: self.list())
        btn21.place(x=420, y=300)


        L1=Label(window,height=4,width=30,padx=18,pady=18,text='LIST')
        L1.place(x=500, y=30)
        #btn211 = Button(window, height=2, width=4, padx=18, pady=18, text='ADD', command=lambda: self.adda(add0))
        #btn211.place(x=20, y=380)


        window.mainloop()
    def clear_txt(self):
        self.string.set('')

    def equal(self):
        results=""

        try:
            result=eval(self.string.get())
        except:
            result='Error'
        self.string.set(result)

    def addchar(self,char):
        self.string.set(self.string.get()+(str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])

    def list(self):
        abc = (self.string12.get())
        L11 = Label(window, padx=18, pady=18, text=abc)
        L11.place(x=self.x, y=self.y)
        self.y+=80

        ijk=(self.string.get())
        L12 = Label(window, padx=18, pady=18, text=ijk)
        L12.place(x=self.x1, y=self.y1)
        self.y1+=80

calculator()
        self.y = 140

        self.x1=600
        self.y1=140

        window.title('Calculator')
        l2=Label(window,text='Enter Price/Calculator',font=20)
        l2.place(x=20,y=30)
        self.string=StringVar()
        entry=Entry(window,textvariable=self.string,font=20)
        entry.place(x=160, y=30)
        l3=Label(window,text='Enter Item',font=20)
        l3.place(x=20, y=80)
        self.string12 = StringVar()
        entry12 = Entry(window, textvariable=self.string12, font=20)
        entry12.place(x=160, y=80)
       # add0=0
        #add1 = (self.string.get())
        #add11=int(add1)
        #add0 = add0+add11

        #entry.bind('<keyPress>',self.keyPress)
        entry.focus()


        btn=Button(window,height=2,width=4,padx=18,pady=18,text='7',command=lambda:self.addchar('7'))
        btn.place(x=20, y=140)
        btn1 = Button(window, height=2, width=4, padx=18, pady=18, text='8',command=lambda:self.addchar('8'))
        btn1.place(x=100, y=140)
        btn2 = Button(window, height=2, width=4, padx=18, pady=18, text='9',command=lambda:self.addchar('9'))
        btn2.place(x=180, y=140)
        btn3 = Button(window, height=2, width=4, padx=18, pady=18, text='/',command=lambda:self.addchar('/'))
        btn3.place(x=260, y=140)
        btn4 = Button(window, height=2, width=4, padx=18, pady=18, text='Clear',command=lambda: self.clear_txt())
        btn4.place(x=340, y=140)
        btn5 = Button(window, height=2, width=4, padx=18, pady=18, text='<-',command=lambda: self.delete(),)
        btn5.place(x=420, y=140)

        btn6 = Button(window, height=2, width=4, padx=18, pady=18, text='4',command=lambda:self.addchar('4'))
        btn6.place(x=20, y=220)
        btn7 = Button(window, height=2, width=4, padx=18, pady=18, text='5',command=lambda:self.addchar('5'))
        btn7.place(x=100, y=220)
        btn8 = Button(window, height=2, width=4, padx=18, pady=18, text='6',command=lambda:self.addchar('6'))
        btn8.place(x=180, y=220)
        btn9 = Button(window, height=2, width=4, padx=18, pady=18, text='*',command=lambda:self.addchar('*'))
        btn9.place(x=260, y=220)
        btn10 = Button(window, height=2, width=4, padx=18, pady=18, text='(',command=lambda:self.addchar('('))
        btn10.place(x=340, y=220)
        btn11 = Button(window, height=2, width=4, padx=18, pady=18, text=')',command=lambda:self.addchar(')'))
        btn11.place(x=420, y=220)


        btn12 = Button(window, height=2, width=4, padx=18, pady=18, text='1',command=lambda:self.addchar('1'))
        btn12.place(x=20, y=300)
        btn13 = Button(window, height=2, width=4, padx=18, pady=18, text='2',command=lambda:self.addchar('2'))
        btn13.place(x=100, y=300)
        btn14 = Button(window, height=2, width=4, padx=18, pady=18, text='3',command=lambda:self.addchar('3'))
        btn14.place(x=180, y=300)
        btn15 = Button(window, height=2, width=4, padx=18, pady=18, text='-',command=lambda:self.addchar('-'))
        btn15.place(x=260, y=300)

        btn16 = Button(window, height=2, width=4, padx=18, pady=18, text='0',command=lambda:self.addchar('0'))
        btn16.place(x=20, y=300)
        btn17 = Button(window, height=2, width=4, padx=18, pady=18, text='.',command=lambda:self.addchar('.'))
        btn17.place(x=100, y=380)
        btn18 = Button(window, height=2, width=4, padx=18, pady=18, text='%',command=lambda:self.addchar('%'))
        btn18.place(x=180, y=380)
        btn19 = Button(window, height=2, width=4, padx=18, pady=18, text='+',command=lambda:self.addchar('+'))
        btn19.place(x=260, y=380)

        btn20 = Button(window, height=2, width=4, padx=18, pady=18, text='=',command=lambda: self.equal())
        btn20.place(x=340, y=300)
        btn21 = Button(window, height=2, width=4, padx=18, pady=18, text='LIST', command=lambda: self.list())
        btn21.place(x=420, y=300)
        L1=Label(window,height=4,width=30,padx=18,pady=18,text='LIST')
        L1.place(x=500, y=30)
        #btn211 = Button(window, height=2, width=4, padx=18, pady=18, text='ADD', command=lambda: self.adda(add0))
        #btn211.place(x=20, y=380)


        window.mainloop()
    def clear_txt(self):
        self.string.set('')

    def equal(self):
        results=""

        try:
            result=eval(self.string.get())
        except:
            result='Error'
        self.string.set(result)

    def addchar(self,char):
        self.string.set(self.string.get()+(str(char)))

    def delete(self):
        self.string.set(self.string.get()[0:-1])

    def list(self):
        abc = (self.string12.get())
        L11 = Label(window,height=4, width=30, padx=18, pady=18, text=abc)
        L11.place(x=self.x, y=self.y)
        self.y+=80

        ijk=(self.string.get())
        L12 = Label(window, height=4, width=30, padx=18, pady=18, text=ijk)
        L12.place(x=self.x1, y=self.y1)
        self.y1+=80











calculator()