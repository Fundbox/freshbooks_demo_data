import os
import random
from faker import Factory
from refreshbooks import api


##### GLOBALS ######
USERNAME = os.environ.get('FRESHBOOKS_USERNAME', 'YOUR FRESHBOOKS USERNAME')
API_TOKEN = os.environ.get('FRESHBOOKS_API_TOKEN','YOUR FRESHBOOKS v1.0 TOKEN')

NUMBER_OF_CLIENTS_TO_CREATE = 3
NUMBER_OF_INVOICES_TO_CREATE = 5
##### GLOBALS ######

##### SETTINGS ####
c = api.TokenClient('%s.freshbooks.com' % USERNAME,API_TOKEN,user_agent='Example/1.0')
faker = Factory.create()
##### SETTINGS ####

##### CREATE CLIENTS ####
def create_clients():
    global i, response
    for i in range(0, NUMBER_OF_CLIENTS_TO_CREATE):
        faker.name()
        response = c.client.create(
            client=dict(
                first_name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                organization=faker.company(),
                p_country=faker.country(),
                p_city=faker.city(),
                p_street1=faker.address().split('\n')[0],
                p_street2=faker.address().split('\n')[1],
                p_state=faker.state(),
                work_phone=faker.phone_number(),
            )
        )
        if response.get('status') == 'ok':
            print "Client with id : %s created." % response.client_id
##### END CREATE CLIENTS ####

##### CREATE INVOICES ####
def create_invoices():
    global resp, j, response
    resp = c.client.list()
    for j in range(0, NUMBER_OF_INVOICES_TO_CREATE):
        response = c.invoice.create(
            invoice=dict(
                client_id=random.choice(resp.clients.client).client_id,
                notes=faker.bs(),
                terms="Net 30",
                status="sent",
                lines=[
                    api.types.line(
                        name=faker.word(),
                        unit_cost=random.choice(('150.2','250','150.11','48.68','850.4')),
                        quantity=random.choice(('10','20','30','40','50'))
                    )
                ]
            )
        )

        print "Invoice %s created!" % response.invoice_id

##### END CREATE INVOICES ####

if __name__ == "__main__":
    create_clients()
    create_invoices()

