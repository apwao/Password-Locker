#!/usr/bin/env python3.6
 
import random                       #importing random module
from user import User               #importing class User
from credential import Credential   #importing class Credential

def create_credential(username,accountname,password):
    """
    create_credential function that creates an instance of the class credential
    """
    new_credential = Credential(username,accountname,password)
    return new_credential

def create_user(name, login_password):
    """
    create_user function that creates an instance of the class user
    """
    new_user = User(name,login_password)
    return new_user

def saveCredential(credential):
    """
    saveCredential function to save the credential created by the user
    """
    credential.save_credential()

def saveUser(user):
    """
    saveUser function to create a user account whenever a user
    signs up with password locker
    """
    user.save_user

def deleteCredential(credential):
    """
    deleteCredential function that helps user delete an existing credential
    """
    credential.delete_credntial()

def findCredential(account_name):
    """
    findCredential function to search for a credential by accountname and 
    return all its details
    """
    return Credential.find_accountname(account_name)

def credentialExists(account_name):
    """
    credentialExists function to check whether a credential exists
    and return True or False
    """
    return Credential.credential_exists(account_name)

def displayCredentials():
    """
    displayCredentials function to display the credentials currently saved
    """
    return Credential.display_credentials()

def displayUser():
    """
    displayUser function to display user details if user has an account
    """
    return User.display_all()

def copyUsername(account_name):
    """
    copyUsername function that enables user to copy their user name to their
    machine clip board
    """
    return Credential.copy_username(account_name)

def copyAccountname(account_name):
    """
    copyAccountname function that enables user to copy their
    accountname to the machine clipboard
    """
    return Credential.copy_accountname(account_name)

def copyPassword(account_name):
    """
    copyPassword function that enables user to copy their password 
    to the machine clipboard
    """
    return Credential.copy_password(account_name)


def main():
    user_name = input("Hello, welcome to Password_Locker. What is your name?")

    print("Hi {}. What would you like to do?".format(user_name))

    while True:
        userShortCodes = input("Use these shortcodes to pick an action: \n ca - Create Account \n ex - Exit Password Locker:\n")

        if userShortCodes == "ca":
            userName = input("Please enter a user name for account set up:")
            loginPassword = input("Please enter your password: ")   
            saveUser(create_user(userName, loginPassword))

        print("The following are details to your account: \n Username: {} \n password: {}".format(userName, loginPassword))
        username_login = input("Thank you for signing up with us. \n please enter your username to login: ")
        password_login = input("Please enter your password: ") 

        if loginPassword == password_login and userName == username_login:
            if User.display_all():
                userShortCodes = input("Would you like to proceed to your credentials? Use this short code: \n  sc - See your credential: \n ")
                if userShortCodes == "sc":

                    while True:
                        short_code = input("Use these shortcodes to choose an action: \n cc- create new credential \n delc - delete credential \n fc - find credential \n cp - copy credential \n ex - exit credentials \n dc -display credential :\n ")    










