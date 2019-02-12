#!/usr/bin/env python3.6
from account import Account
from credentials import Credentials


def create_account(self, f_name, m_name, user_name, password, e_mail):
    '''
    Function to create a new account
    '''
    new_account = Account(self, f_name, m_name, user_name, password, e_mail)
    return new_account


def save_accounts(account):
    '''
    Function to save account
    '''
    account.save_account()


def del_account(account):
    '''
    Function to delete a account
    '''
    account.delete_account()


def find_account(f_name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Account.find_by_user_name(user_name)


def check_existing_accounts(user_name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Account.account_exist(user_name)


def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()

 # _CREDENTIALS_


def create_credentials(credentials_name, usr_name, password, email):
    '''
    Function to create a new account
    '''
    new_credentials = Credentials(credentials_name, usr_name, password, email)

    return new_credentials


def save_credentials(credentials):
    '''
    Function to save account
    '''
    credentials.save_credentials()


def del_credentials(credentials):
    '''
    Function to delete a account
    '''
    credentials.delete_credentials()


def find_credentials(name):
    '''
    Function that finds a account by nane and returns the account
    '''
    return Credentials.find_by_name(name)


def check_existing_credentials(name):
    '''
    Function that check if an account exists with that name and return a Boolean
    '''
    return Credentials.credentials_exist(name)


def display_credentials():
    '''
    Function that returns all the saved accounts
    '''
    return Credentials.display_credentials()


def main():

    print("Hello Welcome to your Pass Word Locker. What is your name?")

    m_name = input()

    print(
        f"Hello {m_name}, sign up to Pass Word Locker to create an account.")

    print('\n')

    while True:

        print("Use these k short codes to operate :\n SU -> SIGN UP.\n DA -> Display your account.\n LN ->LOGIN.\n ex ->exit Pass Word Locker. ")

        short_code = input().lower()

        if short_code == 'su':

            print("Create a Pass Word Locker Account")

            print("_"*10)

            account_name = input('Account name:')

            print('\n')

            m_name = input('Second name:')

            print('\n')

            user_name = input("User Name")
            print('/n')

            password = input('password:')
            print('\n')

            e_mail = input('email : ')

            save_accounts(create_account(self, account_name,
                                         m_name, user_name, password, e_mail))

            print('\n')

            print(
                f"A New {account_name} Account with the user name  {user_name} has been created.")

            print(
                f"You can now login to your {account_name} account using your password.")

            print('\n')

        elif short_code == 'da':

            if display_accounts():

                print("Here is your account and your details")

                print('\n')

                for account in display_accounts():

                    print(
                        f"Account name:{account.account_name}  User name: {account.user_name} Password:{account.password}")

                    print('\n')

            else:

                print('\n')

                print(
                    "You dont seem to have created an account.Sign up to create a new account.")

                print('\n')

        elif short_code == 'ln':

            print("Enter your password to login.")

            search_account = input()

            if check_existing_accounts(search_account):

                search_cred = find_account(search_account)

                print("\033[1;32;1m   \n")

                print(f"You are now logged in to your {account_name} account")

                print("\033[1;37;1m   \n")

                # Credentials

                while True:

                    print('''


                    Use these short codes:


                    CA -> Create new credential.


                    DC -> Display your credentials list


                    ex ->Log out your credentials account.''')

                    short_code = input().lower()

                    if short_code == "ca":

                        print("Create new credential")

                        print('_' * 20)

                        credentials_name = input('Credential name:')

                        print('\n')

                        usr_name = input(f"{credentials_name} user name:")

                        print('\n')

                        print('*' * 20)

                        pwd = input(f"{credentials_name} password:")

                        save_credentials(create_credentials(
                            credentials_name, u_name, pwd, e_address))

                        print('\n')

                        print(
                            f"A New {credentials_name} Account with the user name  {usr_name} has been created.")

                        print('\n')

                    elif short_code == 'dc':

                        if display_credentials():

                            print("Here is your credentials")

                            print('\n')

                            for credentials in display_credentials():

                                print(
                                    f"Credential name:{credentials.credentials_name}  User name: {credentials.usr_name} Password:{credentials.password}")

                                print('\n')

                        else:

                            print('\n')

                            print("You don't seem to have created any account yet")

                            print('\n')

                    elif short_code == "ex":

                        print('\n')

                        print(
                            f"You have logged out your {account_name} account")

                        print('\n')

                        break

            else:

                print('\n')

                print("WRONG PASSWORD!! PLEASE ENTER CORRECT PASSWORD TO LOGIN")

                print('\n')

                print('\n')

        elif short_code == "ex":

            print(
                f"Thanks {user_name} for your time.I hope you enjoyed my service.Bye...")

            break

        else:

            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
