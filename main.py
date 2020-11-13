import ply.lex as lex

tokens = ("NUMBEROFTESTS", "SUCESSFULLTESTS")

t_NUMBEROFTESTS = r"[1][.][.][0-9]+"

t_SUCESSFULLTESTS = r"[o][k][ ][0-9]+"


t_ignore = "\n"

lexer = lex.lex()

f = open("testes/teste1.txt", "r")

# print(f.read())


lexer.input(f.read())


# print(FTests)
numberOfSucessfullTests = 0
while True:
    tok = lexer.token()
    if not tok:
        break
    else:
        if tok.value[0] == "1":
            i = 0
            NTests = ""
            while i < len(tok.value):
                if i > 2:
                    NTests += tok.value[i]
                i += 1
            FTests = int(NTests)
            print("Number of tests: ", FTests)
        elif tok.value[0] == "o":
            numberOfSucessfullTests += 1
print("Sucessfull tests: ", numberOfSucessfullTests)


