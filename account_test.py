import unittest  # Importing the unittest module
from account import Account  # Importing the account class


class TestAccount(unittest.TestCase):

    def setUp(self):

        self.new_account = Account(
            "GitHub", "njoanc", "kazubajoanna12")  # create Account object
