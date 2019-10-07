from tkinter import *
from PIL import ImageTk,Image
from tkinter import messagebox


root = Tk()
root.title("Linedot Cipher Code")
root.configure(background='#343d46')
root.geometry("500x320")
root.iconbitmap('alphabet pics/crypto.ico')




a = ImageTk.PhotoImage(Image.open("alphabet pics/a.png"))
b = ImageTk.PhotoImage(Image.open("alphabet pics/b.png"))
c = ImageTk.PhotoImage(Image.open("alphabet pics/c.png"))
d = ImageTk.PhotoImage(Image.open("alphabet pics/d.png"))
e = ImageTk.PhotoImage(Image.open("alphabet pics/e.png"))
f = ImageTk.PhotoImage(Image.open("alphabet pics/f.png"))
g = ImageTk.PhotoImage(Image.open("alphabet pics/g.png"))
h = ImageTk.PhotoImage(Image.open("alphabet pics/h.png"))
i = ImageTk.PhotoImage(Image.open("alphabet pics/i.png"))
j = ImageTk.PhotoImage(Image.open("alphabet pics/j.png"))
k = ImageTk.PhotoImage(Image.open("alphabet pics/k.png"))
l = ImageTk.PhotoImage(Image.open("alphabet pics/l.png"))
m = ImageTk.PhotoImage(Image.open("alphabet pics/m.png"))
n = ImageTk.PhotoImage(Image.open("alphabet pics/n.png"))
o = ImageTk.PhotoImage(Image.open("alphabet pics/o.png"))
p = ImageTk.PhotoImage(Image.open("alphabet pics/p.png"))
q = ImageTk.PhotoImage(Image.open("alphabet pics/q.png"))
r = ImageTk.PhotoImage(Image.open("alphabet pics/r.png"))
s = ImageTk.PhotoImage(Image.open("alphabet pics/s.png"))
t = ImageTk.PhotoImage(Image.open("alphabet pics/t.png"))
u = ImageTk.PhotoImage(Image.open("alphabet pics/u.png"))
v = ImageTk.PhotoImage(Image.open("alphabet pics/v.png"))
w = ImageTk.PhotoImage(Image.open("alphabet pics/w.png"))
x = ImageTk.PhotoImage(Image.open("alphabet pics/x.png"))
y = ImageTk.PhotoImage(Image.open("alphabet pics/y.png"))
z = ImageTk.PhotoImage(Image.open("alphabet pics/z.png"))
main_1 = ImageTk.PhotoImage(Image.open("alphabet pics/main_pic_1.png"))
main_2 = ImageTk.PhotoImage(Image.open("alphabet pics/main_pic_2.png"))


def manual():
	manual_scr = Toplevel()
	manual_scr.geometry('400x500')
	manual_scr.iconbitmap('alphabet pics/crypto.ico')

	Label(manual_scr, image = main_1).pack(padx = 10,pady = 10)
	Label(manual_scr, image = main_2).pack(padx = 10, pady =10)
	Label(manual_scr, text = 'We think you know it very well').pack(padx = 10, pady = 10)



def show():

	en = Entry_1.get()
	

	en = en.lower()





	if en =='':
		messagebox.showwarning('Warning','There is no letter inserted in the box\n 	GOTCHA \n I knew you will go for it')



	elif len(en) < 11:
		top = Toplevel()
		top.geometry('400x400')
		top.iconbitmap('alphabet pics/crypto.ico')
		label = Label(top, text = "For '"+ en +"' the encryption will be :", font = 5).pack(padx = 10, pady = 10)

		for letter in en:
			if letter == 'a':
				Label(top, image = a).pack()
			if letter == 'b':
				Label(top, image = b).pack()
			if letter == 'c':
				Label(top, image = c).pack()
			if letter == 'd':
				Label(top, image = d).pack()
			if letter == 'e':
				Label(top, image = e).pack()
			if letter == 'f':
				Label(top, image = f).pack()
			if letter == 'g':
				Label(top, image = g).pack()
			if letter == 'h':
				Label(top, image = h).pack()
			if letter == 'i':
				Label(top, image = i).pack()
			if letter == 'j':
				Label(top, image = j).pack()
			if letter == 'k':
				Label(top, image = k).pack()
			if letter == 'l':
				Label(top, image = l).pack()
			if letter == 'm':
				Label(top, image = m).pack()
			if letter == 'n':
				Label(top, image = n).pack()
			if letter == 'o':
				Label(top, image = o).pack()
			if letter == 'p':
				Label(top, image = p).pack()
			if letter == 'q':
				Label(top, image = q).pack()
			if letter == 'r':
				Label(top, image = r).pack()
			if letter == 's':
				Label(top, image = s).pack()
			if letter == 't':
				Label(top, image = t).pack()
			if letter == 'u':
				Label(top, image = u).pack()
			if letter == 'v':
				Label(top, image = v).pack()
			if letter == 'w':
				Label(top, image = w).pack()
			if letter == 'x':
				Label(top, image = x).pack()
			if letter == 'y':
				Label(top, image = y).pack()
			if letter == 'z':
				Label(top, image = z).pack()


	else:

		messagebox.showwarning('Warning',"Your word is longer than 10 character\n Please insert a word which is wthin 10 character")







label_1 = Label(root, text = 'Please insert a word within 10 character max that you want to cipher', bg = '#343d46', fg = 'white', font = 20).pack(padx = 10,pady = (10,0))

Label(root, text = 'This GUI is not for professional use', bg = '#343d46', fg = 'white', font = 5).pack(padx = 10, pady = (0, 10))
Entry_1 = Entry(root, borderwidth = 10, font = 20)
Entry_1.pack(ipady = 10)
Button(root, text = "Encrypt", command = show).pack(padx = 10, pady = (10, 5), ipadx = 10)
Button(root, text = "Exit", command = root.quit, bg = 'black', fg = 'white').pack(padx = 10, pady = 5 , ipadx = 25)
Label(root, text = 'For more information Click Below', bg = '#343d46', fg = 'white', font = 0).pack(padx = 10, pady = 10)
Button(root, text = 'Manual', command = manual).pack(padx = 10, pady = 10, ipadx = 15)

#(root,text)


status = Label(root, text = 'All rights reserved by RAS®', bg = '#343d46', fg = 'white')
status.pack(side = BOTTOM)








root.mainloop()
