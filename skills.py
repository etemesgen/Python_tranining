class Skills:
    def __init__(self, html, css, javascript, php, mysql, python):
        self.html = html
        self.css = css
        self.javascript = javascript
        self.php = php
        self.mysql = mysql
        self.python = python

    def progression(self):
        skillTech = input("Enter the tech concerned: ")
        progressNumber = input("Enter your progression number: ")

        if skillTech == "html":
            print("Your progression status for " + skillTech + " is: " + progressNumber)
        elif skillTech == "css":
            print("Your progression status for " + skillTech + " is: " + progressNumber)
        elif skillTech == "javascript":
            print("Your progression status for " + skillTech + " is: " + progressNumber)
        elif skillTech == "php":
            print("Your progression status for " + skillTech + " is: " + progressNumber)
        elif skillTech == "mysql":
            print("Your progression status for " + skillTech + " is: " + progressNumber)
        elif skillTech == "python":
            print("Your progression status for " + skillTech + " is: " + progressNumber)
        else:
            print("Please enter a a technology of the category html, css, javascript, php, mysql and python !")
