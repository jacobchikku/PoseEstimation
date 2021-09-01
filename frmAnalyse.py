from tkinter import*
import TestProject as tp
import os, fnmatch

def submitForm():    
    strFile = optVariable.get()
        
    if (strFile !=''):
        tp.fncAnalyse(strFile,optSpeedVariable.get())
        print("registration form  seccussfully created...")

root = Tk()
root.geometry('600x600')
root.title("Posture Analysis")

label_0 = Label(root, text="Analyse Player Posture",width=20,font=("bold", 20))
label_0.place(x=120,y=53)

label_1 = Label(root, text="Choose Mode",width=20,font=("bold", 10))
label_1.place(x=70,y=150)

var = IntVar()
Radiobutton(root, text="Batting",padx = 5, variable=var, value=1).place(x=235,y=150)
Radiobutton(root, text="Bowling",padx = 20, variable=var, value=2).place(x=220,y=180)
Radiobutton(root, text="Fielding",padx = 20, variable=var, value=2).place(x=220,y=210)


label_2 = Label(root, text="Video Files",width=20,font=("bold", 10))
label_2.place(x=68,y=250)

flist = fnmatch.filter(os.listdir('.'), '*.mp4')
optVariable = StringVar(root)
optVariable.set("   Select Video   ") # default value
w = OptionMenu(root, optVariable,*flist)
w.pack()
w.place(x=240,y=250)

label_3 = Label(root, text="Speed",width=20,font=("bold", 10))
label_3.place(x=54,y=290)

splist={'Normal', 'Slow Motion', 'Super Slow Motion'}
optSpeedVariable = StringVar(root)
optSpeedVariable.set("   Select Video Speed   ") # default value
w = OptionMenu(root, optSpeedVariable,*splist)
w.pack()
w.place(x=240,y=290)


Button(root, text='Submit', command=submitForm, width=20,bg='brown',fg='white').place(x=180,y=380)


root.mainloop()
