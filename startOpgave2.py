#################################################################################
# Controle op enzymen die knippen in een sequentie
# Bron GenBank bestand: http://www.canr.msu.edu/lgc/GenBankfiles/AF165912.htm
# Auteur: Martijn van der Bruggen
#         HAN University
# Creatie: november 2008 (MvdB)
# Updates:
# november 2009, aanpassing aan nieuw boek (MvdB)
# november 2010, Dictionary met enzymen en knipplaats opgeheven (MvdB)
# november 2011, aanpassing syntax voor Python3 compatibility door Stephan Heijl
# november 2011, leesbaarheid functie aangepast (MvdB) 
# november 2014, aanpassing aan nieuw boek (EK) en extra commentaar
#################################################################################

# Enzymen met knipprofiel
# Voor meer informatie over restrictie enzymen bekijk: http://nl.wikipedia.org/wiki/Restrictie-enzym
# Lijst met restrictie enzymen, sequentie waar ze in knippen en het organisme waar ze in voorkomen
DdeI   = "CTGAG"    #knipt op C^TGAG      Desulfovibrio desulfuricans    	
BspMII = "TCCGGA"   #knipt op T^CCGGA     Klebsiella pneumoniae 
EcoRI  = "GAATTC"   #knipt op G^AATTC     Escherichia coli
HindIII= "AAGCTT"   #knipt op A^AGCTT     Haemophilus influenzae
TaqI   = "TCGA"     #knipt op T^CGA    	  Thermus aquaticus

# Lees een bestand en parse de sequentie
def getSequentie (bestandsnaam):
    bestand = open (bestandsnaam,encoding="latin1")
    startReading = False            #Zolang die false is niets toevoegen aan sequentie
    raw_data = ""   
    for regel in bestand:
        if startReading:            # Hier staat hetzelfde als 'if startReading == True'. 
                                    # De if statement moet een True opleveren om te kunnen plaatsvinden.
                                    # startReading is een bool, dus pas als deze True is, kan de if een True opleveren.
            raw_data += regel[10:]  # lees van iedere regel alleen het DNA
        if "ORIGIN" in regel:
            startReading = True     # Startpunt van DNA sequentie gevonden
    #Verwijder uit de sequentie alle spaties, next line tokens
    sequence= raw_data.replace(' ','').replace('\n','').replace('\r','')
    return sequence                 # retourneer een sequentie zonder extra chars

# Doorzoek nu de sequentie op knipplaatsen.
# Toon voor ieder enzym uit de dictionary of deze knipt of niet.
# In de uitvoer staat bijvoorbeeld:
# >>> BamH1 knipt wel
# >>> EcoRII knipt niet
# (Optioneel) Toon de ontstane fragmenten voor iedere knip

# Bonus: geef per enzym aan op welke posities van het DNA er geknipt is
# De uitvoer wordt dan bijvoorbeeld:
# >>> BamH1 knipt op positie 57
# >>> EcoRII knipt niet


lowerDdeI = DdeI.lower()
if sequentie.find(lowerDdeI) >= 0:
    print('DdeI')
    
lowerBspMII = BspMII.lower()
if sequentie.find(lowerBspMII) >= 0:
    print('BspMII')
    
lowerEcoRI = EcoRI.lower()
if sequentie.find(lowerEcoRI) >= 0:
    print('EcoRI')

lowerHindIII = HindIII.lower()
if sequentie.find(lowerHindIII) >= 0:
    print('HindIII')

lowerTaqI = TaqI.lower()
if sequentie.find(lowerTaqI) >= 0:
    print('TaqI')
    
sequentie = getSequentie("startOpgave2.txt")
cutting = cutSequentie(sequentie)
print(cutting);

