def sum(x, y):
    return x + y

def is_greater_than(number_1, number_2):
    return number_1 > number_2

def login(user, password):
    if((user == "dortiz6@unibe.org") and (password == "dev15#avatar")):
        return True
    else:
        return False

def get_all_contacts():
    contacts = ContactModel.get_contacts()
    return contacts

def get_contact_by_id(id):
    contact = ContactModel.get_contact_by_id(id)
    return contact
