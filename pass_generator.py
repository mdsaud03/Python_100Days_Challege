import random
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y','z']
numbers=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols=['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

uletter=int(input("enter how many letters you want:"))
unumber=int(input("enter how many number you want:"))
usymbol=int(input("enter how many symbol you want:"))

password=[]
for i in range(0,uletter):12
    password.append(random.choice(letters))

for i in range(0,unumber):
    password.append(random.choice(numbers))

for i in range(0,usymbol):
    password.append(random.choice(symbols))

random.shuffle(password)

passwd=""

for i in password:
    passwd+=i



print(f'Your Generated Password: {passwd}')
