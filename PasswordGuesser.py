#Created by Joseph D. Cline Jr. ID: 405QBBT0KO Copyright © 2018 JoeCline.
#This password generator is used to well guess your password, what you first do is enter a word/number or both into the input box which then gets transfered into a variable named Password. After that what happens is the password is broken down into a list with each digit being seperate from the rest and a loop then tries to pin point letters and numbers that match.
Password = input("Please enter your password: \n").upper()
PasswordGuess = list(Password)
OptionLetters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
OptionNumbers = list("0123456789")
Test1 = len(Password)
NumForLet = 0

for x in range(0, Test1):
    while True:
        if PasswordGuess[NumForLet] == OptionLetters[0]:
            print("Letter Matched: A")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[1]:
            print("Letter Matched: B")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[2]:
            print("Letter Matched: C")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[3]:
            print("Letter Matched: D")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[4]:
            print("Letter Matched: E")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[5]:
            print("Letter Matched: F")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[6]:
            print("Letter Matched: G")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[7]:
            print("Letter Matched: H")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[8]:
            print("Letter Matched: I")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[9]:
            print("Letter Matched: J")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[10]:
            print("Letter Matched: K")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[11]:
            print("Letter Matched: L")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[12]:
            print("Letter Matched: M")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[13]:
            print("Letter Matched: N")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[14]:
            print("Letter Matched: O")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[15]:
            print("Letter Matched: P")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[16]:
            print("Letter Matched: Q")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[17]:
            print("Letter Matched: R")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[18]:
            print("Letter Matched: S")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[19]:
            print("Letter Matched: T")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[20]:
            print("Letter Matched: U")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[21]:
            print("Letter Matched: V")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[22]:
            print("Letter Matched: W")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[23]:
            print("Letter Matched: X")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[24]:
            print("Letter Matched: Y")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionLetters[25]:
            print("Letter Matched: Z")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[0]:
            print("Number Matched: 0")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[1]:
            print("Number Matched: 1")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[2]:
            print("Number Matched: 2")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[3]:
            print("Number Matched: 3")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[4]:
            print("Number Matched: 4")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[5]:
            print("Number Matched: 5")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[6]:
            print("Number Matched: 6")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[7]:
            print("Number Matched: 7")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[8]:
            print("Number Matched: 8")
            NumForLet = NumForLet + 1
            break
        elif PasswordGuess[NumForLet] == OptionNumbers[9]:
            print("Number Matched: 9")
            NumForLet = NumForLet + 1
            break
        else:
            print("Please only enter a password that includes numbers and letters")
            break
print("The computer has concluded after " + str(Test1) +" tries that the password entered is: " + str(Password))
