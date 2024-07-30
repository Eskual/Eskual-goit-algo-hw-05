def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
            return "Enter the argument for the command"
        except IndexError:
            return "Enter the argument for the command"

    return inner

def parse_input(user_input:str):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args

@input_error
def show_phone(args, contacts):
    name = ''.join(args)
    return contacts[name]

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

def show_all(contacts):
    return contacts

def main():
    contacts = {}
    print('Welcome to the assistant bot!')
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)
        if command in ['close', 'exit', 'logout']:
            print('Goodbye!')
            break

        elif command == 'hello':
            print('How can I help you?')

        elif command == 'add':
            print(add_contact(args, contacts))

        elif command == 'change':
            print(change_contact(args, contacts))

        elif command == 'phone':
            print(show_phone(args, contacts))

        elif command == 'all':
            print(show_all(contacts))

        else:
            print('Invalid command')

if __name__ == '__main__':
    main()