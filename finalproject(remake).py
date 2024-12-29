import os
import pickle

class Account:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Contact:
    def __init__(self, name, number, division):
        self.name = name
        self.number = number
        self.division = division

# ini global integers jadi gw bisa pake ke mana mana
admin_account = Account("a", "a")
police_accounts = []
user_accounts = []
contacts = []
tries = 3
mode = 0

def load(): #fungsi ini khusus buat nge load file kaya lu nge load file di game ini fungsinya ini tuh namanya file handling cuman nambahin ini aja dan beberapa di fungsi lain
    global police_accounts, user_accounts, contacts #ini ngabil dari fungsi global di atas buat disini
    if os.path.exists('police_accounts.pkl'):
        with open('police_accounts.pkl','rb') as f:
            police_accounts = pickle.load(f) #ini artinya ngeload file police_account dalam mode read binary jadi cuman baca doang
            
    if os.path.exists('user_accounts.pkl'):
        with open('user_accounts.pkl', 'rb') as f:
            user_accounts =  pickle.load(f) #tambahan knp di dalam 'f'? karena kita sudah bilang bahwa os.path itu di representasikan dengan huruf f jadi dari pada tulis semua kita tulis apa yg kita udh representasikan aja
            
    if os.path.exists('contacts.pk'):
        with open('contacts.pkl', 'rb') as f:
            contacts = pickle.load(f)

def save(): #khusus buat ngesave data biar bisa di save atau di overwrite data
    with open('police_accounts.pkl','wb') as f: #kita edit file yg udh di bilin di load() dan buka dengan tipe AB maksudnya append binary artinya lu bisa nge update dari pada cuman overwrite 
        pickle.dump(police_accounts, f)
    with open('user_accounts.pkl', 'wb') as f:
        pickle.dump(user_accounts, f)
    with open('contacts.pkl', 'wb') as f:
        pickle.dump(contacts, f)        

def initmode():
    global mode
    print("Please choose the desired mode.\n")
    print("1. Admin")
    print("2. Police")
    print("3. User")
    print("4. Exit the program\n")
    
    select = int(input("Select: "))
    if select == 1:
        adminmode()
    elif select == 2:
        policemode()
    elif select == 3:
        usermode()
    elif select == 4:
        print("Exiting program...")
        exit()
    else:
        initmode()

def adminmode():
    global tries
    print("You have chosen Admin.")
    print("Please choose the desired mode.\n")
    print("1. Login")
    print("2. Back to the home page\n")

    select = int(input("Select: "))
    if select == 1:
        logadmin()
    elif select == 2:
        initmode()
    else:
        adminmode()

def logadmin():
    global tries
    if tries > 0:
        print(f"You have {tries} attempts left.\n")
        username = input("Username: ")
        password = input("Password: ")

        if username == admin_account.username and password == admin_account.password: #compare kalau password sama username lu sama atau ga
            adminmode2()
        else:
            tries -= 1
            logadmin()
    else:
        print("You have run out of attempts.")
        exit()

def adminmode2():
    global mode #ignore
    print("Welcome to the main menu!")
    print("Your current role is Admin\n")
    print("1. Accounts")
    print("2. Contacts")
    print("3. Log out\n")

    select = int(input("Select: "))
    if select == 1:
        accadmin()
    elif select == 2:
        contmain()
    elif select == 3:
        initmode()
    else:
        adminmode2()

def accadmin(): #cuman bisa di access sama admin
    print("You have chosen Accounts.")
    print("Please choose the desired mode.\n")
    print("1. View the currently registered accounts")
    print("2. Edit the currently registered accounts")
    print("3. Back to the main menu\n")

    select = int(input("Select: "))
    if select == 1:
        viewacc()
    elif select == 2:
        editacc()
    elif select == 3:
        adminmode2()
    else:
        accadmin()
        
