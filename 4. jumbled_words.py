import random
def choose():
    words=['rainbow','computer','science','programming','mathematics','player','condition', 'reverse', 'water','board']
    pick=random.choice(words)
    return pick

def jumble(word):   
    jumbled="".join(random.sample(word,len(word))) #choose len(word) letters in random order
    #(.join())to join the randomly chosen letters and make a word
    return jumbled

def thank(p1n,p2n,p1,p2):
    print(p1n,' Your score is: ',p1)
    print(p2n,' Your score is: ',p2)
    print('Thanks for playing. Bye!')
    
    
def play():
    p1_name=input('Player 1, Please enter your name')
    p2_name=input('Player 2, Please enter your name')
    points_p1=0
    points_p2=0
    turn=0  #to determine which player's turn it is #qstns posed to both players would be same but turns they get alternatively
    while(1): #the game stops whe one of the players wants to quit
        #computer's task
        picked_word=choose() #there is a dictionary and word is chosen from it
        #create question
        qn=jumble(picked_word)
        print(qn)
        #player 1
        if turn%2==0: #at even values of turn its P1's turn to play
            print(p1_name,'This is your turn. ')
            ans=input('What is on my mind?')
            if ans==picked_word:
                points_p1=points_p1+1
                print('Your score is: ',points_p1)
            else:
                print('Better luck next time, I thought: ',picked_word)
            c=int(input('Press 1 to continue'))
            if c==0:
                thank(p1_name,p2_name,points_p1,points_p2)
                break
        #player 2 #at odd values of turn its P2's turn to play
        else:
            print(p2_name,'This is your turn. ')
            ans=input('What is on my mind?')
            if ans==picked_word:
                points_p2=points_p1+1
                print('Your score is: ',points_p2)
            else:
                print('Better luck next time, I thought: ',picked_word)
            c=input('Press 1 to continue')
            if c==0:
                thank(p1_name,p2_name,points_p1,points_p2)
                break
        turn=turn+1
play()