import csv
from time import strftime
from tkinter import *
from tkinter import ttk, messagebox
from datetime import datetime

def timestamp(thai=True):
    if thai == True:
        # TH Date
        stamp = datetime.now()
        stamp = stamp.replace(year=stamp.year + 543)
        stamp = stamp.strftime("{} : %Y-%m-%d {} : %H:%M:%S").format('Date','Time')
    else:
        stamp = datetime.now().strftime("{} : %Y-%m-%d {} : %H:%M:%S").format('Date','Time')
    return stamp

def writefile(quan, price,cal):
    filename = 'data.txt'
    stamp = timestamp()
    
    with open(filename,'a',encoding='utf-8') as file:
        file.write('\n'+ 'Durian : {} kg, price : {} bath, total : {} bath, datetime : {}'.format(quan, price, cal,stamp))
        print('write file complete')

def writecsv(data):
    with open('data.csv','a',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('Write Success')

def readcsv():
    with open('data.csv',newline='',encoding='utf-8') as file:
        fr = csv.reader(file)
        data = list(fr)
        return data

def sumdata():
    result = readcsv()
    sumlist_quan = []
    sumlist_total = []
    for i in result:
        sumlist_quan.append(float(i[1]))
        sumlist_total.append(float(i[2]))
    sumqunan = sum(sumlist_quan)
    sumtotal = sum(sumlist_total)
    return (sumqunan, sumtotal)

def Calculate(event=None):
    quantity = v_quantity.get()
    price = 100
    cal = float(quantity) * price
    print('จำนวน', cal)
    data = [timestamp(), quantity, cal]
    try:
        writefile(quantity,price,cal)
        writecsv(data)
        messagebox.showinfo('total price', 'Durian {} kg price: {:,.2f} bath'.format(quantity,cal))
    except Exception as e:
        print(e)
        messagebox.showinfo('Error', 'Error something')
    
    v_quantity.set('') # clear data
    B1.focus()
    # E1.focus()

GUI = Tk()
GUI.geometry('600x500')
GUI.title('my program')

file = PhotoImage(file='rw.png',height=100,width=100)
IMG = Label(GUI, image=file,text='')
IMG.pack()

L1 = Label(GUI, text='program cal durian', font=('Angsana New','30','bold'))
L1.pack()

L2 = Label(GUI, text='Number of durian', font=('Angsana New','30','bold'),fg='blue')
L2.pack()

v_quantity = StringVar() #position var save data
E1 = ttk.Entry(GUI, textvariable=v_quantity,font=('impact',30))
E1.pack()

B1 = ttk.Button(GUI, text='cal',command=Calculate)
B1.pack(ipadx=30,ipady=20,pady=20)

E1.bind('<Return>',Calculate)

def SummaryData(event):
    # pop up
    sm = sumdata()
    title = 'ยอดสรุปรวมทั้งหมด'
    text = 'จำนวนที่ขายได้ : {} กก. \n ยอดขาย : {:,.2f} บาท'.format(sm[0],sm[1])
    messagebox.showinfo(title,text)
GUI.bind('<F1>', SummaryData)

B1.focus() # ให้ cursor ย้ายไปยังตำแหน่งของ E1
GUI.mainloop()