def editacc(): 
    print("You have chosen edit account")
    print("Please choose what you want to do")
    print("1. Edit a Police account")
    print("2. Edit a User account")
    print("3. Go back to main menu")
    
    select = int(input("select: "))
    if select == 1:
        editaccpolice()
    elif select == 2:
        editaccuser()
    elif select == 3:
        adminmode2()
    else:
        editacc()
        
def editaccpolice():
    print("You are editing account for Police")
    print("What would you like to do?")
    print("1. Change username or password")
    print("2. Delete account")
    
    select = int(input("Select: "))
    
    if select == 1:
        changedetailpol()
    elif select == 2:
        deletepol()
    
def changedetailpol():
    print("You are viewing the account for police")
    if not police_accounts: #ini untuk bilang kalau ga ada data di codenya bakal jalanin code di bawah
        print("No account registerd")
    else:
        for acc in police_accounts:
            print(f"Username: {acc.username}")
    username = str(input("Enter the username you want to edit: "))
    
    account = next((acc for acc in police_accounts if acc.username == username), None) #ini untuk ngesearch apakah usernamenya ada atau ga
    #cara nya dengan mereka menggunakan integer "acc" dan mengabil dari list Police_accounts dengan menganbil acc yang di sini dengan acc yang di atas kita juga ngebilangin bahwa acc.username sama username yang di input itu sama
    #dengan membilang bahwa acc.username == username [nanti gw jelasin lebih jelas]
    
    if account: #ini untuk ngeinput username sama password baru
        new_username = str(input("Enter new username (Dont write if you want to keep the same one): "))
        new_password = (input("Enter new password (same thing leave it blank if you want to keep): "))
    
    if new_username: #ini dua untuk ngeupdate file/list supaya mereka ngeganti jadi password yg baru
        account.username = new_username
    if new_password:
        account.password = new_password
    
    accadmin()

def deletepol():
    global police_accounts
    
    print("You are viewing the account for police")
    if not police_accounts: 
        print("No account registerd")
    else:
        for acc in police_accounts:
            print(f"Username: {acc.username}")
    username = str(input("Enter the username you want to delete (case sensitive): "))
    
    police_accounts = [acc for acc in police_accounts if acc.username != username] #ini kalau mau gw jelasin jadi mereka nge cek dulu data satu persatu
    #arti dari acc.username != username kalau yg sebelumnya itu di masukin ke filenya kalau yg ini data yang tidak sama dari apa yang kita inputkan itu tidak akan di masukan ke file tersebut
    #jadi ilang aja yg di ouputkan atau yg di tetapkan di file itu yg tidak sama dengan apa yg kita input
    
    print(f"Username : {username} have been deleted")
    
    accadmin()
             
    
def editaccuser(): #ini sama aja kaya yg editpolice cuman beda di penamaan di fungsi fungsinya
    print("You are editing account for User")
    print("What would you like to do?")
    print("1. Change username or password")
    print("2. Delete account")
    
    select = int(input("Select: "))
    
    if select == 1:
        changedetailuser()
    elif select == 2:
        deleteuser()
    
def changedetailuser():
    print("You are viewing the account for User")
    if not user_accounts: 
        print("No account registerd")
    else:
        for acc in user_accounts:
            print(f"Username: {acc.username}")
    username = str(input("Enter the username you want to edit: "))
    
    account = next((acc for acc in user_accounts if acc.username == username), None) 
    
    if account: 
        new_username = str(input("Enter new username (Dont write if you want to keep the same one): "))
        new_password = (input("Enter new password (same thing leave it blank if you want to keep): "))
    
    if new_username: 
        account.username = new_username
    if new_password:
        account.password = new_password
    
    accadmin()

def deleteuser():
    global user_accounts
    print("You are viewing the account for police")
    if not user_accounts: 
        print("No account registerd")
    else:
        for acc in user_accounts:
            print(f"Username: {acc.username}")
    username = str(input("Enter the username you want to delete (case sensitive): "))
    
    user_accounts = [acc for acc in user_accounts if acc.username != username] #ini kalau mau gw jelasin jadi mereka nge cek dulu data satu persatu
    #arti dari acc.username != username kalau yg sebelumnya itu di masukin ke filenya kalau yg ini data yang tidak sama dari apa yang kita inputkan itu tidak akan di masukan ke file tersebut
    #jadi ilang aja yg di ouputkan atau yg di tetapkan di file itu yg tidak sama dengan apa yg kita input
    
    print(f"Username : {username} have been deleted")
    
    accadmin()


