# Password Locker
 
# Description
Password Locker is a terminal run python application that allows users to store details i.e. usernames and passwords of their various accounts.

#User Stories
These are the behaviours that the application implements for use by a user.
* As a user I would like:
* To create an account with my details - log in and password
* Store my existing login credentials
* Generate a password for a new credential/account

# Specifications
* Behaviour                                * Input                              * Output
* Display guides for navigation          * In terminal: $./run.py               * Hello Welcome to your Pass Word Locker. What is your name? (once you enter your nname):Use these known short codes to operate 
* Display prompt for creating an account * Enter:SU                             * Enter account name, user name 
*Display prompt for login                * Enter: LN                             * Enter your account pa
* Once logged in                          * You are now logged in to your account * Use these short codes:CA -> Create new credential.DC -> Display your credentials list. ex ->Log out your creden
* Display prompt for creating a creden     * Enter: CA                            * Create new credential, Credential name
* Display a list of credenti               * Enter: DC                             * Prints a list of saved credentials
* Log out account                           * Enter: exit                           * You have logged out your account

. To completely interact with this application,you will need to sign up to have an account,then login to your account and work

# SetUp / Installation Requirements
Prerequisites
python3.6
Good internet connection
For windows users: GitBash
For linux/ubuntu users : Git
# Cloning
In your terminal:
  $ git clone https://github.com/njoanc/Password-Locker.git
  $ cd Python-Password-Locker
# Running the Application
To run the application, in your terminal:
  $ ./run.py
# Testing the Application
To run the tests for the class file and check if it functions well:
  $ python3.6 credentials_test.py
# Technologies Used
Python3.6
# License
