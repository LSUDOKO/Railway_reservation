import mysql.connector as mycon
mydb=mycon.connect(host="localhost",user="root",password="1234")
mycur=mydb.cursor()
from datetime import date
import random as ra

def create_database():
    mycur.execute("create database if not exists RAILWAY")
create_database()

def create_table():
    mycur.execute("use railway ")
    mycur.execute("create table if not exists details( username varchar(50) ,pass varchar(50),phone char(10) primary key)")
create_table()

def details():
    mycur.execute("use railway ")
    mycur.execute("show tables")
    rec=mycur.fetchall()
    for i in rec:
        print(i)

        
def details_():
    mycur.execute("use railway ")
    mycur.execute("select * from details")
    rec=mycur.fetchall()
    for i in rec:
        print(i)
#-----------------------------------------------------------MAIN 2----------------------------------------------------
def main():
    print("\n")
    print("1 BOOK TICKET -")
    print("2 CANCEL TICKET -")
    print("3 UPDATE YOUR PROFILE -")
    print("4 TRAIN DETAILS -")
    print("5 VIEW TICKET -")
    print("6 ISSUE -")
    print("7 FOOD SECTION -")
    print("8 LOG OUT -")
    print("9 GO TO HOME PAGE -")
    print("\n")
    c2=int(input("ENTER YOUR CHOICE :"))
    if c2==1:
        booking()
    elif c2==2:
        cancel()
    elif c2==3:
        up_profile()
    elif c2==4:
        mapp()
    elif c2==5:
        view()
    elif c2==6:
        issue()
    elif c2==7:
        food_de()
    elif c2==8:
        ex()
    elif c2==9:
        log_sign()
    else:
        print("INVALID INPUT :")
        main()
#---------------------------------------------INSERT-----------------------------------------------------------        
def insert():
    global ph
    global pas
    print(" ✅"*23)
    mycur=mydb.cursor()
    mycur.execute("use railway")
    usename=input("ENTER YOUR USER NAME :")
    phone=input("ENTER YOUR PHONE NUMBER :")
    password=input("ENTER YOUR PASSWORD :")
    c_pass=input("ENTER YOUR PASSWORD AGAIN :")
    if password!=c_pass:
        print("WRONG PASSWORD")
        insert()
    elif len(str(password))<8:
        print("\n")
        print("ENTER ATLEAST 8 DIGIT PASSWORD")
        print("\n")
        insert()
    elif len(str(phone))!=10:
            print("ENTER 10 DIGIT PHONE NUMBER :")
            insert()
    else:
        r1=ra.randrange(10,20)
        r2=ra.randrange(10,20)
        print("PROVE YOU ARE NOT A ROBOT :",r1,"+",r2)
        user_ans=int(input("enter your ans"))
        if user_ans==r1+r2:
            try:
                mycur=mydb.cursor()
                sql="insert into details values('{}','{}','{}')".format(usename,password,phone)
                mycur.execute(sql)
                mydb.commit()
                print("ACCOUNT CREATED SUCESSFULLY...\n")
                log_sign()
            except:
                print("PHONE NUMBER ALREADY EXIST :")
                insert()
        else:
            print("❎"*10,"WRONG OUTPUT","❎"*10)
            insert()      
#-----------------------------------------------LOGIN-------------------------------------------------------------
def login():
    global ph
    global pas
    print("✅"*25,"LOGIN","✅"*25)
    ph=input("ENTER YOUR PHONE NUMBER :")
    pas=input("ENTER PASSWORD :")
    mycur.execute("use railway")
    a="select * from details where phone='{}' and pass='{}'".format(ph,pas)
    mycur.execute(a)
    rec=mycur.fetchall()
    if  rec==[]:
        print("DATA  NOT  FOUND")
        log_sign()
        
    else:
        print("LOGIN  SUCCESSFULLY")
        print(" HEY ",rec[0][0])
        main()
        return True
#-------------------------------------------------DELETE-------------------------------------------------------
def delete():
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    print("❎"*15,"DELETE  YOUR  ACCOUNT","❎"*15)
    ph=input("ENTER YOUR PHONE NUMBER")
    pas=input("ENTER PASSWORD : ")
    mycur.execute("use railway")
    mycur.execute("select phone,pass from details where phone='{}' and pass='{}'".format(ph,pas))
    rec=mycur.fetchall()
    for x in rec:
        if x[0]==ph and x[1]==pas:
            mycur.execute("delete from details where phone='{}' and pass='{}'".format(ph,pas))
            mydb.commit()
            print("YOUR  ACCOUNT  DELETED  SUCCESSFULLY ")
            log_sign()
        else:
            print("DATA NOT FOUND")
            log_sign()
