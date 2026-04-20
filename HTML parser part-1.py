from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def print_attrs(self, attrs):
        for name, value in attrs:
            print(f"-> {name} > {value}")

    def handle_starttag(self, tag, attrs):
        print(f"Start : {tag}")
        self.print_attrs(attrs)

    def handle_endtag(self, tag):
        print(f"End   : {tag}")

    def handle_startendtag(self, tag, attrs):
        print(f"Empty : {tag}")
        self.print_attrs(attrs)
parser = MyHTMLParser()
n = int(input())
html_code = ""
for _ in range(n):
    html_code += input() + "\n" 
parser.feed(html_code)
parser.close()
