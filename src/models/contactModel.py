class ContactModel():

    contacts = [
        {"id": 1, "name": "Juan", "last_name": "Pérez", "phone": "1234567890", "email": "juan.perez@example.com"},
        {"id": 2, "name": "Pedro", "last_name": "García", "phone": "0987654321", "email": "pedro.garcia@example.com"},
        {"id": 3, "name": "Mario", "last_name": "López", "phone": "5555555555", "email": "mario.lopez@example.com"},
        {"id": 4, "name": "Luisa", "last_name": "Martínez", "phone": "1111111111", "email": "luisa.martinez@example.com"},
        {"id": 5, "name": "Margarita", "last_name": "Sánchez", "phone": "2222222222", "email": "margarita.sanchez@example.com"},
        {"id": 6, "name": "Ana", "last_name": "Ramírez", "phone": "3333333333", "email": "ana.ramirez@example.com"},
        {"id": 7, "name": "Carlos", "last_name": "González", "phone": "4444444444", "email": "carlos.gonzalez@example.com"},
        {"id": 8, "name": "María", "last_name": "Hernández", "phone": "6666666666", "email": "maria.hernandez@example.com"},
        {"id": 9, "name": "Jorge", "last_name": "Díaz", "phone": "7777777777", "email": "jorge.diaz@example.com"},
        {"id": 10, "name": "Sofía", "last_name": "Torres", "phone": "9999999999", "email": "sofia.torres@example.com"}
    ]

    @classmethod
    def get_contacts(cls):
        return cls.contacts

    @classmethod
    def get_contact_by_id(cls, id):
        for contact in cls.contacts:
            if contact["id"] == id:
                return contact
        return None