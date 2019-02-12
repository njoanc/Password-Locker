import pyperclip

import unittest  # Importing the unittest module
from account import Account  # Importing the account class


class TestAccount(unittest.TestCase):

    def setUp(self):

        self.new_account = Account("Hotmail", "NYIRAMWIZA", "njoanc@hotmail.com",
                                   "kazubajoanna12" "njoanc@hotmail.com")  # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name, "Hotmail")
        self.assertEqual(self.new_account.m_name, "NYIRAMWIZA")
        self.assertEqual(self.new_account.user_name, "njoanc@hotmail.com")
        self.assertEqual(self.new_account.password, "kazubajoanna12")
        self.assertEqual(self.new_account.email, "njoanc@hotmail.com")

    def test_save_account(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_account.save_account()  # saving the new account
        self.assertEqual(len(Account.account_list), 1)

    def test_save_multiple_account(self):
        '''
        test_save_multiple_account to check if we can save multiple contact
        objects to ouraccount_list
        '''
        self.new_account.save_contact()
        test_account = Account(
            "Hotmail", "NYIRAMWIZA", "njoanc@hotmail.com", "kazubajoanna12" "njoanc@hotmail.com")  # new contact
        test_account.save_contact()
        self.assertEqual(len(Account.account_list), 2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Account.account_list = []

# other test cases here

    def test_save_multiple_account(self):
        '''
    test_save_multiple_account to check if we can save multiple account
    objects to our account_list
        '''
        self.new_account.save_account()
        test_account = Account("Hotmail", "NYIRAMWIZA", "njoanc@hotmail.com",
                               "kazubajoanna12" "njoanc@hotmail.com")  # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list), 2)

    def test_delete_account(self):
        '''
        test_delete_contact to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account(
            "Hotmail", "NYIRAMWIZA", "njoanc@hotmail.com", "kazubajoanna12" "njoanc@hotmail.com")  # new account
        test_account.save_account()

        self.new_account.delete_account()  # Deleting an account object
        self.assertEqual(len(Account.account_list), 1)

    def delete_account(self):
        '''
        delete_account method deletes a saved account from the account_list
        '''

        Account.account_list.remove(self)

    def test_find_account_by_account_name(self):
        '''
        test to check if we can find a account by username and display information
        '''

        self.new_account.save_account()
        test_account = Account("Hotmail", "NYIRAMWIZA", "njoanc@hotmail.com",
                               "kazubajoanna12" "njoanc@hotmail.com")  # new account
        test_account.save_account()

        found_account = Account.find_by_account_name("Hotmail")

        self.assertEqual(found_account.m_name, test_account.m_name)

    @classmethod
    def find_by_m_name(cls, m_name):
        '''
        Method that takes in a number and returns an account that matches that username.

        Args:
            username: username to search for
        Returns :
            Account of person that matches the username.
        '''

        for account in cls.account_list:
            if account.account_name == account_name:
                return account

    def test_account_exists(self):
        '''
        test to check if we can return a Boolean  if we cannot find the account.
        '''

        self.new_account.save_account()
        test_account = Account(
            "Gmail", "NYIRAMWIZA", "njoanc@gmail.com", "kazubajoanna12", "njoanc@gmail.com")  # new account
        test_account.save_account()

        account_exists = Account.account_exist("njoanc@gmail.com")

        self.assertTrue(account_exists)

    @classmethod
    def account_exist(cls, m_name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            username: User name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.m_name == m_name:
                return True

        return False

    def test_display_all_accounts(self):
        '''
        method that returns a list of all accounts saved
        '''

        displayed = Account.display_accounts()
        self.assertEqual(displayed, Account.account_list)

    def test_copy_e_mail(self):
        '''
        Test to confirm that we are copying the email address from a found account
        '''

        self.new_account.save_account()
        Account.copy_e_mail("njoanc@gmail.com")

        self.assertEqual(self.new_account.e_mail, pyperclip.paste())

    @classmethod
    def copy_e_mail(cls, m_name):
        account_found = Account.find_by_m_name(m_name)
        pyperclip.copy(account_found.e_mail)


if __name__ == '__main__':
    unittest.main()
