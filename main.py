import requests
import lxml.html
from lxml.html import etree

def parse(html_text):
    tree = lxml.html.document_fromstring(html_text)
    text_titles = tree.xpath("//*[@class='entry-title']/a/text()")
    text_contents = tree.xpath("//*[@class='entry-content entry-excerpt clearfix']/p/text()")
    return text_titles, text_contents

def parsing(url):
    parse(url)
    text = requests.get(url)
    if text.status_code == 200:
        text_title, text_content = parse(text.text)
        for i, t in enumerate(text_title):
            text1 = """
            -------------------------------
            Заголовок ===>  {title}
            Контент   ===>  {content}
            -------------------------------""".format(title=t, content=text_content[i])
            print(text1)
        
def main():
    parsing(input("Ссылку пожалуйста: "))
    


if __name__ == "__main__":
    main()