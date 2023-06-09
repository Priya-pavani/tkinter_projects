'''
Hello I am P. Lakshmi sai priya. This file is about image viewer app. Here you have to change the paths to the image files.
This project is dine at june 6 2023, kindkly check if any changes are required in the future as the modules are always updating
'''


from tkinter import *
#from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()
root.configure(background="lightblue")
#width = root.winfo_screenwidth()
#height = root.winfo_screenheight()
root.title("Image viewer")
#root.attributes("-fullscreen", True)

width = 500
height = 500

img0 = Image.open("tkinterpractice\imageviewerapp\img0.jpg")
img0 = img0.resize((width, height))
img0 = ImageTk.PhotoImage(img0)

img1 = Image.open("tkinterpractice\imageviewerapp\img1.jpg")
img1 = img1.resize((width, height))
img1 = ImageTk.PhotoImage(img1)

img2 = Image.open("tkinterpractice\imageviewerapp\img2.jpg")
img2 = img2.resize((width, height))
img2 = ImageTk.PhotoImage(img2)

img3 = Image.open("tkinterpractice\imageviewerapp\img3.jpg")
img3 = img3.resize((width, height))
img3 = ImageTk.PhotoImage(img3)

img4 = Image.open("tkinterpractice\imageviewerapp\img4.jpg")
img4 = img4.resize((width, height))
img4 = ImageTk.PhotoImage(img4)

img5 = Image.open("tkinterpractice\imageviewerapp\img5.jpg")
img5 = img5.resize((width, height))
img5 = ImageTk.PhotoImage(img5)

img6 = Image.open("tkinterpractice\imageviewerapp\img6.jpg")
img6 = img6.resize((width, height))
img6 = ImageTk.PhotoImage(img6)

img7 = Image.open("tkinterpractice\imageviewerapp\img7.jpg")
img7 = img7.resize((width, height))
img7 = ImageTk.PhotoImage(img7)

img8 = Image.open("tkinterpractice\imageviewerapp\img8.jpg")
img8 = img8.resize((width, height))
img8 = ImageTk.PhotoImage(img8)

img9 = Image.open("tkinterpractice\imageviewerapp\img9.jpg")
img9 = img9.resize((width, height))
img9 = ImageTk.PhotoImage(img9)

img10 = Image.open("tkinterpractice\imageviewerapp\img10.jpg")
img10 = img10.resize((width, height))
img10 = ImageTk.PhotoImage(img10)

img11 = Image.open("tkinterpractice\imageviewerapp\img11.jpg")
img11 = img11.resize((width, height))
img11 = ImageTk.PhotoImage(img11)

image_list = [img0, img1, img2, img3, img4, img5, img6, img7, img8, img9, img10, img11]
index=5
label = Label( image = image_list[index])
label.grid(row = 0, column = 1, columnspan=3)

##################### below function is an action function for next buttton #####################
def next():
    left_button.config(state = "active")
    global index
    
    index+=1
    print(" next index:",index)
    if(index>=len(image_list)):
        global right_button
        right_button.config(state = "disabled")
        global status_bar
        status_bar.config(text = "Image "+str(index)+" of "+str(len(image_list)))
    else:
        
        global label
        label.grid_forget()
        label = Label( image = image_list[index])
        label.grid(row = 0, column = 1, columnspan=3)
        
        status_bar.config(text = "Image "+str(index+1)+" of "+str(len(image_list)))

    


######################## below function is an action function for back function  ##########################

def back():
    global index
    right_button.config(state = "active")
    index-=1
    print(" back index:",index)
    global label
    if index<0:
        
        global left_button
        left_button.config(state = "disabled")
        global status_bar
        
        status_bar.config(text = "Image "+str(index+2)+" of "+str(len(image_list)))

    else:
        
        label.grid_forget()
        label = Label( image = image_list[index])
        label.grid(row = 0, column = 1, columnspan=3)
        
        status_bar.config(text = "Image "+str(index+1)+" of "+str(len(image_list)))

###########  status bar adding ###############################
status_bar = Label( text = "Image "+str(index+1)+" of "+str(len(image_list)) , bd = 2, relief="sunken", anchor = "e")


left_button = Button(text="Back", font = "calibri", bg = "gainsboro", fg = "black",command =back)
left_button.grid( row = 2, column =1, pady = 10)


quit_button = Button(text = "Exit program", fg = "white", bg = "salmon", command = root.quit,  padx=15)
quit_button.config(font = "calibri")
quit_button.grid(row = 2, column = 2,sticky = "ew",pady = 10)


right_button = Button(text="Next", font = "calibri", bg = "gainsboro", fg = "black", command = next )
right_button.grid( row = 2, column =3 ,pady = 10)

status_bar.grid(row =3, column=1,columnspan=3, sticky="ew")



root.mainloop()
