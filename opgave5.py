def main():    
    #searchWord()
    #GCpercentage()
    gcPercentageFound()
    
def searchWord():
    try:
        file = open("IRC_representatidve_cdna.fa")
        bestand = file.readlines()
        word = input("Welk woord zoekt u?")
        for regel in bestand:
            if regel.find(">") >= 0:
                if regel.find(word) >= 0:
                    print(regel)
    except:
        print('Er heeft zich een foutmelding voor gedaan')

def GCpercentage():
    file = open("IRC_representative_cdna.fa")
    bestand = file.readlines();
    gc = 0
    totaal = 0
    for regel in bestand:
        if not(regel.find(">") >= 0):
            gc += regel.count("G") + regel.count("C")
            totaal += len(regel)
    print(100 / totaal * gc)


def gcPercentageFound():
    file = open("test.fa.txt")
    bestand = file.readlines()
    word = input("Welk woord zoekt u?")
    gc = 0
    state = False
    totaal = 0
    for regel in bestand:             
        if regel.find(word) >= 0:
            state = True;
        else:
            state = False
        if state == False:
                gc += regel.count("G") + regel.count("C")
                print(regel)
                if regel.find(">") >= 0:
                    print(regel)
                #rint(totaal)
main()


#print(regel)
#print(str(len(regel)))        
