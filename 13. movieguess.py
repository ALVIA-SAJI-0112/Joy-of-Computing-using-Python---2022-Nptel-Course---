
import random
movie=['anand','drishyam','nayakan','anbe sivam','gol maal','black friday','dangal','manichithrathazhu','taare zameen par']

def create_question(movie):
    n=len(movie)
    letters=list(movie)
    temp=[]
    for i in range(n):
        if letters[i]==' ':
            temp.append(' ')
        else:
            temp.append('*')
    qn=''.join(str(x) for x in temp)
    return qn
    
def is_present(letter,movie):
    c=movie.count(letter)
    if c==0:
        return False
    else:
        return True

def unlock(qn,movie,letter):
    ref=list(movie)
    qn_list=list(qn)
    temp=[]
    n=len(movie)
    for i in range(n):
        if ref[i]==' ' or ref[i]==letter:
            temp.append(ref[i])
        else:
            if qn_list[1]=='*':
                temp.append('*')
            else:
                temp.append(ref[i])
    qn_new=''.join(str(x) for x in temp)
    return qn_new
                
def play():
    p1_name=input("Enter player 1 name: ")
    p2_name=input("Enter player 2 name: ")
    points_p1=points_p2=0
    turn=0
    willing=True
    while willing:
        if(turn%2==0):
            #player 1's turn
            print(p1_name,"Your turn")
            picked_movie=random.choice(movie)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input("Press 1 to guess the movie or 2 to unlock another letter: ")  #user's decision d
                    if d==1:
                        ans=input("Your answer: ")
                        points_p1+=1
                        print("Correct")
                        not_said=False
                        print(p1_name,"Your score: ",points_p1)
                    else:
                        print("wrong ans, try again.")
                else:
                    print(letter,"not found")
            c=input("Press 1 to continue or 0 to quit")
            if c==0:
                print(p1_name,"Your score:",points_p1)
                print(p2_name,"Your score:",points_p2)
                print("Thanks for playing")
                willing=False
        else:
            #player 2's turn
            print(p2_name,"Your turn")
            picked_movie=random.choice(movie)
            qn=create_question(picked_movie)
            print(qn)
            modified_qn=qn
            not_said=True
            while not_said:
                letter=input("Your letter: ")
                if(is_present(letter,picked_movie)):
                    #unlock
                    modified_qn=unlock(modified_qn,picked_movie,letter)
                    print(modified_qn)
                    d=input("Press 1 to guess the movie or 2 to unlock another letter: ")  #user's decision d
                    if d==1:
                        ans=input("Your answer: ")
                        points_p2=points_p2+1
                        print("Correct")
                        not_said=False
                        print(p1_name,"Your score: ",points_p1)
                    else:
                        print("wrong ans, try again.")
                else:
                    print(letter,"not found")
            c=input("Press 1 to continue or 0 to quit")
            if c==0:
                print(p1_name,"Your score:",points_p1)
                print(p2_name,"Your score:",points_p2)
                print("Thanks for playing")
                willing=False
            turn=turn+1
play()