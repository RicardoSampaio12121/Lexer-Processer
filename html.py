import os
from utils import Utils

class Html(object):

    def CreateHtmlMain(self):
        main_string =  ""
        main_string += "<body style=\"background-color:#b0e0e6\">\n"
        main_string += "<h1>INDEX</h1>\n"
        return main_string

    
    def AddHtmlLineHyperLink(self, main_string, path, file):
        main_string += "\t<a href= " + path + ".html" +">" + file +"</a><br>"
        
        return main_string


    def CloseHtmlMain(self, main_string):
        main_string += "</body>\n"
        return main_string

    def CreateHtmlString(self, file_number, successful_tests_list, line_number, previous, next, comments, success, total_tests):
        successTests = ((success / total_tests) * 100) * 3.6


        html_string = "None"
        html_string = "<head>\n"
        html_string += "<style> table, th, td{border: 1px solid black;}\n"
        html_string += """.piechart{margin-top: 20px; display: block; position: absolute; width: 400px; 
                        height: 400px; border-radius: 50%; background-image: conic-gradient( lightgreen """ + str(successTests) + """deg,  red 0deg); }\n"""
        html_string += "body, .piechart { display: outside; justify-content: center; align-items: center; }\n"
        
        html_string += "</style>\n"
        html_string += "</head>\n"

        if previous != "noPrevious":
            html_string += "<a href= " + previous[:-4] + ".html" +">" + "---Previous" +"</a><br>"
        if next != "noNext":
            html_string += "<a href= " + next[:-4] + ".html" +">" + "Next>>>" +"</a><br>"
            
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
            

            if status == "ok":
                html_string += "\t\t<tr style=\"background-color:#32CD32\">\n"
            else:
                html_string += "\t\t<tr style=\"background-color:#FF0000\">\n"
                
            
            html_string += "\t\t\t<th style=\"text-align:left\">" + number + "</th>\n"
            html_string += "\t\t\t<th style=\"text-align:left\">" + status + \
                            "</th>\n"

            html_string += "\t\t</tr>\n"

        html_string += """\t</table>\n"""

        
        html_string += """\t<table style="width:100%">\n"""


        if comments:

            html_string += "\t\t<br><tr style=\"background-color:#ffa500\">\n"
            html_string += "\t\t\t<th style=\"text-align:left;background-color:\">Comentários</th>\n"
            html_string += "\t\t</tr>\n"

            

            for comment in comments:
                html_string += "\t\t<tr style=\"background-color:#32CD32\">\n"
                html_string += "\n\t\t\t<th style=\"text-align:left\">" + comment.value + "</th>"
                             
                html_string += "</tr>"

        html_string += """\t</table>\n"""

        html_string += "<h1>Percentagem de sucesso</h1>"
        html_string += """<div class="piechart"></div>"""
 


        html_string += "</body>"

        return html_string

    def HtmlStringToHtml(self, html_string, doc_name):
        if not os.path.exists("HTML_Documents"):
            os.mkdir("HTML_Documents")

        f = open("HTML_Documents/" + doc_name + ".html", "w")
        f.write(html_string)

        pass
