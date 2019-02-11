import unittest  # Importing the unittest module
from account import Account  # Importing the account class


class TestAccount(unittest.TestCase):

    def setUp(self):

        self.new_account = Account(
            "GitHub", "njoanc", "kazubajoanna12")  # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_account.account_name, "GitHub")
        self.assertEqual(self.new_account.user_name, "njoanc")
        self.assertEqual(self.new_account.password, "kazubajoanna12")

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
            "Test", "user", "test@user.com")  # new contact
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
        test_account = Account("Facebook", "user", "moringa123")  # new account
        test_account.save_account()
        self.assertEqual(len(Account.account_list), 2)

    def test_delete_account(self):
        '''
        test_delete_contact to test if we can remove a account from our account list
        '''
        self.new_account.save_account()
        test_account = Account("Facebook", "user", "moringa123")  # new account
        test_account.save_contact()

        self.new_account.delete_account()  # Deleting a account object
        self.assertEqual(len(Account.account_list), 1)


if __name__ == '__main__':
    unittest.main()
