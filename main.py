# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import mysql.connector


def gen_table():
    print('Program starting')

    i=0
    j=0
    create={}

    mydb = mysql.connector.connect(host="localhost",user="root",password="Ayo128dhy",database="mysql")

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM REFTABLE")

    myresult = mycursor.fetchall()

    for z in myresult:
        print(z)

    for x in myresult:
        i=0
        if x[0] not in create.keys():
            create[x[0]] = ''
        for y in x:
            if i!=0:
                if i==3 and y!=None :
                    create[x[0]] = create[x[0]] + '(' + str(y) + ')' + ' '
                elif y!=None:
                    create[x[0]] = create[x[0]] + y + ' '
            i = i+1
        create[x[0]] = create[x[0]] + ','

    print(create)

    for t in create.keys():
        print('CREATE TABLE ' + t + '(' + create[t][:-1] + ')')
        mycursor.execute('CREATE TABLE ' + t + '(' + create[t][:-1] + ')')






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    gen_table()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
