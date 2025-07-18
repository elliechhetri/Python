import random
import logo
print("Welcome to Secret Spy Survival Simulator!")
name=input("Enter your name:\n")
print(f"Hello {name}, welcome to Operation Phantom")
print(f"Now,{name} if you are ready shall we start.")
while True:
    decide=input("Enter your decision:\t").lower()
    if  decide=="yes" or decide =="ok" or decide=="yay":
        print("""We will decide  if you can play or not further  by playing
          our childhood game rock,paper and scissors  if you lose you can't
           play otherwise you can.""")
        break
    elif decide=="no" or decide=="nah":
        print("Will wait till you are ready")
    else:
        print("Can't Understand can you try again?")

rock="rock"
paper="paper"
scissors="scissors"
comp=["rock","paper","scissors"]
while True:
    new = random.choice(comp)
    user = input("Select either rock,paper or scissors:\n").lower()
    if (user==rock and new==scissors) or(user==scissors and new==paper) or (user==paper and new==rock):
        if user==rock and new==scissors:
            print("you chose Rock")
            print(logo.rock)
            print("computer chose scissors")
            print(logo.scissors)
            print("You Win!")
            break
        elif user==scissors and new==paper:
            print("you chose Scissors")
            print(logo.scissors)
            print("computer chose paper")
            print(logo.paper)
            print("You Win!")
            break
        else:
            print("you chose Paper")
            print(logo.paper)
            print("computer chose Rock")
            print(logo.rock)
            print("You Win!")
            break
    elif (new==rock and user==scissors) or(new==scissors and user==paper) or (new==paper and user==rock):
        if new == rock and user == scissors:
            print("computer chose Rock")
            print(logo.rock)
            print("you chose scissors")
            print(logo.scissors)
            print("computer Win!")
            print("Sorry you can't play further as computer won the game")
            exit()

        elif new==scissors and user==paper:
            print("computer chose Scissors")
            print(logo.scissors)
            print("you chose paper")
            print(logo.paper)
            print("computer  Win!")
            print("Sorry you can't play further as computer won the game")
            exit()
        else:
            print("computer chose Paper")
            print(logo.paper)
            print("you  chose Rock")
            print(logo.rock)
            print("computer  Win!")
            print("Sorry you can't play further as computer won the game")
            exit()
    elif (new==rock and user==rock) or(new==scissors and user==scissors) or (new==paper and user==paper):
        if new==rock and user==rock:
            print("you chose rock")
            print(logo.rock)
            print("computer  chose Rock")
            print(logo.rock)
            print("Tie. choose again")
        elif  new==scissors and user==scissors:
            print("you chose scissors")
            print(logo.scissors)
            print("computer  chose scissors")
            print(logo.scissors)
            print("Tie. choose again")
        else:
            print("you chose paper")
            print(logo.paper)
            print("computer  chose paper")
            print(logo.paper)
            print("Tie. choose again")

    else:
        print("please try again")



print(f"Congratulations {name} for winning rock,paper and scissors" )
random_words = ['kzumo', 'raple', 'qneiv', 'sylod', 'zafut',
                'deqon', 'muvak', 'tigru', 'vopem', 'bynaq']
shift_numbers = [4, 7, 2, 9, 5,
                 3, 1, 6, 8, 2]
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
print("""you will get  random word and
shift number then after that check the message""")

print(logo.logo_cy)

word_cea=random.choice(random_words)
shift_cea=random.choice(shift_numbers)
print(word_cea)
print(shift_cea)
def decrypt(wo,ho):
    hu=""
    for each in wo:
        no=alphabet.index(each)-ho
        no%=len(alphabet)
        hu+=alphabet[no]
    print(f"so your message is\n{hu}")


wo=input("enter your word:\n").lower()
ho=int(input("enter your shift number:\n"))
decrypt(wo,ho)
total=5
num=list("0123456789")
randomuu=random.randint(1,total-1)
ran=total-randomuu
alphabetz=""
numberz=""
for eac in range(randomuu):
    alphabetz+=random.choice(alphabet)
for ea in range(ran):
    numberz+=random.choice(num)
new=alphabetz+numberz
shuf=list(new)
random.shuffle(shuf)
jon=''.join(shuf)
print(f"the code is\n{jon}")
print("Welcome to hang man. You have 6 lives")
print(logo.logo)
lives=6
blank=""
for e in jon:
    blank+="_"
print(blank)
game_over=False
container=[]
guessed_word=[]
while not game_over:
   gs= input("enter a word:\n")
   if gs in guessed_word:
       print(f"you already have guessed the word{gs}")
       continue
   guessed_word+=gs
   word_hangman=""
   for c in jon:
       if c==gs:
           word_hangman+=c
           container.append(c)
           print(f"you have {lives} lives left!")
       elif c in container:
           word_hangman+=c

       else:
           word_hangman+="_"

   print(word_hangman)
   if gs not in jon:
            lives-=1
            print(f"you have {lives} lives left!")
   if lives==0:
        game_over=True
        print("you loose!")
        exit()
   if "_" not in word_hangman:
        print("Congratulations lets go on next step")
        game_over = True
   from logo import stages
   print(stages[lives])


print("Now you are in Second last stage of game")
while True:
    color=input("""choose ay colour door in between "red" "blue" and "yellow".\n""").lower()
    if color=="red":
        print(f"Sorry{name}you came this far but you lost but here is your red toffee 🍬")
        exit()
    elif color=="blue":
        print(f"Sorry{name}you came this far but you lost but here is your blue heart 💙")
        exit()
    elif color=="yellow":
        print("you won $100000")
        print(logo.treasure)
        break
    else:
        print("please write colour name")


print("Final i am giving bonus money to you.choose between a ,b and c ")
while True:
    final_bonus=input("enter a,b or c\n").lower()
    if final_bonus=="a":
        money=15/100*100000+100000
        print(f"""congratulations{name}!You won ${money}""")
        exit()
    elif final_bonus=="b":
        money=10/100*100000+100000
        print(f"""congratulations{name}!You won ${money}""")
        exit()
    elif final_bonus=="c":
        money=9/100*100000+100000
        print(f"""congratulations{name}!You won ${money}""")
        exit()
    else:
        print("Please type either a, b or c to get your reward")