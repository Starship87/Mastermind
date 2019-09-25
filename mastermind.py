import random
code = []
count_whites = 0
count_blacks = 0
guess_count = 0

def new_code():
    global code
    while len(code) <4:
        r = random.randint(0,5)
        if r not in code:
            code.append(r)
def score_guess(guess):
    global code, count_whites, count_blacks, guess_count
    count_whites = 0
    count_blacks = 0
    
    #first check for white
    for i in range(4):
        if guess[i] == str(code[i]):
            count_whites += 1
        else:
            for j in range(4):
                if guess[i] == str(code[j]):
                    count_blacks += 1
                
                
    print("whites:" + str(count_whites) +" blacks: " +str(count_blacks))
    if count_whites == 4:
        #do some win stuff
        print("congradulations you win")
        print("it took you " +str (guess_count) + "guesses")
    elif guess_count == 8:
        #you ran out of guesses 
        print("you lose. The CIA will not hire you")
    else:
        #no win no lose keep going
        player_guess()

        
    
def player_guess():
    global guess_count
    print("pls make a guess")
    guess = input()
    guess_count += 1
    score_guess(guess)



new_code()
print("welcome to mastermind. You will need to guess a four digit code")
print("the avalible digits are 0 to 5")
print("white = good color and black = bad color")
print("you will get up to 8 turns")
player_guess()




