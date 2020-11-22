import os
from utils import Utils

class Html(object):

    #Creates the first part of the Main.html file
    def CreateHtmlMain(self):
        main_string =  ""
        main_string += "<body style=\"background-color:#b0e0e6\">\n"
        main_string += "<h1>INDEX</h1>\n"
        return main_string

    #Adds the hyperlink to the other documents
    def AddHtmlLineHyperLink(self, main_string, path, file):
        main_string += "\t<a href= " + path + ".html" +">" + file +"</a><br>"
        
        return main_string

    #Finnished the Main.html file
    def CloseHtmlMain(self, main_string):
        main_string += "</body>\n"
        return main_string

    #Creates the html documents
    def CreateHtmlString(self, file_name, successful_tests_list, previous, next, comments, success, total_tests):
        successTests = ((success / total_tests) * 100) * 3.6

        #Header of the file
        html_string = "<head>\n"
        html_string += "<style> table, th, td{border: 1px solid black;}\n"
        html_string += """.piechart{margin-top: 20px; display: block; position: absolute; width: 400px; 
                        height: 400px; border-radius: 50%; background-image: conic-gradient( lightgreen """ + str(successTests) + """deg,  red 0deg); }\n"""
        html_string += "body, .piechart { display: outside; justify-content: center; align-items: center; }\n"
        html_string += "</style>\n"
        html_string += "</head>\n"

        #Checks if it has to add a previous and or a next button
        if previous != "noPrevious":
            html_string += "<a href= " + previous[:-4] + ".html" +">" + "---Previous" +"</a><br>"
        if next != "noNext":
            html_string += "<a href= " + next[:-4] + ".html" +">" + "Next>>>" +"</a><br>"

        #Changes the background color to light blue 
        html_string += "<body style=\"background-color:#b0e0e6\">\n"
        
        #Title
        html_string += "\t<h1> Relatório " + file_name + "!</h1>\n"
        
        #Creates a table and add two columns, Teste and Status
        html_string += """\t<table style="width:100%">\n"""
        html_string += "\t\t<tr style=\"background-color:#ffa500\">\n"
        html_string += "\t\t\t<th style=\"text-align:left\">Teste</th>\n"
        html_string += "\t\t\t<th style=\"text-align:left\">Status</th>\n"
        html_string += "\t\t</tr>\n"
        
        #Goes through a list of successful tests to add the value to the trable
        for test in successful_tests_list:
            
            #Gets the status and the number of the test from the token
            status = Utils.GetStatusFromToken(None, test)
            number = Utils.GetNumberFromToken(None, test)
            
            #If status is ok then changes the color of the row to green
            if status == "ok":
                html_string += "\t\t<tr style=\"background-color:#32CD32\">\n"
            #Else to red
            else:
                html_string += "\t\t<tr style=\"background-color:#FF0000\">\n"
                
            #Fills the row spaces with the number and status
            html_string += "\t\t\t<th style=\"text-align:left\">" + number + "</th>\n"
            html_string += "\t\t\t<th style=\"text-align:left\">" + status + \
                            "</th>\n"
            #Closes the row
            html_string += "\t\t</tr>\n"

        #Closes table
        html_string += """\t</table>\n"""

        #If the list of comments is not empty enters here
        if comments:
            
            #Creates a table and a title row
            html_string += """\t<table style="width:100%">\n"""    
            html_string += "\t\t<br><tr style=\"background-color:#ffa500\">\n"
            html_string += "\t\t\t<th style=\"text-align:left;background-color:\">Comentários</th>\n"
            html_string += "\t\t</tr>\n"

            #Goes through the list of comments and fills the table with them
            for comment in comments:
                html_string += "\t\t<tr style=\"background-color:#32CD32\">\n"
                html_string += "\n\t\t\t<th style=\"text-align:left\">" + comment.value + "</th>"                 
                html_string += "</tr>"
            
            #Closes the table
            html_string += """\t</table>\n"""

        #Displays the pie chart with the percentage of success marked as green
        #And unsuccess as red
        html_string += "<h1>Pie-Chart Success</h1>"
        html_string += """<div class="piechart"></div>"""

        #Closes the body of the document
        html_string += "</body>"

        return html_string

    #Converts the html documents streing to actual .html documents
    def HtmlStringToHtml(self, html_string, doc_name):
        if not os.path.exists("HTML_Documents"):
            os.mkdir("HTML_Documents")

        f = open("HTML_Documents/" + doc_name + ".html", "w")
        f.write(html_string)

        pass
