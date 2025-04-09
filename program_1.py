#By: Sabria Fafach
#Date: April 9, 2025
#Title: program_1.py



import tkinter

class Favorite_saying:
    def __init__(self):
        self.main_window=tkinter.Tk()

        self.label=tkinter.Label(self.main_window,text="Only one life 'twill soon be passed.\n"
                                                       "Only what's done for God will last.\n"
                                                       "And when I die how glad I shall be,\n"
                                                       "if the light of my life has burnt out for thee.")

        self.label.pack()

        tkinter.mainloop()

if __name__ == '__main__':
    saying=Favorite_saying()



