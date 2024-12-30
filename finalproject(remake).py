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

admin_account = Account("a", "a")
police_accounts = []
user_accounts = []
contacts = []
tries = 3
mode = 0

def load(): 
    global police_accounts, user_accounts, contacts 
    if os.path.exists('police_accounts.pkl'):
        with open('police_accounts.pkl','rb') as f:
            police_accounts = pickle.load(f) 
            
    if os.path.exists('user_accounts.pkl'):
        with open('user_accounts.pkl', 'rb') as f:
            user_accounts =  pickle.load(f)
            
    if os.path.exists('contacts.pkl'):
        with open('contacts.pkl', 'rb') as f:
            contacts = pickle.load(f)

def save():
    with open('police_accounts.pkl','wb') as f:
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

        if username == admin_account.username and password == admin_account.password: 
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

def accadmin(): 
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
    if not police_accounts: 
        print("No account registerd")
    else:
        for acc in police_accounts:
            print(f"Username: {acc.username}")
    username = str(input("Enter the username you want to edit: "))
    
    account = next((acc for acc in police_accounts if acc.username == username), None) 
    
    if account: 
        new_username = str(input("Enter new username (Dont write if you want to keep the same one): "))
        new_password = (input("Enter new password (same thing leave it blank if you want to keep): "))
    
    if new_username: 
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
    
    police_accounts = [acc for acc in police_accounts if acc.username != username] 
    
    print(f"Username : {username} have been deleted")
    
    accadmin()
             
    
def editaccuser():
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
    
    user_accounts = [acc for acc in user_accounts if acc.username != username] 
    
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
        
    choose = str(input(print("Do you want to go back? (Yes/No)")).strip().lower())
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

    if any(account.username == username for account in police_accounts): 
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
        contviewall(return_func)
    elif select == 2:
        contviewdiv(return_func)
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
        try: 
            divchoice = int(input("Select a division (1-5): "))
            if 1 <= divchoice <= 5:
                division = ["Monaka", "Mya", "Rimu", "Moth", "Yuina"]
                div = division[divchoice - 1] 
                break
            else:
                print("Invalid choice. Please select a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    newcont = Contact(name, number, div)
    contacts.append(newcont)
    
    save()
    
    print(f"Contact {name} added successfully under division {div}.")
    policemode2()


def deletecont():
    print("Delete a Contact.")
    global contacts
    
    print("You are viewing the account for police")
    if not contacts: 
        print("No account registerd")
    else:
        for con in contacts:
            print(f"Username: {con.name}")
    name = str(input("Enter the username you want to delete (case sensitive): "))
    
    contacts = [con for con in contacts if con.name != name] 
    
    print(f"Username : {name} have been deleted")
    
    contmain()


def contviewall(return_func):
    print("You are viewing all accounts")
    
    for contact in contacts:
        print(f"Name: {contact.name}, Phone Number: {contact.number} ")
        
    return_func()

    
def contviewdiv(return_func):
    print("View Contact by Division")
    print("Please choose a division:")
    print("1. Monaka")
    print("2. Mya")
    print("3. Rimu")
    print("4. Moth")
    print("5. Yuina")
    
    while True:
        try:
            divchoice = int(input("Select a division (1-5): "))
            if 1 <= divchoice <= 5:
                division = ["Monaka", "Mya", "Rimu", "Moth", "Yuina"]
                newdiv = division[divchoice - 1] 
               
            else:
                print("Invalid choice. do it again")
                contviewdiv()
        except ValueError:
            print("Invalid input. Please enter a number.")
            
        print(f"Here are the list of contacts in {newdiv}: ")
        found = False 
        for contact in contacts: 
            if contact.division == newdiv:
                print(f"Name : {contact.name},  Phone Number: {contact.number}")
                found = True 
                
        if not found: 
            print("No Contact in this Division")
        return_func()

    
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

        
def backfromcont(return_func):
    print("Do you want to go back?")
    
    choose = (input("Yes/No : ").strip().lower())
    if choose == "yes":
        if return_func == 'police':
            policemode2()
        elif return_func == 'user':
            usermode2()
        else:
            contviewall()
            
    
load()
initmode()
