
class Credentials:

    """


    Class that generates new instances of users.


    """

    credentials_list = []  # empty credentials list

    def __init__(self, credentials_name, usr_name, password, email):

        self.credentials_name = credentials_name

        self.usr_name = usr_name

        self.password = password

    def save_credentials(self):
        '''
        save_credentials method saves credentials objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        '''
        delete_credentials method deletes a saved credentials from the credentials_list
        '''

        Credentials.credentials_list.remove(self)
