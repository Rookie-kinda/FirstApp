# PTP

print('Hello user, i am Python Test Program, or PTP for short, what\'s your name?')
username = input('Enter name here: ')
print('Hello, ' + username.capitalize() + ', What can i do for you today?')


def choice():
    print('Math\nMadlips\nCompare numbers\nEnd program')


def interactive():
    user_choice = input('a/b/c/d/e: ')
    if user_choice == 'a' or user_choice == 'A':
        def calc(x):
            try:
                if '+' in x:
                    i = x.split('+')
                    print(int(i[0]) + int(i[1]))
               elif '-' in x:
                    j = x.split('-')
                    print(int(j[0]) - int(j[1]))
               elif '*' in x:
                    k = x.split('*')
                    print(int(k[0]) * int(k[1]))
               elif '/' in x:
                    s = x.split('/')
                    print(int(s[0]) / int(s[1]))
               else:
                    print('invalid operator')
                    calc(input())
            except ZeroDivisionError:
                print('Don\'t divide by zero...dumbass')
                calc(input())
           calc(input())
calc(input())

            except ValueError:
                print("Please use a propper operator")
                calc(input())
        calc(input())
        again()
    elif user_choice == 'b' or user_choice == 'B':
        color = input('Insert color: ')
        something = input('Type in something: ')
        print('Roses are ' + color + ' Violets are blue ' + something)
        again()

    elif user_choice == 'c' or user_choice == 'C':
        def org():
            try:
                maxnum = (int(float(input('Insert number here: '))), int(float(input('Insert number here: '))), int(float(input('Insert number here: '))), int(float(input('Insert number here: '))))
                print(max(maxnum))
            except ValueError:
                print('Please insert numbers, not in letters')
                org()
        org()
        again()
    elif user_choice == 'd' or user_choice == 'D':
        def evenorodd():
            try:
                even = int(input('insert desired number: '))
                if even % 2 == 0:
                    print('this is an even number')
                else:
                    print('this is an odd number')
            except ValueError:
                print('please use numbers...')
                evenorodd()
        evenorodd()
        again()

    elif user_choice == 'e' or user_choice == 'E':
        print('Goodbye ' + username + ', It was nice meeting you')


def again():
    print('Do you wish to go on?')
    cont = input('y/n: ')
    if cont == 'y':
        interactive()
    else:
        print('Good bye ' + username + ', It was nice meeting you 😊')


choice()
interactive()
