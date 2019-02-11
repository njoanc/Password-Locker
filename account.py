
class Account:

    """
    Class that generates new instances of users.
    """
    account_list = []  # empty account list

    def __init__(self, f_name, m_name, e_mail):
        self.f_name = f_name
        self.m_name = m_name
        self.e_mail = e_mail

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

    def delete_account(self):
        '''
        delete_account method deletes a saved account from the account_list
        '''
        Account.account_list.remove(self)

    @classmethod
    def find_by_account_name(cls, f_name):
        for account in cls.account_list:
            if account.f_name == f_name:
                return account

    @classmethod
    def account_exist(cls, f_name):
        '''
        Method that checks if a account exists from the account list.
        Args:
            account_name: Acc name to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in cls.account_list:
            if account.password == f_name:
                return account

        return False

    @classmethod
    def display_accounts(cls):
        '''
        method that returns the account list
        '''
        return cls.account_list
