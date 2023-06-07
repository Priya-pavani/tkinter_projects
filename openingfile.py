
""" This is not a project but a mere excercise to open files and display them in tkinter window"""

from tkinter import *
from PIL import Image,ImageTk
from tkinter import messagebox
from tkinter import filedialog

root = Tk()

root.geometry("300x300")

def openfile():
    global filename
    filename = filedialog.askopenfilename( initialdir="C://Users//91798//OneDrive//Desktop//stanford_final_project//tkinterpractice//imageviewerapp",
                                      filetypes=(("png files","*png"),
                                                 ("jpg file","*jpg"),
                                                 ("jpeg file","*jpeg")),title = "select an image file")
    print(filename)
    print(type(filename))
    img=Image.open(filename)
    img=img.resize((500,500))
    img=ImageTk.PhotoImage(img)
    
    global label1
    label1.forget()
    global frame1
    
    label1 = Label( frame1,image=img,)
    label1.image = img
    label1.pack()
    frame1.pack(side= "left")
    


frame = Frame(root)

button = Button(frame,text = "open file", bg = "white", fg = "black",font = ("calibri",14) ,command = openfile )
button.pack(side="left")
frame.pack(side="left",fill = "y", padx=50,pady=50)

frame.pack()

frame1 = Frame(root)
img=Image.open(r"tkinterpractice\Upload-PNG-Pic.png")
img=img.resize((500,500))
img=ImageTk.PhotoImage(img)

label1 = Label( frame1,image=img,)
label1.pack()
frame1.pack(side="left")

root.mainloop()
