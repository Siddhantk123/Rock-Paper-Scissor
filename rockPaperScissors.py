import random

def Rock(rock):
    rand=random.randrange(0, 3) #rock paper scissor
    rock=0
    if rand==2:
        print ("You Won!")

    elif rand==1:
        print("You loose")
    else:
        print ("Draw")    



def Paper(paper):
    rand=random.randrange(0, 3) #rock paper scissor
    rock=0
    if rand==1:
        print ("You Won!")

    elif rand==2:
        print("You loose")
    else:
        print ("Draw")    


def Scissor(scissor):
    rand=random.randrange(0, 3) #rock paper scissor
    rock=0
    if rand==1:
        print ("You Won!")

    elif rand==0:
        print("You loose")
    else:
        print ("Draw")    



if __name__ == "__main__":
    print(" Welcome to the Game Rock Paper Scisor")

    input=input("Please Enter rock, paper or scissor\n ")
    if input=='rock':
        Rock(input)
    elif input=='paper':
        Paper(input)
    elif input=='scissor':
        Scissor(input)
    else:
        print("Wrong choice")    


