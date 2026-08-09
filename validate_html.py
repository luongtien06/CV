from html.parser import HTMLParser
import pathlib

class C(HTMLParser):
    def error(self, message):
        raise Exception(message)

parser = C()
text = pathlib.Path(r'e:\WEB\CV\index.html').read_text(encoding='utf-8')
parser.feed(text)
print('HTML parsed successfully')
