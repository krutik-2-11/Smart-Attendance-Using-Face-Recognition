# Import OpenCV2 for image processing
import cv2
import os
from tkinter import *
from Globals import *
import sqlite3
master = Tk()

Label(master, text='Enrollment Number').grid(row=0)
Label(master, text='First Name').grid(row=1)
Label(master, text='Last Name').grid(row=2)
Label(master, text='Year').grid(row=3)
Label(master, text='Branch').grid(row=4)
e1 = Entry(master) 
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)
e1.grid(row=0, column=1) 
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)


def takeImage():        
    enrollment=(e1.get())
    first_name=(e2.get())
    last_name=(e3.get())
    year=(e4.get())
    branch=(e5.get())
    if(enrollment!=None and first_name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "haarcascade_frontalface_default.xml"
        detector=cv2.CascadeClassifier(harcascadePath)
        sampleNum=0
        while(True):
            ret, img = cam.read()
            #gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(img, 1.3, 5)
            for (x,y,w,h) in faces:
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)        
                #incrementing sample number 
                sampleNum=sampleNum+1

                if not os.path.exists('dataset/' + enrollment):
                    os.mkdir('dataset/' + enrollment)
                cv2.imwrite("dataset/" + enrollment + "/" +  str(sampleNum) + ".jpg", img[y:y+h,x:x+w])
                #display the frame
                cv2.imshow('frame',img)
            #wait for 100 miliseconds 
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum>30:
                break
        cam.release()
        insertOrUpdate()
        os.system('spreadsheet.py')
        cv2.destroyAllWindows()
        
        

def insertOrUpdate() :                                            # this function is for database
    enrollment = (e1.get())
    first_name = (e2.get())
    last_name = (e3.get())
    year = (e4.get())
    branch = (e5.get())

    connect = sqlite3.connect('Student_Database.db')
    print ("Opened database successfully")
    connect.execute("CREATE TABLE IF NOT EXISTS Attendance(enrollment TEXT, first_name TEXT, last_name TEXT, year TEXT,branch TEXT)")
    cmd = "SELECT * FROM Attendance WHERE enrollment = " + enrollment                             # selecting the row of an id into consideration
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          # checking wheather the id exist or not
        isRecordExist = 1
    if isRecordExist == 1:                                                      # updating name and roll no
        #connect.execute("UPDATE Attendance SET first_name = ? WHERE enrollment = ?",(first_name, enrollment))
        #connect.execute("UPDATE Attendance SET last_name = ? WHERE enrollment = ?",(last_name, enrollment))
        print('Sorry, Record already exist!!!')
    else:
    	params = (enrollment, first_name,last_name,year,branch)                                               # insering a new student data
    	connect.execute("INSERT INTO Attendance(enrollment,first_name,last_name,year,branch) VALUES(?, ?, ?,?,?)", params)
    connect.commit()                                                            # commiting into the database
    print("data fed successfully!!!")
    connect.close()         
   

    


Button(master,text="Take Image",font=('times new roman',20),bg="maroon",fg="white",command=takeImage).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)
mainloop()









