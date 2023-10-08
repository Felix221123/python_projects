#this projects features the application of a contact list
#all contacs are stored as objects inside in an array in a json file name
#my_contact_list.json
import re
import json
import time
import sys

#contact class
class contact():
    def __init__(self, name, phone_number, email_address):
        self.name = name 
        self.phone_number = phone_number
        self.email_address = email_address

    def updateContacts_option(self):
        print('')
        print('From your contacts, what would you like to update or make changes to\nP for Phone number..\nE for Email Address..')
        user_option = input('enter your choice..').lower()
        if user_option == 'p':
            return 'p'
        elif user_option == 'e':
            return 'e'
        else:
            print('your option was invalid...Exiting..💀')
            sys.exit(0)

    def delete_contact(self):
        print(f'Are you sure you would like to delete the contact from the contact list...\nEnter...\nD for Delete...\nC for Cancel...')
        user_choice = input('Enter your choice...').lower()
        if user_choice == 'd':
            return 'd'
        elif user_choice == 'c':
            return 'c'
        else:
            print('your option was invalid...Exiting..💀')
            sys.exit(0)


        

#list of contact class
class contact_list(contact):
    def __init__(self):
        #inherits attributes from the parent class
        super().__init__('felix', 0 , 'felixbaah47@gmail.com')
        self.list_of_contacts = []
    

    #method to add new contacts to the contact list
    def addcontacts(self):
        is_valid = True
        print('\n')
        print('You want to add more contacts right...Cool')
        print('\n***********  Add Contacts  ***********\n')
        self.name = input('enter the name of the person you want to add...').capitalize()
        print('\n')
        while is_valid:
            self.phone_number = input(f'enter {self.name}\'s phone number..')
            regex_number = '^[0]'
            if len(self.phone_number) == 11 and re.match(regex_number ,self.phone_number):
                print('phone number has been successfully saved')
                break
            elif not re.match(regex_number ,self.phone_number):
                print('this is invalid...phone number has to start with 0..try again..')
                is_valid = True
            elif len(self.phone_number) < 11 :
                print('the phone number you entered was incorrect because it\'s less than 11')
                is_valid = True
            elif len(self.phone_number) > 11:
                print('the phone number you entered was incorrect because it\'s more than 11')
                is_valid = True
            else:
                print('these values are out of range..try again...')
                is_valid = True

        print('\n')        

        while is_valid == True:
            self.email_address = input(f'enter the email address of {self.name}...')
            regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+'
            if re.match(regex , self.email_address):
                print('email is valid and it has been successsfully saved')
                break
            else:
                print('email address is invlaid....try again please..')
                is_valid = True

        print('\n')        
        my_contact_list = {
            'Name' : self.name,
            "Phone Number" : self.phone_number,
            'Email Address' : self.email_address
        }

        print(f'the contact you just added was \n{my_contact_list}')

        #Load existing contacts from the JSON file (if it exists)
        try:
            with open('my_contact_list.json', 'r') as json_file:
                self.list_of_contacts = json.load(json_file)
        except FileNotFoundError:
            self.list_of_contacts = []

        # Add new contacts to the existing list
        self.list_of_contacts.append(my_contact_list)

        # Save the updated list of contacts to the JSON file
        with open('my_contact_list.json', 'w') as json_file:
            json.dump(self.list_of_contacts, json_file)

    
    def search_contact(self):
        is_valid = True
        print('\n')
        print('You want to view contacts right...Cool')
        print('\n***********  View Contacts  ***********\n')

        while is_valid:
            print('you are going to enter name of the person you would like to view their contact details...👍')
            time.sleep(2)
            print('')
            #Load existing contacts from the JSON file (if it exists)
            try:
                with open('my_contact_list.json', 'r') as json_file:
                    self.list_of_contacts = json.load(json_file)
            except FileNotFoundError:
                self.list_of_contacts = []

            is_cont = True    
            while is_cont:
                #area to collect inputs from user to search for name    
                user_name_search = input('enter the name here...').capitalize()

                found_contact = None

                for contact in self.list_of_contacts:
                    if user_name_search == contact["Name"]:
                        found_contact = contact
                        break

                
                if found_contact:
                    print(f'here are the contact detials of {user_name_search}\n{contact}')
                    is_valid = False
                    is_cont = False
                    break
                elif user_name_search == '':
                    print('name cannot be an empty string..')
                    continue
                elif not found_contact:
                    print('')
                    print('the name you entered do not match the contacts on our records')
                    print('would you still like to search for the contacts on our records\nY for yes..\nN for no..')
                    user_choice = input('enter your choice..').lower()
                    print('')
                    if user_choice == 'y':
                        is_cont = True
                        # continue 
                    elif user_choice == 'n':
                        print('it seems you don\'t want to search again..bye bye..😇')
                        is_cont = False
                        sys.exit(0)
                    else:
                        print('Invalid choice. Exiting...😼')
                        sys.exit(0)


    def view_list_of_contact(self):
        print('')
        print('You want to view all your contacts right...Cool')
        print('\n***********  View Contacts  ***********\n')
        time.sleep(2)
        #Load existing contacts from the JSON file (if it exists)
        try:
            with open('my_contact_list.json', 'r') as json_file:
                self.list_of_contacts = json.load(json_file)
        except FileNotFoundError:
            self.list_of_contacts = []

        print('')
        print(f'Here are all your list of contacts \n{self.list_of_contacts}')
        

    def update_contacts(self):
        print('')
        print('You want to update your contacts right...Cool')
        print('\n***********  Update Contacts  ***********\n')
        time.sleep(2)

        #Load existing contacts from the JSON file (if it exists)
        try:
            with open('my_contact_list.json', 'r') as json_file:
                self.list_of_contacts = json.load(json_file)
        except FileNotFoundError:
            self.list_of_contacts = []

        user_choice = self.updateContacts_option()

        if user_choice == 'p':
            print('You want to update their phone number..')
            time.sleep(1)
            print('')
            print('Now you are going to be asked to type the name on the phone number contacts you would like to change...Sounds Cool right😊')
            time.sleep(3)
            print('')
            # user_name = input('enter the name on the contact...').capitalize()
            is_valid = True
            while is_valid:
                user_name = input('enter the name on the contact...').capitalize()

                for contact in self.list_of_contacts:
                    
                    if user_name == contact["Name"]:
                        print('Match found..')
                        print('')
                        print(f'Now you are going to enter the NEW PHONE NUMBER for {contact["Name"]}...Cool')
                        print('')
                        num_valid = True
                        while num_valid:
                            new_number = input('enter the new number..')
                            regex_number = '^[0]'
                            if len(new_number) == 11 and re.match(regex_number ,new_number):
                                contact["Phone Number"] = new_number
                                # Save the updated list of contacts to the JSON file
                                with open('my_contact_list.json', 'w') as json_file:
                                    json.dump(self.list_of_contacts, json_file)
                                print('phone number has been successfully updated')
                                num_valid = False
                                sys.exit(0)
                            elif not re.match(regex_number ,new_number):
                                print('this is invalid...phone number has to start with 0..try again..')
                                num_valid = True
                            elif len(new_number) < 11 :
                                print('the phone number you entered was incorrect because it\'s less than 11')
                                num_valid = True
                            elif len(new_number) > 11:
                                print('the phone number you entered was incorrect because it\'s more than 11')
                                num_valid = True
                            else:
                                print('these values are out of range..try again...')
                                num_valid = True
                    
                    elif user_name != contact["Name"]:
                        print('Contact not found...𝌕')
                        sys.exit(0)

        elif user_choice == 'e':
            print('You want to update their email address..')
            time.sleep(1)
            print('')
            print('Now you are going to be asked to type the name on the phone number contacts you would like to change...Sounds Cool right😊')
            time.sleep(3)
            print('')

            is_valid = True
            while is_valid:
                user_name = input('enter the name on the contact...').capitalize()

                for contact in self.list_of_contacts:
                    
                    if user_name == contact["Name"]:
                        print('Match found..')
                        print('')
                        print(f'Now you are going to enter the NEW EMAIL ADDRESS for {contact["Name"]}...Cool')
                        print('')
                        num_valid = True
                        while num_valid:
                            new_email = input('enter the new email address..')
                            regex = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Za-z]{2,})+'
                            if re.match(regex , new_email):
                                contact["Email Address"] = new_email
                                # Save the updated list of contacts to the JSON file
                                with open('my_contact_list.json', 'w') as json_file:
                                    json.dump(self.list_of_contacts, json_file)
                                print('email is valid and it has been successsfully updated')
                                num_valid = False
                                sys.exit(0)
                            else:
                                print('email address is invlaid....try again please..')
                                num_valid = True
                                    
                    elif user_name != contact["Name"]:
                        print('Contact not found...𝌕')
                        sys.exit(0)


    def deleteContacts(self):
        print('')
        print('You want to delete a contact from your list of contacts right...Cool')
        print('\n***********  Delete Contacts  ***********\n')
        time.sleep(2)

        #Load existing contacts from the JSON file (if it exists)
        try:
            with open('my_contact_list.json', 'r') as json_file:
                self.list_of_contacts = json.load(json_file)
        except FileNotFoundError:
            self.list_of_contacts = []

        print('You want to delete a contact from your contact list right...')
        time.sleep(1)
        print('')
        print('Now you are going to be asked to type the name on the contacts you would like to delete...Sounds Cool right😊')
        time.sleep(3)
        print('')

        is_valid = True
        while is_valid:
            user_name = input('enter the name on the contact...').capitalize()

            for contact in self.list_of_contacts:
                
                if user_name == contact["Name"]:
                    print('Match found..')
                    print('')
                    user_delete_option = self.delete_contact()
                    if user_delete_option == 'd':
                        self.list_of_contacts.remove(contact)
                        # Save the updated list of contacts to the JSON file
                        with open('my_contact_list.json', 'w') as json_file:
                            json.dump(self.list_of_contacts, json_file)

                        print('contact has been successfully deleted')
                        is_valid = False
                        sys.exit(0)
                    elif user_delete_option == 'c':
                        print('Contact deletion canceled..')
                        is_valid = False
                        sys.exit(0)
                    else:
                        print('Invalid option. No changes has been made..')
                        is_valid = False
                        sys.exit(0)
                else:
                    print('Contact not found.')
                    is_valid = False
                    sys.exit(0)
    

    def main_menu(self):
        print('')
        print('******************   Hello User...Welcome...😃   ******************')
        print('')
        print('Here is the Main Menu for your Contacts..\nEnter...\nA for Adding Contacts..\nV for Viewing List Of Contacts..\nS for Searching for Contact..\nU for Updating Contacts..\nD for Deleting Contacts..')
        print('')
        user_menu_choice = input('enter your choice..').lower()
        if user_menu_choice == 'a':
            return self.addcontacts()
        elif user_menu_choice == 'v':
            return self.view_list_of_contact()
        elif user_menu_choice == 's':
            return self.search_contact()
        elif user_menu_choice == 'u':
            return self.update_contacts()
        elif user_menu_choice == 'd':
            return self.deleteContacts()
        else:
            print('your option was invalid...Exiting...💀')
            sys.exit(0)

        
user = contact_list()
user.main_menu()

        

        

