def mainGame(choice, gameStatus):
    if int(choice) == 1:

        print('Game Start\n')

    elif int(choice) == 2:

        print('Help Screen\n')

    elif int(choice) == 3:

        print('Game Closed\n')
        gameStatus = 1

    else:

        print('Invalid Input. Please try again.\n')

    return gameStatus

gameFinished = 0

while gameFinished == 0:
    print('********************')
    print('|Welcome to Hangman|')
    print('|                  |')
    print('| 1.) Play Hangman |')
    print('| 2.) Help         |')
    print('| 3.) Quit         |')
    print('********************')

    userChoice = input('User choice: ')

    if userChoice != '1' and userChoice != '2' and userChoice != '3':
        print('Invalid Input. Please try again.\n')
    else:
        gameFinished = mainGame(userChoice, gameFinished)
