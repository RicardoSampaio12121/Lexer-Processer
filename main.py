import ply.lex as lex
import sys
import os

from html import Html
from utils import Utils

tokens = ("NUMBEROFTESTS", "SUCESSFULLTESTS", "NOTSUCESSFULLTESTS", "SUBTEST", "COMMENTS")

numberOfSucessfullTests = 0
numberOfNotSucessfullTests = 0
nTests = 0
subTestsEntering = 0
numberOfSubtests = 0
counterSub = 0
numberOfSucessfullSubTests = 0
numberOfSubtestsNotSucessFull = 0
numberOfTests = 0
numberOfSubTests2 = 0

listOfSucessfullTests = []
comments = []


def t_NUMBEROFTESTS(t):
    r"[1][.][.][0-9]+"
    global subTestsEntering, numberOfSubtests, nTests, counterSub

    if subTestsEntering == 0:
        nTests = int(t.value[3:])
    else:
        numberOfSubtests += int(t.value[3:])
        subTestsEntering -= 1
        counterSub += int(t.value[3:])

    return t


def t_SUCESSFULLTESTS(t):
    r"ok[ ][0-9]+([ ][-#][ ].+)?"

    global numberOfSucessfullTests, numberOfSucessfullSubTests, listOfSucessfullTests, counterSub, numberOfTests

    listOfSucessfullTests.append(t)

    if subTestsEntering == 0 & counterSub == 0:
        numberOfSucessfullTests += 1
        numberOfTests += 1

    else:
        numberOfSucessfullSubTests += 1
        counterSub -= 1

    return t


def t_NOTSUCESSFULLTESTS(t):
    r"not[ ]ok[ ][0-9]+([ ][-#][ ].+)?"

    global numberOfNotSucessfullTests, numberOfSubtestsNotSucessFull, counterSub, listOfSucessfullTests, numberOfTests
    listOfSucessfullTests.append(t)

    if subTestsEntering == 0 & counterSub == 0:
        numberOfNotSucessfullTests += 1
        numberOfTests += 1

    else:
        numberOfSubtestsNotSucessFull += 1
        counterSub -= 1

    return t


def t_SUBTEST(t):
    r"[#][ ]Subtest[:].+"

    global subTestsEntering, numberOfSubTests2
    subTestsEntering += 1
    numberOfSubTests2 += 1

    return t


def t_COMMENTS(t):
    r"[#].+"
    comments.append(t)
    return t


t_ignore = " \n"


def t_error(t):
    print("Wrong Syntax, skipping...")
    t.lexer.skip(1)


lexer = lex.lex()
file = sys.argv[1]  
f = ""
_isFile = False
# If it gets a file as an argument
try:
    f = open("Testes/" + file, "r")
    _isFile = True
except:
    pass

# If it gets a folder as an argument 
teste3 = ""
if _isFile == False:
    teste4 = Html.CreateHtmlMain(None)
    i = 0
    previous_link = ""
    next_link = ""
    amount_fo_files = 0
    for file in os.listdir(sys.argv[1]): amount_fo_files += 1 

    for file in os.listdir(sys.argv[1]):
        i += 1
        t = open(sys.argv[1] + "/" + file, "r")
        
        lexer.input(t.read())
        
        
        for token in iter(lexer.token, None):
            pass

        testNumber = Utils.GetNumberOfFile(None, file)

        if i == 1:
            previous_link = "noPrevious"
            next_link = Utils.NextFileInDirectory(None, sys.argv[1], file)
        
        elif i == amount_fo_files:
            previous_link = Utils.PreviousFileInDirectory(None, sys.argv[1], file)
            mext_link = "noNext"

        else: 
            previous_link = Utils.PreviousFileInDirectory(None, sys.argv[1], file)
            next_link = Utils.NextFileInDirectory(None, sys.argv[1], file)


        teste3 = Html.CreateHtmlString(None, testNumber, listOfSucessfullTests, i, previous_link, next_link, comments, numberOfSucessfullSubTests+numberOfSucessfullTests, numberOfTests + numberOfSubTests2)
        
        
        Html.HtmlStringToHtml(None, teste3, file[:-4])
        
        teste4 = Html.AddHtmlLineHyperLink(None, teste4, file[:-4], file[:-4])
        t.close()

        #Print report to the terminal/console
        Utils.PrintReport(None, nTests, numberOfSucessfullTests, numberOfSubTests2, numberOfSucessfullSubTests)


        listOfSucessfullTests.clear()
        comments.clear()
        nTests = 0
        numberOfSucessfullTests = 0
        numberOfSucessfullSubTests = 0
        numberOfTests = 0
        numberOfSubTests2 = 0


        #Relatorio terminal





    teste4 = Html.CloseHtmlMain(None, teste4)
    Html.HtmlStringToHtml(None, teste4, "Main")

else:
    lexer.input(f.read())
    for token in iter(lexer.token, None): 
        pass

    testNumber = Utils.GetNumberOfFile(None, file)
    teste3 = None
    teste3 = Html.CreateHtmlString(None, testNumber, listOfSucessfullTests)
    
    Html.HtmlStringToHtml(None, teste3, file[:-4])
    f.close()

#print("Number of main tests:", nTests)
#print("Sucessfull tests:", numberOfSucessfullTests)
#print("Percentage of not sucessfull test:", (numberOfNotSucessfullTests / nTests) * 100, "%")
#print("Number Subtests: ", numberOfSubtests)
#print("Sucessfull Subtests: ", numberOfSucessfullSubTests)
#if numberOfSubtests > 0:
#    print("Percentage of not sucessfull subtests:", numberOfSubtestsNotSucessFull / numberOfSubtests * 100, "%")
#else:
#    print("Percentage of not sucessfull subtests: 0%")