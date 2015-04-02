import re

def main():
    sequentie = getSequentie()
    checkDNA(sequentie)
    rna = getRNA(sequentie)
    codonSearch(rna)
    

#checkt of het dna is 
def checkDNA(sequentie):
    try:        
        #[] betekenen alleen deze karakters mogen voorkomen
        # a|b is a of b
        #krijg alleen de atgc terug in een list
        #hiernaar vergelijk je de lengte van het hele bestand met die van de regex
        regexsequentie = re.findall(r"[a|t|g|c]", sequentie)
        regex_sequentie_length = len(regexsequentie)
        sequentie_length = len(sequentie)    
        if sequentie_length == regex_sequentie_length:
            print('dit is alleen DNA')
        else:
            print('Dit is geen DNA')
    except:
        print('Er is iets fout gegaan probeer het opnieuw')

#krijgt de sequentie uit het bestand
def getSequentie():
    try:
        bestand = open("sequentie.txt")
        sequentie = bestand.read()
        return sequentie
    except:
        print('Er gaat iets fout')

def getRNA(coding):
    #van coding naar de template van daar naar de rna strand
    #coding = 'ctgat'
    #dit zou in 1 regel code kunnen 
    template = coding.replace("a", "T").replace("g", "C").replace("c", "G").replace("t","A")
    rna = template.replace("G", "c").replace("A", "u").replace("C", "g").replace("T","a").upper()
    return rna


def codonSearch(rna):
    #bool staat standerd op false deze word op true gezet op het moment dat er een start cordon word gevonden en weer op false gezet als er een stop codon word gevonden
    #print(rna)
    startcodons = ['AUG','UGG']
    stopcodons = ['UAG','UGA','UAA']
    RNA12 = 'AUGTTCUAAATCUGGAATATATUGA'
    print(RNA12)
    i = 0
    b = 0
    bool = False
    for nuc in RNA12:
        if bool == False:
            if RNA12[i:i+3] in startcodons:
                begin = i
                position = i
                end = i + 3
                bool = True
                print('Start codon gevonden op positie: ' + str(i))        
        if(bool == True):
            b += 1
            if b == 3:
                position += 3
                end += 3
                if RNA12[position:end] in stopcodons:
                    print("stop codon gevonden op positie: " +str(position))
                    print('Gevonden transcript: \n' + RNA12[begin:end])
                    bool = False
                b = 0
        
        
        i += 1
main()
