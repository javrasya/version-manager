import os
from unittest import TestCase
from os.path import dirname
from src.parser.xml import XMLParser

__author__ = 'ahmetdal'


class testXmlParser(TestCase):
    def setUp(self):
        with open(os.path.join(dirname(dirname(dirname(__file__))), 'test_resources', 'test_xml')) as f:
            self.content = f.read()

        self.parser = XMLParser(xpaths=['./mvn:version'], namespaces={'mvn': 'http://maven.apache.org/POM/4.0.0'})

    def test_xpath_is_none(self):
        try:
            XMLParser()
            self.assertFalse(True)
        except Exception as e:
            self.assertEqual("File version xpaths must be given for xml parser type.", str(e))

    def test_current_version(self):
        # current_version test
        self.assertEquals('0.2.0', self.parser.current_version(self.content))

    def test_update_version(self):
        # update_version test
        content = self.parser.update_version(self.content, '0.2.1')
        updated_current_version = self.parser.current_version(content)
        self.assertEqual('0.2.1', updated_current_version)
        self.assertTrue("<?xml version='1.0' encoding='utf-8'?>" in content)
        self.assertTrue("<!--Comment shouldn't be removed-->" in content)
