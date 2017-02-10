#draw spaces
#take guess
#draw guessed letter and strikes
#print out win/lose
import random


wordList = ['canada', 'usa', 'chile', 'japan', 'china', 'korea', 'mexico', 'united kingdom', 'ireland', 'spain', 'france', 'australia', 'russia', 'thailand', 'india', 'sweden']

def letterGame():
    secretWord = random.choice(wordList)
    print("Guess what country I'm thinking of: ")
    blank = ("_" * (len(secretWord)))
    print(blank)
    test = list(secretWord)
    blankList = list(blank)
    print(test)
    guess = str(input(">"))
    if guess in secretWord:
        secretWordIndexes = [i for i, n in enumerate(test) if n == guess]
        print(secretWordIndexes)
        for n in secretWordIndexes:
            del blankList[secretWordIndexes[n]]
            blankList.insert(secretWordIndexes[n], guess)
            print(blankList)
    else:
        print("Blank")


letterGame()



