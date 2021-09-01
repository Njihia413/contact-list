import unittest #Importing the unittest module
from contact import Contact #Importing the contact class

class TestContact(unittest.TestCase):
    def setUp(self):
        self.new_contact = Contact("Lyn","Muthoni","0796654066","sonnie2154@gmail.com")

    def tearDown(self):
        Contact.contact_list = []

    #First test to check if our contact objects are being instantiated correctly
    def test_instance(self):
        self.assertEqual(self.new_contact.first_name,"Lyn")
        self.assertEqual(self.new_contact.last_name,"Muthoni")
        self.assertEqual(self.new_contact.phone_number,"0796654066")
        self.assertEqual(self.new_contact.email,"sonnie2154@gmail.com")

    #Second test to check if we can save contacts into the contact list
    def test_save_contact(self):
        self.new_contact.save_contact() #saving the new contact
        self.assertEqual(len(Contact.contact_list),1)

    #Third test to test if we can save multiple contacts
    def test_save_multiple_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") #new contact
        test_contact.save_contact()
        self.assertEqual(len(Contact.contact_list),2)

    #Fourth test to test if we can remove a contact from our contact list
    def test_delete_contact(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0712345678","test@user.com") #new contact
        test_contact.save_contact()
        self.new_contact.delete_contact() #Deleting a contact object
        self.assertEqual(len(Contact.contact_list),1)

    #Fifth test to check if we can find a contact by phone number and display information
    def test_find_contact_by_number(self):
        self.new_contact.save_contact()
        test_contact = Contact("Test","user","0711223344","test@user.com") #new contact
        test_contact.save_contact()
        found_contact = Contact.find_by_number("0711223344")
        self.assertEqual(found_contact.email,test_contact.email)
        

if __name__ == '__main__':
    unittest.main()        
