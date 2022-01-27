import csv

def writecsv(data):
    with open('data.csv','w',newline='',encoding='utf-8') as file:
        fw = csv.writer(file)
        fw.writerow(data)
    print('Success')

d = ['2021-05-11 10:15:10',50,5000]
# writecsv(d)


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

result = sumdata()
print(result)

