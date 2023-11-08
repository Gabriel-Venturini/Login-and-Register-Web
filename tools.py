import json

def read_json():
    ''' Opens the JSON file to use it whenever needed '''
    with open('users.json', 'r') as file:
        data = json.load(file)
    return data


def write_json(new_user):
    ''' Gets the actual JSON file then changes
    it content '''
    data_file = read_json()
    data_file.update(new_user)
    with open('users.json', 'w') as file:
        json.dump(data_file, file, indent=4)


def register(login, psswd, email):
    ''' Gets 3 args then create a formatted var for them '''
    new_user = {
        login: [
            {
                "email": email,
                "password": psswd
            }
        ]
    }
    write_json(new_user)


def login(login, psswd):
    ''' Opens JSON file then search for the user
    in the list using the name as an index '''
    data = read_json()
    try:
        for person in data[login.lower()]:
            if psswd == person['password']:
                return 1
            else:
                return 0
    except KeyError:
        return 0

# new_user = register()
# login() 
# I used this section to test the code