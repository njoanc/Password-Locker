#!/usr/bin/env python3.6
from account import Account


def create_account(acname, usname, password):
    '''
    Function to create a new account
    '''
    new_account = Account(acname, usname, password)
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


def find_account(usname):
    '''
    Function that finds a account by username and returns the account
    '''
    return Account.find_by_usname(usname)


def check_existing_accounts(usname):
    '''
    Function that check if a account exists with that username and return a Boolean
    '''
    return Account.account_exist(usname)


def display_accounts():
    '''
    Function that returns all the saved accounts
    '''
    return Account.display_accounts()


def copy_usname():
    '''
    Function that returns all the saved usernames
    '''
    return Account.copy_usnames()


def main():
    print("Hello Welcome to your account list. What is your Account name?")
    account_name = input()

    print(f"Hello {account_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes : ca - create a new account, da - display accounts, fa -find an account, ex -exit the account list ")

        short_code = input().lower()

        if short_code == 'cc':
            print("New Account")
            print("-"*10)

            print("Account Name ....")
            f_name = input()

            print("User Name ...")
            l_name = input()

            print("Password ...")
            p_number = input()

            # create and save new account.
            save_accounts(create_account(ac_name, us_name, password))
            print('\n')
            print(f"New Account {ac_name} {us_name} created")
            print('\n')

        elif short_code == 'da':

            if display_accounts():
                print("Here is a list of all your accounts")
                print('\n')

                for account in display_accounts():
                    print(
                        f"{account.account_name} {account.user_name} .....{account.password}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any accounts saved yet")
                print('\n')

        elif short_code == 'fa':

            print("Enter the username you want to search for")

            search_user_name = input()
            if check_existing_accounts(search_user_name):
                search_account = find_account(search_user_name)
                print(
                    f"{search_account.account_name} {search_account.user_name}")
                print('-' * 20)

                print(f"Account Name.......{search_account.account_name}")
                print(f"User Name.......{search_account.user_name}")
            else:
                print("That account does not exist")

        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")


if __name__ == '__main__':

    main()
