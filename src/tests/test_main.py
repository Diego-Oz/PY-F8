import pytest
from src.main import login, get_all_contacts, get_contact_by_id
from src.models.contactModel import ContactModel

# CONTACTS
def test_get_contacts_not_none():
    contacts = ContactModel.get_contacts()
    assert contacts != None

def test_get_contacts_has_elements():
    contacts = ContactModel.get_contacts()
    assert len(contacts) > 0

def test_get_contacts_check_elements_length():
    contacts = ContactModel.get_contacts()
    for contact in contacts:
        assert len(contact) > 0

def test_get_all_contacts_not_none():
    contacts = ContactModel.get_contacts()
    assert contacts != None

def test_get_all_contacts_has_elements():
    contacts = ContactModel.get_contacts()
    assert len(contacts) > 0

def test_get_contact_by_id_not_none():
    contact = ContactModel.get_contact_by_id(9)
    assert contact != None

def test_get_contact_by_id_has_correct_id():
    contact = ContactModel.get_contact_by_id(9)
    assert contact["id"] == 9
