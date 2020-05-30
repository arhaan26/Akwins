import sqlite3
#Backend

def studentData():

    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS student(id INTEGER PRIMARY KEY, StdID text, Firstname text, Lastname text, DOB text, Age text, Gender text, Address text, Mobile text)")
    con.commit()
    con.close()

def AddStdRec(StdID, Firstname, Lastname, DOB, Age, Gender, Address, Mobile):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?)", (StdID, Firstname, Lastname, DOB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()

def viewData():
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    rows = cur.fetchall()
    con.close()
    return rows

def deleteRec(id):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(StdID = "", Firstname = "", Lastname = "", DOB = "", Age = "", Gender = "", Address = "", Mobile  = ""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student WHERE StdID = ? OR Firstname = ? OR Lastname = ? OR DOB = ? OR Age = ? OR Gender = ? OR Address = ? OR Mobile = ? ", (StdID, Firstname, Lastname, DOB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows

def updateData(id, StdID = "", Firstname = "", Lastname = "", DOB = "", Age = "", Gender = "", Address = "", Mobile  = ""):
    con = sqlite3.connect("student.db")
    cur = con.cursor()
    cur.execute("UPDATE student SET StdID = ? , Firstname = ? , Lastname = ? , DOB = ?, Age - ?, Gender = ?, Address, Mobile = ?", (StdID, Firstname, Lastname, DOB, Age, Gender, Address, Mobile, id))
    rows = cur.fetchall()
    con.close()
    return rows


studentData()