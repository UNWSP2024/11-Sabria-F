#By: Sabria Fafach
#Date: April 9, 2025
#Title: program_2.py


import tkinter
import tkinter.messagebox

class Info:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.my_button=tkinter.Button(self.main_window,text="Click for info.",command=self.show_info)
        self.quit_button=tkinter.Button(self.main_window,text="Quit",command=self.main_window.destroy)

        self.my_button.pack()
        self.quit_button.pack()

        tkinter.mainloop()

    def show_info(self):
        tkinter.messagebox.showinfo("Information","Sabria Fafach\n 1600 Pennsylvania Avenue NW,\n Washington, DC 20500")


if __name__ == '__main__':
    info=Info()


