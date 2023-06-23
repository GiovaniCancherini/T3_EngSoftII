class Student:
    def __init__(self, name, document_number, address, registration_number=None):
        self.name = name
        self.document_number = document_number
        self.address = address
        self.registration_number = registration_number

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_document_number(self):
        return self.document_number

    def set_document_number(self, document_number):
        self.document_number = document_number

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_registration_number(self):
        return self.registration_number

    def set_registration_number(self, registration_number):
        self.registration_number = registration_number