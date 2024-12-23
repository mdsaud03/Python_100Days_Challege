print("""

           _            _       _             
          | |          | |     | |            
  ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ 
 / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__|
| (_| (_| | | (__| |_| | | (_| | || (_) | |   
 \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   

 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |                           
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |                           
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

""")



def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

calc={
    "+" : add,
    "-" : sub,
    "*" : multiply,
    "/" : divide,
}
# print(calc["*"](10,2))
def calculator():

    should_continue = True

    num1=float(input("type the first number:"))

    while should_continue:
        for symbol in calc:
            print(symbol)
        calc_symbol=input("pick an operation:")
        num2=float(input("type the second number:"))
        answer=calc[calc_symbol](num1,num2)
        print(f'{num1} {calc_symbol} {num2} = {answer}')

        choice=input(f"type 'y' to continue calculating with {answer}, or 'n' to start new calculation")

        if choice=='y':
            num1=answer
        else:
            should_continue=False
            print("\n"*100)
            calculator()

calculator()