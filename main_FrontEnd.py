# Frontend

from tkinter import *
import tkinter.messagebox

import stdDatabase_Backend

class Student():

    def __init__(self, root):
        self.root = root
        self.root.title("Akwins - Your Student Data Manager")
        self.root.geometry("1350x7500+0+0")
        self.root.config(bg = "#3399FF")

        StdID = StringVar()
        Firstname = StringVar()
        Lastname = StringVar()
        DOB = StringVar()
        Age = StringVar()
        Gender = StringVar()
        Address = StringVar()
        Mobile = StringVar()

#==========================================================================================================================================================

        def iExit():
                iExit = tkinter.messagebox.askyesno("Akwins", "Are you sure you want to exit?")
                if iExit > 0:
                        root.destroy()
        
        def ClearData():
                self.txtStdID.delete(0, END)
                self.txtFirstname.delete(0, END)
                self.txtLastname.delete(0, END)
                self.txtDOB.delete(0, END)
                self.txtAge.delete(0, END)
                self.txtGender.delete(0, END)
                self.txtAddress.delete(0, END)
                self.txtMobile.delete(0, END)

        def AddData():
                if(len(StdID.get()) != 0):
                        stdDatabase_Backend.AddStdRec(StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                        MyStudentList.delete(0, END)
                        MyStudentList.insert(END, (StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()))

        def DisplayData():
               MyStudentList.delete(0, END)
               for row in stdDatabase_Backend.viewData():
                        MyStudentList.insert(END, row, str(""))

        
        
        def StudentRec(event):
                global sd
                
                searchStd = MyStudentList.curselection() [0]
                sd = MyStudentList.get(searchStd)

                self.txtStdID.delete(0, END)
                self.txtStdID.insert(END, sd[1])
                self.txtFirstname.delete(0, END)
                self.txtFirstname.insert(END, sd[2])
                self.txtLastname.delete(0, END)
                self.txtLastname.insert(END, sd[3])
                self.txtDOB.delete(0, END)
                self.txtDOB.insert(END, sd[4])
                self.txtAge.delete(0, END)
                self.txtAge.insert(END, sd[5])
                self.txtGender.delete(0, END)
                self.txtGender.insert(END, sd[6])
                self.txtAddress.delete(0, END)
                self.txtAddress.insert(END, sd[7])
                self.txtMobile.delete(0, END)
                self.txtMobile.insert(END, sd[8])

        def searchDatabase():
                MyStudentList.delete(0, END)
                for row in stdDatabase_Backend.searchData(StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get()):
                        MyStudentList.insert(END, row, str(""))

        def update():
              if(len(StdID.get()) != 0):
                      stdDatabase_Backend.deleteRec(sd[0]) 

              if(len(StdID.get()) != 0):
                      stdDatabase_Backend.AddStdRec(StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())
                      MyStudentList.delete(0, END)
                      MyStudentList.insert(END, StdID.get(), Firstname.get(), Lastname.get(), DOB.get(), Age.get(), Gender.get(), Address.get(), Mobile.get())

                
        def DeleteData():
                if(len(StdID.get()) != 0):
                        stdDatabase_Backend.deleteRec(sd[0])
                        ClearData()
                        DisplayData()


# =========================================================================================================================================================

        MainFrame = Frame(self.root, bg = "#3399FF")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd = 2, padx = 54, pady = 8, bg = "#F8F8FF", relief = RIDGE)
        TitleFrame.pack(side = TOP)
        
        self.lblTitle = Label(TitleFrame, font = ("Arial", 47 ,"bold"), text = "Akwins - System Data Manager", bg = "#F8F8FF")
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd = 2, width = 1350, height = 70, padx = 18, pady = 10, bg = "#F8F8FF", relief = RIDGE)
        ButtonFrame.pack(side = BOTTOM)

        DataFrame = Frame(MainFrame, bd = 1, width = 1350, height = 400, padx = 20, pady = 20, bg = "#3399FF")
        DataFrame.pack(side = BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd = 1, width = 1000, height = 600, padx = 20,  relief = RIDGE, bg = "#F8F8FF", font = ("Arial", 20 ,"bold"), text = "Student Info\n")
        DataFrameLEFT.pack(side = LEFT)

        DataFrameRIGHT = LabelFrame(DataFrame, bd = 1, width = 450, height = 300, padx = 31, pady = 3, relief = RIDGE, bg = "#F8F8FF", font = ("Arial", 20 ,"bold"), text = "Student Data\n")
        DataFrameRIGHT.pack(side = RIGHT)

