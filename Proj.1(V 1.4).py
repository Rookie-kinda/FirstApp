# PTP

print('Hello user, i am Python Test Program, or PTP for short, what\'s your name?')
username = input('Enter name here: ')
print('Hello, ' + username.capitalize() + ', What can i do for you today?')


def choice():
    print('Math\nMadlips\nCompare numbers\nEnd program')


def interactive():
    user_choice = input('a/b/c/d/e: ')
    if user_choice == 'a' or user_choice == 'A':
        def math():
            try:
                num1 = float(input('Insert Number: '))
                operation = input('Insert desired operation: ')
                num2 = float(input('Insert another number: '))
                if operation == '+':
                    print(float(num1 + num2))
                elif operation == '-':
                    print(float(num1 - num2))
                elif operation == '*':
                    print(float(num1 * num2))
                elif operation == '/':
                    print(float(num1 / num2))
                else:
                    print('Invalid operation, please use summation, subtraction, multiplication, or division')
                    math()
            except ValueError:
                print('Please insert a number (whole or decimal)')
                math()

            except ZeroDivisionError:
                print('You can\'t divide by zero')
                math()
        math()
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
        print('Goodbye ' + username.capitalize() + ', It was nice meeting you')


def again():
    print('Do you wish to go on?')
    cont = input('y/n: ')
    if cont == 'y':
        interactive()
    else:
        print('Good bye ' + username.capitalize() + ', It was nice meeting you 😊')


choice()
interactive()
