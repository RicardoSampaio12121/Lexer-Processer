#Autho: Ricardo Sampaio
#Author: Cláudio Silva
#Date: 22/11/2020

import os

#Some methods that helps us through the code
class Utils:

    #Gets the status from a token("ok" or "not ok")
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

    #Gets the number from a token
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

    #Gets which is the next file in the given directory and the current file
    def NextFileInDirectory(self, directory, current_file):
        
        current_passed = False

        for file in os.listdir(directory):
            
            if current_passed:
                return file
        
            if file == current_file:
                current_passed = True

        return "nada"

    #Gets which is the previous file in the given directory and the current file
    def PreviousFileInDirectory(self, directory, current_file):

        for file in os.listdir(directory):

            if file == current_file:
                return previous_file

            previous_file = file

    #Prints a simple report to the terminal
    def PrintReport(self, main_tests, number_of_successful_tests, number_of_subtests, number_of_successful_subtests):
        print("Number of main tests: ", main_tests)
        print("Number of successful main tests: ", number_of_successful_tests)
        print("Percentage of unsuccessful main tests: " + str(((main_tests - number_of_successful_tests) / main_tests) * 100) + "%")
        
        if number_of_subtests != 0: 
            print("Number of subtests: ", number_of_subtests)
            print("Number of successful subtests: ", number_of_successful_subtests)
            print("Percentage of unccessful subtests: " + str(((number_of_subtests - number_of_successful_subtests) / number_of_subtests) * 100) + "%")
        print("---------------------------------------------------------------------------------------")
