from faker import Faker
fake = Faker(['pl_PL'])

class BaseContact():
    def __init__(self, first_name, last_name, 
                 private_phone_number, private_email):
        self.first_name = first_name
        self.last_name = last_name
        self.private_phone_number = private_phone_number
        self.private_email = private_email
    
    @property
    def name_length(self):
        return len(self.first_name)+len(self.last_name)
    
    def __repr__(self):
        return f'Private contact:\nfirst name: {self.first_name}, \nlast name: {self.last_name}, \nprivate phone number: {self.private_phone_number}, \nprivate email: {self.private_email}'
    
    def contact(self):
        print (f'Wybieram numer {self.private_phone_number} i dzwonię prywatnie do {self.first_name} {self.last_name}.')

class BusinessContact(BaseContact):
    '''
    stanowisko, nazwa firmy, telefon służbowy
    '''
    def __init__(self, job, company_name, company_phone_number, company_email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.job = job
        self.company_name = company_name
        self.company_phone_number = company_phone_number
        self.company_email = company_email

    def contact(self):
        print (f'Wybieram numer {self.company_phone_number} i dzwonię służbowo do {self.first_name} {self.last_name}.')

    def __repr__(self):
        return f'Business contact:\nfirst name: {self.first_name}, \nlast name: {self.last_name}, \ncompany phone number: {self.company_phone_number}, \ncompany email: {self.company_email}'


def create_contacts(visit_card_type, cards_number):
    person_in_private = [BaseContact(first_name=fake.first_name(),
                        last_name=fake.last_name(),
                        private_phone_number=f'+48 {fake.msisdn()[:9]}',
                        private_email=None) for _ in range(cards_number)]
    for person in person_in_private:
        person.private_email = f'{person.first_name.lower()}.{person.last_name.lower()}@{fake.free_email_domain()}'

    person_in_business = [BusinessContact(first_name = person.first_name, 
                            last_name = person.last_name,
                            private_phone_number = person.private_phone_number,
                            private_email = person.private_email,
                            job = fake.job(),
                            company_name=fake.company(),
                            company_phone_number=f'+48 {fake.msisdn()[:9]}',
                            company_email=None
                            ) for person in person_in_private]
    for person in person_in_business:
        person.company_email = f"{person.first_name.lower()}.{person.last_name.lower()}@{fake.domain_name()}"

    if visit_card_type == 'private':
        for person in person_in_private:
            person.contact()
    elif visit_card_type == 'business':
        for person in person_in_business:
            person.contact()


create_contacts('business', 5)
create_contacts('private', 5)
