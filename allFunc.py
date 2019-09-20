import clipboard
import lxml.etree as etree
import xml.etree.ElementTree as ele
from xml.etree.ElementTree import Element, dump
from math import *
import myFile


def make_substring(str_msg, str_name):
    num = str_msg.find('<')
    if (num == -1):
        error_xml()
        return "뭔가 입력이 필요합니다.";
    root = Element("xml")
    str_msg = str_msg[num:]
    elem = ele.fromstring(str_msg)
    root.append(elem)
    indent(elem, 0)
    tree = ele.ElementTree(elem)
    tree.write("xslt\\hh.xml", encoding="utf-8")
    tree = ele.parse("xslt\\hh.xml")
    parsedXml = etree.parse("xslt/hh.xml")
    str2 = etree.tostring(parsedXml, pretty_print=True, encoding='utf-8').decode()
    chstr = "<tr><td>"
    for i in range(30):
        chstr += "&nbsp;"
    chstr += "</tr></td><table"
    dom = etree.parse("xslt\\hh.xml")
    xslt = etree.parse("xslt\\" + myFile.findXslt(str_name) + ".xslt")
    transform = etree.XSLT(xslt)
    newdom = transform(dom)
    str1 = str(etree.tostring(newdom, pretty_print=True))[2:].replace("\\n", "")
    str1 = str(str1).replace("<table", chstr)
    f = open("xslt\\abc.html", 'w', encoding='utf8')
    f.write(str1)
    f.close()
    return str2


def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level + 1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i


def error_xml(asd):
    print("에러 발생")
    print(asd)
