import hashlib
def signup():
    email=input("Enter the email adress:")
    pwd=input("Enter the password: ")
    conf_pwd=input("Enter the password again: ")

    if conf_pwd == pwd:
        enc=conf_pwd.encode()
        hash1=hashlib.md5(enc).hexdigest
        hash_str=str(hash1)
        with open("Sign_up.txt","w") as f:
            f.write(email + "\n")
            f.write(hash_str)
        f.close()
        print("You have registered successfully")
    else:
        print("Password is not same as above! \n")


def login():
    email=input("Enter the email adress: ")
    pwd=input("Enter the password: ")
    auth=pwd.encode()
    auth_hash=hashlib.md5(auth).hexdigest
    with open("Sign_up.txt","r") as f:
        stored_email,stored_password=f.read().split("\n")
    f.close()
    if stored_email == email and stored_password == pwd:
        print("Logged in Successfully!")
    else:
        print("login failed \n")

while 1:
    print("******** LOGİN SYSTEM ********")
    print("1.Sign_up")
    print("2.Login")
    print("3.Exit")
    ch=int(input("What is your choice: "))
    if ch == 1:
        signup()
    elif ch == 2:
        login()
    elif ch == 3:
        break
    else:
        print("Wrong choice!")    


    





     
 




