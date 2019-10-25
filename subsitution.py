import collections
import string
import random


mostUsedLetterNumbers = 9
mostUsedLetters = ['e','t','a','o','i','n','s','h','r','d','l','c','u','m','w','f','g','y','p','b','v','k','j','x','q','z']


#plain Text ---------------------------------------------------------------------------
#Lies den Text  
text = "until modern times cryptography referred almost exclusively to encryption which is the process of converting ordinary information into unintelligible text"
print("Cleartext:")
text = text.lower()
print(text)

#crypt with random.shuffle ---------------------------------------------------------------------------

abc = list(string.ascii_lowercase) #abcdef....+ lower letter

key = abc[:]  
random.shuffle(key);
#print (key) #this is my key I want to get in the end

e= dict(zip(abc,key))  
#print e

#print text
ct = ""

for c in text:
    #print(e[c])
    if c == ' ':
        ct = ct + " "
    else:
        ct = ct + e[c]

print("\nChippertext:\n",ct)

#Count File ---------------------------------------------------------------------------

letters = collections.Counter(text)

#print letters
print ("\nFound letters:")
for key,count in letters.iteritems():
    if key == '\n':
        print ("newlines",count)
    elif key == ' ':
        print ("spaces",count)
    else:
        print (key, count)

#del spaces and newlines
del letters['\n']
del letters[' ']
#----------------------------------------------------------------
#get letter count
topLetters = letters.most_common(mostUsedLetterNumbers)
#print topLetters

#replace letters
i=0
replacedText= ct
for i in range(0,mostUsedLetterNumbers):
    replacedText = string.replace(replacedText,topLetters[i][0],mostUsedLetters[i])

print ("\nDecrypted:\n",replacedText)

print ("\nOriginal text:\n",text)