import os
from utils import Utils

class Html(object):

    def CreateHtmlMain(self):
        main_string = ""
        main_string += "<body style=\"background-color:#b0e0e6\">\n"
        main_string += "<h1>INDEX</h1>\n"
        return main_string

    
    def AddHtmlLineHyperLink(self, main_string, path, file):
        main_string += "\t<a href= " + path + ".html" +">" + file +"</a><br>"
        
        return main_string


    def CloseHtmlMain(self, main_string):
        main_string += "</body>\n"
        return main_string

    def CreateHtmlString(self, file_number, successful_tests_list):
        html_string = "None"
        html_string = "<head>\n"
        html_string += "<style> table, th, td{border: 1px solid black;}</style>\n"
        html_string += "</head>\n"

        html_string += "<body style=\"background-color:#b0e0e6\">\n"
        html_string += "\t<h1> Relatório " + str(file_number) + "!</h1>\n"
        html_string += """\t<table style="width:100%">\n"""
        html_string += "\t\t<tr style=\"background-color:#ffa500\">\n"
        html_string += "\t\t\t<th style=\"text-align:left\">Teste</th>\n"
        html_string += "\t\t\t<th style=\"text-align:left\">Status</th>\n"
        html_string += "\t\t</tr>\n"
        
        

        for test in successful_tests_list:
            status = Utils.GetStatusFromToken(None, test)
            number = Utils.GetNumberFromToken(None, test)
            
            #print(status)

            if status == "ok":
                html_string += "\t\t<tr style=\"background-color:#32CD32\">\n"
            else:
                html_string += "\t\t<tr style=\"background-color:#FF0000\">\n"
                
            
            html_string += "\t\t\t<th style=\"text-align:left\">" + number + "</th>\n"
            html_string += "\t\t\t<th style=\"text-align:left\">" + status + \
                            "</th>\n"

            html_string += "\t\t</tr>\n"

        html_string += """\t</table>\n"""

        html_string += "</body>"

        return html_string

    def HtmlStringToHtml(self, html_string, doc_name):
        if not os.path.exists("HTML_Documents"):
            os.mkdir("HTML_Documents")

        f = open("HTML_Documents/" + doc_name + ".html", "w")
        f.write(html_string)

        pass
