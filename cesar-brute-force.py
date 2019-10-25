
texte = input('Votre Phrase : ')
alphabet = "abcdefghijklmnopqrstuvwxyz"

for a in range(1,26):
    phrase_a_decrypter = ' '
    for b in texte:
        if alphabet.find(b) != -1:
            phrase_a_decrypter += alphabet[(alphabet.find(b) + a) % 26]
        else:
            phrase_a_decrypter += b
    print(phrase_a_decrypter)