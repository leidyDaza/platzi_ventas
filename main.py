clients ='pablo,ricardo,'

def create_client(client_name):
    global clients
    if client_name not in clients:
        clients+=client_name
        _add_comma()
    else:
        print('Client already is the client\'s list') 
    
def list_clients():
    global clients
    print(clients)    

def update_client(client_name, update_client_name):
    global clients
    if client_name in clients:
        clients=clients.replace(client_name+',',update_client_name+',')
    else: 
        print('Client is not in clients list')


def _add_comma():
    global clients
    clients+=','

def __print_welcome():
    saludo="Bienvenidos a platzi ventas"
    print(saludo.center(20,'o'))
    print("*"*50)
    print('What would you like to do today?')#que es lo que quieres hacer hoy
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')


def _get_cliente_name():
    return input('What is the client name? ')


if __name__=='__main__':# este es el punto de entrada
    __print_welcome()

    command=input()
    command=command.upper()

    if command=='C':
        client_name=_get_cliente_name()
        create_client(client_name)
        list_clients()
    elif command =='D':
        pass
    elif command=='U':
        client_name=_get_cliente_name()
        update_client_name=input('What is the update client name: ')
        update_client(client_name,update_client_name)
        list_clients()
    else:
        print('Invalid command')
        list_clients()
    