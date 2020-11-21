from utils import Utils


class Html(object):

    def CreateHtmlString(self, file_number, successful_tests_list):
        html_string = "<head>\n"
        html_string += "<style> table, th, td{border: 1px solid black;}</style>\n"
        html_string += "</head>\n"

        html_string += "<body>\n"
        html_string += "\t<h1> Relatório " + str(file_number) + "!</h1>\n"
        html_string += """\t<table style="width:100%">\n"""
        html_string += "\t\t<tr>\n"
        html_string += "\t\t\t<th style=\"text-align:left\">Teste</th>\n"
        html_string += "\t\t\t<th style=\"text-align:left\">Status</th>\n"
        html_string += "\t\t</tr>\n"

        for test in successful_tests_list:
            html_string += "\t\t<tr>\n"

            status = Utils.GetStatusFromToken(None, test)
            number = Utils.GetNumberFromToken(None, test)

            html_string += "\t\t\t<th style=\"text-align:left\">" + number + "</th>\n"
            if status == "ok":
                html_string += "<\t\t\t<th style=\"text-align:left\" \"background-color:#32CD32\">" + status + \
                               "</th>\n"
            else:
                html_string += "<\t\t\t<th style=\"text-align:left\" \"background-color:#FF0000\">" + status + \
                               "</th>\n"

            html_string += "\t\t</tr>\n"

        html_string += """\t</table style="width:100%">\n"""

        html_string += "</body>"

        return html_string

    def HtmlStringToHtml(self, html_string):
        f = open("Teste.html", "w")
        f.write(html_string)

        pass

    def example(self):
        var = 'goodbye'
        index = open("index.html").read().format(first_header='goodbye',
                                                 p1='World',
                                                 p2='Hello')
        return index

