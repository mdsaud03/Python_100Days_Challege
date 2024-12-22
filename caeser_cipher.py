print("""   ######
  #     #
 #  CAESAR  #
#  CIPHER  #
 #  #####  #
  #     #
   ###### """)


alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caeser(original,shift_num,encode_or_decode):
    result = ""
    if encode_or_decode == "decode":
        shift_num *= -1

    for letter in original:

        if letter not in alphabet:
            result += letter
        else:
            position = alphabet.index(letter) + shift_num
            position %= len(alphabet)
            result += alphabet[position]

    print(f" the {encode_or_decode}d result: {result}")

should_continue=True
while should_continue:
    direction=input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")
    text=input("enter your message:\n")
    shift=int(input("how many shift you want:\n"))

    caeser(original=text,shift_num=shift,encode_or_decode=direction)

    restart=input("Type 'Yes' to continue, Type 'No' to terminate\n")
    if restart=="no":
        should_continue=False
        print("Exited!!!")

