
import random     

def num_me(x=10):
    guess_number=random.randint(1,x)
    print("I thought a number from 1 to 10, could you guess it?")
    guesses=0
    while True:
        guesses+=1
        guess=int(input('>>>'))
        if guess<guess_number:
            print("wrong,my number is bigger than this.Try again.")
        elif guess>guess_number:
            print("wrong, my number is less than yours.Try again.")
        else:
            break 
    print(f"congrats. you found with {guesses} guesses.")    
    return guesses




def num_pc(x=10):
    input(f'from 1 to {x} you think a number then press any button, i will find:')
    below=1
    above= x
    guesses=0
    while True:
        guesses+=1
        if below!=above:
            guess=random.randint(below,above)
        else:
            guess=below
        answer=input(f"you thought [{guess}] number:\n"
                     f"if it is bigger then press(b), right(r), or less (l)".lower())
        if answer=="l":
            above=guess-1
        elif answer=='b':
            below=guess+1
        else:
            break
    print(f'i found with {guesses} guesses.')
    return guesses
                     

def play(x=10):
    play_again=True
    while play_again:
        guesses_me = num_me(x)
        guesses_pc = num_pc(x)
        if guesses_me>guesses_pc:
            print('thats cool, i won the game')
        elif guesses_me<guesses_pc:
               print('ohh noo, you won the game')
        else:
            print('its equal')
        play_again=int(input('Do you wanna play again, yes(1), no(0): '))
        