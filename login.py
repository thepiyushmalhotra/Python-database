import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="cart"
)

def signup():
    a=input("Enter Name:")
    b=input("Enter Email:")
    c=input("Enter Password:")
    d=input("Enter City:")
    e=input("Enter Phone:")
    mycursor = mydb.cursor()
    sql = "INSERT INTO cart (name,email,password,city,phone) VALUES (%s,%s,%s,%s,%s)"
    val = (a,b,c,d,e)
    mycursor.execute(sql, val)
    mydb.commit()


def login():
    b=input("Enter Email:")
    c=input("Enter Password:")
    mycursor = mydb.cursor()
    sql = "SELECT * FROM cart where email=%s"
    val = (b,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    print (myresult)
    Email=myresult[0][1]
    Pass=myresult[0][2]
    if(b==Email and c==Pass):
        print("Login Successfully")
    else:
        print("Invalid ID or Password")

#mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE cart (name VARCHAR(255), email VARCHAR(255), password varchar(20), city varchar(20), phone varchar(20))")

print("Press 1 for Signup")
print("Press 2 for Login")
a=int(input("Enter Your Choice:"))
if(a==1):
    signup()
if(a==2):
    login()
