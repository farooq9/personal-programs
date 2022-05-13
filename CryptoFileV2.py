from cryptography.fernet import Fernet

# Generate a new key on your choice
def generate_key(key_name):
    key = Fernet.generate_key()

    with open(f'{key_name}.key', 'wb') as key_name:
        key_name.write(key)

# important code
# with open('mykey.key', 'rb') as mykey:
#     key = mykey.read()
    # print('Your key is: ',key)

# Encrypt a file
def encrypt(filename):
    f = Fernet(key)  #key

    with open(f'{filename}.txt', 'rb') as original_file:
        original = original_file.read()
    encrypted = f.encrypt(original)

    with open(f'{filename}.txt', 'wb') as encryped_file:
        encryped_file.write(encrypted)
    print(f' {filename} encrypted succesfully')

# Decrypt a file with the same key
def decrypt(filename):
    f = Fernet(key)

    with open(f'{filename}.txt', 'rb') as encryptd_file:
        encrypted  = encryptd_file.read()
    decrypted = f.decrypt(encrypted)

    with open(f'{filename}.txt', 'wb') as decrypted_file:
        decrypted_file.write(decrypted)
    print(f' {filename} decrypted succesfully')

# huge display name & version
def banner():
    print('\n')
    print('    ░█████╗░██████╗░██╗░░░██╗██████╗░████████╗░█████╗░███████╗██╗██╗░░░░░███████╗')
    print('    ██╔══██╗██╔══██╗╚██╗░██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔════╝██║██║░░░░░██╔════╝')
    print('    ██║░░╚═╝██████╔╝░╚████╔╝░██████╔╝░░░██║░░░██║░░██║█████╗░░██║██║░░░░░█████╗░░')
    print('    ██║░░██╗██╔══██╗░░╚██╔╝░░██╔═══╝░░░░██║░░░██║░░██║██╔══╝░░██║██║░░░░░██╔══╝░░')
    print('    ╚█████╔╝██║░░██║░░░██║░░░██║░░░░░░░░██║░░░╚█████╔╝██║░░░░░██║███████╗███████╗')
    print('    ░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░░░░╚═╝░░░░╚════╝░╚═╝░░░░░╚═╝╚══════╝╚══════╝')
    print('    Abdul Farooq                                                     version 2.0 ')
banner()

# the 4 choices
def choices():
    print(' \n 1. Encrypt a File')
    print(' 2. Decrypt a File')
    print(' 3. Generate new key')
    print(' 4. Exit')
choices()

while True:
    option = input('    \n Enter your choice: ')
    if option == '1':
        file1 = input(' Specify file to Encrypt: ')

        try:
            private_key = input(f' Specify the key name for {file1}: ')
            with open(f'{private_key}.key', 'rb') as private_key:
                key = private_key.read()
            encrypt(file1)
            print('',file1, ' Encrypted with ', private_key)
        except FileNotFoundError:
            print(' Key not found!! or File not found, Try again')

    elif option == '2':
        filell = input(' Specify file to Decrypt: ')

        try:
            private_key = input(f' Specify the key name for {filell}: ')
            with open(f'{private_key}.key', 'rb') as private_key:
                key = private_key.read()
                
            try:
                decrypt(filell)
                print('',filell, ' Decrypted with ', private_key)
            except binascii.Error:
                print('File might be already Decrypted, Pleas check')
                
        except FileNotFoundError:
            print(' Key not found!! or File not found, Try again')

    elif option == '3':
        new_name = input('  Give a unique key name: ')
        generate_key(new_name)

        with open(f'{new_name}.key', 'rb') as private_key:
            key = private_key.read()

        print(f'\nNew {new_name}.key = ', key, '\n')  #key

    elif option == '4':
        print(' Process Terminated\n')
        exit()
    else:
        print(' Option not found!!')
# Use wisely


try:
    print('hello')
except binascii.Error:
    print('hello')

