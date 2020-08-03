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


def markString(predictionList, textList):
    blueStartSpan = r"<span class='highlight blue'>"
    greenStartSpan = r"<span class='highlight green'>"
    redStartSpan = r"<span class='highlight red'>"
    endSpan = r"</span>"
    bigOutputList = []
    smallerList = predictionList[0]
    predictionListCounter = 0
    for textIndivList in textList:
        smallOutputList = []
        for textIndivItem in textIndivList:
            value = list(smallerList[predictionListCounter].values())[0]
            predictionListCounter += 1
            if value == "Context":
                textIndivItem = blueStartSpan + textIndivItem + endSpan
            elif value == "Legislation":
                textIndivItem = greenStartSpan + textIndivItem + endSpan
            elif value == "Provision":
                textIndivItem = redStartSpan + textIndivItem + endSpan
            smallOutputList.append(textIndivItem)
        bigOutputList.append(smallOutputList)
    return bigOutputList


def flattenHtmlAndProcessedText(modList, paraList):
    outputString = ''
    for indivModList, indivParaList in zip(modList, paraList):
        if len(indivParaList) > 1:
            outputString += r'<p>' + " ".join(indivModList) + r'</p>'
        else:
            outputStirng += paraList[0] + " ".join(indivModList)
        outputString += r'<p/>'
    return outputString


rawText = findText('raw1text.html')
paraList = saveParaMarks(rawText)
print(paraList)
# assert len(paraList) == 170
outputList = preprocessText(rawText)
print(outputList)
outputString = createString(outputList)
print(outputString)
# print(outputString)
# modList = markString(prediction, outputList)
# modOutput = flattenHtmlAndProcessedText(modList, paraList)
# htmlOutput = open("html2Text.html", "w", errors="ignore")
# htmlOutput.write(modOutput)
# htmlOutput.close()
