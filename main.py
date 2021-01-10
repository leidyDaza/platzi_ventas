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

def _add_comma():
    global clients
    clients+=','

def __print_welcome():
    print("Bienvenidos a platzi ventas")
    print("*"*50)
    print('What would you like to do today?')#que es lo que quieres hacer hoy
    print('[C]reate client')
    print('[D]elete client')

if __name__=='__main__':# este es el punto de entrada
    __print_welcome()

    command=input()

    if command=='C':
        client_name=input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command =='D':
        pass
    else:
        print('Invalid command')
    list_clients()
    