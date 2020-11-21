import ply.lex as lex

from html import Html
from utils import Utils

tokens = ("NUMBEROFTESTS", "SUCESSFULLTESTS", "NOTSUCESSFULLTESTS", "SUBTEST", "COMMENTS")

numberOfSucessfullTests = 0
numberOfNotSucessfullTests = 0
nTests = 0
subTestsEntering = 0
numberOfSubtests = 0
numberOfSucessfullSubTests = 0
numberOfSubtestsNotSucessFull = 0

listOfSucessfullTests = []


def t_NUMBEROFTESTS(t):
    r"[1][.][.][0-9]+"
    global subTestsEntering, numberOfSubtests, nTests

    if subTestsEntering == 0:
        nTests = int(t.value[3:])
    else:
        numberOfSubtests += int(t.value[3:])
        subTestsEntering -= 1

    return t


def t_SUCESSFULLTESTS(t):
    r"ok[ ][0-9]+([ ][-#][ ].+)?"

    global numberOfSucessfullTests, numberOfSucessfullSubTests, listOfSucessfullTests

    listOfSucessfullTests.append(t)

    if subTestsEntering == 0:
        numberOfSucessfullTests += 1
    else:
        numberOfSucessfullSubTests += 1

    return t


def t_NOTSUCESSFULLTESTS(t):
    r"not[ ]ok[ ][0-9]+([ ][-#][ ].+)?"

    global numberOfNotSucessfullTests, numberOfSubtestsNotSucessFull

    if subTestsEntering == 0:
        numberOfNotSucessfullTests += 1
    else:
        numberOfSubtestsNotSucessFull += 1

    return t


def t_SUBTEST(t):
    r"[#][ ]Subtest[:].+"

    global subTestsEntering
    subTestsEntering += 1

    return t


def t_COMMENTS(t):
    r"[#].+"
    print("Comentario encontrado!")

    return t


# não lê os tabs do ficheiro

t_ignore = " \n"


def t_error(t):
    print("Wrong Syntax, skipping...")
    t.lexer.skip(1)


lexer = lex.lex()
file = "Testes/teste3.txt"
f = open(file, "r")

lexer.input(f.read())


for token in iter(lexer.token, None):
    pass

print("Number of tests:", nTests)
print("Sucessfull tests:", numberOfSucessfullTests)
print("Percentage of not sucessfull test:", (numberOfNotSucessfullTests / nTests) * 100, "%")
print("Number Subtests: ", numberOfSubtests)
print("Sucessfull Subtests: ", numberOfSucessfullSubTests)
if numberOfSubtests > 0:
    print("Percentage of not sucessfull subtests:", numberOfSubtestsNotSucessFull / numberOfSubtests * 100, "%")
else:
    print("Percentage of not sucessfull subtests: 0%")

print("-----------------------------------------------------------------------------------------")
for token in listOfSucessfullTests:
    print(token.value)
print("-----------------------------------------------------------------------------------------")

inteiro = Utils.GetNumberOfFile(None, file)

teste3 = Html.CreateHtmlString(None, inteiro, listOfSucessfullTests)
print(inteiro)
Html.HtmlStringToHtml(None, teste3)
