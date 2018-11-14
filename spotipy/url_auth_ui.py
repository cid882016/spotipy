from tkinter import *


class ReturnURLFromEntry:
    def __init__(self):
        self.url_value = None

        # Url Dialog ui elements
        self.master = Tk()
        self.master.title("Copy Webbrowser URL")

        self.empty_line = Label(self.master, text="", height=0, width=50)
        self.empty_line.pack()
        self.url_label = Label(self.master, text="Copy Webbrowser URL here:")
        self.url_label.pack()

        self.url_entry = Entry(self.master, width=50)
        self.url_entry.pack()
        self.url_entry.focus_set()

        self.empty_line = Label(self.master, text="", height=0, width=50)
        self.empty_line.pack()

        self.b = Button(self.master, text="Save and close", width=10, command=self.set_url_callback)
        self.b.pack()

        mainloop()

    def set_url_callback(self):
        self.url_value = self.url_entry.get()

        self.master.quit()
        self.master.destroy()

