from tkinter import *
import os
def shutdown():
	return os.system("shutdown /s /t 1")
def restart():
	return os.system("shutdown /r /t 1")
def logout():
	return os.system("shutdown -l")
master = Tk()
master.configure(bg='light grey')
Button(master, text="Shutdown", command=shutdown).grid(row=0, column = 0)
Button(master, text="Restart", command=restart).grid(row=0, column = 1)
Button(master, text="Log out", command=logout).grid(row=0, column = 2)
mainloop()