#--------------------------------------------EXIT-----------------------------------------------------------
def ex():
    exit()
#----------------------------------------
def c_tdetails():
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway ")
    mycur.execute("create table if not exists tdetails(train_no char(5) not null ,\
tname varchar(50) not null ,sfrom varchar(25) not null,sto varchar(25) not null ,\
day varchar(50) not null,time float(10) not null)")
c_tdetails()    

#-------------------------------------------TRAIN DETAILS---------------------------------------------------
def ins_train():
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()

    mycur.execute("use railway")
    a="insert into tdetails values(%s,%s,%s,%s,%s,%s)"
    value=[("12267","MUMBAI CENTRAL - AHMEDABAD DURONTO EXP","MUMBAI","AHMEDABAD","M,T,W,T,F,SU,ST",23.25),\
           ("22201","KOLKATA SEALDAH - PURI DURONTO EXPRESS","KOLKATA","PURI","M,W,F",20.00),("\
22204","SECUNDERABAD - VISAKHAPATNAM AC DURONTO EXPRESS","SECUNDERABAD","VISAKHAPATNAM","M,W,S",20.15),("\
12426","JAMMU TAWI - NEW DELHI RAJDHANI EXPRESS","JAMMU","NEW DELHI","M,T,W,T,F,S,S",19.40),("\
12019","HOWRAH - RANCHI SHATABDI EXPRESS","HOWRAH","RANCHI","M,T,W,T,F,S",6.05),("\
12295","BANGALORE CITY - DANAPUR SANGHAMITRA SF EXP","BANGALORE","DANAPUR","M,T,W,T,F,S,S",9.00),("\
12801","PURI - NEW DELHI PURUSHOTTAM SF EXPRESS","PURI"," NEW DELHI","M,T,F",21.45),("\
12833","AHMEDABAD - HOWRAH SF EXPRESS","AHMEDABAD","HOWRAH","T,S",00.15)]
    mycur.executemany(a,value)
    mydb.commit()
#ins_train()
#-------------------------------------------------COUCH-----------------------------------------------------
def couch():
    mycur.execute("use railway")
    mycur.execute("create table if not exists couch( class varchar(10) not null,price float(5) not null)")
couch()
def in_couch():
    mycur.execute("use railway")
    a="insert into couch values (%s,%s)"
    v=[["AC",1200],["SLEEPER",700],["GENERAL",500]]
    mycur.executemany(a,v)
    mydb.commit()

def booking_table():
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    mycur.execute("create table if not exists booking(name varchar(10),mbno char(10),age int(5),gender char(1),stpoint varchar(20),endpoint varchar(20),dat date,tdat date,train_no varchar(50),couch varchar(10),FARE int,seat int)")
booking_table()
#------------------------------------------------------BOOKING---------------------------------------------------   
def booking():
    lst=[]
    lst2=[]
    import mysql.connector as mycon
    from datetime import date
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    name=input("ENTER YOUR NAME :")
    age=int(input("ENTER YOUR AGE :"))
    gen=input("ENTER YOUR GENDER (m--(male),f--(female),n--(none of these)")
    sql="select * from tdetails"
    mycur.execute(sql)
    rec=mycur.fetchall()
    for i in rec:
        print(i)
        lst2.append(i)
    trno=input("ENTER TRAIN NO FROM ABOVE LIST:")
    for o in lst2:
        if  o[0]==trno:  
            date1=input('ENTER DATE OF JOURNEY(dd):')
            date2=input('ENTER MONTH OF JOURNEY(mm):')
            date3=input('ENTER YEAR OF JOURNEY(yyyy):')
            today = date.today()
            dat=date3+"-"+date2+"-"+date1
            seat=ra.randrange(1,30)
            ticketno=ra.randrange(1,10)
            sql1="select * from couch"
            mycur.execute(sql1)
            rec1=mycur.fetchall()
            for n in rec1:
                print(n)
                lst.append(n)
            co=input("ENTER COUCH :")
            for i in lst:
                if i[0]==co.upper():
                    s="insert into booking values('{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(name,ph,age,gen,o[2],o[3],dat,today,o[0],i[0],i[1],seat)
                    mycur.execute(s)
                    mydb.commit()
                    print("TICKET BOOK SUCESSFULLY...")
                    main()
        else:
            print("ENTER CORRECT DATA")
            main()
