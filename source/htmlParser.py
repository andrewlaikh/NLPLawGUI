# Utility parser to 1. create string for prediction for NER 2. process prediction into HTML for streamlit
import string

from bs4 import BeautifulSoup


def findText(fileName):
    soup = open(fileName, "r", encoding="UTF-8")
    soup = BeautifulSoup(soup, from_encoding="UTF-8")
    if not soup.find('div', attrs={'class': 'texte'}):
        return
    else:
        text = soup.find('div', attrs={'class': 'texte'})
        return str(text)


def saveParaMarks(text):
    paraList = []
    for line in text.splitlines():
        paraStartPrefix = (r'<p>', r'</p>')
        if line.startswith(paraStartPrefix):
            if line.startswith(r'<p>'):
                paraList.append([r'<p>', r'</p>'])
            else:
                paraList.append([r'</p>'])
    return paraList


def preprocessText(text):
    outputList = []
    text = text.replace(r'<p>', '')
    text = text.replace(r'</p>', '')
    puncList = string.punctuation.replace("/", '').replace("(", "").replace(")", "").replace(",", "")
    text.translate(str.maketrans('', '', puncList))
    for line in text.splitlines():
        if line.startswith('<div class') or line.startswith('</div>'):
            continue
        output = []
        line = line.strip()
        line = line.replace(' +', ' ')
        wordsInLine = line.split(' ')
        for word in wordsInLine:
            if not word.isspace() and not word == '':
                output.append(word)
        outputList.append(output)
    return outputList


def createString(textList):
    outputString = ''
    for individualList in textList:
        for item in individualList:
            outputString += item + ' '
    return outputString


def markString(prediction, textList):
    blueStartSpan = r"<span class='highlight blue'>"
    greenStartSpan = r"<span class='highlight green'>"
    redStartSpan = r"<span class='highlight red'>"
    endSpan = r"</span>"
#     next step is to match prediction to output and use it as is


rawText = findText('raw1text.html')
paraList = saveParaMarks(rawText)
assert len(paraList) == 170
outputList = preprocessText(rawText)
outputString = createString(outputList)
# print(outputList)
print(outputString)
# print(paraList)
outputString = outputString.replace(' +', ' ')
print(len(outputString.split(' ')))
# markString(prediction,textList)
# proposed: algo find chars and see if match if not
# continue down next char to find match
# keep going but note that python is slow
