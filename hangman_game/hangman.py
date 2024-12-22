import random
from hangman_words import word_list
from hangman_art import stages

print(''' 
  _                                               
 | |                                              
 | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | | | | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_| 
                    __/ |                       
                   |___/ 
''')
#select the word from list using random module
selected_word=random.choice(word_list)
print(selected_word)

#find the word length and assign a variable
length=len(selected_word)

#create empty variable and add underscore using loop based on word length
placeholder=""
for position in range(length):
    placeholder+="_"
print(placeholder)

#get input from user for guessing letter
lives=6
correct_letter=[]
gameover=False
while not gameover:
    print(f"***********************{lives}/6 LIVES LEFT***********************")
    guess=input("guess the letter:").lower()

#match the words and user input by using loop and if-else statement
    if guess in correct_letter:
        print(f"you already guessed {guess}")
    display=""

    for letter in selected_word:
        if letter==guess:
            display+=letter
            correct_letter.append(guess)
        elif letter in correct_letter:
            display+=letter
        else:
            display+="_"
    print(display)

    if guess not in selected_word:
        lives-=1
        print(f"you guessed {guess}, that is not in the word. you lose the life.")
        if lives==0:
            gameover=True
            print(f"***********************{selected_word}YOU LOSE***********************")

    if "_" not in display:
        gameover=True
        print("***********************YOU ARE WIN***********************")


    print(stages[lives])