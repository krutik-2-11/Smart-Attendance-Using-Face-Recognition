#import module from tkinter for UI
from tkinter import *
#from playsound import playsound
import os
from datetime import datetime;
#creating instance of TK
root=Tk()

root.configure(background="white")

#root.geometry("300x300")

def enterStudent():
    
    os.system("EnterStudentInfo.py")
    
def trainDataset():
    
    os.system("py training_dataset.py")

def takeAttendance():

    os.system("py recognizer.py")
    playsound('sound.mp3')

#def attendanceSheet():    
  # os.startfile(os.getcwd()+"/developers/diet1frame1first.html");

#def credit():
   # os.startfile(os.getcwd()+"/firebase/attendance_files/attendance"+str(datetime.now().date())+'.xls')
   
def exitWindow():

    root.destroy()

#stting title for the window
root.title("FACE RECOGNITION ATTENDANCE SYSTEM")

#creating a text label
Label(root, text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",20),fg="white",bg="maroon",height=2).grid(row=0,rowspan=2,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating first button
Button(root,text="Enter New Student",font=("times new roman",20),bg="#0D47A1",fg='white',command=enterStudent).grid(row=3,columnspan=2,sticky=W+E+N+S,padx=5,pady=5)

#creating second button
Button(root,text="Train Dataset",font=("times new roman",20),bg="#0D47A1",fg='white',command=trainDataset).grid(row=4,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating third button
#Button(root,text="Recognize + Attendance",font=('times new roman',20),bg="#0D47A1",fg="white",command=takeAttendance).grid(row=5,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#creating attendance button
#Button(root,text="Attendance Sheet",font=('times new roman',20),bg="#0D47A1",fg="white",command=attendanceSheet).grid(row=6,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

#Button(root,text="Developers and Credits",font=('times new roman',20),bg="#0D47A1",fg="white",command=credit).grid(row=8,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)

Button(root,text="Exit",font=('times new roman',20),bg="maroon",fg="white",command=exitWindow).grid(row=9,columnspan=2,sticky=N+E+W+S,padx=5,pady=5)


root.mainloop()