def viewacc():
    print("Choose what you want.\n")
    print("1. View all accounts")
    print("2. View only Police")
    print("3. View only User")
    
    select = int(input("Select: "))
    if select == 1:
        viewallacc()
    elif select == 2:
        viewonlypol()
    elif select == 3:
        viewonlyuser()
    else:
        viewacc()
        
def viewallacc():
    print("You are viewing all accounts")
    
    for account in police_accounts + user_accounts:
        print(f"Username: {account.username}, Role: {'Police' if account in police_accounts else 'User'}\n")
        
    choose = str(input(print("Do you want to go back? (Yes/No)")).strip().lower()) #artinya dari strip itu bisa di bilang mereka itu ngilang yg namanya "white space" apa artinya? mereka ngilangin spasi tabs dan enter dari kata yang di inputkan dan di ganti dengan lower biar jadi auto lower case selalu
    if choose == 'yes':
        adminmode2()
    elif choose == 'no':
        initmode()
        return
    else:
        viewallacc()

def viewonlypol():
    print("You are viewing all accounts in Police Section")
    
    for account in police_accounts:
        print(f"Username: {account.username}\n")
        
    choose = str(input(print("Do you want to go back? (Yes/No)")).strip().lower())
    if choose == 'yes':
        adminmode2()
    elif choose == 'no':
        initmode()
        return
    else:
        viewonlypol()
    
def viewonlyuser():
    print("You are viewing all accounts in User Section")
    
    for account in user_accounts:
        print(f"Username: {account.username}\n")
    choose = str(input(print("Do you want to go back? (Yes/No)")).strip().lower())
    if choose == 'yes':
        adminmode2()
    elif choose == 'no':
        initmode()
        return
    else:
        viewonlyuser()
    
    
def policemode():
    print("You have chosen Police.")
    print("Please choose the desired mode.\n")
    print("1. Login")
    print("2. Register")
    print("3. Back to the home page\n")

    select = int(input("Select: "))
    if select == 1:
        login_police()
    elif select == 2:
        register_police()
    elif select == 3:
        initmode()
    else:
        policemode()

def usermode():
    print("You have chosen User.")
    print("Please choose the desired mode.\n")
    print("1. Login")
    print("2. Register")
    print("3. Back to the home page\n")

    select = int(input("Select: "))
    if select == 1:
        login_user()
    elif select == 2:
        register_user()
    elif select == 3:
        initmode()
    else:
        usermode()

def register_police():
    print("Register as Police.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm your password: ")

    if any(account.username == username for account in police_accounts): #khusus ngecheck kalau namanya udh di ambil atau tidak dengan ngecompare yg udh ada di list sama yg di tulis
        print("Username exist please make another one :)")
        return register_police()
        
    if password == confirm_password:
        police_accounts.append(Account(username,password))
        save()
        print("Police account successfully registered!")
        goback('police')
    else:
        print("Passwords do not match. Try again.")
        register_police()
    initmode()

