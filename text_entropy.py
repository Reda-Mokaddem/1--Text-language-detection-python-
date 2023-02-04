from function import Entropy

# degree of Entropy
degree = 5

# Open the random text file
with open('random.txt', "r",encoding='utf-8') as file:
    # Read the contents of the file
    text = file.read()
    print("random text------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    print(text)
    cardinal = len(text)

# Open the french text file
with open('french.txt', "r",encoding='utf-8') as file, open('french1.txt', "w",encoding='utf-8') as file1:
    print("texte francais----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    new_contents1 = file.read(cardinal)
    file1.write(new_contents1)
    print(new_contents1)

# Open the english text file
with open('english.txt', "r",encoding='utf-8') as file, open('english1.txt', "w",encoding='utf-8') as file1:
    print("english text----------------------------------------------------------------------------------------------------------------------------------------------------------------------")
    new_contents1 = file.read(cardinal)
    file1.write(new_contents1)
    print(new_contents1)

A=Entropy('random.txt',degree)
B=Entropy('french1.txt',degree)
C=Entropy('english1.txt',degree)

# Printing entropies
print("\nThe entropy of the text you provided is :",A)
print("\nThe average entropy of the french sample is :",B)
print("\nThe average entropy of the english sample is :",C)
print("\n")

# comparing text entropy to average entropies
if (abs(A-B)>abs(A-C)) :
    print("The text you provided appears to be written in English")
else :
    print("The text you provided appears to be written in French")
 