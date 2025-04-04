
#exDict1.py

def main():

    phonebook = {'Tra':'222-3621', 'Alex':'715-2077', 'Sandip':'920-7777'}

    print(phonebook)
    phonebook['Quynh'] = '111-2222'     #adding
    print(phonebook)
    phonebook['Tra'] = '000-0000'
    print(phonebook)
    phonebook['Isaac'] = '000-0000'
    print(phonebook)
    print()

    key, value = phonebook.popitem()
    print(f'The last pair is {key}:{value}.')
    print(phonebook)
    print()
    print(phonebook.values())
    print()

    number = phonebook.get('Cristi', 'Not Found')
    print(f"Cristi's phone number is {number}.")
    print()

    ph_num = phonebook.pop('Tra', 'Not Found')
    print(f"Tra's phone number is {ph_num}.")
    print()
    '''
    if 'Tra' in phonebook:
        del phonebook['Tra']

    else:    
        print(f'Tra is not in phonebook')
'''

    print(phonebook)

    print(f'There are {len(phonebook)} paris.')
    print()

    for item in phonebook.items():
        print(item)

    print() 

    for key, value in phonebook.items():
        print(f'{key} - {value}')

    print()    

    for key in phonebook:
        print(f'{key} - {phonebook[key]}')

    print()
    phonebook.clear()
    print(phonebook)
    print()

'''
    name = input('Enter the name: ')

    try: 
        print(f"{name}'s number is {phonebook[name]}.")

    except:
        print(f"{name} is not found!")

    if name in phonebook:
        print(f"{name}'s number is {phonebook[name]}.")

    else:
        print(f"{name} is not found!")
'''

main()