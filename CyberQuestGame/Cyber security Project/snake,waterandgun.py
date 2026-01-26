# import random

# print('Welcome to Snake-Water-Gun Game')
# rounds = int(input('Enter number of rounds: '))
# choices = {'g':'s', 's':'w', 'w':'g'}
# p_score = c_score = 0
# for i in range(1, rounds+1):
#       p = input("Choose s for Snake, w for Water, g for Gun: ").strip()
#       if p not in choices:
#             print("Invalid input, try again\n")
#             continue
#       Computer = random.choice(list(choices.keys()))
#       print(f'You choose:  {p}, \n  computer choose:  {Computer}')
#       if choices[Computer] == p:
#             c_score += 1
#       elif choices[p] == Computer:
#             p_score += 1
#       else:
#             print(f"\t Round {i} is Draw")
#       print(f'Your score in round {i} is : {p_score}')
#       print(f'Computer score in round {i} is : {c_score}')

# print(f'Your final score is : {p_score}')
# print(f'Computer final score is : {c_score}')
# if p_score > c_score:
#       print("Congratulations!! You Won")
# elif c_score > p_score:
#       print("You lose!!")
# else:
#       print("Match Draw!!")

# import random

# def rec():
#  play=int(input("if you want to play press 1 aur pressc any key"))
#  if play==1:
#   Computer=['s','w','g']
#   Computer=random.choice(list(Computer))
#   print(Computer)
  
# rec()
# d=['s','w','g']
# d=random.choice(list(d))
# print(d)

# import random

# win_matrix = []
# choice_list = ["Snake" , "Water" , "Gun"]
# win_matrix = [['D' , 'W' , 'L'],['L' , 'D' , 'W'],['W' , 'L' , 'D']]
# dict_points = {'S' : 0 , 'W' :1 , 'G':2 }

# player_1 = input("Player1 Select your option from (Snake,Water,Gun)?")

# player_2 = random.choice(choice_list)
# print(f"System selected ::  {player_2} ")

# print("Player1  you : " , win_matrix[dict_points[player_1[0]]][dict_points[player_2[0]]])


from random import choice

def score_func():
    c_score = p_score = 0
    total_round=int(input("how many round do you want play:"))
    for round in range(1,total_round):
 
        computer_choice=['s','w','g']
        computer=choice(list(computer_choice))
        d={'s':0,'w':1,'g':2}

        person=str(input("User choices between gun, snake and water is : ").strip())
 
        print("Computer choices between gun, snake and water is : " , computer )
 
        print(f"Computer choose {computer} and Person choose {person}")

        if person == 'w' or person == 's' or person == 'g':
            if computer == person:
                print("match is draw")
            elif computer == 's' and person == 'w':
                c_score += 1
                print("computer is the winner")
            elif computer == 'w' and person == 'g':
                c_score += 1
                print("computer is winner")

            elif computer == 'g' and person == 's':
                print("computer is the winner")
                c_score += 1
            else:
                print("person is winner")
                p_score += 1
        else:
            print("you input invalid character")
    print(c_score)
    print(p_score)
    again_play=input("Do you want to continue Press y for continue:")

    if again_play=="y":
        return score_func()



score_func()



