import random
def game():
    print("you are playing the game...")
    score=random.randint(1,62)
    #yahn sey score uthega 
    with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\highscore.txt") as f:
        hiscore=f.read() #yeh ek varriable hai
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"your score:{score}")
    
    if(score>hiscore):
        with open(r"C:\Users\Lenovo\Desktop\python2\chapter 9\highscoreF.txt","w") as f:
            f.write(str(hiscore))
    return score
game()