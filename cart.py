import mysql.connector;

conn = mysql.connector.connect(host='localhost' , database = 'test' , user='root',
                               password='')


if conn.is_connected():
    print("Connected")



def insertdata(oid,cn,ina,qt):
    if (conn.is_connected()):
        cursor = conn.cursor()
        sql = "insert into cart values('%d','%s','%s','%d')"
        args=(oid,cn,ina,qt)
        cursor.execute(sql%args)
        conn.commit()
        print("inserted")


def createDB():
    cursor = conn.cursor()
    sql = "create table cart(orderid int(2),custname varchar(10),itemname varchar(10) , qty int(2))"
    cursor.execute(sql)
    print("done")

createDB()

def displayDelete(idd):
   if conn.is_connected():
       cursor = conn.cursor()
       sql = "delete from cart where orderid='%d'"
       args=(idd)
       cursor.execute(sql%args)
       conn.commit()
       cursor.close()
       print("record successfully Deleted")


def displayAll():
   if conn.is_connected():
       cursor = conn.cursor()
       sql = 'select * from cart'
       cursor.execute(sql)
       rows=cursor.fetchall()
       for row in rows:
           print(row)
           cursor.close()


def update(oid,cn,ina,qt):
    if (conn.is_connected()):
        cursor = conn.cursor()
        sql = "update cart  set custname='%s' and   itemname='%s' and qty='%s'   where orderid='%d' "
        args=(oid,cn,ina,qt)
        cursor.execute(sql%args)
        conn.commit()
        print("Updated")


def displayArgs(eno):
   if conn.is_connected():
       cursor = conn.cursor()
       sql = "select * from cart where orderid='%d'"
       args=(eno)
       cursor.execute(sql%args)
       rows=cursor.fetchall()
       for row in rows:
           print("\n\n\n\n\nOrder id is         ",row[0])
           print("Custermer name is   ",row[1])
           print("Item name  is       ",row[2])
           print("Qty  is             ",row[3])
           cursor.close()


#createDB()

ch=0
while ch!=5:
    print("1) Insert ")
    print("2) Update ")
    print("3) Delete ")
    print("4) Bill ")
    print("5) Exit ")
    ch=int(input("Enter your choice "))
    if ch==1:
        a=int(input("Enter Order id "))
        b=input("Enter cust name ")
        c=input("Enter item name ")
        d=int(input("Enter Qty "))
        insertdata(a,b,c,d)
    elif ch==2:
        a=int(input("Enter Order id "))
        b=input("Enter cust name ")
        c=input("Enter item name ")
        d=int(input("Enter Qty "))
        update(a,b,c,d)
    elif ch==3:
        a=int(input("Enter Order id "))
        displayDelete(a)
    elif ch==4:
        a=int(input("Enter Order id "))
        displayArgs(a)
    else:
        print("invalid choice")
