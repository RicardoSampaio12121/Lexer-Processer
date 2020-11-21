class Utils:

    def GetNumberOfFile(self, file_path):
        i = 0
        while file_path[i + 1] != '.':
            i += 1

        return int(file_path[i])


    def GetStatusFromToken(self, token):
        status = ""
        i = 0

        while i < len(token.value):
            status += token.value[i]
            if status == "ok":
                return status
            elif status == "not ok":
                return status
            i += 1


    def GetNumberFromToken(self, token):
        number = ""
        i = 0
        if token.value[0] == 'o':
            aux = token.value[3:]
        else:
            aux = token.value[8:]

        print(aux)
        print(len(aux))
        print(i)
        while aux != ' ':
            number += aux[i]
            i += 1
            if len(aux) == i:
                break

        print("sai do while")
        return number

