database = {}

def init():

    isValidOptionSelected = False
    print('Welcome to CWest Studios')

    while isValidOptionSelected == False:

        haveAccount = int(input('Do you have account with us: 1 (Yes) 2 (No) \n'))

        if(haveAccount == 1):
            isValidOptionSelected = True
            login()
        elif(haveAccount == 2):
            isValidOptionSelected = True
            register()
        else:
            print('invalid option selected')
  
def login():
    print('***Login***')
    Account_Number = ('Enter Your Account Number')
    Password = ('Enter Your Password')

def register():
    print('***Register***')
    email = input('Enter Your Email address\n')
    First_Name = ('Enter Your First Name\n')
    Last_Name = ('Enter Your Last Name\n')
    Password = ('Create a password')

    accountNumber = generatingAccountNumber()

    database[accountNumber] = [First_Name, Last_Name, email, Password]

    print('Account Created')
    login()

    return database

def bankOperations():
    print('this is a bank operation')

def generateAccountNumber():
    print('Generating Account Number')
    return random.randrange(2222222222, 8888888888)

  