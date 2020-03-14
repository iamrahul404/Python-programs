import os
import base64
import hashlib
import sys
import getpass
import pyperclip

#p = "rahulkumar"
#hashlib.md5(p.encode()).hexdigest()
location="D:\\Rahul"
passFile="jsdfssdjcbsddaihsdhasjdakjsda.bin"
finalPassFile=location + "/" + passFile
# master password
programPassword = "37dff0cd99ecc47c60aeea102185262a" #'rahulkumar' 
passDict = {}

#all the helpers functions
def encodeString(strToEncode):
    # return is bytes
    return base64.encodebytes(strToEncode.encode())
def decodeString(strToDecode):
    # return is String
    return base64.decodebytes(strToDecode).decode()
def validateUser():
    try: 
        p = getpass.getpass()
    except Exception as error: 
        print('ERROR', error) 
    else: 
        if hashlib.md5(p.encode()).hexdigest() == programPassword:
            return True
        else:
            print ("Wrong Password" )
            return False
def save():
    try: 
        file = open(finalPassFile,"wb")
    except Exception as error: 
        print('ERROR', error) 
    else:
        for key,value in passDict.items():
            file.write(key)
            file.write(value)
        file.close()
def load():
    try: 
        file = open(finalPassFile,"rb")
    except Exception as error: 
        print('ERROR', error) 
    else: 
        lines = file.readlines()
        file.close()
        loadingKey=True
        keyValue = ""
        for line in lines:
            if loadingKey:
                passDict[line] = ""
                keyValue = line
                loadingKey = False
            else:
                loadingKey = True
                passDict[keyValue] = line
def addPassword(key,value):
    passDict[encodeString(key)] = encodeString(value)
    
def getPassword(key):
    #use a try and except block to safely get the password
    return decodeString(passDict[encodeString(key)])
def getAllUser():
    load()
    for k,v in passDict.items():
        print(decodeString(k))
def menu():
    print("")
    print("1. Get password")
    print("2. Add password")
    print("3. Show All User")
    print("4. Exit")
    option = 0
    try:
        option = int(input("Enter your choice: "))
    except Exception as error:
        print("Error: " + str(error))
        menu()
    print("")
    if option > 4:
        print("Error: please enter valid integer in range")
        menu()
    elif option == 4:
        sys.exit(0)
    elif option == 3:
        getAllUser()
    elif option == 1:
        print("please enter website for which you need password")
        key = input("username: ")
        show_on_screen_opt = True
        pass_value = ""
        try:
            load()
            pass_value = getPassword(key)
            #print(pass_value)
            pyperclip.copy(pass_value)
            print("your password is successfully copied to clipboard, Please paste where needed")
        except:
            print("Password for this username is not available")
            show_on_screen_opt =False
        if show_on_screen_opt:
            try:
                opt = int(input("1 to show on screen: "))
                if opt == 1:
                    print(pass_value)
            except:
                print("")
    elif option == 2:
        user = input("UserName/Website: ")
        try:
            print("Enter password")
            user_pass = getpass.getpass()
            addPassword(user,user_pass)
            save()
        except Exception as error: 
            print('ERROR: ', error)
            print("do the all entry again")
    else:
        print("please check your inputs")
def main():
    print("Please validate yourself: ")
    if validateUser():
        while 1:
            menu()
    else:
        print("Cannot verify you sorry!")

main()
