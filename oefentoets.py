#naam: Wouter Wajer
#datum: 03-12-2014


def main():
    bestand = open("flu.txt","r")
    zoekWoord(bestand,"Singapore")
    hostLijst(bestand)
    bepaalAA(bestand)

#kijkt of een woord voorkomt in het bestand 
def zoekWoord(bestand,woord):
    try:
        for regel in bestand:
            if woord.upper() in regel.upper():
                print(regel)            
    except:
        print('Er heeft zich een foutmelding voor gedaan')
 
#haalt een lijst op met alle hosts en haalt de gedupliceerde er uit
def hostLijst(bestand):
    try:
        noduplicates = []
        list = splitfile(bestand)
        for regel in list:            
            if regel[2] not in noduplicates:
                noduplicates.append(regel[2])                
        print(noduplicates)
    except:
        print('Er heeft zich een foutmelding voor gedaan')

#bepaalt het gemiddelde van de aminozuren
#uitkomst telt alle list waardes bij elkaar op
#i kijkt hoeveel list items er aanwezig zijn
#hierna kan je het gemiddelde berekenen wat alles bij elkaar opgeteld is / het aantal
def bepaalAA(bestand):
    try:
        list = splitfile(bestand)
        uitkomst = 0
        i = 0
        for regel in list:
            uitkomst += int(regel[1])
            i += 1
        avg = uitkomst / i
        print(avg)
    except:
        print('Er heeft zich een foutmelding voorgedaan')

#functie zorgt ervoor dat elke regel gesplitst word en aan de array split word toegevoegd
def splitfile(bestand):
    try:
        i = 0
        split = []
        for regel in bestand:            
            split.append(regel.split())
            i += 1
        return split
    except:
        print('Er heeft zich een foutmelding voorgedaan')
