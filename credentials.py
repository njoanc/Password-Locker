
class Credential:

    Credential_list = []

    def __init__(self, face_bookp, email_p):
        self.face_bookp = face_bookp
        self.email_p = email_p

    def save_Credential(self):
        '''
        Function created to save credentials
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        Function added to delete credentials
        '''
        Credential.info_list.remove(self)

    @classmethod
    def display_credential(cls):
        '''
        a class method involves the whole class the display credential display user information
        '''
        return cls.credential_list
