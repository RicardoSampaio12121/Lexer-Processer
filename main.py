import ply.lex as lex

tokens = ("NUMBEROFTESTS", "SUCESSFULLTESTS", "NOTSUCESSFULLTESTS", "SUBTEST", "COMMENTS")

t_NUMBEROFTESTS = r"[1][.][.][0-9]+"

t_SUCESSFULLTESTS = r"ok[ ][0-9]+([ ][-#][ ].+)?"

t_NOTSUCESSFULLTESTS = r"not[ ]ok[ ][0-9]+([ ][-#][ ].+)?"# estas ai?

t_SUBTEST = r"[#][ ]Subtest[:].+"

t_COMMENTS = r"[#].+"

# não lê os tabs do ficheiro

t_ignore = " \n"


def t_error(t): 
    print ("Wrong Syntax, skipping...")
    t.lexer.skip(1)
    

lexer = lex.lex()

f = open("testes/teste5.txt", "r")

# print(f.read())


lexer.input(f.read())


# print(FTests)
numberOfSucessfullTests = 0
numberOfNotSucessfullTests = 0
nTests = 0
subTestsEntering = 0
numberOfSubtests = 0
numberOfSucessfullSubTests = 0
numberOfSubtestsNotSucessFull = 0

while True:
    tok = lexer.token()
    if not tok:
        break
    else:
        if tok.type == "NUMBEROFTESTS":
            if subTestsEntering == 0:
                nTests = int(tok.value[3:])
            if subTestsEntering > 0:
                numberOfSubtests += int (tok.value[3:])
                subTestsEntering -= 1

        if tok.type == "SUCESSFULLTESTS":
            if subTestsEntering == 0:
                numberOfSucessfullTests += 1
            if subTestsEntering > 0:
                numberOfSucessfullSubTests += 1

        if tok.type == "NOTSUCESSFULLTESTS":
             if subTestsEntering == 0: 
                numberOfNotSucessfullTests += 1
             if subTestsEntering > 0:
                numberOfSubtestsNotSucessFull += 1

        if tok.type == "SUBTEST":
            subTestsEntering += 1

        if tok.type == "COMMENTS":
           print ("Comentario encontrado")

print("Number of tests:", nTests)
print("Sucessfull tests:", numberOfSucessfullTests)
print("Percentage of not sucessfull test:", (numberOfNotSucessfullTests / nTests) * 100, "%")
print("Number Subtests: ", numberOfSubtests)
print("Sucessfull Subtests: ", numberOfSucessfullSubTests)
if numberOfSubtests > 0:
    print("Percentage of not sucessfull subtests:", numberOfSubtestsNotSucessFull / numberOfSubtests * 100, "%")
else:
    print("Percentage of not sucessfull subtests: 0%") 

