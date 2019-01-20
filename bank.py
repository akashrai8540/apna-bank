import sys
import datetime
import sqlite3
import re
account_no=0
d_name=''
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z ]')
    string = charRe.search(string)
    return not bool(string)
def mainscreen():
    try:
        print('\t\t\t APNA BANK')
        print('1:create account')
        print('2:Login')
        print('3:exit')
        ch=int(input('Please enter your choice'))
        return ch
    except:
        print("!OOPS Please enter correct choice and try again Later")
def valid_email(email_id):
    return bool(re.search(r"^[\w\.\+\-]+\@[\w]+\.[a-z]{2,3}$", email_id))
def create_account():
    u_name=input('enter user name for Registration eg:amit@123:...:')
    len1=len(u_name)
    if(len1<12):
        if(u_name.isdigit()):
            z=input("enter any key to exit")
            sys.exit()
        else:
            pass
    else:
        z=input("enter any key to exit")
        sys.exit()
    d_u_name=[]
    conn=sqlite3.connect('users_detail1.db')
    c=conn.cursor()
    c.execute('select u_name from info7')
    cust=c.fetchall()
    for i in cust:
        d_u_name.append(i[0])
    conn.commit()
    conn.close()
    if(u_name in d_u_name):
        print('User name already taken')
    else:
        print('User name avilable for registration')
        print('Now fill your full name,mobile no,email_id,aadhar_no one by one carefully')
        print('Do not provide any wrong information')
        cust_name=input('enter your full name')
        cust_name1= cust_name.replace(" ","")
        cust_name2=is_allowed_specific_char(cust_name)
        if(cust_name2):
            pass
        else:
            print('Invalid/Access denied')
            z=input("enter any key to exit")
            sys.exit()
        mobile_no=input('enter 10 digit mobile no excluding country code')
        len1=len(mobile_no)
        if((mobile_no.isdigit())and(len1==10)):
            pass
        else:
            print('Invalid/Access denied')
            z=input("enter any key to exit")
            sys.exit()
        email_id=input('enter your mail_id')
        emailid=valid_email(email_id)
        if(emailid):
            pass
        else:
            print('Invalid/Access denied')
            z=input("enter any key to exit")
            sys.exit()
			
        aadhar_no=input('enter your 12 digit aadhar no')
        len1=len(aadhar_no)
        if((aadhar_no.isdigit())and(len1==12)):
            pass
        else:
            z=input("enter any key to exit")
            print('Invalid/Access denied')
            sys.exit()
        conn=sqlite3.connect('users_detail1.db')
        c=conn.cursor()
        c.execute("insert into info7(u_name,name,mobile,email,aadhar) values(?,?,?,?,?)",(u_name,cust_name,mobile_no,email_id,aadhar_no))
        conn.commit()
        conn.close()
        conn=sqlite3.connect('users_detail1.db')
        c=conn.cursor()
        c.execute("select * from info7 where u_name=?",(u_name,))
        emp2 = c.fetchall()
        for k in emp2:
            print('HELLO %s you have created your account succesfully'%(cust_name))
            print(( "\nPlease note your account no and username for login= %d"%k[0])+(' , ')+u_name+('  respectively'))
        x=cust_name1+str(k[0])
        c.execute("create table {}(s_no integer primary key autoincrement ,date1 text,debit integer,credit integer,balance integer)".format(x))
        conn.commit()
        conn.close()
        conn=sqlite3.connect('users_detail1.db')
        c=conn.cursor()
        c.execute("insert into {}(balance) values(0)".format(x))
        conn.commit()
        conn.close()
        
def login():
    
    try:
        
        global account_no
        global d_name
        u_name=input('enter your user name for login')
        account_no=int(input('enter your account no'))
        conn=sqlite3.connect('users_detail1.db')
        c=conn.cursor()
        c.execute("select account_no,name from info7 where u_name=?",(u_name,))
        cust=c.fetchall()
        for i in cust:
            d_account_no=i[0]
            d_name=i[1]
        conn.commit()
        conn.close()
        if(account_no==d_account_no):
            return True
        else:
            return False
    except:
        pass
def main():
    try:
        print ('1.Deposit')
        print ('2.Withdrawl')
        print ('3.Balance')
        print ('4.Mini statement')
        print('5.Exit')
        ch=int(input('enter choice:'))
        return ch
    except:
        print('enter correct choice')
