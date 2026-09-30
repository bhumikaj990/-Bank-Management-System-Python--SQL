from mysql import connector
conn=connector.connect(
    user='root',
    password='Bhumika@123',
    host='localhost',
    port=3306,
    database='bank_management_database'
)
print("connected succesfully...")

cur=conn.cursor()

def create_account():
    name=input("enter the name :")
    phone=input("enter the phone number :")
    address=input("enter the address :")
    balance=float(input("enter the balance :"))
    cur.execute("insert into accounts(name,phone,address,balance) values(%s,%s,%s,%s)",(name,phone,address,balance))
    conn.commit()
    print("account created succesfully...")
# create_account()    

def view_account():
    account_no=int(input("enter the account no :"))
    cur.execute(f"select * from accounts where account_no={account_no}")
    data=cur.fetchone()
    if data:
        print("account no :",data[0])
        print("Name       :",data[1])
        print("Phone      :",data[2])
        print("Address    :",data[3])
        print("Balance    :",data[4])
    else:
        print("Account not found")    

# view_account() 

def deposite_amount():
    account_no=int(input("enter the account no :"))
    cur.execute("select * from accounts")
    data=cur.fetchone()
    if account_no in data:
        amount=float(input("enter the amount :"))
        if amount>0:
            cur.execute(f"update accounts set balance=balance+{amount} where account_no={account_no}")
            print("Amount deposite succesfully")
        else:
            print("please enter the valid amount")    
    else:
        print("account no not exists")  
    conn.commit()        

# deposite_amount()  

def withdraw_amount():
    account_no=int(input("enter the account no :"))
    cur.execute("select * from accounts")
    data=cur.fetchone()
    if account_no in data:
        amount=float(input("enter the amount :"))
        if amount<data[4]:
            cur.execute(f"update accounts set balance=balance-{amount} where account_no={account_no}")
            print("Amount withdraw succesfully")
        else:
            print("insufficient balance")
        conn.commit()        

# withdraw_amount()

def check_balance():
    account_no=int(input("enter the account number :"))
    cur.execute(f"select * from accounts where account_no={account_no}")
    data=cur.fetchone()
    if data:
        balance=data[4]
        print("available balance :",balance)
    else:
        print("account not found")    
        conn.commit()

# check_balance()        

def delete_account():
    account_no=int(input("enter the account no :"))
    cur.execute(f"select * from accounts where account_no={account_no}")
    data=cur.fetchone()
    if data:
        cur.execute(f"delete from accounts where account_no={account_no}")
        print("account deleted succesfully")
    else:
        print("account not found")    
    conn.commit()
# delete_account()        

while True:
    print(f'''
          1.Create Account
          2.View Account
          3.Deposite Amount
          4.Withdraw amount
          5.Check Balance
          6.Delete Account
          7.Exit

         ''')
    choice=int(input("enter your choice :"))
    if choice==1:
        create_account()
    elif choice==2:
        view_account()
    elif choice==3:
        deposite_amount()
    elif choice==4:
        withdraw_amount()
    elif choice==5:
        check_balance()
    elif choice==6:
        delete_account()
    elif choice==7:
        print("Thank You...")    
        break
    else:
        print("invalid choice")                    

