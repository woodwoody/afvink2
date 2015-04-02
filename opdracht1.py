#copyright shit bv
#auteurs Wouter Wajer en Remco de Boer
#copyright geschonden door: Julian Lerrick,Brecht van den Berg,Esther Kok

aspertaamG = float(input('Geef het aantal gram aspertaam? '))
aspertaamKM = float(input('Geef het aantal kubieke meter cola? '))

#mol aspertaam berekenen
mol = aspertaamG / 294.30
print('Het aantal mol aspartaam bedraagd: ' + str(mol))

#hoeveelheid aspertaam in mg

#aantal mg
aspertaamMG = aspertaamG / 1000

aspertaamMGL = aspertaamMG / aspertaamKM
aspertaamFles = aspertaamMGL * 1.5

print('In een fles van anderhalve lite zit: ' + str(aspertaamFles) + ' MG aspertaam')

#maximaal aantal flessen cola

adi = 40 * 70;
maxfles = adi / aspertaamFles

print('Een klant mag maximaal: ' + str(maxfles) + ' van deze flessen cola drinken')
