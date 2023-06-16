from tkinter import *
import sqlite3 as s
root = Tk()

root.title("Daatabase app")
# connecting to the data base
conn = s.connect("address_database.db")

# creating a cursor
cur = conn.cursor()


# creating a table

'''cur.execute("""CREATE TABLE  address(  

first_name text,
last_name text,
city text,
state text,
zipcode integer
)""")'''


#################### submit records function ###################################

def submit():
    conn = s.connect("address_database.db")

    # creating a cursor
    cur = conn.cursor()



    cur.execute("INSERT INTO address VALUES(:f_name,:l_name,:city,:state,:zip)",{
        'f_name' : f_name.get(),
        'l_name' : l_name.get(),
        'city': city.get(),
        'state' : state.get(),
        'zip' : zip.get()
    })

    f_name.delete(0,END)
    l_name.delete(0,END)
    city.delete(0,END)
    state.delete(0,END)
    zip.delete(0,END)

    # commiting changes
    conn.commit()

    # closing connection
    conn.close()

#####################  showing records function  #################################

def show_records():
    conn = s.connect("address_database.db")

    # creating a cursor
    cur = conn.cursor()
    cur.execute("SELECT *,oid FROM address")
    records= cur.fetchall()
    all_record = ""
    for record in records:
        all_record += str(record) + "\n"
    print(records)
    show_all = Label(root, text = all_record, font = ("calibri",17))
    show_all.grid(row = 7, column= 0 ,columnspan= 2, pady = 10,sticky= "ew")
    


    # commiting changes
    conn.commit()

    # closing connection
    conn.close()





# ######################## creating entry fields #######################################################

f_name = Entry(root, relief="sunken" ,background = "white", font = ("calibri",19))
f_name.grid(row = 0,column = 1)
l_name = Entry(root, relief="sunken", bg="white", font = ("calibri",19))
l_name.grid(row = 1,column = 1)
city = Entry(root, relief="sunken", bg="white", font = ("calibri",19))
city.grid(row = 2,column = 1)
state = Entry(root, relief="sunken",  bg="white", font = ("calibri",19))
state.grid(row = 3,column = 1)
zip = Entry(root, relief="sunken",  bg="white", font = ("calibri",19))
zip.grid(row = 4,column = 1)



############################# creting entry text labels #########################################

f_label = Label(root,text = "First name: ", font = ("calibri",19))
f_label.grid(row=0,column=0)
l_label = Label(root,text = "Last name: ", font = ("calibri",19))
l_label.grid(row=1,column=0)
city_label = Label(root,text = "City name: ", font = ("calibri",19))
city_label.grid(row=2,column=0)
state_label = Label(root,text = "State name: ", font = ("calibri",19))
state_label.grid(row=3,column=0)
zip_label = Label(root,text = "Zip code: ", font = ("calibri",19))
zip_label.grid(row=4,column=0)



################### CREATING SUBMIT RECORD  #################################################

submit_btn = Button(root,text= "submit", bg = "orchid1", font = ("calibri,19"),command=submit)
submit_btn.grid(row = 5 , column=0,columnspan=2,pady=20,sticky="ew")

########## CREATING SHOW RECORD BUTTON #####################################################

show_btn = Button(root,text= "Show all records", bg = "orchid1", font = ("calibri,19"),command=show_records)
show_btn.grid(row = 6 , column=0,columnspan=2,sticky="ew")


# commiting changes
conn.commit()

# closing connection
conn.close()


root.mainloop()