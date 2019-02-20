import string

def numberOfLannister(myFile):
    num = 0
    for str in myFile:
        tmp = str.split(' ')
        for word in tmp:
            if 'Lannister' in word:
                num+=1
    return num

def inverseLetter(str):
    resStr = ''
    for ch in str:
        if 'A' <= ch <= 'Z':
            resStr += ch.lower()
        elif 'a' <= ch <= 'z':
            resStr += ch.upper()
        else:
            resStr += ch
    return resStr

def longestWord(inputName, outputName):
    try:
        maxLength = 0
        words = []
        infile = open(inputName,"r")
        outfile = open(outputName,"w")

        for str in infile:
            newStr = ''
            for ch in str:
                if ch not in string.punctuation:
                    newStr += ch
                newStr.split()
            listOfWords = newStr.split()
            for word in listOfWords:
                if len(word) > maxLength:
                    words = []
                    words.append(word)
                    maxLength = len(word)
                elif len(word) == maxLength:
                    words.append(word)

        print('The length of longest words is',maxLength,'\nThe list of them:',file=outfile)
        for str in words:
            print(str, file=outfile)

        infile.close()
        outfile.close()
    except FileNotFoundError:
        print('The given file is not findable.')

#MAIN------------------------------------------------
# # EX1:
# while True:
#     try:
#         a = int(input('Give me a number: '))
#         print(a)
#         break
#     except ValueError:
#         print('That was not a valid number.')

# # EX2:
# try:
#     myFile = open("C:\\Users\\otthoni\\Desktop\\input.txt","r")
#     for str in myFile:
#         print(str)
#     myFile.close()
# except FileNotFoundError:
#     print('The given file is not findable.')


# # EX3:
try:
    myFile = open("input.txt","r")
    print('"Lannister" occurs', numberOfLannister(myFile), 'times in the text.')
    myFile.close()
except FileNotFoundError:
    print('The given file is not findable.')

# # EX4:
# try:
#     infile = open("..\\input.txt","r")
#     outfile = open("..\\output.txt","w")
#     for str in infile:
#         print(inverseLetter(str),file=outfile)
#     infile.close()
#     outfile.close()
# except FileNotFoundError:
#     print('The given file is not findable.')


# EX5:
# longestWord('..\\input.txt','..\\longestWords.txt')