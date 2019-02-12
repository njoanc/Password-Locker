import unittest  # Importing the unittest module

from credentials import Credentials  # Importing the credentials class


class TestCredentials(unittest.TestCase):
    def setUp(self):

        self.new_credentials = Credentials(
            "NYIRAMWIZA", "Jeanne", "kazubajoanna12", "njoanc@gmail.com")  # create Account object

    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_credentials.credentials_name, "NYIRAMWIZA")

        self.assertEqual(self.new_credentials.usr_name, "Jeanne")
        self.assertEqual(self.new_credentials.password, "kazubajoanna12")
        self.assertEqual(self.new_credentials.email, "njoanc@gmail.com")

    def test_save_credentials(self):
        '''
        test_save_account test case to test if the account object is saved into
         the account list
        '''
        self.new_credentials.save_credentials()  # saving the new account
        self.assertEqual(len(Credentials.credentials_list), 1)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_account to check if we can save multiple account
        objects to our account_list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "kazubajoanna123", "test@user.com")  # new account
        test_credentials.save_credentials()

        self.assertEqual(len(Credentials.credentials_list), 2)

    def test_delete_credentials(self):
        '''
        test_delete_account to test if we can remove an account from our account list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "kazubajoanna123", "test@user.com")  # account
        test_credentials.save_credentials()

        self.new_credentials.delete_credentials()  # Deleting an account object
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_find_credentials_by_credentials_name(self):
        '''
        test to check if we can find an account by account_name and display information
        '''

        self.new_credentials.save_credentials()
        test_credentials = Credentials(
            "Test", "user", "kazubajoanna123", "test@user.com")  # new account
        test_credentials.save_credentials()

        found_credentials = Credentials.find_by_name("Test")

        self.assertEqual(found_credentials.email, test_credentials.email)


if __name__ == '__main__':
    unittest.main()