#--------------------------------------------VIEW BOOKED TICKET-----------------------------------------
def view():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    mbno=input("ENTER MOBILE NUMBER : ")
    mycur.execute("select * from booking where mbno='{}'".format(mbno))
    rec=mycur.fetchall()
    for i in rec:
        print(i)
    mydb.commit()
    main()
#---------------------------------------------CANCEL BOOKED TICKET----------------------------------
def cancel():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    name=input("ENTER YOUR NAME :")
    mbno=input("ENTER MOBILE NUMBER : ")
    try:
        mycur.execute("select * from booking where name='{}' and mbno='{}'".format(name,mbno))
        rec=mycur.fetchall()
    except:
        print("ENTER CORRECT PHONE NUMBER AND NAME")
        main()
    try:
        mycur.execute("delete from booking where name='{}' and mbno='{}'".format(name,mbno))
        mydb.commit()
    except:
        print("DATA NOT FOUND...")
        main()
    for i in rec:
        print("YOUR TICKET CANCEL SUCESSFULLY")
        print("FROM ",i[4],"TO",i[5],"ON",i[6 ])
        main()
#-----------------------------------------------UPDATE PROFILE------------------------------------------- 
def up_profile():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    ph=input("ENTER MOBILE NUMBER :")
    pas=input("ENTER PASSWORD :")
    mycur.execute("use railway")
    mycur.execute("select phone,pass from details where phone='{}' and pass='{}'".format(ph,pas))
    rec=mycur.fetchall()
    for x in rec:
        if x[0]==ph and x[1]==pas:
            user=input("ENTER NEW USER NAME :")
            passw=input("ENTER NEW PASSWORD :")
            mycur.execute("update details set username='{}' ,pass='{}'where phone='{}'".format(user,passw,ph))
            mydb.commit()
            print("YOUR DATA UPDATE  SUCCESSFULLY ")
            main()
        else:
            print("DATA NOT FOUND")
            main()
#---------------------------------VIEW TRAIN DETAILS---------------------------------------------------
def mapp():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    value=[("12267","MUMBAI CENTRAL - AHMEDABAD DURONTO EXP","MUMBAI","AHMEDABAD","M,T,W,T,F,SU,ST",23.25),\
           ("22201","KOLKATA SEALDAH - PURI DURONTO EXPRESS","KOLKATA","PURI","M,W,F",20.00),("\
22204","SECUNDERABAD - VISAKHAPATNAM AC DURONTO EXPRESS","SECUNDERABAD","VISAKHAPATNAM","M,W,S",20.15),("\
12426","JAMMU TAWI - NEW DELHI RAJDHANI EXPRESS","JAMMU","NEW DELHI","M,T,W,T,F,S,S",19.40),("\
12019","HOWRAH - RANCHI SHATABDI EXPRESS","HOWRAH","RANCHI","M,T,W,T,F,S",6.05),("\
12295","BANGALORE CITY - DANAPUR SANGHAMITRA SF EXP","BANGALORE","DANAPUR","M,T,W,T,F,S,S",9.00),("\
12801","PURI - NEW DELHI PURUSHOTTAM SF EXPRESS","PURI"," NEW DELHI","M,T,F",21.45),("\
12833","AHMEDABAD - HOWRAH SF EXPRESS","AHMEDABAD","HOWRAH","T,S",00.15)]
    for i in value:
       print(i)
    main()
#-----------------------------------------ISSUE------------------------------------------------------------------
def cre_issue():
    mycur.execute("use railway")
    mycur.execute("create table if not exists issue(isssue varchar(100),phone char(10))")
cre_issue()
def issue():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    a="insert into issue value(%s,%s)"
    m=input("ENTER YOUR ISSUE :")
    n=[(m,ph)]
    mycur.executemany(a,n)
    mydb.commit()
    print("YOUR ISSUE SUBMITTED SUCESSFULLY")
    main()
#---------------------------------FOOD SECTION--------------------------------------------------------------
def cr_food():
    mycur.execute("use railway")
    mycur.execute("create table if not exists food (food_name varchar(1000),veg_nonveg varchar(50),time varchar(50),fare int(10))")
