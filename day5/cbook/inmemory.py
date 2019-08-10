from contact import Contact
from beautifultable import BeautifulTable
class InMemoryImpl:

    contact_list = []

    @classmethod
    def addContact(cls):
        name = input('Enter the name: ')
        email = input('Enter the email: ')
        mobile = input('Enter the mobile: ')
        addr = input('Enter the address: ')
        cls.contact_list.append(Contact(name,email,mobile,addr))
        print(f'Contact added successfully with name {name}')
    
    @classmethod
    def deleteContact(cls):
        if len(cls.contact_list)>0:
            name = input('Enter the name that has to be deleted:')
            contact = cls.get_contact_by_name(name)
            if contact:
                cls.contact_list.remove(contact)
                print(f'Conatct {name} is deleted successfully')
                InMemoryImpl._paint(cls.contact_list)
            else:
                print(f'Contact with name {name} is not found')
        else:
            print('Not found')

    @classmethod
    def viewContact(cls):
        InMemoryImpl._paint(cls.contact_list)

    @classmethod
    def search(cls):
        if len(cls.contact_list):
            name = input('Enter the name to search: ')
            s_list = list(filter(lambda x:name.lower() in x.get__name().lower(),cls.contact_list))
        
            if len(s_list)>0:
                InMemoryImpl._paint(s_list)
                print(f'Number of contacts : {len(s_list)}')
            else:
                print(f'There is no data found with name {name}')
        else:
            print('Contact book is empty')
    
    @classmethod
    def updateContact(cls):
        if len(cls.contact_list)>0:
            name = input('Enter the name to update:')
            contact = cls.get_contact_by_name(name)
            if contact:
                print('1.Name 2.Email 3.Mobile 4.Address')
                c = int(input('Enter your choice: '))
                if c == 1:
                    print(f'Old name : {contact.get__name()}')
                    name = input('Enter new name: ')
                    contact.set__name(name)

                elif c==2:
                    print(f'Old email : {contact.get__email()}')
                    email = input('Enter new email: ')
                    contact.set__email(email)
                elif c==3:
                    print(f'Old mobile : {contact.get__mobile()}')
                    mob = input('Enter the new mobile: ')
                    #if mob:
                    contact.set__mobile(mob)
                else:
                    print(f'Old address : {contact.get__address}')
                    addre = input('Enter new address: ')
                    contact.set__address(addre)
                print(f'Contact {name} is updated successfully')
            else:
                print('COntact not found;Cannot perform update')

        else:
            print('Not found')

    @staticmethod
    def _paint(lst):
        if len(lst) != 0:
            table = BeautifulTable()
            table.column_headers = ['Name','Email','Mobile','Address']
            for c in lst:
                table.append_row([c.get__name(),c.get__email(),c.get__mobile(),c.get__address()])

            print(table)
        else:
            print(f'Contact book is empty')

    @classmethod
    def get_contact_by_name(cls,name):

        if len(cls.contact_list)>0:
            contact = list(filter(lambda x:x.get__name().lower() == name.lower(), cls.contact_list))
        return contact[0] if contact else None