import pandas as pd
from random import randint

table = []
operators = "+=-*/%"
specical_symbols = ",()&$@!;"
addresses = {}


def distinguish_token(token):
    if token in operators:
        return 'operators'
    if token in specical_symbols:
        return 'specical_symbols'
    return 'identifier'


def create_table(exp):
    global address
    tokens = [*exp]
    for token in tokens:
        enter_symbol(token)


def generate_random():
    while True:
        i = randint(1000, 10000)
        if i not in addresses.values():
            return i


def get_address(token):
    if token not in addresses.keys():
        addresses[token] = generate_random()
        return addresses[token]
    return addresses[token]


def enter_symbol(token):
    table.append({
        'symbol': token,
        'address': get_address(token),
        'type': distinguish_token(token)
    })


def remove_symbol(token):
    global table
    table = filter(
        lambda row: False if row['symbol'] == token else True, table)


def search_table(token):
    result = filter(
        lambda row: True if row['symbol'] == token else False, table)
    return result


if __name__ == "__main__":
    while True:
        option = int(input(
            "\n1. Create entry\n2. Search symbol in table\n3. Add symbol\n4. Remove symbol\n5. View table\n6. Exit \n# Enter Your Choice: "))

        if option == 6:  # EXIT
            break

        elif option == 1:  # Create entry
            expText = input("Enter Expression: ")
            create_table(expText)

        elif option == 2:  # Search symbol in table
            token = input("Enter symbol to search: ")
            print(pd.DataFrame(search_table(token)))

        elif option == 3:  # Add symbol
            token = input("Enter symbol to search: ")
            enter_symbol(token)

        elif option == 4:  # Remove symbol
            token = input("Enter symbol to Remove: ")
            remove_symbol(token)

        elif option == 5:  # View table
            print(pd.DataFrame(table))

        else:
            print("Wrong Option")
        print("\n")

'''
OUTPUT:
Please select an option:
1. Create entry
2. Search in symbol table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
Enter your choice: 1
Enter the expression: a*b*c=d
Entry added successfully!
Please select an option:
1. Create entry
2. Search in symbol table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
Enter your choice: 5
Symbol  Type
a        Identifier
*        Operator
b        Identifier
c        Identifier
=        Operator
d        Identifier
Please select an option:
1. Create entry
2. Search in symbol table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
Enter your choice: 2
Enter the symbol to search: b
b is a Identifier
Please select an option:
1. Create entry
2. Search in symbol table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
Enter your choice: 3
Enter the symbol to add: 2
Enter the type of symbol (Identifier or Operator): Identifier
Symbol added successfully!
Please select an option:
1. Create entry
2. Search in symbol table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
Enter your choice: 5
Symbol  Type
2. Search in symbol table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
Enter your choice: python -u "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L - 1\deon.py"
Traceback (most recent call last):
  File "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L - 1\main.py", line 40, in <module>
    choice = int(input("Enter your choice: "))
ValueError: invalid literal for int() with base 10: 'python -u "c:\\Users\\Atharva Pawar\\Documents\\Engineering COMPS\\SEM__6\\SPCC\\Labs\\L - 1\\deon.py"'
PS C:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L - 1> python -u "c:\Users\Atharva Pawar\Documents\Engineering COMPS\SEM__6\SPCC\Labs\L - 1\deon.py"

1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 1
Enter Expression: z=a*b*c-d+e/g-f 



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 5
   symbol  address        type
0       z     2388  identifier
1       =     7160   operators
2       a     7558  identifier
3       *     7262   operators
4       b     7354  identifier
5       *     7262   operators
6       c     3325  identifier
7       -     4947   operators
8       d     3423  identifier
9       +     1261   operators
10      e     9609  identifier
11      /     5151   operators
12      g     8374  identifier
13      -     4947   operators
14      f     3414  identifier



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 2
Enter symbol to search: a
  symbol  address        type
0      a     7558  identifier



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 3
Enter symbol to search: y



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 2
Enter symbol to search: y
  symbol  address        type
0      y     7129  identifier



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 4
Enter symbol to Remove: y



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 5
   symbol  address        type
0       z     2388  identifier
1       =     7160   operators
2       a     7558  identifier
3       *     7262   operators
4       b     7354  identifier
5       *     7262   operators
6       c     3325  identifier
7       -     4947   operators
8       d     3423  identifier
9       +     1261   operators
10      e     9609  identifier
11      /     5151   operators
12      g     8374  identifier
13      -     4947   operators
14      f     3414  identifier



1. Create entry
2. Search symbol in table
3. Add symbol
4. Remove symbol
5. View table
6. Exit
# Enter Your Choice: 6










'''
