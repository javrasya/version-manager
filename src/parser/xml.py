from __future__ import absolute_import

from xml.etree import ElementTree

from src.parser.parser import Parser

try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

__author__ = 'ahmetdal'

XML_PARSER = 'xml'


class XMLParser(Parser):
    file_type = XML_PARSER

    def __init__(self, xpaths=None, namespaces=None, *args, **kwargs):
        if not namespaces:
            namespaces = {}
        super(XMLParser, self).__init__()
        self.xpaths = xpaths
        self.namespaces = namespaces
        for v in namespaces.values():
            ElementTree.register_namespace('', v)

        if not self.xpaths:
            raise Exception("File version xpaths must be given for xml parser type.")

    def __get_tree(self, content):
        return ElementTree.ElementTree(ElementTree.fromstring(content, parser=CommentedTreeBuilder()))

    def update_version(self, content, new_version):
        tree = self.__get_tree(content)
        root = tree.getroot()
        for xpath in self.xpaths:
            element = root.find(xpath, namespaces=self.namespaces)
            if element is not None:
                element.text = new_version
        io = StringIO()
        tree.write(io, encoding='utf-8', xml_declaration=True)
        return io.getvalue()

    def current_version(self, content):
        tree = self.__get_tree(content)
        root = tree.getroot()
        try:
            for xpath in self.xpaths:
                version = root.findtext(xpath, namespaces=self.namespaces)
                if version:
                    return version
        except SyntaxError:
            pass


class CommentedTreeBuilder(ElementTree.XMLTreeBuilder):
    def __init__(self, html=0, target=None):
        ElementTree.XMLTreeBuilder.__init__(self, html, target)
        self._parser.CommentHandler = self.handle_comment

    def handle_comment(self, data):
        self._target.start(ElementTree.Comment, {})
        self._target.data(data)
        self._target.end(ElementTree.Comment)
