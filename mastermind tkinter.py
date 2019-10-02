import random
import tkinter


root = tkinter.Tk()
color_picker = ''

COLORS = ['red','yellow','lime','blue','blanchedalmond','purple']
code = []
count_whites = 0
count_blacks = 0
guess_count = 0
current_guess = [''] * 4

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


def open_color_picker(pos, btn):
    global color_picker
    color_picker = tkinter.Toplevel(root)
    color1 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[0], command=lambda:close_color_picker(pos, btn, COLORS[0]))
    color1.grid(row=0, column=0)
    color2 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[1], command=lambda:close_color_picker(pos, btn, COLORS[1]))
    color2.grid(row=0, column=1)
    color3 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[2], command=lambda:close_color_picker(pos, btn, COLORS[2]))
    color3.grid(row=0, column=2)
    color4 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[3], command=lambda:close_color_picker(pos, btn, COLORS[3]))
    color4.grid(row=0, column=3)
    color5 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[4], command=lambda:close_color_picker(pos, btn, COLORS[4]))
    color5.grid(row=0, column=4)
    color6 = tkinter.Button(color_picker, width=4, height=2, bg=COLORS[5], command=lambda:close_color_picker(pos, btn, COLORS[5]))
    color6.grid(row=0, column=5)

def close_color_picker(pos, btn, newcolor):
    global color_picker
    color_picker.destroy()
    btn.config(bg=newcolor)
    current_guess[pos] = newcolor
    
   
def draw():
    global canvas
    canvas.delete(tkinter.ALL)
    canvas.create_rectangle(0,0,cwidth, cheight, fill="lime")

#buttons for tkinter
b1 = tkinter.Button(root, width=4, height=2, bg="#999999", command=lambda:open_color_picker(0,b1))
b1.grid(row=1, column=0)
b2 = tkinter.Button(root, width=4, height=2, bg="#999999", command=lambda:open_color_picker(1,b2))
b2.grid(row=1, column=1)
b3 = tkinter.Button(root, width=4, height=2, bg="#999999", command=lambda:open_color_picker(2,b3))
b3.grid(row=1, column=2)
b4 = tkinter.Button(root, width=4, height=2, bg="#999999", command=lambda:open_color_picker(3,b4))
b4.grid(row=1, column=3)

#submit button
submit = tkinter.Button(root, text="Submit Guess", font="Arial 16 bold", padx=10)
submit.grid(row=1, column=4, padx=20)

#canvas
cwidth=300
cheight=400
canvas = tkinter.Canvas(root, width=cwidth, height=cheight)
canvas.grid(row=2, column=0, columnspan=5)

new_code()
draw()

root.mainloop()

