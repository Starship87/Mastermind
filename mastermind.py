import random
code = []
count_whites = 0
count_blacks = 0

def new_code():
    global code
    while len(code) <4:
        r = random.randint(0,5)
        if r not in code:
            code.append(r)
def score_guess(guess):
    global code
    #first check for white
    for i in range(4):
        if guess[i] == str(code[i]):
            count_whites += 1
        else:
            for j in range(4):
                if guess[i] == str(code[j]):
                    count_blacks += 1
                
                
            
            
            
    #then check for black

    
new_code()
print("welcome to mastermind. You will need to guess a four digit code")
print("the avalible digits are 0 to 5")
print("white = good color and black = bad color")
print("you will get up to 8 turns")
guess = input()
score_guess(guess)



