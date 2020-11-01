#!/usr/bin/env python3

import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master=master
        self.pack()
        self.create_widgets()

    def create_widgets(self):

        # create a tkinter menu widget
        self.menubar = tk.Menu(self)
        """ activebackground
The background color that will appear on a choice when it is under the mouse. """
        self.menubar["activebackground"]="green"
        """activeborderwidth
Specifies the width of a border drawn around a choice when it is under the mouse.
Default is 1 pixel. """
        self.menubar["activeborderwidth"]= 5
        # activeforeground
        """ The foreground color that will appear on a choice when it is
under the mouse."""
        self.menubar["activeforeground"]="yellow"
        # bg
        """The background color for choices not under the mouse. """
        self.menubar["bg"]="red"
        # bd
        """The width of the border around all the choices. Default is 1. """
        self.menubar["bd"] = 5
        # cursor
        """The cursor that appears when the mouse is over the choices, but
only when the menu has been torn off. """
        self.menubar["cursor"] = "pirate"
        # disabledforeground
        """The color of the text for items whose state is DISABLED."""
        #self.menubar["disabledforeground"]= "DISABLED"

        # font
        """The default font for textual choices."""
        self.menubar["font"]="Helvetica"
        # fg
        """The foreground color used for choices not under the mouse."""
        self.menubar["fg"]="green"
        
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        # add_command (options)
        """Adds a menu item to the menu."""
        self.filemenu.add_command(label="New", command=None)
        self.filemenu.add_command(label="Edit", command=None)
        # add_radiobutton( options )
        """Creates a radio button menu item."""
        self.filemenu.add_radiobutton(label="Black")
        # add_checkbutton( options )
        """Creates a check button menu item. """
        self.filemenu.add_checkbutton(label="Red")
        # 5. add_separator()
        """Adds a separator line to the menu."""
        self.filemenu.add_separator()
        
        self.filemenu.add_command(label="Quit", command=self.master.destroy)
        # add_cascade(options)
        """Creates a new hierarchical menu by associating a given menu to a
parent menu"""
        self.menubar.add_cascade(label="File",menu=self.filemenu)

        self.master.config(menu=self.menubar)
        
        # create a tkinter menubutton widget
        self.tk_mb= tk.Menubutton(self, text="Tkinter Widgets")
        self.tk_mb.pack(side="top")
        self.tk_mb["activebackground"] = "blue"
        self.tk_mb["activeforeground"] = "red"
        self.tk_mb["anchor"] = "sw"
        self.tk_mb["bg"]="yellow"
        #self.tk_mb["bitmap"]="info"
        self.tk_mb["bd"] = 5
        self.tk_mb["cursor"] = "dot"
        
        self.menu = tk.Menu(self.tk_mb, tearoff=3)
        self.tk_mb["menu"] = self.menu
        self.menu.add_checkbutton(label="Label")
        self.menu.add_checkbutton(label="Button")
        
        # create a button
        self.hi_there=tk.Button(self)
        self.hi_there["text"]="Salut, Lume!\n(click me)"
        self.hi_there["command"]=self.say_hi
        self.hi_there.pack(side="top")

        # create quit button
        self.quit=tk.Button(self, text="QUIT", fg="red", command=self.master.destroy)
        self.quit.pack(side="bottom")

    # Function 
    def say_hi(self):
        print("Salut tuturor!")

root = tk.Tk()
root.title("Tkinter Menu")
root.geometry("600x750")
#root.config(menu=root.menubar)
app=Application(master=root)
app.mainloop()
