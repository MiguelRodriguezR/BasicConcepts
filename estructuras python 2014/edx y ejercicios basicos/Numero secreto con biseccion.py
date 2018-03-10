# Create by Miguel Rodriguez
# bisection search for guesses a secret number
num=100
print ("Please think of a number between 0 and 100! ")
Guess='l'
num=num/2
low=0
high=99
option='y'
while Guess=='l' or Guess=='h':
    print ("Is your secret number " + str(num)+"? ")
    Guess=str(input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly "))
    if Guess=='l':
        low=num
        if num>100:
            num=99
    elif Guess=='h':
        high=num
    elif Guess=='c':
        break
    else:
        print("Sorry, I did not understand your input.")
        Guess='h'
        option='n'
    if option!='n':
        num = int((high + low)/2.0)
    else:
        option='y'
