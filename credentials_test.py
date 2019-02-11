
import unittest  # Importing the unittest module


from credentials import Credentials  # Importing the account class


class TestCredentials(unittest.TestCase):

    def setUp(self):

        self.new_credentials = Credentials(
            "NYIRAMWIZA", "njoanc@gmail.com", "kazubajoanna12")  # create Account object