def register_user():
    print("Register as User.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    confirm_password = input("Confirm your password: ")
    
    if any(account.username == username for account in user_accounts): 
        print("Username exist please make another one :)")
        return register_user()

    if password == confirm_password:
        user_accounts.append(Account(username,password))
        save()
        print("User account successfully registered!")
        goback('user')
    else:
        print("Passwords do not match. Try again.")
        register_user()
    initmode()

def login_police():
    print("Login as Police.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for account in police_accounts:
        if account.username == username and account.password == password:
            print("Login successful!\n")
            policemode2()
    print("Invalid credentials. Try again.")
    policemode()

def policemode2():
    global mode
    print("Welcome your current role is Police!")
    print("Please choose what you want to do.")
    print("1. Add a Contact")
    print("2. View Contacts")
    print("3. Log out")
    
    select = int(input("Select: "))
    if select == 1:
        addcont()
    elif select == 2:
        contview(policemode2)
    elif select == 3:
        goback('police')
    else:
        policemode2()

def login_user():
    print("Login as User.")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    for account in user_accounts:
        if account.username == username and account.password == password:
            print("Login successful!\n")
            usermode2()
    print("Invalid credentials. Try again.")
    usermode()

def usermode2():
    global mode
    for account in user_accounts:
        print(f"Welcome to the main menu {account.username}")
        print("Please choose the desired options")
        print("Please choose what you want to do.")
        print("1. View a Contact")
        print("2. Log out")
        
        select = int(input("Select: "))
        if select == 1:
            contview(usermode2)
        elif select == 2:
            goback('user')
        else:
            usermode2()
            
        
def contmain():
    print("You have chosen Contacts.")
    print("Please choose the desired mode.\n")
    print("1. View Contacts")
    print("2. Edit Contacts")
    print("3. Back to the main menu\n")

    select = int(input("Select: "))
    if select == 1:
        contview(adminmode2)
    elif select == 2:
        contedit()
    elif select == 3:
        adminmode2()
    else:
        contmain()
    
def contview(return_func):
    print("You have Chosen View Contacts")
    print("Please choose the desired mode.\n")
    print("1. View all Contacts")
    print("2. View Per-Division")
    print("3. Back to menu")
    
    select = int(input("Select: "))
    if select == 1:
        contviewall()
    elif select == 2:
        contviewdiv()
    elif select == 3:
        return_func()
    else:
        contview(return_func)
        

def contedit():
    print("You have chosen Edit Contacts.")
    print("Please choose the desired mode.\n")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Back to the main menu\n")

    select = int(input("Select: "))
    if select == 1:
        addcont()
    elif select == 2:
        deletecont()
    elif select == 3:
        adminmode2()
    else:
        contedit()

def addcont():
    print("Add a new Contact.")
 
    name = input("Name: ")
    number = input("Phone Number: ")
    
    print("Please choose a division:")
    print("1. Monaka")
    print("2. Mya")
    print("3. Rimu")
    print("4. Moth")
    print("5. Yuina")

   
    while True:
        try: #karena kita akan membuat jawabannya menjadi integer buat main aman gw masukin try biar jalan codenya 
            #emg buat apa try? try itu salah satu bagian code dimana mereka "mencoba" codenya buat error jadi merekan kaya suruh codenya untuk "coda dah code ini jika mereka memberikan integer tapi kalau ga jalanin except"
            divchoice = int(input("Select a division (1-5): "))
            if 1 <= divchoice <= 5:
                divisions = ["Monaka", "Mya", "Rimu", "Moth", "Yuina"]
                division = divisions[divchoice - 1] #alasan knp gw kasih -1 karena di list buat python kan mereka mulainya dari 0 jadi kalau gw masukin satu di choice mereka malah bakal ke list yg kedua dan itu "Mya" jadi
                #untuk ngecounter ini gw kasih -1 biar input kita di kurangin 1 aja dari pada suruh mereka masukin 0-4
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    new_contact = Contact(name, number, division)
    contacts.append(new_contact)
    
    save()
    
    print(f"Contact {name} added successfully under division {division}.")
    policemode2()


def deletecont():
    print("Delete a Contact.")


def contviewall():
    print("View all Contacts.")

    
def contviewdiv():
    print("enter")
    
def goback(return_func):
    print("Do you want to go back to the login page?")
    
    select = (input("Yes/No : ").strip().lower())
    if select == "yes":
        if return_func == 'police':
            login_police()
        elif return_func == 'user':
            login_user()
        else:
            initmode()
    elif select == "no":
        initmode()
    else:
        goback(return_func)
        
        
    
load()
initmode()
