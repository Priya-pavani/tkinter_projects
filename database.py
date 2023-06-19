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
    global show_all
    show_all.forget()
    all_record = ""
    for record in records:
        all_record += str(record) + "\n"
    print(records)
    show_all = Label(root, text = all_record, font = ("calibri",17))
    show_all.grid(row = 10, column= 0 ,columnspan= 2, pady = 10,sticky= "ew")
    # commiting changes
    conn.commit()
    # closing connection
    conn.close()

###########################  delete record function #############################################

def delete():
    """This function is used to delete a record."""
    conn = s.connect("address_database.db")
    # creating a cursor
    cur = conn.cursor()
    cur.execute("DELETE FROM address where oid = "+ del_box.get())
    del_box.delete(0,END)
    conn.commit()
    # closing connection
    conn.close()   

############################  saving overwritten values or updated values  ###############################


def overwritten_saving():
    conn = s.connect("address_database.db")
    # creating a cursor
    cur = conn.cursor()

    cur.execute("UPDATE address SET  first_name = :f_name_edit , last_name = :l_name_edit ,city = :city_edit,  state = :state_edit ,zipcode= :zip_edit  where oid = :oid",{
        'f_name_edit' : f_name_edit.get(),
        'l_name_edit' : l_name_edit.get(),
        'city_edit' : city_edit.get(),
        'state_edit' :state_edit.get(),
        'zip_edit' : zip_edit.get(),
        'oid' : del_box.get()
    })
    # commiting changes
    conn.commit()

    # closing connection
    conn.close()

    edit.destroy()




############################  Updating record function #################################################

def updating():
    global edit
    edit = Tk()
    global f_name_edit
    global l_name_edit
    global city_edit
    global state_edit
    global zip_edit

    edit.title("Updating the seclected record")
    f_name_edit = Entry(edit, relief="sunken" ,background = "white", font = ("calibri",19))
    f_name_edit.grid(row = 0,column = 1)
    l_name_edit = Entry(edit, relief="sunken", bg="white", font = ("calibri",19))
    l_name_edit.grid(row = 1,column = 1)
    city_edit = Entry(edit, relief="sunken", bg="white", font = ("calibri",19))
    city_edit.grid(row = 2,column = 1)
    state_edit = Entry(edit, relief="sunken",  bg="white", font = ("calibri",19))
    state_edit.grid(row = 3,column = 1)
    zip_edit = Entry(edit, relief="sunken",  bg="white", font = ("calibri",19))
    zip_edit.grid(row = 4,column = 1)



    ############################# creting entry text labels #########################################

    f_label_edit = Label(edit,text = "First name: ", font = ("calibri",19))
    f_label_edit.grid(row=0,column=0)
    l_label_edit = Label(edit,text = "Last name: ", font = ("calibri",19))
    l_label_edit.grid(row=1,column=0)
    city_label_edit = Label(edit,text = "City name: ", font = ("calibri",19))
    city_label_edit.grid(row=2,column=0)
    state_label_edit = Label(edit,text = "State name: ", font = ("calibri",19))
    state_label_edit.grid(row=3,column=0)
    zip_label_edit = Label(edit,text = "Zip code: ", font = ("calibri",19))
    zip_label_edit.grid(row=4,column=0)

    ########## CREATING SHOW RECORD BUTTON #####################################################

    show_btn = Button(edit,text= "Save the changes", bg = "DodgerBlue", font = ("calibri,19"), command = overwritten_saving)
    show_btn.grid(row = 6 , column=0,columnspan=2,sticky="ew",pady = 20)

    # connecting to the data base
    conn = s.connect("address_database.db")

    # creating a cursor
    cur = conn.cursor()
    global id
    id = del_box.get()

    cur.execute("SELECT * FROM address where oid="+ id)
    record = cur.fetchall()\
    
        
    for i in record:
        f_name_edit.insert(0,i[0])
        l_name_edit.insert(0,i[1])
        city_edit.insert(0,i[2])
        state_edit.insert(0,i[3])
        zip_edit.insert(0,i[4])
    print(record)
    if record == [] :
        f_name_edit.insert(0,"NOT AVAILABLE")
        l_name_edit.insert(0,"NOT AVAILABLE")
        city_edit.insert(0,"NOT AVAILABLE")
        state_edit.insert(0,"NOT AVAILABLE")
        zip_edit.insert(0,"NOT AVAILABLE")


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

submit_btn = Button(root,text= "submit", bg = "DodgerBlue", font = ("calibri,19"),command=submit)
submit_btn.grid(row = 5 , column=0,columnspan=2,pady=20,sticky="ew")

########## CREATING SHOW RECORD BUTTON #####################################################

show_btn = Button(root,text= "Show all records", bg = "DodgerBlue", font = ("calibri,19"),command=show_records)
show_btn.grid(row = 6 , column=0,columnspan=2,sticky="ew")

################### CREATING DELETE RECORD ENTRY BOX ALONG WITH THE LABEL #########################
del_box = Entry(root, background ="snow",font = ("claibri",18) )
del_box.grid(row =7,column=1,pady =10 ,padx = 20)
del_label = Label(root, text = "ID: " , font = ("calibri",19))
del_label.grid(row = 7,column=0)

#####################  DELETE BUTTON CREATION ###################################

del_btn = Button(root,text = "Delete a record", font = ("calibri",19),bg = "tomato",command = delete)
del_btn.grid(row = 8,column=0,columnspan=2,sticky="ew")


################  CREATING UPDATE BUTTON CREATION ######################################

up_btn = Button(root, text = "Update a record" , font = ("calibri",19), bg ="DodgerBlue", command = updating )
up_btn.grid(row =9, column = 0,columnspan=2,sticky= "ew",pady = 10)
# commiting changes
conn.commit()

# closing connection
conn.close()
all_record = ""
show_all = Label(root, text = all_record, font = ("calibri",17))
show_all.grid(row = 10, column= 0 ,columnspan= 2, pady = 10,sticky= "ew")

root.mainloop()