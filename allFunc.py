import lxml.etree as etree
import sys
import xml.etree.ElementTree as ele
from xml.etree.ElementTree import Element


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
    xslt = etree.parse("xslt\\" + findXslt(str_name) + ".xslt")
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


def setList():
    f = open("xslt/item_list.txt", "r")
    s = ""
    while True:
        r = f.readline()
        n = r.split(",")
        if n[0] != 'EOF\n':
            s += n[0]
        elif n[0] == "EOF\n":
            break
        s += ","
    f.close()
    return s


def findXslt(str_name):
    f = open("xslt/item_list.txt", "r")
    while True:
        r = f.readline()
        n = r.split(",")
        if n[0] == str_name:
            f.close()
            return str(n[1]).replace("\n", "")
        elif n[0] == "EOF\n":
            break
    f.close()
    return "xslt_scf_gibon"


def inputList(str1, str2, target):
    f = open("xslt/item_list.txt", "r")
    s = str1 + "," + str2 + "\n"
    r = f.readlines()
    k = 0
    for i in r:
        n = i.split(",")
        if n[0] == 'EOF\n':
            break
        elif n[0] == target:
            r[k] += s
            print(r[k])
            break;
        k += 1
    f.close()
    f = open("xslt/item_list.txt", "w")
    f.writelines(r)
    f.close()


def deleteList(target):
    f = open("xslt/item_list.txt", "r")
    r = f.readlines()
    k = 0
    for i in r:
        n = i.split(",")
        if n[0] == 'EOF\n':
            break
        elif n[0] == target:
            r[k] = ""
            break;
        k += 1
    f.close()
    f = open("xslt/item_list.txt", "w")
    f.writelines(r)
    f.close()


def error_xml(make_error):
    print("에러 발생")
    print(make_error)


def getCorrectNode(root, t):
    s = ""
    for child in root:
        if child.tag != "":
            try:
                s += t + "[" +child.tag + "] : " + child.text + "\n"
                s += getCorrectNode(child, t + "  ")
            except:
                s += "\n"
        else:
            print("!"+child.tag+"!")
    return s