def deposit():
    global account_no
    global d_name
    d_name=d_name.replace(" ","")
    bal=input('enter balance to deposit in your account')
    len1=len(bal)
    if((bal.isdigit())and(len1<=6)):
        pass
    else:
        print("invalid amount/heavy amount")
        z=input("enter any key to exit")
        sys.exit()
    x=d_name+str(account_no)
    conn=sqlite3.connect('users_detail1.db')
    c=conn.cursor()
    c.execute("select max(s_no) from "+x)
    cust=c.fetchall()
    for i in cust:
        s_no1=i[0]
    c.execute("select balance from {} where s_no={}".format(x,s_no1))
    cust=c.fetchall()
    for i in cust:
        d_balance=i[0]
    d_new_balance=d_balance+int(bal)
    da=str(datetime.date.today())
    c.execute("insert into {}(date1,credit,balance) values({},{},{})".format(x,da,bal,d_new_balance))
    print('money deposited successfully')
    conn.commit()
    conn.close()
def balance():
    global account_no
    global d_name
    d_name=d_name.replace(" ","")
    x=d_name+str(account_no)
    conn=sqlite3.connect('users_detail1.db')
    c=conn.cursor()
    c.execute("select max(s_no) from "+x)
    cust=c.fetchall()
    for i in cust:
        s_no1=i[0]
    c.execute("select balance from {} where s_no={}".format(x,s_no1))
    cust=c.fetchall()
    for i in cust:
        s_no1=i[0]
    print("your total available balace is",s_no1)
    conn.commit()
    conn.close()
def withdrawl():
    global account_no
    global d_name
    d_name=d_name.replace(" ","")
    try:
        withd_amount=int(input('enter amount to withdrawl from account'))
    except:
        print("enter correct amount to withdrawl/try after few minute")
        z=input("enter any key to exit")
        sys.exit()
    x=d_name+str(account_no)
    conn=sqlite3.connect('users_detail1.db')
    c=conn.cursor()
    c.execute("select max(s_no) from "+x)
    cust=c.fetchall()
    for i in cust:
        s_no1=i[0]
    c.execute("select balance from {} where s_no={}".format(x,s_no1))
    cust=c.fetchall()
    for i in cust:
        s_no1=i[0]
    new_d_balance=s_no1-withd_amount
    if((s_no1<2000)or(new_d_balance<2000)):
        print('withdrawl amount can not be proccessd due to minimum balance')
    else:
        da=str(datetime.date.today())
        c.execute("insert into {}(date1,debit,balance) values({},{},{})".format(x,da,withd_amount,new_d_balance))
        print("successfully withdrawl ")
    conn.commit()
    conn.close()
def ministatement():
    global account_no
    global d_name
    d_name=d_name.replace(" ","")
    x=d_name+str(account_no)
    conn=sqlite3.connect('users_detail1.db')
    c=conn.cursor()
    c.execute("select * from "+x)
    cust=c.fetchall()
    print('s_no\tdate\tdebit\tcredit\tbalance')
    for i in cust:
        print(i[0],i[1],i[2],i[3],i[4])
    conn.commit()
    conn.close()
while True:
    screen=mainscreen()
    if screen==1:
        create_account()
    elif screen==2:
        match=login()
        if match:
            while True:
                m=main()
                if m==1:
                    deposit()
                    r=input('Do you want to continue (y/n)..:')
                    if r=='y':
                        continue
                    elif r=='n':
                        break
                    
                
                elif m==2:
                    withdrawl()
                    r=input('Do you want to continue (y/n)..:')
                    if r=='y':
                        continue
                    elif r=='n':
                        break   
                elif m==3:
                    balance()
                    r=input('Do you want to continue (y/n)..:')
                    if r=='y':
                        continue
                    elif r=='n':
                        break
                elif m==4:
                    ministatement()
                    r=input('do you want to continue(y/n)..:')
                    if r=='y':
                        continue
                    elif r=='n':
                        break
                else:
                    break
        else:
            print('Invalid details try again')
        r=input('Do you want to Return to HOME PAGE(y/n)..:')
        if r=='y':
            continue
        elif r=='n':
            break  
    else:
        print('invalid selection/access denied')
        z=input("enter any key to exit")
        sys.exit()
