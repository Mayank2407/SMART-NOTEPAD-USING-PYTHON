#Lect 21
import tkinter
import tkinter.ttk
root=tkinter.Tk()
root.geometry('500x400')
my_text=tkinter.Text(root)
my_text.config(wrap='word',relief=tkinter.FLAT)
my_Scroll_bar=tkinter.ttk.Scrollbar(root)
my_Scroll_bar.pack(side=tkinter.RIGHT,fill=tkinter.Y)
my_text.pack(fill=tkinter.BOTH,expand=True)
my_Scroll_bar.config(command=my_text.yview)
my_text.config(yscrollcommand=my_Scroll_bar.set)
root.mainloop()