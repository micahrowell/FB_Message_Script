import os
import sys

numFiles = int(sys.argv[1])
i = 0
k = 1
uniqueFilenames = []

while i <= numFiles:
    fileName = str(i) + '.html'
    file = open(fileName,'r')
    fileContents = []
    newFilename = ''
    for line in file:
        fileContents.append(line)
        if line[15:32] == 'Conversation with':
            j = 33
            while line[j] != '<':
                j += 1
            newFilename = line[33:j]
    newFilename = newFilename.replace('&#039;',"'")
    newFilename = newFilename.replace('/','')
    if newFilename in uniqueFilenames:
        newFilename += str(k)
        k += 1
    else:
        uniqueFilenames.append(newFilename)
    newFilename += '.html'
    newFile = open(newFilename, 'w')
    newFile.writelines(fileContents)
    file.close()
    os.remove(fileName)
    i += 1
