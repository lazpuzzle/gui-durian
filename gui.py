from tkinter import *
from tkinter import ttk, messagebox

emp = {
    000 : 'HP',
    '111' : 'LG',
    '222' : 'MSI'
}
GUI = Tk()
GUI.title('My program')
GUI.geometry('500x300')

L = Label(GUI, text = 'please enter you ssid : ', font=('Angsana New',20)).pack(pady=20)

v_text = StringVar()
E1 = ttk.Entry(GUI, textvariable= v_text, font=('Angsana New',20))
E1.pack(pady=20)

def Click():
    code = v_text.get()
    print('Code :', code)
    if code in emp:
        result = emp[code]
        messagebox.showinfo('info','Result Code: {} Name : {}'.format(code, result))
    else:
        messagebox.showwarning('Error','Result: Error, Code Not Found')

B1 = ttk.Button(GUI, text='Search', command=Click)
B1.pack(ipadx=50, ipady=30, pady=30)

GUI.mainloop()