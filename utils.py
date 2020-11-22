import os

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
            aux = token.value[6:]
        
        while aux != ' ':
           
            number += aux[i]
            i += 1
            if len(aux) == i:
                break

        return number


    def NextFileInDirectory(self, directory, current_file):
        
        current_passed = False

        for file in os.listdir(directory):
            
            if current_passed:
                return file
        
            if file == current_file:
                current_passed = True

        return "nada"

    def PreviousFileInDirectory(self, directory, current_file):

        for file in os.listdir(directory):

            if file == current_file:
                return previous_file

            previous_file = file

    def PrintReport(self, main_tests, number_of_successful_tests, number_of_subtests, number_of_successful_subtests):
        print("Number of main tests: ", main_tests)
        print("Number of successful main tests: ", number_of_successful_tests)
        print("Percentage of unsuccessful main tests: " + str(((main_tests - number_of_successful_tests) / main_tests) * 100) + "%")
        
        if number_of_subtests != 0: 
            print("Number of subtests: ", number_of_subtests)
            print("Number of successful subtests: ", number_of_successful_subtests)
            print("Percentage of unccessful subtests: " + str(((number_of_subtests - number_of_successful_subtests) / number_of_subtests) * 100) + "%")
        print("---------------------------------------------------------------------------------------")
