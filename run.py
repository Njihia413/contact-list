#!shebang
from contact import Contact

#Function to create a new contact
def create_contact(fname,lname,phone,email):
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

#Function to save contacts
def save_contacts(contact):
    contact.save_contact()

#Function to delete contact
def del_contact(contact):
    contact.delete_contact()

#Function for finding a contact
def find_contact(number):
    return Contact.find_by_number(number)   

#Function to check if a contact exists
def check_existing_contacts(number):
    return Contact.contact_exist(number)

#Function to display all contacts
def display_contacts():
    return Contact.display_contacts()