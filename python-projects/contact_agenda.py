class ContactAgenda:
    
    """
    A class to manage a contact agenda.

    Attributes:
        contacts (dict): A dictionary to store contacts, where keys are contact IDs and values are dictionaries
                         containing contact information.
        favorite_contacts (set): A set to store the IDs of favorite contacts.
        next_id (int): An integer to track the next ID for new contacts.

    Methods:
        add_contact(name, number, email): Add a new contact to the agenda.
        remove_contact(contact_id): Remove a contact from the agenda.
        favorite_contact(contact_id): Mark a contact as favorite.
        unfavorite_contact(contact_id): Remove favorite status from a contact.
        get_contacts(): Get the dictionary of all contacts.
        display_contacts(): Display all contacts sorted by their numbers.
        edit_contact(contact_id, new_name=None, new_number=None, new_email=None): Edit an existing contact.
        display_favorite_contacts(): Display only favorite contacts.
    """
    
    def __init__(self):
        """
        Initialize the ContactAgenda with an empty contacts dictionary, an empty set for favorite contacts,
        and a starting ID of 1.
        """
        self.contacts = {}
        self.favorite_contacts = set()
        self.next_id = 1



    def add_contact(self, name, number, email):
        """
        Add a new contact to the agenda.

        Args:
            name (str): The name of the contact.
            number (int): The phone number of the contact.
            email (str): The email address of the contact.
        """
        if not name or not number or not email:
            print("Todos os campos são obrigatórios!")
            return

        if number in [contact['number'] for contact in self.contacts.values()]:
            print("Contato já existe com esse número!")
            return

        contact = {
            'id': self.next_id,
            'name': name,
            'number': number,
            'email': email,
            'favorite': False
        }
        self.contacts[self.next_id] = contact
        self.next_id += 1
        print(f"Contato {name} adicionado com sucesso!")


    def remove_contact(self, contact_id):
        """
        Remove a contact from the agenda.

        Args:
            contact_id (int): The ID of the contact to be removed.
        """
        if contact_id not in self.contacts:
            print("Contato não encontrado!")
            return

        del self.contacts[contact_id]
        print(f"Contato com ID {contact_id} removido")


    def favorite_contact(self, contact_id):
        """
        Mark a contact as favorite.

        Args:
            contact_id (int): The ID of the contact to be marked as favorite.
        """
        if contact_id not in self.contacts:
            print("Contato não encontrado!")
            return

        self.contacts[contact_id]['favorite'] = True
        self.favorite_contacts.add(contact_id)
        print(f"Contato com ID {contact_id} favoritado")


    def unfavorite_contact(self, contact_id):
        """
        Remove favorite status from a contact.

        Args:
            contact_id (int): The ID of the contact to be removed from favorites.
        """
        if contact_id not in self.contacts:
            print("Contato não encontrado!")
            return

        self.contacts[contact_id]['favorite'] = False
        self.favorite_contacts.discard(contact_id)
        print(f"Contato com ID {contact_id} desfavoritado")


    def get_contacts(self):
        """
        Get the dictionary of all contacts.

        Returns:
            dict: A dictionary containing all contacts, where keys are contact IDs and values are dictionaries
                  containing contact information.
        """
        return self.contacts


    def display_contacts(self):
        """Display all contacts sorted by their IDs."""
        sorted_contacts = sorted(self.contacts.items(), key=lambda item: item[0])
        for contact_id, contact in sorted_contacts:
            star = '★' if contact_id in self.favorite_contacts else ''
            print(f"{contact_id}. {star} {contact['name']}: {contact['number']} - {contact['email']}")



    def edit_contact(self, contact_id, new_name=None, new_number=None, new_email=None):
        """
        Edit an existing contact.

        Args:
            contact_id (int): The ID of the contact to be edited.
            new_name (str, optional): The new name of the contact (default is None).
            new_number (int, optional): The new phone number of the contact (default is None).
            new_email (str, optional): The new email address of the contact (default is None).
        """
        if contact_id not in self.contacts:
            print("Contato não encontrado!")
            return

        if new_number and new_number in [contact['number'] for contact in self.contacts.values()]:
            print("Já existe um contato com esse novo número!")
            return

        if new_name:
            self.contacts[contact_id]['name'] = new_name

        if new_number:
            self.contacts[contact_id]['number'] = new_number

        if new_email:
            self.contacts[contact_id]['email'] = new_email

        print(f"Contato com ID {contact_id} editado com sucesso!")


    def display_favorite_contacts(self):
        """Display only favorite contacts."""
        star = '★'
        sorted_contacts = sorted(self.contacts.items(), key=lambda item:item[0])
        for contact_id, contact in sorted_contacts:
            star = '★' 
            if contact_id in self.favorite_contacts:
                print(f"{contact_id}. {star} {contact['name']}: {contact['number']} - {contact['email']}")
        return


agenda = ContactAgenda()


while True:
    try:
        print("\n1 - Adicionar Contato")
        print("2 - Remover Contato")
        print("3 - Favoritar Contato")
        print("4 - Desfavoritar Contato")
        print("5 - Listar Contatos")
        print("6 - Editar Contato")
        print("7 - Listar Contatos Favoritos")
        print("8 - Sair")
        option = int(input("Escolha uma opção: "))

        if option == 1:
            name = input("Digite o nome do contato: ")
            while True:
                try:
                    number = int(input("Digite o número do contato: "))
                    break
                except Exception:
                    print("Número inválido, tente novamente!")

            email = input("Digite o e-mail do contato: ")
            agenda.add_contact(name, number, email)

        elif option == 2:
            agenda.display_contacts()
            contact_id = int(input("Digite o ID do contato: "))
            agenda.remove_contact(contact_id)

        elif option == 3:
            agenda.display_contacts()
            contact_id = int(input("Digite o ID do contato: "))
            agenda.favorite_contact(contact_id)

        elif option == 4:
            agenda.display_contacts()
            contact_id = int(input("Digite o ID do contato: "))
            agenda.unfavorite_contact(contact_id)

        elif option == 5:
            agenda.display_contacts()

        elif option == 6:
            agenda.display_contacts()
            contact_id = int(input("Digite o ID do contato: "))
            new_name = input("Digite o novo nome do contato (ou deixe em branco para não alterar): ")
            new_number = input("Digite o novo número do contato (ou deixe em branco para não alterar): ")
            new_email = input("Digite o novo e-mail do contato (ou deixe em branco para não alterar): ")
            agenda.edit_contact(contact_id, new_name if new_name else None, new_number if new_number else None, new_email if new_email else None)

        elif option == 7:
            agenda.display_favorite_contacts()

        elif option == 8:
            print("Encerrando...")
            break
        else:
            print("Opção inválida!")
    except:
        print("Entrada inválida, tente novamente")
