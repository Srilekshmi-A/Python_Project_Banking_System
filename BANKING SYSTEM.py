#Python Project - Banking System

listusername = ["Anna", "Bob", "Catherine", "David", "Elsa", "Frank", "Geetha", "Harsha"]
listplace = ["Kerala", "Delhi", "Goa", "Tamilnadu", "Kerala", "Gujarath", "Kerala", "Kerala"]
listage = [27, 25, 63, 52, 65, 45, 56, 36]
listyear = [2022, 2019, 2006, 2005, 2004, 2010, 2015, 2014]
listpassword = ["1001", "2002", "3003", "4004", "5005", "6006", "7007", "8008"]
listbalance = [3000, 10000, 1000, 8000, 5005, 6006, 7007, 8008]
listtransaction = [30, 10, 52, 10, 5, 32, 7, 2]

from datetime import date

def start():
    print("---------WELCOME TO THE BANKING SYSTEM--------")

def stop():
    print("---------THANK YOU ! VISIT AGAIN--------")

def login():
    print('''        1)ACCOUNT LOGIN
        2)NEW ACCOUNT CREATION
        3)EXIT''')

    b = int(input("Enter your choice : "))

    if b == 1:
        username = input("Enter your username: ")  # get username
        password = input("Enter your password:  ")  # get password
        if username not in listusername:
            print("Invalid username")
            print("Try again!!")
        else:
            global nameindex
            nameindex = listusername.index(username)
            if listpassword[nameindex] == password:
                print("** Login Succesfull ** ")
                services()
            else:
                print("Incorrect password")
                print("Try again!!")
    elif b == 2:
        n=accountcreation()
    elif b==3:
        stop()
    else:
        print("Please enter a valid choice \n Try again")

def services():
    print('''        1)DEPOSIT MONEY
        2)WITHDRAW MONEY
        3)CHECK ACCOUNT BALANCE
        4)CHECK NUMBER OF TRANSACTIONS
        5)ACCOUNT HOLDER DETAILS''')

    d = int(input("Enter your choice: "))

    if d == 1:
        deposit = Depositmoney()
    elif d == 2:
        withdraw = Withdrawmoney()
    elif d == 3:
        bal = Checkaccountbalance()
    elif d == 4:
        tran = nooftranscations()
    elif d == 5:
        tran = details()
    else:
        print("Invalid choice")
        stop()

def Depositmoney():
    global money_to_be_deposited
    money_to_be_deposited = int(input("Enter amount to be deposited : "))

    if money_to_be_deposited < 100:
        print("Please deposit money in denominations of 100")
        print("Try again!!")
    else:
        listbalance[nameindex] += money_to_be_deposited
        listtransaction[nameindex] += 1
        print("**  Money deposited successfully  **")
        print('''            1)GO BACK TO SERVICES
                2)EXIT''')
        h = int(input("Enter your choice : "))
        if h == 1:
            services()
        elif h == 2:
            stop()
        else:
            print("invalid choice")
            stop()

def Withdrawmoney():
    global money_to_be_withdrawed
    money_to_be_withdrawed = int(input("Enter the amount to be withdrawn : "))

    if listbalance[nameindex] <= 1000:
        print("Cannot withdraw money from your account \n Need to maintain  minimum balance amount \n Try again!!")
    else:
        if money_to_be_withdrawed>=listbalance[nameindex]:
            print("Insufficient amount!!")
            stop()
        else:
            listbalance[nameindex] -= money_to_be_withdrawed
            listtransaction[nameindex] += 1
            print("**  Withdrawal Successful  **")
            print('''            1)GO BACK TO SERVICES
                    2)EXIT''')
            h = int(input("Enter your choice : "))
            if h == 1:
                services()
            elif h==2:
                stop()
            else:
                print("invalid choice")
                stop()

def nooftranscations():
    t = listtransaction[nameindex]
    print("Number of transactions till now is  ", t)
    print('''            1)GO BACK TO SERVICES
            2)EXIT''')
    h = int(input("Enter your choice : "))
    if h == 1:
        services()
    elif h == 2:
        stop()
    else:
        print("invalid choice")
        stop()

def Checkaccountbalance():
    x = listbalance[nameindex]
    print("Your account balance is ", x, "Rupees")
    print('''            1)GO BACK TO SERVICES
            2)EXIT''')
    h = int(input("Enter your choice : "))
    if h == 1:
        services()
    elif h == 2:
        stop()
    else:
        print("invalid choice")
        stop()

def accountcreation():
    global new_name
    new_name=input("Enter your Name : ")
    listusername.append(new_name)
    global new_age
    new_age= input("Enter your age : ")
    listage.append(new_age)
    global new_place
    new_place = input("Enter your Place : ")
    listplace.append(new_place)
    global new_year
    y1=date.today()
    new_year = y1.year
    listyear.append(new_year)
    global new_password
    new_password = input("Enter your Password : ")
    listpassword.append(new_password)
    listtransaction.append(0)
    listbalance.append(0)
    print("**  New account created  **")
    print("Login again to make transactions or Exit")
    l = login()

def details():
    print("Name : ", listusername[nameindex])
    print("Age : ", listage[nameindex])
    print("Place : ", listplace[nameindex])
    print("Year of opening account : ", listyear[nameindex])
    print('''            1)GO BACK TO SERVICES
            2)EXIT''')
    h = int(input("Enter your choice : "))
    if h == 1:
        services()
    elif h == 2:
        stop()
    else:
        print("invalid choice")
        stop()


start()
login()





