cr_food()
def food():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    a=[("Bread Slice (2nos)50 gms,Veg cutlet (2nos) 100 gms,Butter in blister pack 8gms,Tomato ketchup in sachets(1nos)12gms,Casserole 1","\
veg","breakfast",100),("Bread Slice (2 nos) 50 gms,Omelette/Boiled Eggs (2 eggs) 90 gms,,Butter in blister pack 8gms,Tomato ketchup in sachets(1nos)","\
nonveg","breakfast",120),("Rice Plain 150 gms,2Parathas/4Chapatis in wrappers 100gms,Dal/sambar(Thick) 150 gms,Mix Veg 100gms,Pickly in sachet 12 gms","\
veg","lunch",150),("Rice Plain 150 gms,2Parathas/4Chapatis in wrappers 100gms,Dal/sambar(Thick) 150 gms,Chicken Curry (60 gms boneless chicken & Gravy 90 gms)","\
nonveg","lunch",180),("Rice- 200 gm Rajma/ Chole- 150 gm Pickle sachet/ blister pack- 10-15 gm Packed in Casserole, with Spoon, tissue paper, sanitizer (1ml sachet)","\
veg","dinner",150),("Butter chicken with 70 gms of Boneless chicken ","\
nonveg","dinner",200)]
    sql="insert into food values(%s,%s,%s,%s)"
    mycur.executemany(sql,a)
    mydb.commit()
#food()
def food_de():
    global asw
    asw=(ph,)
    
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    print("1. BREAKFAST")
    print("2.LUNCH")
    print("3.DINNER")
    ch=int(input("WHICH TYPE OF MEAL DO YOU WANT"))
    
    if ch==1:
        mycur.execute("select * from food where time='breakfast'")
        rec=mycur.fetchall()
        for i in rec:
            print(i)
        print("1.veg")
        print("2.non veg")
        cn=int(input("ENTER WHICH TYPE OF MEAL YOU WANT"))
        
        if cn==1:
            mycur.execute("select * from food where time='breakfast' and veg_nonveg='veg'")
            re=mycur.fetchall()
            for i in re:
                print(i)
                print(type(i))
                asw=asw+i
        if cn==2:
            mycur.execute("select * from food where time='breakfast' and veg_nonveg='nonveg'")
            re=mycur.fetchall()
            for i in re:
                print(i)
                asw=asw+i
    if ch==2:
        mycur.execute("select * from food where time='lunch'")
        rec=mycur.fetchall()
        for i in rec:
            print(i)
        print("1.veg")
        print("2.non veg")
        cn=int(input("ENTER WHICH TYPE OF MEAL YOU WANT"))
        if cn==1:
            mycur.execute("select * from food where time='lunch' and veg_nonveg='veg'")
            re=mycur.fetchall()
            for i in re:
                print(i)
                asw=asw+i
        if cn==2:
            mycur.execute("select * from food where time='lunch' and veg_nonveg='nonveg'")
            re=mycur.fetchall()
            for i in re:
                print(i)
                asw=asw+i
    if ch==3:
        mycur.execute("select * from food where time='dinner'")
        rec=mycur.fetchall()
        for i in rec:
            print(i)
        print("1.veg")
        print("2.non veg")
        cn=int(input("ENTER WHICH TYPE OF MEAL YOU WANT"))
        
        if cn==1:
            mycur.execute("select * from food where time='dinner' and veg_nonveg='veg'")
            re=mycur.fetchall()
            for i in re:
                print(i)
                asw=asw+i
        if cn==2:
            mycur.execute("select * from food where time='dinner' and veg_nonveg='nonveg'")
            re=mycur.fetchall()
            for i in re:
                print(i)
                asw=asw+i
    print(asw)
    foodby()
def cre_food():
    mycur.execute("use railway")
    mycur.execute("create table if not exists foodby(phone char(10),food_name varchar(1000),veg_nonveg varchar(50),time varchar(50),fare  int(10))")
cre_food()
def foodby():
    import mysql.connector as mycon
    mydb=mycon.connect(host="localhost",user="root",password="1234")
    mycur=mydb.cursor()
    mycur.execute("use railway")
    lstf=[list(asw)]
    sql="insert into foodby values(%s,%s,%s,%s,%s)"
    mycur.executemany(sql,lstf)
    mydb.commit()
    print("FOOD SECTION FULL SUCESSFULLY")
    main()
#-----------------------------------------------------------MAIN 1---------------------------------------------------
def log_sign():
    print("🚉"*32,"WELCOME  TO  THE  RAILWAY  RESERVATION  SYSTEM ","🚉"*33)
    print("\n")
    print("1. CREATE  ACCOUNT :")
    print("2. LOGIN :")
    print("3. DELETE  ACCOUNT :")
    print("4. EXIT ")
    print("\n")
    c1=int(input("enter your choice"))
    if c1==1:
        insert()
    elif c1==2:
        login()
    elif c1==3:
        delete()
    elif c1==4:
        ex()
    else:
        print("wrong input choosen")
        log_sign()
log_sign()

    
