import random

#todo
#1 zie beschrijving

def main():
    word = getWord()
    UserChoose(word)    

#zet de woorden in een list en kiest een random woord
def getWord():
    try:
        bestand = open("test.txt")
        wordFile = bestand.read()
        word = []
        # Alle woorden in het bestand hebben een spatie in de 3 onderstaande regels code
        # worden de woorden in een list gezet en daarna met de choice functie word er een random woord gereturned
        words = list(wordFile.split())
        word = random.choice(words)
        bestand.close()
        return word
    except IOError:
        bestand = open('test.txt', 'w')
        print('Sluit het programma en voeg woorden toe aan het bestand')

      
#gebruiker geeft een letter op deze functie zorgt voor de algemene afhandeling
def UserChoose(word):
    empty_arr = getEmptyList(word)    
    i = 0
    strafpunt = 0
    letterlist = []
    while (i <= 9):
        try:
            letter = str(input("geef uw letter op: "))
        except ValueError: 
            print('er is iets fout gegegaan met het invoeren')
        if checkLetter(letter,letterlist) == True:            
            quessWord = setLetterList(empty_arr,word,letter)
            print('\n\n'+quessWord+'\n\n')            
            if letter in word:           
                if(quessWord.find('-') == -1):
                    print('Gefeliciteerd gewonnen')
                    main()
            else:
                strafpunt = strafpunt + 1
                if(strafpunt == 10):
                    galg(10)
                    print('helaas je hebt verloren! het programma start overnieuw')
                    main()            
                i = i + 1
            galg(strafpunt)
        else:
            print('Deze letter heeft u al gebruikt')
        
            
#handeld de galg afbeelding af
def galg(i):
    step = [
            '',
            '|\n|\n|\n|\n- - - -',
            '----------\n|\n|\n|\n|\n- - - - - -',
            '---------\n|/\n|\n|\n|\n- - - - - -',
            '---------\n|/\t|\n|\n|\n|\n- - - - - -',
            '---------\n|/      |\n|       0\n|\n|\n- - - - - -',
            '---------\n|/      |\n|       0\n|\t|\n|\n- - - - - -',
            '---------\n|/       |\n|        0\n|       /|\n|\n- - - - - -',
            '---------\n|/       |\n|        0\n|       /|\ \n|\n- - - - - -',
            '---------\n|/       |\n|        0\n|       /|\ \n|       / \n- - - - - -',
            '---------\n|/      |\n|       0\n|      /|\ \n|      / \ \n- - - - - -']
    print(step[i])

#functie checkt of de letter al geweest is of niet returned een bool
def checkLetter(letter,letterlist):       
    if letter in letterlist:
         return False
    else:
        letterlist.append(letter)
        return True

#######################################################################
#hier worden de letters die geraden zijn getoont in de juiste volgorde#
#######################################################################

#maakt een list die evenveel elementen bevat als het woord aan letters
#input: schaap
#output: ['-','-','-','-','-','-']
def getEmptyList(word):
    #zet de letters als listitems in een list
    wordlist = list(word);
    empty_arr = []
    for item in wordlist:
        #veranderd de letter naar een -
        empty_arr.append('-')
    return empty_arr

#functie zet de gekozen letter op de correcte plaatsen in de list en returned een string
def setLetterList(empty_arr,word,chooseLetter):
    for i, letter in enumerate(word):
        if letter == chooseLetter:
            empty_arr[i] = chooseLetter    
    correct_string= ''.join(empty_arr)
    return correct_string
    
main()
