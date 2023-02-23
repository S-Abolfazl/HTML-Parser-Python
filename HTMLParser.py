from bs4 import BeautifulSoup, Comment
import re


class HTMLParser:
    def __init__(self, html_doc):
        self.html_doc = html_doc

    def set_html_doc(self, html_doc):
        self.html_doc = html_doc

    def find_first(self, output_arg, **finding_args):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        element = post.find(**finding_args)
        if element is None:
            raise Exception('No Such Tag')
        if output_arg == 'string':
            return element.get_text()
        if output_arg == 'name':
            return element.name
        return str(element.get(output_arg))

    def find_all(self, n, output_arg, **finding_args):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        elements = post.find_all(**finding_args)
        list = ()
        if output_arg == 'string':
            for element in elements:
                list.append(element.get_text())
        else:
            for element in elements:
                if element.get(output_arg) is None:
                    list.append('')
                else:
                    list.append(element.get(output_arg))
        if len(list) == 0:
            raise Exception('No Such Tag')
        elif n >= len(list):
            return list
        else:
            return list[0:n]

    def find_parent(self, output_arg, **finding_args):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        element = post.find(**finding_args)
        if element is None:
            raise Exception('No Such Tag')
        if output_arg == 'name':
            return element.parent.name
        if element.parent.has_attr(output_arg):
            return element.parent.get(output_arg)[0]
        return ''

    def find_grandparent(self, n, output_arg, **finding_args):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        element = post.find(**finding_args)
        if len(list(element.parents)) - 1 < n:
            raise Exception('No Such Parent')

        i = 1
        for parent in element.parents:
            if output_arg == 'name' and i == n:
                return parent.name
            if parent.has_attr(output_arg) and i == n:
                return parent.get(output_arg)[0]
            i += 1

    def remove_comment(self, **finding_args):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        element = post.find(finding_args.values())
        if isinstance(element.string, Comment):
            self.html_doc = re.sub(str(element), '', self.html_doc, 1)
        else:
            raise Exception('No Comments Found')

    def remove_all_comments(self):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        for element in post(text=lambda text: isinstance(text, Comment)):
            element.extract()
        if self.html_doc == post:
            raise Exception('No Such Tag')
        self.html_doc = post

    def remove_tag(self, **finding_args):
        post = BeautifulSoup(self.html_doc, 'html.parser')
        element = post.find(**finding_args)
        if element is None:
            raise Exception('No Such Tag')
        self.html_doc = re.sub(str(element), '', self.html_doc, 1)


with open('html-doc.txt', 'r', encoding='utf-8') as file:
    doc = file.read()
x = HTMLParser(doc)
values = {
    'class': 'section'
}
x.html_doc = '<p class=555555><span><p class=123><b>example</b></p></span></p>'
tag_name = x.find_grandparent(2, "class", name='b', string='example')
print(tag_name)
# g.remove_tag(name='div')
