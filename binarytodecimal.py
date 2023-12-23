#BINARY TO DECIMAL

# bstring=input("Enter a string of bits: ")
# decimal=0
# exponent=len(bstring)-1
# for digit in bstring:
#     decimal=decimal+int(digit)*2**exponent
#     exponent=exponent-1
# print("The integer value is", decimal)

# #DECIMAL TO BINARY
# decimal=int(input("Enter a decimal integer: "))
# if decimal ==0:
#     print(0)
# else:
#     print("Quotient Remainder Binary")
#     bstring=""
#     while decimal>0:
#         remainder=decimal%2
#         decimal=decimal//2
#         bstring=str(remainder)+bstring
#         print("%5d%8d%12s"%(decimal,remainder,bstring))
#     print("The binary representation is", bstring)



# sentence=input("Enter a sentence: ")
# #Enter a sentence:  This sentence has no long words.
# listofwords=sentence.split()
# print("There are", len(listofwords), "words.")

# sum=0
# for word in listofwords:
#     sum+=len(word)
# print("The average word lenght is", sum/len(listofwords))

# f=open("myfile.txt",'w')
# f.write("First line.\nSecond line.\n")
# f.close()

# import random
# f=open("Integer.txt", 'w')
# for count in range(500):
#     number=random.randint(1,500)
#     f.write(str(number)+"\n")
# f.close()

# f=open("myfile.txt", 'r')
# text=f.read()
# print(text)

# f=open("integer.txt", 'r')
# sum=0
# for line in f:
#     line=line.strip()
#     number=int(line)
#     sum+=number
# print("The sum is", sum)

# f=open("integer.txt", 'r')
# sum=0
# for line in f:
#     wordlist=line.split()
#     for word in wordlist:
#         number=int(word)
#         sum+=number
# print("The sum is", sum)

# import os
# currentDirectoryPath=os.getcwd()
# listofFileNames=os.listdir(currentDirectoryPath)
# # for name in listofFileNames:
# #     if ".txt" in name:
# #         print(name)

# '''
# Program: textanalysis.py
# Author: Ken
# Computes and displays the Flesch Index and the Grade 
# Level Equivalent for the readibility of a text file.
# '''
# #Text the inputs
# fileName=input("Enter the file name: ")
# inputFile=open(fileName, 'r')
# text=inputFile.read()
# #Count the sentence
# sentences=text.count('.')+text.count('?')+\
#             text.count(':')+text.count(';')+\
#             text.count('!')
# #Count the words
# words=len(text.split())

# #count the syllables
# syllables=0
# for word in text.split():
#     for vowal in ['a','e','i','o','u']:
#         syllables+=word.count(vowal)
#     for ending in ['es','ed','e']:
#         if word.endswith(ending):
#             syllables-=1
#     if word.endswith('le'):
#         syllables+=1

# #Compute the Flesch Index and Grade Level
# index=206.835-1.015*(words/sentences)-\
# #         84.6*(syllables/words)
# # level=round(0.39*(words/sentences)+11.8*\
# #             (syllables/words)-15.59)
# #output the results
# print("The Flesch Index is", index)
# print("The Grade Level Equivalent is", level)
# print(sentences, "sentences")
# print(words, "words")
# print(syllables,"syllables")


data="No way!"
a=data.find("way!")
print(a)










