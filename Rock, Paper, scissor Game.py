stop = False
while(not stop):
    answerP1 = input('Player 1: Please type your choice: Rock, Paper, Scissor: ')
    answerP2 = input('Player 2: Please type your choice: Rock, Paper, Scissor: ')

    if answerP1 == answerP2:
        print('GAME DRAW')
    elif answerP1 == 'Rock' and answerP2 == 'Scissor':
        print('Player 1 Wins')
    elif answerP1 == 'Paper' and answerP2 == 'Rock':
        print('Player 1 Wins')
    elif answerP1 == 'Scissor' and answerP2 == 'Paper':
        print('Player 1 Wins')
    elif answerP1 == 'Scissor' and answerP2 == 'Rock':
        print('Player 2 Wins')
    elif answerP1 == 'Rock' and answerP2 == 'Paper':
        print('Player 2 Wins')
    elif answerP1 == 'Paper' and answerP2 == 'Scissor':
        print('Player 2 Wins')
    else:
        print('Wrong answer. Please type Rock, Paper or Scissor in your next attempt!')


    answer = input('Do you want to star a new game? (Yes or No)')


    if answer == 'Yes':
        print('New game will begin')
    elif answer == 'No':
        stop = True
        print('GAME OVER')
    else:
        print('Wrong answer, Please type Yes or No in your next attempt')
        
