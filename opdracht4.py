def main():
    bestand = open("sequentie.txt")
    file = bestand.readline()
    getPercentage(file)
    isDNA(file)
    getComplement(file)
    GetCodons(file)

def getPercentage(bestand):    
    print(100 / len(bestand) * (bestand.count("g") + bestand.count("c")))

def isDNA(bestand):
    print(bestand.count("g") + bestand.count("c") + bestand.count("a") + bestand.count("t") - len(bestand) > 0)

def getComplement(bestand):
    print(bestand.replace("a", "T").replace("g", "C").replace("c", "G").replace("t","A").lower())

def GetCodons(bestand):
    codon = ''
    for i in range(0, len(bestand),3):
        codon += ' ' + bestand[i:i+3]
        if(bestand[i:i+3] == 'tta'):
            print(codon)
    
main()



    
    
