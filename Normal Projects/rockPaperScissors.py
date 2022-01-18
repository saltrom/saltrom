import random
first = 0
second = 0
def pc_game(dtkm, first, second):
    tkm = random.randint(1,3)
    if (tkm == 1 and dtkm == 1):
        first = first + 1
        second = second + 1
        print "Player:", first
        print "Computer:", second
        print '''Player: Rock     Computer: Rock   Result: Draw \n'''
        result = open('result.txt', 'a')
        result.write('Player: 1 \t Computer: 1 \n')
        result.close()
    if (tkm == 2 and dtkm == 1):
        first = first
        second = second + 1
        print "Player: ", first
        print "Computer:", second
        print '''Player: Rock     Computer: Paper   Result: You lose \n'''
        result = open('result.txt', 'a')
        result.write('Player: 0 \t Computer: 1 \n')
        result.close()
    if (tkm == 3 and dtkm == 1):
        first = first + 1
        second = second
        print "Player:", first
        print "Computer:", second
        print '''Player: Scissors   Computer: Paper   Result: You win \n'''
        result = open('result.txt', 'a')
        result.write('Player: 1 \t Computer: 0 \n')
        result.close()
    if (tkm == 1 and dtkm == 2):
        first = first + 1
        second = second
        print "Player:", first
        print "Computer:", second
        print '''Player: Paper   Computer: Rock   Result: You win \n'''
        result = open('result.txt', 'a')
        result.write('Player: 1 \t Computer: 0 \n')
        result.close()
    if (tkm == 2 and dtkm == 2):
        first = first + 1
        second = second + 1
        print "Plater:", first
        print "Computer:", second
        print '''Player: Paper     Computer: Paper   Result: Draw \n'''
        result = open('result.txt', 'a')
        result.write('Player: 1 \t Computer: 1 \n')
        result.close()
    if (tkm == 3 and dtkm == 2):
        first = first
        second = second + 1
        print "Player:", first
        print "Computer:", second
        print '''Player: Paper     Computer: Scissors   Result: You lose \n'''
        result = open('result.txt', 'a')
        result.write('Player: 0 \t Computer: 1 \n')
        result.close()
    if (tkm == 1 and dtkm == 3):
        first = first
        second = second + 1
        print "Player:", first
        print "Computer:", second
        print '''Player: Scissors     Computer: Rock   Result: You lose \n'''
        result = open('result.txt', 'a')
        result.write('Player: 0 \t\t Computer: 1 \n')
        result.close()
    if (tkm == 2 and dtkm == 3):
        first = first + 1
        second = second
        print "Player:", first
        print "Computer:", second
        print '''Player: Scissors     Computer: Paper   Result: You win \n'''
        result = open('result.txt', 'a')
        result.write('Player: 1 \t Computer: 0 \n')
        result.close()
    if (tkm == 3 and dtkm == 3):
        first = first + 1
        second = second + 1
        print "Player:", first
        print "Computer:", Second
        print '''Player: Scissors     Computer: Scissors   Result: Draw \n'''
        result = open('result.txt', 'a')
        result.write('Player: 1 \t Computer: 1 \n')
        result.close()

while 1:
    print '''Please select a game.        if select '0' game terminates.

0-) Exit
1-) Rock Paper Scissors \n\n'''
          
    end = input()
    if (end == 0):
        print "Game terminated"
        break
    if (end == 1):
        dtkm = input("Select: 1 - Rock \t 2 - Paper \t 3 - Scissors \n\n\n")
        pc_game(dtkm, first, second)
