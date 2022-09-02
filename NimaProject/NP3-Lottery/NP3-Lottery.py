from random import choices

print('NP3-lottery V1.0 running...')
print('\nto use app you must add a list of members')
print('after that you will receive a winner list')
print('if you enter restart you\'r member list while deleted\n')

all_list = []

def add_mode():
    print('\nAdd mode')
    while True:
        print('\nfor exit of add mode enter 0')
        all_input = input('please enter a name : ')
        if all_input == '0':
            print('\nexiting add mode...\n')
            option_list()
        all_list.append(all_input)
        print('name added successfully')


def choices_mode():
    print('\nChoices mode\n')
    choices_number = int(input('enter a number of winners : '))
    all_choices = choices(all_list, k=choices_number)
    print('\nwinner list :')
    for i in all_choices:
        print(i)
    print('\nexiting choices mode...\n')
    option_list()


def delete_list():
    all_list = []
    print('\napp restarted')
    print('\nexiting restart mode...\n')
    option_list()

def option_list():
    while True:
        print('Options :')
        print('1) Add mode')
        print('2) Choices mode')
        print('3) Restart')
        print('4) Exit\n')
        option = int(input('Enter a number : '))
        if option == 1:
            add_mode()
        elif option == 2:
            if all_list == []:
                print('you must enter a list in add mode first\n')
            else:
                choices_mode()
        elif option == 3:
            delete_list()
        elif option == 4:
            print('\napp ended')
            print('thank you for use my app')
            break
        else:
            print('wrong input')
            print('you must enter a number between 1 to 4')
            option_list()
option_list()