# ===================================================================================================================================================================================================================================

        self.lblStdID = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Student ID:", padx = 2, pady = 2, bg = "#F8F8FF")
        self.lblStdID.grid(row = 0, column = 0, sticky = W)

        self.txtStdID = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = StdID, width = 39)
        self.txtStdID.grid(row = 0, column = 1)
#===================================================================================================================================================================================
        self.lblFirstname = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Firstname:", padx = 2, pady = 2, bg = "#F8F8FF")
        self.lblFirstname.grid(row = 1, column = 0, sticky = W)

        self.txtFirstname = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = Firstname, width = 39)
        self.txtFirstname.grid(row = 1, column = 1)

#======================================================================================================================================================================================================

        self.lblLastname = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Lastname:", padx = 2, pady = 2, bg = "#F8F8FF")
        self.lblLastname.grid(row = 2, column = 0, sticky = W)

        self.txtLastname = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = Lastname, width = 39)
        self.txtLastname.grid(row = 2, column = 1)

# ===================================================================================================================================================================================================================================

        self.lblDOB = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Date Of Birth:", padx = 2, pady = 3, bg = "#F8F8FF")
        self.lblDOB.grid(row = 3, column = 0, sticky = W)

        self.txtDOB = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = DOB, width = 39)
        self.txtDOB.grid(row = 3, column = 1)

# ===================================================================================================================================================================================================================================

        self.lblAge = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Age:", padx = 2, pady = 3, bg = "#F8F8FF")
        self.lblAge.grid(row = 4, column = 0, sticky = W)

        self.txtAge = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = Age, width = 39)
        self.txtAge.grid(row = 4, column = 1)

# ===================================================================================================================================================================================================================================

        self.lblGender = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Gender:", padx = 2, pady = 3, bg = "#F8F8FF")
        self.lblGender.grid(row = 5, column = 0, sticky = W)

        self.txtGender = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = Gender, width = 39)
        self.txtGender.grid(row = 5, column = 1)

# ===================================================================================================================================================================================================================================

        self.lblAddress = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Address:", padx = 2, pady = 3, bg = "#F8F8FF")
        self.lblAddress.grid(row = 6, column = 0, sticky = W)

        self.txtAddress = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = Address, width = 39)
        self.txtAddress.grid(row = 6, column = 1)

# ===================================================================================================================================================================================================================================

        self.lblMobile = Label(DataFrameLEFT, font = ("Arial", 20 ,"bold"), text = "Mobile No:", padx = 2, pady = 3, bg = "#F8F8FF")
        self.lblMobile.grid(row = 7, column = 0, sticky = W)

        self.txtMobile = Entry(DataFrameLEFT, font = ("Arial", 20 ,"bold"), textvariable = Mobile, width = 39)
        self.txtMobile.grid(row = 7, column = 1)

#=====================================================================================================================================================================================================================================


        MyScrollbar = Scrollbar(DataFrameRIGHT)
        MyScrollbar.grid(row = 0, column = 1, sticky = "ns")

        MyStudentList = Listbox(DataFrameRIGHT, width = 41, height = 16, font = ("Arial", 12, "bold"), yscrollcommand = MyScrollbar.set)
        MyStudentList.bind('<<ListboxSelect>>', StudentRec)
        MyStudentList.grid(row = 0, column = 0, padx = 8)

        MyScrollbar.config(command = MyStudentList.yview)

#===================================================================================================================================================================

        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Add New", height = 1, width = 10, bd = 4, command = AddData)
        btnAddNew.grid(row = 0, column = 0)
        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Display", height = 1, width = 10, bd = 4, command = DisplayData)
        btnAddNew.grid(row = 0, column = 1)
        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Clear", height = 1, width = 10, bd = 4, command = ClearData)
        btnAddNew.grid(row = 0, column = 2)
        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Delete", height = 1, width = 10, bd = 4, command = DeleteData)
        btnAddNew.grid(row = 0, column = 3)
        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Search", height = 1, width = 10, bd = 4, command = searchDatabase)
        btnAddNew.grid(row = 0, column = 4)
        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Update", height = 1, width = 10, bd = 4, command = update)
        btnAddNew.grid(row = 0, column = 5)
        btnAddNew = Button(ButtonFrame, font = ("Arial", 20 ,"bold"), text = "Exit", height = 1, width = 10, bd = 4, command = iExit)
        btnAddNew.grid(row = 0, column = 6)

if __name__ == "__main__":
    root = Tk()
    applicaton = Student(root)
    root.mainloop()
