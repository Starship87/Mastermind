import random
import tkinter

root = tkinter.Tk()

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
    
    for i in range(4):
        if guess[i] == str(code[i]):
            count_whites += 1
        else:
            for j in range(4):
                if guess[i] == str(code[j]):
                    count_blacks += 1
                
                
    print("whites:" + str(count_whites) +" blacks: " +str(count_blacks))
    if count_whites == 4:
        print("congradulations you win")
        print("it took you " +str (guess_count) + "guesses")
    elif guess_count == 8:
        print("you lose. The CIA will not hire you")
    else:
        player_guess()

        
    
def player_guess():
    global guess_count
    print("pls make a guess")
    guess = input()
    guess_count += 1
    score_guess(guess)



new_code()

#buttons for tkinter
b1 = tkinter.Button(root, width=4, height=2, bg="#00214b")
b1.grid(row=1, column=0)
b2 = tkinter.Button(root, width=4, height=2, bg="#999999")
b2.grid(row=1, column=1)
b3 = tkinter.Button(root, width=4, height=2, bg="#999999")
b3.grid(row=1, column=2)
b4 = tkinter.Button(root, width=4, height=2, bg="#999999")
b4.grid(row=1, column=3)

root.mainloop()




