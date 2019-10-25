texte = input('Votre Phrase : ')
alphabet = "abcdefghijklmnopqrstuvwxyz"

décalage = 13

chiffrage = ''

for c in texte:
    if c in alphabet:
            chiffrage += alphabet[(alphabet.index(c)+décalage)%(len(alphabet))]

print('Votre message chiffré : ' + chiffrage)  