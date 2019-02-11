
class Account:

    """


    Class that generates new instances of users.


    """

    account_list = []  # empty account list

    def __init__(self, account_name, user_name, password):
        self.account_name = account_name
        self.user_name = user_name
        self.password = password

    def save_account(self):
        '''
        save_account method saves account objects into account_list
        '''

        Account.account_list.append(self)

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list
