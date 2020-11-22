#Author: Ricardo Sampaio
#Author: Cláudio Silva
#Date: 22/11/2020
#Resumo: Lexer processor that reads TAP documents and makes reports via terminal and html dcocuments


import ply.lex as lex
import sys
import os

from html import Html
from utils import Utils

tokens = ("NUMBEROFTESTS", "SUCESSFULLTESTS", "NOTSUCESSFULLTESTS", "SUBTEST", "COMMENTS")

#Declaring necessary vars
numberOfSucessfullTests = 0
numberOfNotSucessfullTests = 0
nTests = 0
subTestsEntering = 0
counterSub = 0
numberOfSucessfullSubTests = 0
numberOfSubtestsNotSucessFull = 0
numberOfSubTests = 0


#And lists
listOfSucessfullTests = []
comments = {}


def t_NUMBEROFTESTS(t):
    r"[1][.][.][0-9]+"
    global subTestsEntering, nTests, counterSub

    if subTestsEntering == 0:
        nTests = int(t.value[3:])
    else:
        subTestsEntering -= 1
        counterSub += int(t.value[3:])

    return t


def t_SUCESSFULLTESTS(t):
    r"ok[ ][0-9]+([ ][-][ ].+)?"

    global numberOfSucessfullTests, numberOfSucessfullSubTests, listOfSucessfullTests, counterSub, numberOfSubTests, currentTest

    listOfSucessfullTests.append(t)
    currentTest = t
    if subTestsEntering == 0 & counterSub == 0:
        numberOfSucessfullTests += 1

    else:
        numberOfSucessfullSubTests += 1
        numberOfSubTests += 1
        counterSub -= 1

    return t


def t_NOTSUCESSFULLTESTS(t):
    r"not[ ]ok[ ][0-9]+([ ][-][ ].+)?"

    global currentTest, numberOfNotSucessfullTests, numberOfSubtestsNotSucessFull, counterSub, listOfSucessfullTests, numberOfSubTests
    
    listOfSucessfullTests.append(t)

    currentTest = t

    if subTestsEntering == 0 & counterSub == 0:
        numberOfNotSucessfullTests += 1

    else:
        numberOfSubtestsNotSucessFull += 1
        numberOfSubTests += 1
        counterSub -= 1

    return t


def t_SUBTEST(t):
    r"[#][ ]Subtest[:].+"

    global subTestsEntering, currentTest
    currentTest = t
    subTestsEntering += 1

    return t


def t_COMMENTS(t):
    r"[#].+"
    comments[t.value] = currentTest
    return t


t_ignore = " \n"


def t_error(t):
    print("Wrong Syntax, skipping...")
    t.lexer.skip(1)


lexer = lex.lex()

#Get the file/Folder from terminal/console
file = sys.argv[1]  

_isFile = False

# If it gets a file as an argument
try:
    f = open("Testes/" + file, "r")
    _isFile = True
except:
    pass

# If it gets a folder as an argument 
if _isFile == False:
    htmlMain = Html.CreateHtmlMain(None)
    i = 0
    amount_of_files = 0

    #Counts the amount of files in the directory
    for file in os.listdir(sys.argv[1]): amount_of_files += 1 

    #Goes throught the files inside the directory
    for file in os.listdir(sys.argv[1]):
        i += 1
        t = open(sys.argv[1] + "/" + file, "r")
        
        lexer.input(t.read())
        
        #Goes through every token
        for token in iter(lexer.token, None):
            pass
        
        #Checks if it's the first file in process
        #If it is then the html of the documents
        #Won't have a previous file button
        if i == 1:
            previous_link = "noPrevious"
            next_link = Utils.NextFileInDirectory(None, sys.argv[1], file)
        
        #If it is the last file
        #The next button won't do anything
        elif i == amount_of_files:
            previous_link = Utils.PreviousFileInDirectory(None, sys.argv[1], file)
            mext_link = "noNext"

        #If it's between, then they'll work just fine
        else: 
            previous_link = Utils.PreviousFileInDirectory(None, sys.argv[1], file)
            next_link = Utils.NextFileInDirectory(None, sys.argv[1], file)

        #Builds the html document in a string
        htmlString = Html.CreateHtmlString(None, file[:-2], listOfSucessfullTests, previous_link, next_link, comments, numberOfSucessfullSubTests+numberOfSucessfullTests, nTests + numberOfSubTests)
        
        #Converts the html in the string to a .html document
        Html.HtmlStringToHtml(None, htmlString, file[:-2])
        
        #Adds an hyperlink to the document created in the previous line in the main .html file
        htmlMain = Html.AddHtmlLineHyperLink(None, htmlMain, file[:-2], file[:-2])
        
        t.close()

        #Print report to the terminal/console
        Utils.PrintReport(None, nTests, numberOfSucessfullTests, numberOfSubTests, numberOfSucessfullSubTests)

        #Resets all the vars being used in this loop
        listOfSucessfullTests.clear()
        comments.clear()
        nTests = 0
        numberOfSucessfullTests = 0
        numberOfSucessfullSubTests = 0
        numberOfSubTests = 0

    #Closes the body of the main .html file
    htmlMain = Html.CloseHtmlMain(None, htmlMain)
    #Converts the main string to a .html
    Html.HtmlStringToHtml(None, htmlMain, "Main")

#If the input is a file
else:
    lexer.input(f.read())
    
    #Goes through the tokens
    for token in iter(lexer.token, None): 
        pass
    
    #Builds the html document in a string
    htmlString = Html.CreateHtmlString(None, file[:-2], listOfSucessfullTests, "noPrevious", "noNext", comments, numberOfSucessfullSubTests+numberOfSucessfullTests, nTests + numberOfSubTests)
    
    #Converts the string to a .html
    Html.HtmlStringToHtml(None, htmlString, file[:-2])
    f.close()

    #Print report
    Utils.PrintReport(None, nTests, numberOfSucessfullTests, numberOfSubTests, numberOfSucessfullSubTests)

    #Resets the vars
    listOfSucessfullTests.clear()
    comments.clear()
    nTests = 0
    numberOfSucessfullTests = 0
    numberOfSucessfullSubTests = 0
    numberOfSubTests = 0